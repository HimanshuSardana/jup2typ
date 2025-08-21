#import "@preview/showybox:2.0.4": showybox

#let title(body) = [
  #box(
    width: 100%,
    inset: 10pt,
    radius: 4pt,
    fill: orange.lighten(70%),
    stroke: 1pt + orange.darken(30%),
  )[
    #align(center + horizon)[
      #smallcaps()[#text(size: 12pt, weight: "bold")[= #body]]
    ]
  ]
]

#let question(qno, body) = [
  #showybox(
    frame: (
      border-color: orange,
      title-color: orange,
      body-color: white,
    ),
    title-style: (
      color: white,
      weight: "bold",
      align: left,
      boxed-style: (
        radius: 4pt,
      ),
    ),
    title: [
      #smallcaps()[#text(size: 10pt, weight: "bold")[
          == Question #qno
        ]]
    ],
  )[#body
    #v(1mm)
  ]
]

#let solution(content) = [
  #block(inset: 12pt, radius: 5pt, width: 100%, stroke: (thickness: 1.3pt, dash: "dashed", paint: orange))[
    #text( weight: "bold", size: 9pt, fill: orange)[#smallcaps()[Solution]] \
    #v(-2mm)
    #text( size: 10pt)[#content]
  ]
]

#let output(content) = [
  #block(inset: 5pt, radius: 5pt, width: 100%)[
    #text( weight: "bold", size: 9pt, fill: orange)[#smallcaps()[Output]] \
    #v(-2mm)
    #text(size: 10pt)[#content]
  ]
]
