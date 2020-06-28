(* Content-type: application/vnd.wolfram.mathematica *)

(*** Wolfram Notebook File ***)
(* http://www.wolfram.com/nb *)

(* CreatedBy='Mathematica 12.0' *)

(*CacheID: 234*)
(* Internal cache information:
NotebookFileLineBreakTest
NotebookFileLineBreakTest
NotebookDataPosition[       158,          7]
NotebookDataLength[     16647,        467]
NotebookOptionsPosition[     13942,        412]
NotebookOutlinePosition[     14285,        427]
CellTagsIndexPosition[     14242,        424]
WindowFrame->Normal*)

(* Beginning of Notebook Content *)
Notebook[{
Cell[BoxData[{
 RowBox[{
  RowBox[{"a", " ", "=", " ", "3"}], ";", " ", 
  RowBox[{"b", " ", "=", " ", "4"}], ";", " ", 
  RowBox[{"n", " ", "=", " ", "37"}], ";"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{
   RowBox[{"sumEC", "[", 
    RowBox[{"p1_", ",", "p2_"}], "]"}], ":=", 
   RowBox[{"(", "\[IndentingNewLine]", 
    RowBox[{
     RowBox[{
      RowBox[{"{", 
       RowBox[{"x1", ",", "y1"}], "}"}], " ", "=", " ", "p1"}], ";", " ", 
     RowBox[{
      RowBox[{"{", 
       RowBox[{"x2", ",", "y2"}], "}"}], " ", "=", " ", "p2"}], ";", 
     "\[IndentingNewLine]", 
     RowBox[{"If", "[", 
      RowBox[{
       RowBox[{"p1", "\[Equal]", "p2"}], ",", "\[IndentingNewLine]", 
       RowBox[{"s", " ", "=", " ", 
        RowBox[{"Mod", "[", 
         RowBox[{
          RowBox[{
           RowBox[{"(", 
            RowBox[{
             RowBox[{"3", "*", 
              RowBox[{"x1", "^", "2"}]}], " ", "+", " ", "a"}], ")"}], "*", 
           RowBox[{"ModularInverse", "[", 
            RowBox[{
             RowBox[{"2", "*", "y1"}], ",", "n"}], "]"}]}], ",", "n"}], 
         "]"}]}], ",", "\[IndentingNewLine]", 
       RowBox[{"s", " ", "=", " ", 
        RowBox[{"Mod", "[", 
         RowBox[{
          RowBox[{
           RowBox[{"(", 
            RowBox[{"y2", "-", "y1"}], ")"}], "*", 
           RowBox[{"ModularInverse", "[", 
            RowBox[{
             RowBox[{"x2", "-", "x1"}], ",", "n"}], "]"}]}], ",", "n"}], 
         "]"}]}]}], "]"}], ";", "\[IndentingNewLine]", 
     RowBox[{"Print", "[", "s", "]"}], ";", "\[IndentingNewLine]", 
     RowBox[{"Mod", "[", 
      RowBox[{
       RowBox[{"{", 
        RowBox[{
         RowBox[{
          RowBox[{"s", "^", "2"}], "-", "x1", "-", "x2"}], ",", 
         RowBox[{
          RowBox[{"s", "*", 
           RowBox[{"(", 
            RowBox[{"x1", "-", 
             RowBox[{"(", 
              RowBox[{
               RowBox[{"s", "^", "2"}], "-", "x1", "-", "x2"}], ")"}]}], 
            ")"}]}], "-", "y1"}]}], "}"}], ",", "n"}], "]"}]}], 
    "\[IndentingNewLine]", ")"}]}], ";"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{
   RowBox[{"sumEC", "[", "p1_", "]"}], " ", ":=", " ", 
   RowBox[{"sumEC", "[", 
    RowBox[{"p1", ",", "p1"}], "]"}]}], ";"}]}], "Input",
 CellChangeTimes->{{3.800213970112854*^9, 3.8002140501335626`*^9}, {
   3.800214081958521*^9, 3.8002144403328753`*^9}, {3.800214501458599*^9, 
   3.800214544237414*^9}, {3.80021479085603*^9, 3.8002148135117135`*^9}, {
   3.8002151938781047`*^9, 3.8002151961600437`*^9}, {3.8002154470009346`*^9, 
   3.8002154584628153`*^9}, 3.8002158978152885`*^9, {3.8002957212443333`*^9, 
   3.800295738267318*^9}, {3.800295870427247*^9, 3.8002958750580144`*^9}, 
   3.8006517933756146`*^9, {3.8006532905457435`*^9, 3.8006533009552*^9}, {
   3.800653390603329*^9, 3.8006534200562553`*^9}, {3.8006535911905375`*^9, 
   3.80065359137809*^9}, 3.800653887226659*^9, {3.8006539540078783`*^9, 
   3.8006539604937315`*^9}},
 CellLabel->
  "In[111]:=",ExpressionUUID->"c87ef0ad-d030-423e-a32a-c39bcc607b06"],

Cell[CellGroupData[{

Cell[BoxData[
 RowBox[{"sumEC", "[", 
  RowBox[{
   RowBox[{"{", 
    RowBox[{"0", ",", 
     RowBox[{"-", "1"}]}], "}"}], ",", 
   RowBox[{"{", 
    RowBox[{"2", ",", "1"}], "}"}]}], "]"}]], "Input",
 CellChangeTimes->{{3.800214430534483*^9, 3.800214432835773*^9}, {
  3.800214463151246*^9, 3.8002144725590563`*^9}},
 CellLabel->"In[27]:=",ExpressionUUID->"b8d27c1e-590b-4931-aa66-e291dfd89f51"],

Cell[BoxData[
 RowBox[{"{", 
  RowBox[{"1000000006", ",", "2"}], "}"}]], "Output",
 CellChangeTimes->{3.8002144745035496`*^9, 3.80021450790138*^9, 
  3.8002145506942315`*^9},
 CellLabel->"Out[27]=",ExpressionUUID->"a4d2c6f5-e929-42cd-bba8-17a32bac20fc"]
}, Open  ]],

Cell[BoxData[{
 RowBox[{"7", " ", "\[Rule]", " ", "a"}], "\[IndentingNewLine]", 
 RowBox[{"(", 
  RowBox[{"7", ",", "3"}], ")"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{"y", "^", "2"}], " ", "=", " ", 
  RowBox[{
   RowBox[{"x", "^", "3"}], " ", "+", " ", 
   RowBox[{"a", "*", "x"}], " ", "+", " ", "b"}]}]}], "Input",
 CellChangeTimes->{{3.800214709824953*^9, 3.800214729369326*^9}, {
  3.8002151162060413`*^9, 3.800215128860577*^9}, {3.8002958010079556`*^9, 
  3.8002958063061347`*^9}},ExpressionUUID->"a5f5fb1c-2d63-4d8b-b1ab-\
e80d5c82f2e3"],

Cell[CellGroupData[{

Cell[BoxData[
 RowBox[{"Mod", "[", 
  RowBox[{
   RowBox[{"(", 
    RowBox[{
     RowBox[{"3", "^", "2"}], "-", 
     RowBox[{"7", "^", "3"}], "-", 
     RowBox[{"7", "*", "7"}]}], ")"}], ",", "127"}], "]"}]], "Input",
 CellChangeTimes->{{3.8002147409505177`*^9, 3.800214781716203*^9}, {
  3.800295821532797*^9, 3.8002958587560177`*^9}},
 CellLabel->"In[9]:=",ExpressionUUID->"7aacd24c-3e2b-4a61-92df-94b0ba13ad0c"],

Cell[BoxData["125"], "Output",
 CellChangeTimes->{
  3.800214785676781*^9, {3.800295848079775*^9, 3.8002958592249007`*^9}},
 CellLabel->"Out[9]=",ExpressionUUID->"8314d5db-5a56-47c9-85cb-2890fc345f4d"]
}, Open  ]],

Cell[CellGroupData[{

Cell[BoxData[
 RowBox[{"16", " ", "\[Equal]", " ", 
  RowBox[{
   RowBox[{"1", "^", "3"}], " ", "+", " ", 
   RowBox[{"13", "*", "1"}], " ", "+", " ", "2"}]}]], "Input",
 CellChangeTimes->{{3.800215145147892*^9, 3.8002151612858524`*^9}},
 CellLabel->"In[38]:=",ExpressionUUID->"23d6ffc5-bb92-4bc0-a52a-345b4cf2b319"],

Cell[BoxData["True"], "Output",
 CellChangeTimes->{3.80021516198142*^9},
 CellLabel->"Out[38]=",ExpressionUUID->"6f669d05-9753-4afc-9dfe-2aa57de94685"]
}, Open  ]],

Cell[CellGroupData[{

Cell[BoxData[
 RowBox[{"TableForm", "[", 
  RowBox[{"NestList", "[", 
   RowBox[{"sumEC", ",", 
    RowBox[{"{", 
     RowBox[{"7", ",", "3"}], "}"}], ",", "4"}], "]"}], "]"}]], "Input",
 CellChangeTimes->{{3.8002154049989862`*^9, 3.800215406233729*^9}, {
   3.8002154364200897`*^9, 3.8002155091018505`*^9}, {3.8002155489598837`*^9, 
   3.8002155530387883`*^9}, 3.8002159056716166`*^9, {3.800215955069483*^9, 
   3.800215959828227*^9}, {3.8002972843954177`*^9, 3.800297285864524*^9}, {
   3.800297319884014*^9, 3.8002973202180386`*^9}},
 CellLabel->"In[20]:=",ExpressionUUID->"750ac28c-4338-41bc-96a3-4f99a63ddac4"],

Cell[BoxData[
 TagBox[GridBox[{
    {"7", "3"},
    {"38", "48"},
    {"73", "115"},
    {"94", "5"},
    {"84", "94"}
   },
   GridBoxAlignment->{"Columns" -> {{Left}}, "Rows" -> {{Baseline}}},
   GridBoxSpacings->{"Columns" -> {
       Offset[0.27999999999999997`], {
        Offset[2.0999999999999996`]}, 
       Offset[0.27999999999999997`]}, "Rows" -> {
       Offset[0.2], {
        Offset[0.4]}, 
       Offset[0.2]}}],
  Function[BoxForm`e$, 
   TableForm[BoxForm`e$]]]], "Output",
 CellChangeTimes->{{3.800215482399688*^9, 3.800215509509343*^9}, 
   3.800215553370082*^9, 3.8002159063749533`*^9, {3.800215956184836*^9, 
   3.800215960297782*^9}, {3.8002972957882476`*^9, 3.8002973205730534`*^9}},
 CellLabel->
  "Out[20]//TableForm=",ExpressionUUID->"a4433dad-494a-4025-9ea6-\
7cfc17fb6ee7"]
}, Open  ]],

Cell[CellGroupData[{

Cell[BoxData[
 RowBox[{"Fold", "[", 
  RowBox[{"sumEC", ",", " ", 
   RowBox[{"{", 
    RowBox[{
     RowBox[{"{", 
      RowBox[{"38", ",", "48"}], "}"}], ",", 
     RowBox[{"{", 
      RowBox[{"94", ",", "5"}], "}"}], ",", 
     RowBox[{"{", 
      RowBox[{"84", ",", "94"}], "}"}]}], "}"}]}], "]"}]], "Input",
 CellChangeTimes->{{3.800297478466427*^9, 3.8002975398442945`*^9}},
 CellLabel->"In[21]:=",ExpressionUUID->"2b79875a-d968-4fa6-bf44-e004c029c7db"],

Cell[BoxData[
 RowBox[{"{", 
  RowBox[{"7", ",", "124"}], "}"}]], "Output",
 CellChangeTimes->{3.8002975412313952`*^9},
 CellLabel->"Out[21]=",ExpressionUUID->"06756c51-8099-44dd-be9a-52cc0c48213c"]
}, Open  ]],

Cell[BoxData[{
 RowBox[{
  RowBox[{"a", " ", "=", " ", 
   RowBox[{"-", "4"}]}], ";", " ", 
  RowBox[{"b", " ", "=", " ", "1"}], ";", " ", 
  RowBox[{"n", " ", "=", " ", "127"}], ";"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{
   RowBox[{"sumECnM", "[", 
    RowBox[{"p1_", ",", "p2_"}], "]"}], ":=", 
   RowBox[{"(", "\[IndentingNewLine]", 
    RowBox[{
     RowBox[{
      RowBox[{"{", 
       RowBox[{"x1", ",", "y1"}], "}"}], " ", "=", " ", "p1"}], ";", " ", 
     RowBox[{
      RowBox[{"{", 
       RowBox[{"x2", ",", "y2"}], "}"}], " ", "=", " ", "p2"}], ";", 
     "\[IndentingNewLine]", 
     RowBox[{"If", "[", 
      RowBox[{
       RowBox[{"p1", "\[Equal]", "p2"}], ",", "\[IndentingNewLine]", 
       RowBox[{"s", " ", "=", " ", 
        RowBox[{
         RowBox[{"(", 
          RowBox[{
           RowBox[{"3", "*", 
            RowBox[{"x1", "^", "2"}]}], " ", "+", " ", "a"}], ")"}], "/", 
         RowBox[{"(", 
          RowBox[{"2", "*", "y1"}], ")"}]}]}], ",", "\[IndentingNewLine]", 
       RowBox[{"s", " ", "=", " ", 
        RowBox[{
         RowBox[{"(", 
          RowBox[{"y2", "-", "y1"}], ")"}], "/", 
         RowBox[{"(", 
          RowBox[{"x2", "-", "x1"}], ")"}]}]}]}], "]"}], ";", 
     "\[IndentingNewLine]", 
     RowBox[{"{", 
      RowBox[{
       RowBox[{
        RowBox[{"s", "^", "2"}], "-", "x1", "-", "x2"}], ",", 
       RowBox[{
        RowBox[{"s", "*", 
         RowBox[{"(", 
          RowBox[{"x1", "-", 
           RowBox[{"(", 
            RowBox[{
             RowBox[{"s", "^", "2"}], "-", "x1", "-", "x2"}], ")"}]}], 
          ")"}]}], "-", "y1"}]}], "}"}]}], "\[IndentingNewLine]", ")"}]}], 
  ";"}], "\[IndentingNewLine]", 
 RowBox[{
  RowBox[{
   RowBox[{"sumECnM", "[", "p1_", "]"}], " ", ":=", " ", 
   RowBox[{"sumEC", "[", 
    RowBox[{"p1", ",", "p1"}], "]"}]}], ";"}]}], "Input",
 CellChangeTimes->{{3.800298020776411*^9, 3.8002981367447414`*^9}, {
  3.8006524701166086`*^9, 3.8006525918858347`*^9}, {3.800652641662654*^9, 
  3.8006527657338953`*^9}, {3.8006531414859276`*^9, 3.8006531426108274`*^9}},
 CellLabel->"In[74]:=",ExpressionUUID->"d78f5f7f-25ac-49a3-9474-8ebbb7d9f858"],

Cell[CellGroupData[{

Cell[BoxData[
 RowBox[{"sumECnM", "[", 
  RowBox[{
   RowBox[{"{", 
    RowBox[{"0", ",", 
     RowBox[{"-", "1"}]}], "}"}], ",", 
   RowBox[{"{", 
    RowBox[{"2", ",", "1"}], "}"}]}], "]"}]], "Input",
 CellChangeTimes->{{3.8002980933369136`*^9, 3.800298109455194*^9}, {
  3.8002981548320456`*^9, 3.800298160599478*^9}},
 CellLabel->"In[27]:=",ExpressionUUID->"d6aa6b61-2adb-4703-8fc5-6fd1f5be6d95"],

Cell[BoxData[
 RowBox[{"{", 
  RowBox[{
   RowBox[{"-", "1"}], ",", "2"}], "}"}]], "Output",
 CellChangeTimes->{3.8002981616865454`*^9},
 CellLabel->"Out[27]=",ExpressionUUID->"10ee2b72-d234-4a61-8834-b8794fdbee0d"]
}, Open  ]],

Cell[CellGroupData[{

Cell[BoxData[
 RowBox[{"sumECnM", "[", 
  RowBox[{
   RowBox[{"{", 
    RowBox[{
     RowBox[{"-", "1"}], ",", "2"}], "}"}], ",", 
   RowBox[{"{", 
    RowBox[{"2", ",", "1"}], "}"}]}], "]"}]], "Input",
 CellChangeTimes->{{3.8002981703659306`*^9, 3.8002981725071945`*^9}},
 CellLabel->"In[28]:=",ExpressionUUID->"a2f86985-0fda-4abe-8450-05f60de3284c"],

Cell[BoxData[
 RowBox[{"{", 
  RowBox[{
   RowBox[{"-", 
    FractionBox["8", "9"]}], ",", 
   RowBox[{"-", 
    FractionBox["53", "27"]}]}], "}"}]], "Output",
 CellChangeTimes->{3.8002981738237114`*^9},
 CellLabel->"Out[28]=",ExpressionUUID->"3eb0aa8f-be7d-47b1-b8f2-b0cff05ce3b8"]
}, Open  ]],

Cell[CellGroupData[{

Cell[BoxData[
 RowBox[{"sumECnM", "[", 
  RowBox[{
   RowBox[{"{", 
    RowBox[{"0", ",", 
     RowBox[{"-", "1"}]}], "}"}], ",", 
   RowBox[{"{", 
    RowBox[{
     RowBox[{"-", "1"}], ",", "2"}], "}"}]}], "]"}]], "Input",
 CellChangeTimes->{{3.80029820246786*^9, 3.8002982066878777`*^9}},
 CellLabel->"In[29]:=",ExpressionUUID->"55f10baa-1029-40d4-9b37-3e9bc2d19bc0"],

Cell[BoxData[
 RowBox[{"{", 
  RowBox[{"10", ",", "31"}], "}"}]], "Output",
 CellChangeTimes->{3.8002982070788336`*^9},
 CellLabel->"Out[29]=",ExpressionUUID->"34f08040-2187-491b-be1a-ceae366c87fa"]
}, Open  ]],

Cell[CellGroupData[{

Cell[BoxData[
 RowBox[{"sumECnM", "[", 
  RowBox[{
   RowBox[{"{", 
    RowBox[{"0", ",", 
     RowBox[{"-", "1"}]}], "}"}], ",", 
   RowBox[{"{", 
    RowBox[{"10", ",", "31"}], "}"}]}], "]"}]], "Input",
 CellChangeTimes->{{3.8002982165658274`*^9, 3.8002982189415364`*^9}},
 CellLabel->"In[30]:=",ExpressionUUID->"661376d2-f4b0-48c3-bfc4-674207d6c9c3"],

Cell[BoxData[
 RowBox[{"{", 
  RowBox[{
   FractionBox["6", "25"], ",", 
   FractionBox["29", "125"]}], "}"}]], "Output",
 CellChangeTimes->{3.800298219285409*^9},
 CellLabel->"Out[30]=",ExpressionUUID->"37bfde71-da3e-4602-a46d-31ee06697a2a"]
}, Open  ]],

Cell[CellGroupData[{

Cell[BoxData[
 RowBox[{
  RowBox[{"{", 
   RowBox[{"x", ",", "y"}], "}"}], "=", 
  RowBox[{"sumECnM", "[", 
   RowBox[{
    RowBox[{"{", 
     RowBox[{"10", ",", "31"}], "}"}], ",", 
    RowBox[{"{", 
     RowBox[{
      RowBox[{"-", "1"}], ",", "2"}], "}"}]}], "]"}]}]], "Input",
 CellChangeTimes->{{3.8002982284917192`*^9, 3.800298232150284*^9}, {
  3.8006530919664764`*^9, 3.8006530946923075`*^9}},
 CellLabel->"In[77]:=",ExpressionUUID->"184286f7-4188-43dd-b63d-79407e44e721"],

Cell[BoxData[
 RowBox[{"{", 
  RowBox[{
   RowBox[{"-", 
    FractionBox["248", "121"]}], ",", 
   FractionBox["1021", "1331"]}], "}"}]], "Output",
 CellChangeTimes->{
  3.8002982324442935`*^9, {3.80065204655497*^9, 3.8006520574591627`*^9}, {
   3.800652480358457*^9, 3.8006525336310863`*^9}, {3.8006525639197626`*^9, 
   3.800652595242915*^9}, {3.800652644637558*^9, 3.800652734483073*^9}, 
   3.80065277101956*^9, 3.800653095442532*^9, 3.8006531641239624`*^9},
 CellLabel->"Out[77]=",ExpressionUUID->"d7a4ee4c-7180-4b66-92b5-6c01829c53fd"]
}, Open  ]]
},
WindowSize->{1536, 781},
WindowMargins->{{-8, Automatic}, {Automatic, -8}},
FrontEndVersion->"12.0 for Microsoft Windows (64-bit) (April 8, 2019)",
StyleDefinitions->"Default.nb"
]
(* End of Notebook Content *)

(* Internal cache information *)
(*CellTagsOutline
CellTagsIndex->{}
*)
(*CellTagsIndex
CellTagsIndex->{}
*)
(*NotebookFileOutline
Notebook[{
Cell[558, 20, 3038, 75, 200, "Input",ExpressionUUID->"c87ef0ad-d030-423e-a32a-c39bcc607b06"],
Cell[CellGroupData[{
Cell[3621, 99, 396, 10, 28, "Input",ExpressionUUID->"b8d27c1e-590b-4931-aa66-e291dfd89f51"],
Cell[4020, 111, 253, 5, 32, "Output",ExpressionUUID->"a4d2c6f5-e929-42cd-bba8-17a32bac20fc"]
}, Open  ]],
Cell[4288, 119, 551, 12, 67, "Input",ExpressionUUID->"a5f5fb1c-2d63-4d8b-b1ab-e80d5c82f2e3"],
Cell[CellGroupData[{
Cell[4864, 135, 415, 10, 28, "Input",ExpressionUUID->"7aacd24c-3e2b-4a61-92df-94b0ba13ad0c"],
Cell[5282, 147, 201, 3, 32, "Output",ExpressionUUID->"8314d5db-5a56-47c9-85cb-2890fc345f4d"]
}, Open  ]],
Cell[CellGroupData[{
Cell[5520, 155, 316, 6, 28, "Input",ExpressionUUID->"23d6ffc5-bb92-4bc0-a52a-345b4cf2b319"],
Cell[5839, 163, 151, 2, 32, "Output",ExpressionUUID->"6f669d05-9753-4afc-9dfe-2aa57de94685"]
}, Open  ]],
Cell[CellGroupData[{
Cell[6027, 170, 615, 11, 28, "Input",ExpressionUUID->"750ac28c-4338-41bc-96a3-4f99a63ddac4"],
Cell[6645, 183, 800, 23, 113, "Output",ExpressionUUID->"a4433dad-494a-4025-9ea6-7cfc17fb6ee7"]
}, Open  ]],
Cell[CellGroupData[{
Cell[7482, 211, 459, 12, 28, "Input",ExpressionUUID->"2b79875a-d968-4fa6-bf44-e004c029c7db"],
Cell[7944, 225, 198, 4, 32, "Output",ExpressionUUID->"06756c51-8099-44dd-be9a-52cc0c48213c"]
}, Open  ]],
Cell[8157, 232, 2150, 58, 181, "Input",ExpressionUUID->"d78f5f7f-25ac-49a3-9474-8ebbb7d9f858"],
Cell[CellGroupData[{
Cell[10332, 294, 400, 10, 28, "Input",ExpressionUUID->"d6aa6b61-2adb-4703-8fc5-6fd1f5be6d95"],
Cell[10735, 306, 215, 5, 32, "Output",ExpressionUUID->"10ee2b72-d234-4a61-8834-b8794fdbee0d"]
}, Open  ]],
Cell[CellGroupData[{
Cell[10987, 316, 351, 9, 28, "Input",ExpressionUUID->"a2f86985-0fda-4abe-8450-05f60de3284c"],
Cell[11341, 327, 282, 8, 49, "Output",ExpressionUUID->"3eb0aa8f-be7d-47b1-b8f2-b0cff05ce3b8"]
}, Open  ]],
Cell[CellGroupData[{
Cell[11660, 340, 369, 10, 28, "Input",ExpressionUUID->"55f10baa-1029-40d4-9b37-3e9bc2d19bc0"],
Cell[12032, 352, 198, 4, 32, "Output",ExpressionUUID->"34f08040-2187-491b-be1a-ceae366c87fa"]
}, Open  ]],
Cell[CellGroupData[{
Cell[12267, 361, 353, 9, 28, "Input",ExpressionUUID->"661376d2-f4b0-48c3-bfc4-674207d6c9c3"],
Cell[12623, 372, 242, 6, 49, "Output",ExpressionUUID->"37bfde71-da3e-4602-a46d-31ee06697a2a"]
}, Open  ]],
Cell[CellGroupData[{
Cell[12902, 383, 480, 13, 28, "Input",ExpressionUUID->"184286f7-4188-43dd-b63d-79407e44e721"],
Cell[13385, 398, 541, 11, 49, "Output",ExpressionUUID->"d7a4ee4c-7180-4b66-92b5-6c01829c53fd"]
}, Open  ]]
}
]
*)

