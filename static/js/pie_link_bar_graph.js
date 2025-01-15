// @Author: PT
// @CreateTime: 2024-06-05
// @Description:证素-证柱状图 方药饼图 联动图
// @Version:1.0

function pie_link_bar_graph(zs1, score1, zheng, dbf, cm_jl) {
  var pie_link_bar_graph = echarts.init(document.getElementById('pie_link_bar_graph'));
  // 证素
  var zs_plbg = zs1
  // 证素得分
  var score_plbg = score1
  // 证
  var zheng_plbg = zheng
  // 代表方
  var dbf_plbg = dbf
  // 与证对应的 中药—剂量列表
  var cm_jl_plbg = cm_jl

  // 中药-剂量 变成特定格式，方便绘图
  var yao = new Array()
  for (var k = 0; k < zheng_plbg.length; k++) {
    // 取一行中药-剂量
    var cm_jl_list = cm_jl_plbg[k]
    // 取出对象的键，中药
    var cm_key = Object.keys(cm_jl_list)
    // 对象不能直接求length，用对象的键的长度
    var len_temp = cm_key.length
    // 取出对象的值，剂量
    var jl_value = Object.values(cm_jl_list)
    // 设个临时列表
    var list_temp = []
    for (var m = 0; m < len_temp; m++) {
      // 设置一个对象
      let obj = {
        'name': cm_key[m],
        'value': jl_value[m]
      }
      list_temp.push(obj)
    }
    yao.push(list_temp)
  }

  // 计算每个证的总得分
  var scoreAlls = []
  for (var i = 0; i < zheng_plbg.length; i++) { scoreAlls[i] = 0 }
  for (var i = 0; i < zheng_plbg.length; i++) {
    for (var j = 0; j < zs_plbg.length; j++) {
      scoreAlls[i] += score_plbg[j][i];
    }
    // 保留一位小数
    scoreAlls[i] = scoreAlls[i].toFixed(1)
  }

  var tooltip = {
    trigger: "axis",
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
      res = params[0].axisValue + "<br/>" + "总得分：";
      for (var i = 0; i < zheng_plbg.length; i++) {
        if (params[0].axisValue == zheng_plbg[i]) {
          res = res + scoreAlls[i] + "<br/>";
        }
      }
      for (var i = 0; i < params.length; i++) {
        if (params[i].data != 0) {
          res = res + params[i].marker + params[i].seriesName + ":" + params[i].data + "<br/>";
        }
      }
      return res;
    },
  }

  option = {
    tooltip: tooltip,
    legend: [
      {
        orient: 'vertical',
        left: 'right',
        y: '2%',
        itemWidth: 15,
        itemHeight: 9,
        itemGap: 5,
        data: yao[zheng_plbg.length - 1],
      },
      {
        orient: 'vertical',
        left: 'right',
        y: '60%',
        itemWidth: 15,
        itemHeight: 9,
        itemGap: 5,
        data: zs_plbg
      },
    ],
    title: [
      {
        x: '2%',
        y: '1%',
        text: zheng_plbg[zheng_plbg.length - 1],
        textStyle: {
          fontSize: 16
        },
        subtext: dbf_plbg[zheng_plbg.length - 1],
        subtextStyle: {
          fontSize: 16
        }
      },
      {
        x: 'center',
        y: '42%',
        text: '代表方药饼图 联动 证-证素得分图',
        textStyle: {
          fontSize: 18
        },
      }
    ],
    xAxis: {
      type: 'category',
      data: zheng_plbg
    },
    yAxis: {
      fridIndex: 0,
    },
    // 柱状图的位置和大小
    grid: {
      top: '48%',
      x: '7%',
      right: '16%',
      bottom: '3%'
    },
    series:
      [
        //联动的方药饼图
        {
          name: yao[zheng_plbg.length - 1],
          data: yao[zheng_plbg.length - 1],
          type: 'pie',
          id: 'pie',
          radius: '38%',
          // 方药饼图位置
          center: ['45%', '22%'],
          emphasis: {
            focus: 'self'
          },
          label: {
            formatter: '{b}:{@100}g'
          },
          color: ['rgb(199, 229, 195)', 'rgb(130, 173, 194)', 'rgb(126, 114, 168)', 'rgb(212, 106, 143)', 'rgb(245, 135, 139)', 'rgb(255, 204, 161)', 'rgb(75, 173, 196)', 'rgb(99, 101, 207)', 'rgb(186, 125, 219)', 'rgb(255, 115, 157)', 'rgb(255, 232, 168)', 'rgb(166, 207, 99)', 'rgb(232, 109, 109)', 'rgb(252, 176, 124)', 'rgb(138, 209, 159)', 'rgb(202, 140, 126)']
        },
        // 设置5个证素的属性
        {
          name: zs_plbg[0],
          data: score_plbg[0],
          color: 'rgb(234, 108, 146)',
          type: 'bar',
          smooth: true,
          seriesLayoutBy: 'row',
          emphasis: { focus: 'series' }
        },
        {
          name: zs_plbg[1],
          data: score_plbg[1],
          color: 'rgb(240, 165, 115)',
          type: 'bar',
          smooth: true,
          seriesLayoutBy: 'row',
          emphasis: { focus: 'series' }
        },
        {
          name: zs_plbg[2],
          data: score_plbg[2],
          color: 'rgb(255, 229, 144)',
          type: 'bar',
          smooth: true,
          seriesLayoutBy: 'row',
          emphasis: { focus: 'series' }
        },
        {
          name: zs_plbg[3],
          data: score_plbg[3],
          color: 'rgb(162, 222, 176)',
          type: 'bar',
          smooth: true,
          seriesLayoutBy: 'row',
          emphasis: { focus: 'series' }
        },
        {
          name: zs_plbg[4],
          data: score_plbg[4],
          color: 'rgb(158, 184, 255)',
          type: 'bar',
          smooth: true,
          seriesLayoutBy: 'row',
          emphasis: { focus: 'series' }
        },
      ]
  };
  pie_link_bar_graph.setOption(option);

  // 自动轮播
  var app1 = {
    currentIndex: -1,
  };
  // 轮两轮停止
  var count_lb = 0;
  var int = setInterval(function () {
    var dataLen = score_plbg[0].length;
    count_lb = count_lb + 1
    if (count_lb > 2 * dataLen) {
      clearInterval(int);
    }
    // 取消之前高亮的图形
    pie_link_bar_graph.dispatchAction({
      type: 'downplay',
      seriesIndex: 1,
      dataIndex: app1.currentIndex
    });
    app1.currentIndex = (app1.currentIndex + 1) % dataLen;
    // 高亮当前图形
    pie_link_bar_graph.dispatchAction({
      type: 'highlight',
      seriesIndex: 1,
      dataIndex: app1.currentIndex,
    });
    // 显示tooltip
    pie_link_bar_graph.dispatchAction({
      type: 'showTip',
      seriesIndex: 1,
      dataIndex: app1.currentIndex
    });
  }, 1500);

  // 鼠标移动到某个上面的时候
  pie_link_bar_graph.on('updateAxisPointer', function (event) {
    const xAxisInfo = event.axesInfo[0];
    if (xAxisInfo) {
      const dimension = xAxisInfo.value;
      pie_link_bar_graph.setOption({
        title: [
          {
            x: '2%',
            y: '1%',
            text: zheng_plbg[dimension],
            textStyle: {
              fontSize: 16
            },
            subtext: dbf_plbg[dimension],
            subtextStyle: {
              fontSize: 16
            }
          },
        ],
        legend: [
          {
            orient: 'vertical',
            left: 'right',
            y: '2%',
            itemWidth: 15,
            itemHeight: 9,
            itemGap: 5,
            data: yao[dimension],
          },
        ],
        series: [
          {
            data: yao[dimension],
            id: 'pie',
            label: {
              formatter: '{b}: {@[' + dimension + ']} g'
            }
          },
        ]
      });
    }
  });

  // 自适应大小
  window.addEventListener("resize", function () {
    pie_link_bar_graph.resize();
  })
}
