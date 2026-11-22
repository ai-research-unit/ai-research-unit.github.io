# __The Intersection Table: Where Each Carrier Meets $\operatorname{Sym}$ and $\Lambda$__

## Introduction

**The subject.** The sixteen splits twice: into the two squares of dimensions ten and six, and into the four carriers of dimensions seven, five, three and one. The article tabulates the intersections of the two decompositions, checks the margins, and shows that the table is forced by the parity rule: each carrier lies wholly in one square, so the table is diagonal and the two decompositions are compatible without mixing.

**The order of the article.** The table comes first; its margins and its forcing second. The alternating pattern of the entries follows, then the comparison with the row of the elements, and the reading closes.

**It assumes** *The Parity Rule: $\operatorname{Sym}^{2}=V_3\oplus V_1$ and $\Lambda^{2}=V_2\oplus V_0$*, *The Symmetric and Antisymmetric Parts of the Operator Space* and *The Clebsch–Gordan Decomposition: $\tfrac32\otimes\tfrac32=\bigoplus_{k=0}^{3}V_k$*. **The row of the elements is** where the table has two rows and two columns; here it has four rows and two columns.

**The result in one line.** The intersections are $(7,0)$, $(0,5)$, $(3,0)$ and $(0,1)$ for the labels $3,2,1,0$, so each carrier meets exactly one square, in its full dimension.

**Boundaries.** The parity rule is *The Parity Rule*; the failure of invariance under the Cartan element is *Neither Half Is Invariant*; the carriers are defined in *The Clebsch–Gordan Decomposition: $\tfrac32\otimes\tfrac32=\bigoplus_{k=0}^{3}V_k$*.

## The Table

**Theorem.** The intersection of each carrier with each square has the dimensions
$$
\begin{array}{c|cc|c}
 & \operatorname{Sym}^{2} & \Lambda^{2} & \text{total}\\ \hline
V_3 & 7 & 0 & 7\\
V_2 & 0 & 5 & 5\\
V_1 & 3 & 0 & 3\\
V_0 & 0 & 1 & 1\\ \hline
\text{total} & 10 & 6 & 16
\end{array}
$$

*Proof.* The parity rule states that the symmetric square is the sum of the carriers of odd label and the alternating square the sum of those of even label; the intersections are therefore the carriers themselves or zero, according to the parity.

**Corollary.** The row sums are the carrier dimensions and the column sums are the square dimensions, so the table is a decomposition of the sixteen in two directions.

*Proof.* Each row sums to the dimension of its carrier, each column to the dimension of its square, and the total is sixteen in both directions.

**Corollary.** The table has no zero row and no zero column, so neither decomposition is contained in the other.

*Proof.* Each carrier meets one square in its full dimension, and each square contains two carriers.

**The reading.** The table is the record of how the two decompositions of the sixteen meet, and the record is as simple as possible: a diagonal table with the four carrier dimensions on it.

## The Margins

**Proposition.** The margins of the table are the only data the two decompositions share, and they are the numbers $10,6$ and $7,5,3,1$.

*Proof.* The margins are the dimensions of the two squares and of the four carriers, and they are computed without reference to each other.

**Corollary.** The table is determined by its margins and by the parity rule, and no further choice enters.

*Proof.* With each carrier confined to one square, the entries are the carrier dimensions placed in the column of its parity.

**Corollary.** A table with a row split between the two columns would contradict the parity rule, and with it the assignment of the labels.

*Proof.* A carrier lying in both squares would have to be a sum of an odd and an even part, and the parity of its label would be undefined.

**The reading.** The margins are the two dimension counts, and the parity is the only structural input. This is why the table can be written without computing a single intersection: the parity decides all eight entries.

## The Alternating Pattern

**Theorem.** Read along the labels from three to zero, the entries of the symmetric column alternate between the full carrier dimension and zero, and the entries of the alternating column do the opposite.

*Proof.* The parity of the label decides the column, and consecutive labels have opposite parity.

**Corollary.** The carrier of the highest label lies in the symmetric square and the carrier of the lowest label in the alternating square.

*Proof.* The labels three and zero.

**Corollary.** The sum of the symmetric column is one more than the sum of the alternating column, and the difference is four.

*Proof.* $10-6=4$, the dimension of the module.

**The reading.** The alternating pattern is the parity rule read along the table. It is the reason the two columns have the totals they have, and it is the only pattern the table displays.

## The Comparison with the Row of the Elements

**Proposition.** In the row of the elements the table has the two rows $V_1$ and $V_0$ with entries $(3,0)$ and $(0,1)$, and the margins are $3,1$ and $3,1$.

*Proof.* The parity rule for the two-dimensional module.

**Corollary.** The larger table is the smaller one doubled in the number of rows, with the parity preserved throughout.

*Proof.* The four labels of the larger table are the two of the smaller one together with the two new ones, and the parity assignment is the same.

**Corollary.** The two tables have the same column totals ratio, ten to six and three to one, and the ratios differ.

*Proof.* $10/6=5/3$ and $3/1=3$.

**The reading.** The tables of the two rows have the same shape of alternation and different margins. The difference is the number of carriers per square, and this is the only difference the intersection data records.

## The Two Halves as Unions of Carriers

**Proposition.** The symmetric square is the sum of the carriers of labels three and one, of dimensions $7+3=10$, and the alternating square is the sum of the carriers of labels two and zero, of dimensions $5+1=6$.

*Proof.* The addition rule for the symmetric square of the module of label $\tfrac32$ gives the carriers of labels three and one, and the rule for the alternating square gives those of labels two and zero.

**Corollary.** The two halves have dimensions ten and six, and each is a union of two carriers, so the intersection table with the halves is the table with the carriers read in pairs.

*Proof.* The dimensions and the table.

**Corollary.** The parity of the label decides the half, and the sign of the symmetry is therefore an invariant of the carrier and not of the vector.

*Proof.* A carrier lies in one half and its label has a fixed parity.

**The reading.** The splitting into symmetric and alternating parts is coarser than the splitting into carriers but finer than the whole space, and it is the only intermediate splitting of the four. A vector of the space knows which half it lies in before it knows which carrier, and the two facts are decided by the same parity.

## The Reading

**The table is the whole statement.** Two decompositions of one space meet in a table whose entries are forced, once the parity rule is known. Nothing in the table requires the values of the operators, and nothing in it depends on a choice of basis.

**The table is not a coincidence.** The diagonality is the statement that a carrier has a definite parity, which is the statement that the labels are integers and the module has half-integer weight. The two facts are one fact, read on the sixteen.

**The table has a cost.** Because each carrier sits in one square, the projection onto a square is a sum of two carrier projectors and not a single one, and a computation that needs one carrier has to subtract the other. This is the price of the diagonality, and it is a small one.

## Further Reading

- [The Parity Rule: $\operatorname{Sym}^{2}=V_3\oplus V_1$ and $\Lambda^{2}=V_2\oplus V_0$](the-parity-rule-the-two-squares-of-the-module.html), for the assignment of the carriers to the squares.
- [The Symmetric and Antisymmetric Parts of the Operator Space](the-symmetric-and-antisymmetric-parts-of-the-biquaternion-operator-space.html), for the two halves.
- [Neither Half Is Invariant: the Cartan Element Carries $\operatorname{Sym}$ into $\Lambda$](neither-half-is-invariant-the-cartan-element.html), for the action that does not respect the table.
- [The Clebsch–Gordan Decomposition: $\tfrac32\otimes\tfrac32=\bigoplus_{k=0}^{3}V_k$](the-clebsch-gordan-decomposition-of-the-biquaternion-operators.html), for the four carriers.
