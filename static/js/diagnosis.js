// @Author: PT
// @CreateTime: 2024-06-05
// @Description:中医诊疗
// @Version:1.0

const body = document.querySelector('body'),
  shell = body.querySelector('nav'),
  toggle = body.querySelector('.toggle');

// 点击toggle元素时触发事件
toggle.addEventListener("click", () => {
  // 切换shell元素的close类
  shell.classList.toggle("close");
})

// 弹出文模态框
function popuptextToggle() {
  // 打开对应模态框
  popup_text = document.getElementById('popup_text');
  popup_text.classList.toggle('active');
}

// 弹出舌图模态框
function popupToggle() {
  // 打开对应模态框
  popup = document.getElementById('popup');
  popup.classList.toggle('active');
}

// 推荐搜索词点击事件
var change = document.getElementById("symptom");
function ksClick() {
  change.value = change.value + "咳嗽 "
}
function frClick() {
  change.value = change.value + "发热 "
}
function ttClick() {
  change.value = change.value + "头痛 "
}
function stbbClick() {
  change.value = change.value + "舌苔薄白 "
}
function jbClick() {
  change.value = change.value + "经闭 "
}
function jswwClick() {
  change.value = change.value + "进食无味 "
}

// 舌图点击事件
function img1Click() {
  change.value = change.value + "舌淡红而小 "
}
function img2Click() {
  change.value = change.value + "舌淡 "
}
function img3Click() {
  change.value = change.value + "舌淡胖 "
}
function img4Click() {
  change.value = change.value + "舌淡紫 "
}
function img5Click() {
  change.value = change.value + "舌赤 "
}
function img6Click() {
  change.value = change.value + "舌绛 "
}
function img7Click() {
  change.value = change.value + "舌红嫩小 "
}
function img8Click() {
  change.value = change.value + "舌红胖 "
}
function img9Click() {
  change.value = change.value + "舌黯红 "
}
function img10Click() {
  change.value = change.value + "舌尖红 "
}
function img11Click() {
  change.value = change.value + "舌边红 "
}
function img12Click() {
  change.value = change.value + "舌起芒刺 "
}
function img13Click() {
  change.value = change.value + "舌有裂纹 "
}
function img14Click() {
  change.value = change.value + "舌紫黯 "
}
function img15Click() {
  change.value = change.value + "舌有斑点 "
}
function img16Click() {
  change.value = change.value + "舌有齿印 "
}
function img17Click() {
  change.value = change.value + "舌体萎软 "
}
function img18Click() {
  change.value = change.value + "舌体歪斜 "
}
function img19Click() {
  change.value = change.value + "舌动异常 "
}
function img20Click() {
  change.value = change.value + "舌体强硬 "
}
function img21Click() {
  change.value = change.value + "舌白如镜 "
}
function img22Click() {
  change.value = change.value + "舌绛深紫 "
}
function img23Click() {
  change.value = change.value + "舌体溃烂 "
}
function img24Click() {
  change.value = change.value + "舌体干燥 "
}
function img25Click() {
  change.value = change.value + "舌下脉络曲张 "
}
function img26Click() {
  change.value = change.value + "舌苔薄白 "
}
function img27Click() {
  change.value = change.value + "舌苔白 "
}
function img28Click() {
  change.value = change.value + "苔白如积粉 "
}
function img29Click() {
  change.value = change.value + "舌苔腐垢 "
}
function img30Click() {
  change.value = change.value + "舌苔黄 "
}
function img31Click() {
  change.value = change.value + "舌苔灰黑 "
}
function img32Click() {
  change.value = change.value + "舌苔黄白相兼 "
}
function img33Click() {
  change.value = change.value + "舌苔腻 "
}
function img34Click() {
  change.value = change.value + "苔剥 "
}
function img35Click() {
  change.value = change.value + "舌苔润滑 "
}
function img36Click() {
  change.value = change.value + "舌苔干燥 "
}

// 提示框
var toastr;
toastr.options = {
  closeButton: true,
  debug: false,
  progressBar: true,
  positionClass: "toast-top-center",
  onclick: null,
  showDuration: "300",
  hideDuration: "1000",
  timeOut: "1500",
  extendedTimeOut: "1000",
  showEasing: "swing",
  hideEasing: "linear",
  showMethod: "fadeIn",
  hideMethod: "fadeOut"
};

// 诊疗按钮点击事件
function treatClick() {
  // 获取输入框内容
  var values = document.getElementById('symptom').value
  // 传给后端的数据
  var data = {
    "flag": 1,
    "values": values
  }

  $.ajax({
    url: "getdata",
    type: "GET",
    // 将data值传到后端，以json形式
    data: data,
    dataType: "json",
    // 接收后端传来的值
    success: function (response) {
      // 弹出提示框
      toastr.success('开始中医智能诊疗！');
      // 将接收值转换成相应格式
      neo4j_data = response.neo4j_data
      data_zheng = neo4j_data['data_zheng']
      data_zs = neo4j_data['data_zs']
      data_zz = neo4j_data['data_zz']
      data_link = neo4j_data['data_link']

      zzbm = response.zzbm
      new_zs = response.new_zs
      l = response.l

      score_sort = response.score_sort
      zs = score_sort['zs']
      score = score_sort['score']

      zh_dict = response.zh_dict
      zheng = zh_dict['zheng']
      zs1 = zh_dict['zs']
      score1 = zh_dict['score']

      zheng_final = response.zheng_final

      zh_dbf_cm = response.zh_dbf_cm
      dbf = zh_dbf_cm['dbf']
      cm_jl = zh_dbf_cm['cm_jl']

      // 执行各个图表可视化函数
      stacked_bar_graph(zzbm, new_zs, l)
      radar_graph(new_zs, l, zzbm)
      treemap_graph(zs, score)
      pie_link_bar_graph(zs1, score1, zheng, dbf, cm_jl)
      node_re_graph(data_zheng, data_zs, data_zz, data_link)

    },
    error: function (XMLHttpRequest, textStatus, errorThrown) {
      debugger
      // 状态码
      console.log(XMLHttpRequest.status);
      // 状态
      console.log(XMLHttpRequest.readyState);
      // 错误信息
      console.log(textStatus);
      toastr.error('网页无响应！')
    }
  })
}

// 搜索提示
function SearchSuggest(searchFuc) {
  var input = $('#suggest_input');
  var suggestWrap = $('#search_suggest');
  var key = "";

  var init = function () {
    // 当按下按键时（keyup）
    input.bind('keyup', sendKeyWord);
    // 当输入域失去焦点 (blur)
    input.bind('blur', function () {
      setTimeout(hideSuggest, 100)
    })
  }

  // 隐藏搜索提示框
  var hideSuggest = function () {
    suggestWrap.hide();
  }

  const container = document.getElementById('search_suggest');

  // 发送请求，根据输入内容到后台查询
  var sendKeyWord = function (event) {
    // 键盘选择下拉项
    if (suggestWrap.css('display') == 'block' && event.keyCode == 38 || event.keyCode == 40) {
      var current = suggestWrap.find('li.hover');
      // 键盘↑键
      if (event.keyCode == 38) {
        if (current.length > 0) {
          // 除去这个的hover，定位到上一个
          var prevLi = current.removeClass('hover').prev();
          // 如果还有上一个
          if (prevLi.length > 0) {
            // 对上一个加上hover
            prevLi.addClass('hover');
            // 控制滚动条的滚动步长
            container.scrollTop -= 24;
            // 设置输入框的值  返回li的当前内容
            input.val(prevLi.html());
            // 点击事件的时候再添加到输入框中
          }
          else {
            // 最后一个 li
            var last = suggestWrap.find('li:last');
            last.addClass('hover');
            // 滚动条到最底部
            container.scrollTop = container.scrollHeight;
            input.val(last.html());
          }
        }
      }
      // 键盘↓键
      else if (event.keyCode == 40) {
        if (current.length > 0) {
          var nextLi = current.removeClass('hover').next();
          // 如果下一个还有
          if (nextLi.length > 0) {
            nextLi.addClass('hover');
            container.scrollTop += 24;
            input.val(nextLi.html());
          }
          else {
            // 第一个 li
            var first = suggestWrap.find('li:first');
            first.addClass('hover');
            // 滚动条回到最上面
            container.scrollTop = 0;
            input.val(first.html());
          }
        }
      }
    }
    // 输入字符
    else {
      var valText = $.trim(input.val());
      if (valText == '' || valText == key) {
        return
      }
      searchFuc(valText);
      key = valText;
    }
  }

  // 请求返回后，执行数据展示
  this.dataDisplay = function (data) {
    if (data.length <= 0) {
      suggestWrap.hide();
      return
    }

    // 搜索提示框添加 li 并显示
    var li;
    var tmpFrag = document.createDocumentFragment();
    suggestWrap.find('ul').html('');
    for (var i = 0; i < data.length; i++) {
      li = document.createElement('li');
      li.innerHTML = data[i];
      // appendChild是用于添加子元素的纯DOM方法
      tmpFrag.appendChild(li);
    }
    suggestWrap.find('ul').append(tmpFrag);
    suggestWrap.show();

    // 为 li 绑定鼠标事件
    suggestWrap.find('li').hover(function () {
      suggestWrap.find('li').removeClass('hover');
      $(this).addClass('hover');
    }, function () {
      $(this).removeClass('hover');
    }).bind('click', function () {
      input.val(this.innerHTML);
      suggestWrap.hide();
    });
  }
  init();
};

// 实例化输入提示的JS，参数为查询时调用的函数名
var searchSuggest = new SearchSuggest(sendKeyWordToBack);

function sendKeyWordToBack(keyword) {
  // 传给后端的数据
  var data = {
    "keyword": keyword
  }

  $.ajax({
    url: "getkeyword",
    type: "GET",
    // 将data值传到后端，以json形式
    data: data,
    dataType: "json",
    // 接收后端传来的值
    success: function (response) {
      var aData = []
      keyword_result = response.keyword_result
      for (var i = 0; i < keyword_result.length; i++) {
        aData.push(keyword_result[i]);
      }
      searchSuggest.dataDisplay(aData);
    },
    error: function (XMLHttpRequest, textStatus, errorThrown) {
      debugger
      // 状态码
      console.log(XMLHttpRequest.status);
      // 状态
      console.log(XMLHttpRequest.readyState);
      // 错误信息
      console.log(textStatus);
      toastr.error('网页无响应！')
    }
  })
}

// 确认按钮点击事件
function confirmClick() {
  // 获取文模态框中输入框的值
  var confirm_input = document.getElementById('suggest_input')
  // 增加症状
  change.value = change.value + confirm_input.value + " "
}
