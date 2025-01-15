// @Author: PT
// @CreateTime: 2024-06-05
// @Description:诊断结果图 症状-证素-证关系图
// @Version:1.0

function node_re_graph(data_zheng, data_zs, data_zz, data_link) {
  // 基于准备好的dom，初始化echarts实例
  var node_re_graph = echarts.init(document.getElementById('node_re_graph'));

  // 实体数据
  let dataInfo = [{
    name: data_zheng['name'],
    category: data_zheng['category'],
    value: [100, 150]
  }]
  // 添加证素实体数据
  for (var i = 0; i < data_zs.length; i++) {
    dataInfo[i + 1] = { name: data_zs[i]['name'], category: data_zs[i]['category'], value: [50, 10 + 70 * (data_zs.length - 1 - i)] }
  }
  // 添加症状实体数据
  for (var j = 0; j < data_zz.length; j++) {
    dataInfo[j + 1 + data_zs.length] = { name: data_zz[j]['name'], category: data_zz[j]['category'], value: [0, 20 + 95 * (data_zz.length - 1 - j)] }
  }

  option = {
    title: {
      text: "诊断结果图",
      top: "top",
      left: "center"
    },
    tooltip: {
      trigger: 'item',
      formatter: function (x) {
        // if 为选择节点的时候
        if (x.data.name) {
          str = '标准名：' + x.data.name
        }
        else {
          str = ''
        }
        return str
      }
    },
    legend: {
      orient: 'vertical',
      left: 'right',
      y: '2%',
      itemWidth: 15,
      itemHeight: 9,
      itemGap: 5,
      data: ['症状', '证素', '证']
    },
    animationDuration: 1500,
    animationEasingUpdate: 'quinticInOut',
    xAxis: {
      show: false,
      type: 'value'
    },
    yAxis: {
      show: false,
      type: 'value'
    },
    series: [{
      type: 'graph',
      coordinateSystem: 'cartesian2d',
      legendHoverLink: false,
      hoverAnimation: true,
      nodeScaleRatio: false,
      symbolSize: 60,
      center: ['50%', '50%'],
      edgeSymbol: ['circle', 'arrow'],
      edgeSymbolSize: [2, 10],
      edgeLabel: {
        show: false,
        normal: {
          show: true,
          position: 'middle',
          textStyle: {
            color: 'black',
            fontWeight: 'bold'
          },
          formatter: "{c}"
        }
      },
      focusNodeAdjacency: true,
      roam: true,
      categories: [{
        name: '证',
        itemStyle: {
          normal: {
            color: "rgb(247, 151, 103)",
          }
        }
      }, {
        name: '证素',
        itemStyle: {
          normal: {
            color: "rgb(255, 196, 84)",
          }
        }
      }, {
        name: '症状',
        itemStyle: {
          normal: {
            color: "rgb(241, 102, 103)",
          }
        }
      }],
      //圆形节点上面的文字
      label: {
        normal: {
          position: "inside",
          show: true,
          textStyle: {
            color: '#fff',
            fontSize: 14,
            fontWeight: 'bold'
          },
        }
      },
      force: {
        repulsion: 1000,
      },
      lineStyle: {
        normal: {
          width: 2,
          color: 'rgb(66, 37, 23)'
        }
      },
      data: dataInfo,
      links: data_link
    }]
  }
  node_re_graph.setOption(option)

  // 自适应大小
  window.addEventListener("resize", function () {
    node_re_graph.resize();
  })
}
