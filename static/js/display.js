// @Author: PT
// @CreateTime: 2024-06-05
// @Description:图谱展示
// @Version:1.0

const body = document.querySelector('body'),
  shell = body.querySelector('nav'),
  toggle = body.querySelector('.toggle');

// 点击toggle元素时触发事件
toggle.addEventListener("click", () => {
  // 切换shell元素的close类
  shell.classList.toggle("close");
})

// 推荐搜索词点击事件
var change = document.getElementById("search");
// 咳嗽标签点击事件
function ksClick() {
  change.value = "咳嗽"
}
// 舌淡标签点击事件
function sdClick() {
  change.value = "舌淡"
}

// 知识图谱关系图 + 点击节点显示属性
function kg_gxt(data1, links1, categories1) {
  var myChart = echarts.init(document.getElementById('kg_graph'));
  var data1 = data1;
  var links1 = links1;
  var categories1 = categories1;

  option = {
    tooltip: {
      trigger: 'item',
      formatter: function (x) {
        // if 为选择节点的时候
        if (x.data.id) {
          str = '标准名：' + x.data.name
        }
        else {
          if (x.data.score == null) {
            if (x.data.jl == null) {
              str = ''
            }
            else {
              str = '剂量为：' + x.data.jl
            }
          }
          else {
            str = '得分为：' + x.data.score
          }
        }
        return str
      }
    },
    toolbox: {
      show: true,
      feature: {
        // 保存为图片
        saveAsImage: {
          show: true
        }
      }
    },
    legend: [{
      data: categories1.map(function (a) {
        return a.name;
      }),
      y: '1%',
      x: '5%'
    }],
    series: [{
      type: 'graph',
      layout: 'force',
      symbolSize: 60,
      roam: true,
      edgeSymbol: ['circle', 'arrow'],
      edgeSymbolSize: [2, 10],
      edgeLabel: {
        normal: {
          textStyle: {
            fontSize: 20
          }
        }
      },
      force: {
        repulsion: 1000,
        edgeLength: [8, 15]
      },
      draggable: true,
      lineStyle: {
        normal: {
          width: 3,
          color: 'rgb(66, 37, 23)'
        }
      },
      edgeLabel: {
        normal: {
          show: true,
          textStyle: {
            color: 'black',
            fontWeight: 'bold'
          },
          formatter: function (x) {
            // 边上显示文字
            return x.data.name;
          }
        }
      },
      label: {
        normal: {
          show: true,
          textStyle: {
            color: 'black',
            fontSize: '14',
            fontWeight: 'bold'
          },
          position: 'inside',
          distance: 5,
          formatter: function (x) {
            // 节点上显示文字
            return x.data.name
          }
        }
      },
      focusNodeAdjacency: true,
      // 数据
      data: data1,
      links: links1,
      categories: categories1,
      color: ['rgb(241, 102, 103)', 'rgb(87, 199, 227)', 'rgb(236, 181, 201)', 'rgb(247, 151, 103)', 'rgb(255, 196, 84)', 'rgb(141, 204, 147)', 'rgb(217, 200, 174)']
    }],
  };

  myChart.setOption(option);

  var change = document.getElementById("change");
  var s1 = document.getElementById("s1");
  var s2 = document.getElementById("s2");
  var s3 = document.getElementById("s3");
  var s4 = document.getElementById("s4");
  var s5 = document.getElementById("s5");
  var s6 = document.getElementById("s6");
  var s7 = document.getElementById("s7");
  var s8 = document.getElementById("s8");
  var s9 = document.getElementById("s9");
  var s10 = document.getElementById("s10");
  var s11 = document.getElementById("s11");
  var s12 = document.getElementById("s12");

  myChart.on('click', function (params) {
    // 点击相应节点，在卡片中显示该节点的image
    if (params.data.category == '症状') {
      var img = params.data.image
      change.src = img

      var a1 = 'ID：'
      s1.innerHTML = a1

      var a2 = params.data.ID
      s2.innerHTML = a2

      var a3 = '标准名：'
      s3.innerHTML = a3

      var a4 = params.data.name
      s4.innerHTML = a4

      var a5 = '拼音：'
      s5.innerHTML = a5

      var a6 = params.data.py
      s6.innerHTML = a6

      var a7 = '种类：'
      s7.innerHTML = a7

      var a8 = params.data.zl
      s8.innerHTML = a8

      var a9 = ''
      s9.innerHTML = a9

      var a10 = ''
      s10.innerHTML = a10

      var a11 = ''
      s11.innerHTML = a11

      var a12 = ''
      s12.innerHTML = a12
    }

    if (params.data.category == '症状别名') {
      var img = '../static/images/中药.png'
      change.src = img

      var a1 = 'ID：'
      s1.innerHTML = a1

      var a2 = params.data.ID
      s2.innerHTML = a2

      var a3 = '其标准名：'
      s3.innerHTML = a3

      var a4 = params.data.bzm
      s4.innerHTML = a4

      var a5 = '别名：'
      s5.innerHTML = a5

      var a6 = params.data.name
      s6.innerHTML = a6

      var a7 = '拼音：'
      s7.innerHTML = a7

      var a8 = params.data.py
      s8.innerHTML = a8

      var a9 = ''
      s9.innerHTML = a9

      var a10 = ''
      s10.innerHTML = a10

      var a11 = ''
      s11.innerHTML = a11

      var a12 = ''
      s12.innerHTML = a12
    }

    if (params.data.category == '症状种类') {
      var img = '../static/images/中药.png'
      change.src = img

      var a1 = 'ID：'
      s1.innerHTML = a1

      var a2 = params.data.ID
      s2.innerHTML = a2

      var a3 = '标准名：'
      s3.innerHTML = a3

      var a4 = params.data.name
      s4.innerHTML = a4

      var a5 = '拼音：'
      s5.innerHTML = a5

      var a6 = params.data.py
      s6.innerHTML = a6

      var a7 = ''
      s7.innerHTML = a7

      var a8 = ''
      s8.innerHTML = a8

      var a9 = ''
      s9.innerHTML = a9

      var a10 = ''
      s10.innerHTML = a10

      var a11 = ''
      s11.innerHTML = a11

      var a12 = ''
      s12.innerHTML = a12
    }

    if (params.data.category == '证') {
      var img = '../static/images/中药.png'
      change.src = img

      var a1 = 'ID：'
      s1.innerHTML = a1

      var a2 = params.data.ID
      s2.innerHTML = a2

      var a3 = '标准名：'
      s3.innerHTML = a3

      var a4 = params.data.name
      s4.innerHTML = a4

      var a5 = '种类：'
      s5.innerHTML = a5

      var a6 = params.data.zl
      s6.innerHTML = a6

      var a7 = '必有证素：'
      s7.innerHTML = a7

      var a8 = params.data.byzs
      s8.innerHTML = a8

      var a9 = '或有证素：'
      s9.innerHTML = a9

      var a10 = params.data.hyzs
      s10.innerHTML = a10

      var a11 = '脏腑：'
      s11.innerHTML = a11

      var a12 = params.data.zf
      s12.innerHTML = a12
    }

    if (params.data.category == '证素') {
      var img = '../static/images/中药.png'
      change.src = img

      var a1 = 'ID：'
      s1.innerHTML = a1

      var a2 = params.data.ID
      s2.innerHTML = a2

      var a3 = '标准名：'
      s3.innerHTML = a3

      var a4 = params.data.name
      s4.innerHTML = a4

      var a5 = '拼音：'
      s5.innerHTML = a5

      var a6 = params.data.py
      s6.innerHTML = a6

      var a7 = '是否为病位：'
      s7.innerHTML = a7

      var a8 = params.data.bw
      s8.innerHTML = a8

      var a9 = ''
      s9.innerHTML = a9

      var a10 = ''
      s10.innerHTML = a10

      var a11 = ''
      s11.innerHTML = a11

      var a12 = ''
      s12.innerHTML = a12
    }

    if (params.data.category == '代表方') {
      var img = '../static/images/中药.png'
      change.src = img

      var a1 = 'ID：'
      s1.innerHTML = a1

      var a2 = params.data.ID
      s2.innerHTML = a2

      var a3 = '代表方：'
      s3.innerHTML = a3

      var a4 = params.data.name
      s4.innerHTML = a4

      var a5 = ''
      s5.innerHTML = a5

      var a6 = ''
      s6.innerHTML = a6

      var a7 = ''
      s7.innerHTML = a7

      var a8 = ''
      s8.innerHTML = a8

      var a9 = ''
      s9.innerHTML = a9

      var a10 = ''
      s10.innerHTML = a10

      var a11 = ''
      s11.innerHTML = a11

      var a12 = ''
      s12.innerHTML = a12
    }

    if (params.data.category == '中药') {
      var img = params.data.image
      change.src = img

      var a1 = 'ID：'
      s1.innerHTML = a1

      var a2 = params.data.ID
      s2.innerHTML = a2

      var a3 = '中药名：'
      s3.innerHTML = a3

      var a4 = params.data.name
      s4.innerHTML = a4

      var a5 = '性味：'
      s5.innerHTML = a5

      var a6 = params.data.xw
      s6.innerHTML = a6

      var a7 = '归经：'
      s7.innerHTML = a7

      var a8 = params.data.gj
      s8.innerHTML = a8

      var a9 = ''
      s9.innerHTML = a9

      var a10 = ''
      s10.innerHTML = a10

      var a11 = ''
      s11.innerHTML = a11

      var a12 = ''
      s12.innerHTML = a12
    }
  })

  // 自适应大小
  window.addEventListener("resize", function () {
    myChart.resize();
  })
}
