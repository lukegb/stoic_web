// ==ClosureCompiler==
// @output_file_name default.js
// @compilation_level ADVANCED_OPTIMIZATIONS
// ==/ClosureCompiler==

var Player = {
  resize: function(immediate) {
    if (!immediate) {
      if (Player.debounceResize) {
        clearTimeout(Player.debounceResize);
      }
      Player.debounceResize = setTimeout(function() { Player.resize(true); }, 20);
      return;
    }
    Player.debounceResize = null;

    var bcr = Player.playerEl.getBoundingClientRect();
    var compStyle = window.getComputedStyle(Player.playerEl.parentNode);
    var width = bcr.right - bcr.left - Player.toPixels(compStyle.paddingLeft) - Player.toPixels(compStyle.paddingRight);

    var height = Player.computeHeight(width);
    console.log(width, height);

    Player.resizeEls.forEach(function(el) {
      el.width = width;
      el.height = height;
    });
  },
  computeHeight: function(width) {
    var ratio = Player.config.ratio || '16:9';
    var ratioBits = ratio.split(':').map(function(x) { return +x });
    return width / ratioBits[0] * ratioBits[1];
  },
  toPixels: function(val) {
    return parseInt(val, 10);
  },
  doesSupport: function(what) {
    Player.log("Evaluating availability of: " + what);
    switch (what) {
      case 'hls':
        var ret = document.createElement('video').canPlayType('application/vnd.apple.mpegURL');
        return ret == 'probably' || ret == 'maybe';
      case 'dash':
        return !!window.MediaSource && window.MediaSource.isTypeSupported('video/mp4; codecs="avc1.42E01E,mp4a.40.2"');
      case 'rtmp':
        return true;
      default:
        throw new Exception("Don't know how to check support for '" + what + "'!");
    }
  },
  go: function(what, targetEl) {
    while (targetEl.firstNode) {
      targetEl.removeChild(targetEl.firstNode);
    }

    switch (what) {
      case 'hls':
        var videoEl = document.createElement("video");
        videoEl.src = Player.config.sources.hls;
        videoEl.autoplay = true;
        videoEl.controls = true;
        targetEl.appendChild(videoEl);
        Player.resizeEls = [videoEl];
        Player.done();
        return;
      case 'dash':
        Player.loadJs(Player.config.staticThings.dashjs, function() {
          var videoEl = document.createElement("video");
          videoEl.controls = true;
          targetEl.appendChild(videoEl);
          Player.resizeEls = [videoEl];
          var context = new Dash.di.DashContext();
          var player = new MediaPlayer(context);
          player.startup();
          player.attachView(videoEl);
          player.attachSource(Player.config.sources.dash);          
          Player.done();
        }, function() {
          Player.tryNext();
        });
        return;
      case 'rtmp':
        var width = 640, height = 360;

        var obj = document.createElement('object');
        obj.width = width, obj.height = height;

        var baseParams = {'flashvars': 'src=' + encodeURIComponent(Player.config.sources.rtmp) + '&streamType=live&autoPlay=true', 'allowFullScreen': 'true', 'allowscriptaccess': 'always', 'wmode': 'direct'};

        var objParams = {'movie': Player.config.staticThings.strobe};
        for (var param in baseParams) {
          if (!baseParams.hasOwnProperty(param)) continue;
          objParams[param] = baseParams[param];
        }
        for (var param in objParams) {
          if (!objParams.hasOwnProperty(param)) continue;
          var objParam = document.createElement('param');
          objParam.name = param;
          objParam.value = objParams[param];
          obj.appendChild(objParam);
        }

        var embed = document.createElement('embed');
        var embedParams = {'src': Player.config.staticThings.strobe};
        for (var param in baseParams) {
          if (!baseParams.hasOwnProperty(param)) continue;
          embedParams[param] = baseParams[param];
        }
        for (var param in embedParams) {
          if (!embedParams.hasOwnProperty(param)) continue;
          embed.setAttribute(param, embedParams[param]);
        }
        obj.appendChild(embed);

        targetEl.appendChild(obj);
        Player.resizeEls = [obj, embed];
        Player.done();
        return;
    }
  },
  done: function() {
    // we apparently found something that works, yay
    Player.resize(true);
  },
  tryNext: function() {
    var nextPreference = null;
    while (nextPreference === null || !Player.doesSupport(nextPreference)) {
      nextPreference = Player.config.preference.shift();
    }
    Player.go(nextPreference, Player.playerEl);
  },
  loadJs: function(script, onOk, onFail) {
    var done = false;
    var doonce = function(x) {
      return function() {
        if (done) return;
        done = true;
        return x();
      }
    };
    var execOk = function() {
      Player.log("Successfully loaded: " + script);
      onOk();
    };
    var execFail = function() {
      Player.log("Failed to load: " + script);
      onFail();
    };
    var scriptEl = document.createElement('script');
    scriptEl.addEventListener('load', doonce(execOk));
    scriptEl.addEventListener('error', doonce(execFail));
    scriptEl.addEventListener('readystatechange', function() {
      if (scriptEl.readyState === "complete") {
        return doonce(execOk)();
      }
    });
    scriptEl.src = script;
    document.body.appendChild(scriptEl);
  },
  log: function(x) {
    if (Player.config.debug)
      console.log(x);
  },
  config: {
    debug: false,
    ratio: '16:9',
    preference: ['dash', 'hls', 'rtmp'],
    sources: {
      rtmp: '',
      hls: '',
      dash: ''
    },
    staticThings: {
      strobe: '',
      dashjs: ''
    }
  }
};

/** @export */
Player.init = function(playerEl) {
  Player.playerEl = playerEl;

  Player.resizeEls = [];

  window.addEventListener('resize', function() { Player.resize(false); });
  Player.tryNext();
};
