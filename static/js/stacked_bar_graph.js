// @Author: PT
// @CreateTime: 2024-06-05
// @Description:堆叠柱状图  证素-证得分
// @Version:1.0

function stacked_bar_graph(zzbm, new_zs, l) {
  var stacked_bar_graph = echarts.init(document.getElementById('stacked_bar_graph'));
  // 用户输入的症状
  var zz = zzbm
  // 涉及的所有证素
  var zs_sbg = new_zs
  // 对应得分
  var score_sbg = l

  // 记录输入的症状个数
  var zzcount = zz.length
  // 记录输入的证素个数
  var zscount = zs_sbg.length
  // 画堆叠图需要的数据结果
  var result = []

  // 最后证素对应的症状得分一一对应结果
  function resultReset(zs_sbg, score_sbg, zzcount, zscount) {
    // 找到对应证素得分列表
    for (var i = 0; i < zscount; i++) {
      result[i] = { name: zs_sbg[i], data: [] }
      // 找到该证素对应症状得分
      for (var j = 0; j < zzcount; j++) {
        result[i].data[j] = score_sbg[i][j]
      }
    }
  }
  resultReset(zs_sbg, score_sbg, zzcount, zscount)

  // 堆叠柱状图数据集
  var dataArr_sbg = {
    // 症状
    xdata: zz,
    // 证素及其得分
    result: result
  }

  // color合集（26种）
  var color = [
    [{ offset: 0, color: "#e58d8c", }, { offset: 0.5, color: "#e58d8c", }, { offset: 0.5, color: "#e58d8c", }, { offset: 1, color: "#e58d8c", }],
    [{ offset: 0, color: "rgb(199, 229, 195)", }, { offset: 0.5, color: "rgb(199, 229, 195)", }, { offset: 0.5, color: "rgb(199, 229, 195)", }, { offset: 1, color: "rgb(199, 229, 195)", }],
    [{ offset: 0, color: "rgb(255, 232, 168)", }, { offset: 0.5, color: "rgb(255, 232, 168)", }, { offset: 0.5, color: "rgb(255, 232, 168)", }, { offset: 1, color: "rgb(255, 232, 168)", }],
    [{ offset: 0, color: "rgb(130, 173, 194)", }, { offset: 0.5, color: "rgb(130, 173, 194)", }, { offset: 0.5, color: "rgb(130, 173, 194)", }, { offset: 1, color: "rgb(130, 173, 194)", }],
    [{ offset: 0, color: "rgb(232, 109, 109)", }, { offset: 0.5, color: "rgb(232, 109, 109)", }, { offset: 0.5, color: "rgb(232, 109, 109)", }, { offset: 1, color: "rgb(232, 109, 109)", }],
    [{ offset: 0, color: "rgb(212, 106, 143)", }, { offset: 0.5, color: "rgb(212, 106, 143)", }, { offset: 0.5, color: "rgb(212, 106, 143)", }, { offset: 1, color: "rgb(212, 106, 143)", }],
    [{ offset: 0, color: "rgb(245, 135, 139)", }, { offset: 0.5, color: "rgb(245, 135, 139)", }, { offset: 0.5, color: "rgb(245, 135, 139)", }, { offset: 1, color: "rgb(245, 135, 139)", }],
    [{ offset: 0, color: "rgb(252, 176, 124)", }, { offset: 0.5, color: "rgb(252, 176, 124)", }, { offset: 0.5, color: "rgb(252, 176, 124)", }, { offset: 1, color: "rgb(252, 176, 124)", }],
    [{ offset: 0, color: "rgb(255, 115, 157)", }, { offset: 0.5, color: "rgb(255, 115, 157)", }, { offset: 0.5, color: "rgb(255, 115, 157)", }, { offset: 1, color: "rgb(255, 115, 157)", }],
    [{ offset: 0, color: "rgb(202, 140, 126)", }, { offset: 0.5, color: "rgb(202, 140, 126)", }, { offset: 0.5, color: "rgb(202, 140, 126)", }, { offset: 1, color: "rgb(202, 140, 126)", }],
    [{ offset: 0, color: "rgb(138, 209, 159)", }, { offset: 0.5, color: "rgb(138, 209, 159)", }, { offset: 0.5, color: "rgb(138, 209, 159)", }, { offset: 1, color: "rgb(138, 209, 159)", }],
    [{ offset: 0, color: "rgb(255, 204, 161)", }, { offset: 0.5, color: "rgb(255, 204, 161)", }, { offset: 0.5, color: "rgb(255, 204, 161)", }, { offset: 1, color: "rgb(255, 204, 161)", }],
    [{ offset: 0, color: "rgb(75, 173, 196)", }, { offset: 0.5, color: "rgb(75, 173, 196)", }, { offset: 0.5, color: "rgb(75, 173, 196)", }, { offset: 1, color: "rgb(75, 173, 196)", }],
    [{ offset: 0, color: "rgb(126, 114, 168)", }, { offset: 0.5, color: "rgb(126, 114, 168)", }, { offset: 0.5, color: "rgb(126, 114, 168)", }, { offset: 1, color: "rgb(126, 114, 168)", }],
    [{ offset: 0, color: "rgb(99, 101, 207)", }, { offset: 0.5, color: "rgb(99, 101, 207)", }, { offset: 0.5, color: "rgb(99, 101, 207)", }, { offset: 1, color: "rgb(99, 101, 207)", }],
    [{ offset: 0, color: "rgb(166, 207, 99)", }, { offset: 0.5, color: "rgb(166, 207, 99)", }, { offset: 0.5, color: "rgb(166, 207, 99)", }, { offset: 1, color: "rgb(166, 207, 99)", }],
    [{ offset: 0, color: "rgb(186, 125, 219)", }, { offset: 0.5, color: "rgb(186, 125, 219)", }, { offset: 0.5, color: "rgb(186, 125, 219)", }, { offset: 1, color: "rgb(186, 125, 219)", }],
    [{ offset: 0, color: "#faaa9f", }, { offset: 0.5, color: "#faaa9f", }, { offset: 0.5, color: "#faaa9f", }, { offset: 1, color: "#faaa9f", }],
    [{ offset: 0, color: "#d6b39d", }, { offset: 0.5, color: "#d6b39d", }, { offset: 0.5, color: "#d6b39d", }, { offset: 1, color: "#d6b39d", }],
    [{ offset: 0, color: "#9dc3c4", }, { offset: 0.5, color: "#9dc3c4", }, { offset: 0.5, color: "#9dc3c4", }, { offset: 1, color: "#9dc3c4", }],
    [{ offset: 0, color: "#c3a196", }, { offset: 0.5, color: "#c3a196", }, { offset: 0.5, color: "#c3a196", }, { offset: 1, color: "#c3a196", }],
    [{ offset: 0, color: "rgb(236,114,125)", }, { offset: 0.5, color: "rgb(236,114,125)", }, { offset: 0.5, color: "rgb(236,114,125)", }, { offset: 1, color: "rgb(236,114,125)", }],
    [{ offset: 0, color: "rgb(217,118,90)", }, { offset: 0.5, color: "rgb(217,118,90)", }, { offset: 0.5, color: "rgb(217,118,90)", }, { offset: 1, color: "rgb(217,118,90)", }],
    [{ offset: 0, color: "rgb(253,213,87)", }, { offset: 0.5, color: "rgb(253,213,87)", }, { offset: 0.5, color: "rgb(253,213,87)", }, { offset: 1, color: "rgb(253,213,87)", }],
    [{ offset: 0, color: "rgb(136,171,218)", }, { offset: 0.5, color: "rgb(136,171,218)", }, { offset: 0.5, color: "rgb(136,171,218)", }, { offset: 1, color: "rgb(136,171,218)", }],
    [{ offset: 0, color: "#FFCC99", }, { offset: 0.5, color: "#FFCC99", }, { offset: 0.5, color: "#FFCC99", }, { offset: 1, color: "#FFCC99", }],
  ]

  var series = dataArr_sbg.result.reduce((pre, cur, index) => {
    pre.push(
      {
        z: index + 1,
        stack: '总量',
        type: 'bar',
        name: cur.name,
        barWidth: 30,
        data: cur.data,
        itemStyle: { color: { type: 'linear', x: 0, x2: 1, y: 0, y2: 0, colorStops: color[index] } },
      })
    return pre
  }, [])

  // 标题
  var title = {
    show: true,
    text: '症状-证素得分图',
    x: 'right',
    y: '5px'
  }

  // 全局提示框，显示症状所有的证素以及得分
  // 点击x轴提示框出现
  var tooltip = {
    trigger: "axis",
    confine: true,
    axisPointer: {
      type: "cross",
      label: {
        formatter: function (params) {
          if (params.seriesData.length === 0) {
            window.mouseCurValue = params.value;
          }
        }
      }
    },
    formatter: function (params) {
      var res = "";
      res = params[0].axisValue + "<br/>"
      for (var i = 0; i < params.length; i++) {
        if (params[i].data != 0) {
          res = res + params[i].marker + params[i].seriesName + ":" + params[i].data + "<br/>";
        }
      }
      return res;
    },
  }

  var legend = {
    data: dataArr_sbg.result.map(item => item.name),
    textStyle: { fontSize: 12, color: '#000' },
    itemWidth: 15,
    itemHeight: 9,
    itemGap: 5,
    orient: 'vertical',
    left: 'left',
    y: '1%',
    x: '0%'
  }
  // 绘制网格的范围
  var grid = { top: '15%', left: '22%', right: '0.5%', bottom: '7%' }

  // x轴
  var xAxis = {
    axisTick: { show: true },
    axisLine: { lineStyle: { color: 'rgba(0, 0, 0, 0.3)' } },
    axisLabel: { textStyle: { fontSize: 12, color: '#000' }, },
    data: dataArr_sbg.xdata
  }

  // y轴
  var yAxis = [{
    splitLine: { lineStyle: { color: 'rgba(0, 0, 0, 0.05)' } },
    axisLine: { show: true, },
    axisLabel: { textStyle: { fontSize: 12, color: '#000' } }
  }]

  // 渲染
  option = { title, tooltip, xAxis, yAxis, series, grid, legend }

  // 自动轮播
  var app = {
    currentIndex: -1,
  };
  // 轮三轮停止
  var count_lb = 0;
  var int = setInterval(function () {
    var dataLen = zz.length
    count_lb = count_lb + 1
    if (count_lb > 3 * dataLen) {
      clearInterval(int);
    }
    // 取消之前高亮的图形
    stacked_bar_graph.dispatchAction({
      type: 'downplay',
      seriesIndex: 0,
      dataIndex: app.currentIndex
    });
    app.currentIndex = (app.currentIndex + 1) % dataLen;
    // 高亮当前图形
    stacked_bar_graph.dispatchAction({
      type: 'highlight',
      seriesIndex: 0,
      dataIndex: app.currentIndex,
    });
    // 显示tooltip
    stacked_bar_graph.dispatchAction({
      type: 'showTip',
      seriesIndex: 0,
      dataIndex: app.currentIndex
    });
  }, 1500);
  stacked_bar_graph.setOption(option)

  // 自适应大小
  window.addEventListener("resize", function () {
    stacked_bar_graph.resize();
  })
}
