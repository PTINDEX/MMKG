// @Author: PT
// @CreateTime: 2024-06-05
// @Description:证素雷达图
// @Version:1.0

function radar_graph(new_zs, l, zzbm) {
  var radar_graph = echarts.init(document.getElementById('radar_graph'));
  // 证素
  var zs_rg = new_zs
  // 证素得分
  var score_rg = l

  // 找到得分最高的分，+1当边的最大值
  var countzz = zzbm.length
  var countzs = zs_rg.length
  var datamax1 = 0
  for (var i = 0; i < countzs; i++) {
    for (var j = 0; j < countzz; j++) {
      if (score_rg[i][j] > datamax1) {
        datamax1 = score_rg[i][j]
      }
    }
  }
  datamax1 = datamax1 + 1

  // 计算每个证素总得分
  var num = 0
  for (var i = 0; i < countzz; i++) {
    num += score[0][i]
  }

  // 症状放在雷达图最外边的角
  var dataname = zzbm
  // 指示器的内容设置
  var indicator = []
  for (var i = 0; i < dataname.length; i++) {
    indicator.push({
      name: dataname[i],
      max: datamax1
    })
  }

  option = {
    legend: {
      data: [`${zs_rg[0]}`],
      orient: 'horizontal',
      icon: "circle",
      right: '5%',
      top: '5%',
      itemWidth: 8,
      itemHeight: 8,
      textStyle: {
        fontSize: '18',
        color: 'rgba(0,0,0,0.8)',
        fontWeight: 'bold'
      },
    },
    title: [{
      text: [`{span|${zs_rg[0]}${num}分}`],
      bottom: 'center',
      left: 'center',
      textStyle: {
        rich: {
          span: {
            fontSize: 20,
            color: '#000',
          }
        }
      }
    },
    {
      text: '证素得分图',
      left: '1%',
      top: '5%',
    }],
    radar: {
      center: ["50%", "50%"],
      radius: "65%",
      splitArea: {
        areaStyle: {
          color: ['rgb(251,246,240)'].reverse(),
        }
      },
      axisLine: {
        show: true,
        lineStyle: {
          color: "#ccc"
        }
      },
      splitLine: {
        show: true,
        lineStyle: {
          color: "#ccc"
        }
      },
      name: {
        formatter: function (name) {
          var i = dataname.indexOf(name)
          return `{name3|${name}} {name1|${score_rg[0][i]}}`
        },
        lineHeight: 0,
        rich: {
          name1: {
            color: '#000',
            align: 'center'
          },
          name3: {
            color: '#606266',
            align: 'center'
          }
        }
      },
      indicator: indicator
    },
    series: [{
      name: `${zs_rg[0]}`,
      type: "radar",
      symbol: "none",
      areaStyle: {
        normal: {
          color: 'rgb(151,115,91)',
        }
      },
      itemStyle: {
        color: 'rgb(151,115,91)',
      },
      lineStyle: {
        width: 0
      },
      data: [score_rg[0]]
    }]
  }
  radar_graph.setOption(option)

  // 自动轮播
  var setint = {
    currentIndex: -1,
  };
  // 轮一轮停止
  var count_lb = 0;
  var int = setInterval(function () {
    // 记录到第几个证素了
    var a = (setint.currentIndex++) % countzs
    count_lb = count_lb + 1
    if (count_lb > countzs) {
      clearInterval(int);
    }
    // 计算总得分
    var num = 0
    for (var i = 0; i < countzz; i++) {
      num = num + score_rg[a][i]
    }
    // 保留一位小数（四舍五入）
    num = num.toFixed(1)

    radar_graph.setOption(option = {
      legend: {
        data: [`${zs_rg[a]}`],
        orient: 'horizontal',
        icon: "circle",
        right: '5%',
        top: '5%',
        itemWidth: 8,
        itemHeight: 8,
        textStyle: {
          fontSize: '18',
          color: 'rgba(0,0,0,0.8)',
          fontWeight: 'bold'
        },
      },
      title: [{
        text: [`{span|${zs_rg[a]}${num}分}`],
        bottom: 'center',
        left: 'center',
        textStyle: {
          rich: {
            span: {
              fontSize: 20,
              color: '#000'
            }
          }
        }
      },
      {
        text: '证素得分图',
        left: '1%',
        top: '5%',
      }],
      radar: {
        center: ["50%", "50%"],
        radius: "65%",
        splitArea: {
          areaStyle: {
            color: ['rgb(251,246,240)'].reverse(),
          }
        },
        axisLine: {
          show: true,
          lineStyle: {
            color: "#ccc"
          }
        },
        splitLine: {
          show: true,
          lineStyle: {
            color: "#ccc"
          }
        },
        name: {
          formatter: function (name) {
            var i = dataname.indexOf(name)
            return `{name3|${name}} {name1|${score_rg[a][i]}}`
          },
          lineHeight: 0,
          rich: {
            name1: {
              color: '#000',
              align: 'center'
            },
            name3: {
              color: '#606266',
              align: 'center',
            }
          }
        },
        indicator: indicator
      },
      series: [{
        name: `${zs_rg[a]}`,
        type: "radar",
        symbol: "none",
        areaStyle: {
          normal: {
            color: 'rgb(151,115,91)',
          }
        },
        itemStyle: {
          color: 'rgb(151,115,91)',
        },
        lineStyle: {
          width: 0
        },
        data: [score_rg[a]]
      }]
    })
  }, 1500);

  // 自适应大小
  window.addEventListener("resize", function () {
    radar_graph.resize();
  })
}
