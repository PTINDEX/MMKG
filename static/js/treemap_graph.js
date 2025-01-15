// @Author: PT
// @CreateTime: 2024-06-05
// @Description:矩形树图 证素得分前五
// @Version:1.0

function treemap_graph(zs, score) {
  var treemap_graph = echarts.init(document.getElementById('treemap_graph'));
  // 得分前五证素
  var zs_tg = zs
  // 得分前五证素得分
  var score_tg = score
  var data = []
  function dataReset(zs_tg, score_tg) {
    for (var i = 0; i < 5; i++) {
      data[i] = { name: zs_tg[i], value: score_tg[i] }
    }
  }
  dataReset(zs_tg, score_tg)

  option = {
    title: {
      text: '证素得分前五图',
      left: '1%',
      bottom: '0%'
    },
    series: {
      type: 'treemap',
      itemStyle: {
        borderWidth: 0,
        borderColor: "transparent",
        normal: {
          label: {
            show: true,
            textStyle: {
              fontSize: 16,
              fontWeight: 'bold'
            }
          },
        },
        emphasis: {
          label: {
            show: true
          }
        }
      },
      data: data,
      left: '12%',
      top: '2%',
      // 下面的小黑块（面包屑）
      breadcrumb: {
        left: '48%'
      }
    },
    color: ['rgb(234, 108, 146)', 'rgb(240, 165, 115)', 'rgb(255, 229, 144)', 'rgb(162, 222, 176)', 'rgb(158, 184, 255)'],
  };
  treemap_graph.setOption(option)

  // 自适应大小
  window.addEventListener("resize", function () {
    treemap_graph.resize();
  })
}
