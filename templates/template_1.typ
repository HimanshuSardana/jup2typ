#let title(content) = [
  #box(width: 100%, fill: blue.lighten(80%), inset: 10pt)[
    #align(center + horizon)[
      #text(font: "Montserrat", weight: "bold", size: 12pt, fill: blue)[#content]
    ]
  ]
]

#let question(number, body) = context [
  #box(inset: 10pt, width: 100%, stroke: (thickness: 1pt, dash: "dashed", paint: blue))[
    #text(font: "Montserrat", weight: "bold", size: 10pt, fill: blue)[Question #number] \
    #text(font: "Montserrat", weight: "medium")[#body]
  ]
]

#let solution(content) = [
  #box(inset: 10pt, width: 100%, stroke: (thickness: 1.3pt, dash: "dashed", paint: blue))[
    #text(font: "Montserrat", weight: "bold", size: 10pt, fill: blue)[Solution] \
    #v(-2mm)
    #text(font: "Montserrat", size: 10pt)[#content]
  ]
]

#let output(content) = [
  #box(inset: 5pt, width: 100%)[
    #text(font: "Montserrat", weight: "bold", size: 10pt, fill: blue)[Output] \
    #v(-2mm)
    #text(font: "Montserrat", size: 10pt)[#content]
  ]
]
