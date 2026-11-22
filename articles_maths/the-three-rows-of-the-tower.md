# __The Three Rows of the Tower__

## Introduction

**The subject.** The biquaternion algebra sits in a tower of three rows. The first row is the algebra itself, of complex dimension four; the second is its operator space, of dimension sixteen; the third is the operator space of the second order, of dimension two hundred and fifty-six. The article compares the three rows, their slots, their addition rules, and the two copies of the rotation algebra that act on the same sixteen-dimensional space.

**The order of the article.** The three rows are defined first. The slot of a row and the law that produces the next row follow, then the two small addition rules, the coincidence of spaces with a difference of labels, and the arithmetic of the third row.

**It assumes** *The Clebsch–Gordan Decomposition of the Biquaternion Algebra* and *$\operatorname{End}(\mathbb{B})$ as an Algebra: the Regular Representation*. **The row of the elements is** the first of the three, and the row of the operators is the second; the third is reached from the second by the same construction.

**The result in one line.** The three rows have dimensions $4,16,256$, slots $\tfrac12,\tfrac32,\tfrac{15}{2}$, and addition rules whose carrier dimensions are $3+1$, $7+5+3+1$ and the sum of the first sixteen odd numbers, which is $256$.

**Boundaries.** The row of the elements is the subject of the two articles on the Clebsch–Gordan series and on the carriers; the second row is the subject of this batch of articles; the general form of the law is *The Law of the Module and the Chain of Carriers at Every Order*.

## The Three Rows

**Definition.** The **row of the elements** is the algebra $\mathbb{B}$ itself, of complex dimension four, read as a module for the copy of the rotation algebra that the algebra carries. The **row of the operators** is $\operatorname{End}(\mathbb{B})$, of complex dimension sixteen. The **row of the second order** is $\operatorname{End}(\operatorname{End}(\mathbb{B}))$, of complex dimension two hundred and fifty-six.

**Proposition.** The three dimensions are the squares of the dimensions of the modules, and the modules have dimensions $2,4,16$.

*Proof.* The module of the first row is a minimal left ideal, of dimension two, and the algebra is the square of the module. The module of the second row is the algebra of the first, of dimension four, and the operator space is its square. The module of the third row is the operator space, of dimension sixteen, and the second-order space is its square.

**Corollary.** The **slot** of a row, the label of its module, is $\tfrac12$, $\tfrac32$ and $\tfrac{15}{2}$.

*Proof.* A carrier of label $j$ has dimension $2j+1$, so a module of dimension $d$ has slot $\tfrac{d-1}{2}$; at $d=2,4,16$ this gives the three values.

**Corollary.** The slot of each row is one half of the square root of the dimension of its algebra, minus one half.

*Proof.* The dimension of the algebra is $d^{2}$, so $\tfrac{d-1}{2}=\tfrac{\sqrt{d^{2}}-1}{2}$.

**The reading.** The tower is built by squaring. Every row is the endomorphism algebra of the row below, and the module of every row is the algebra below it; the slots grow from one half to three halves to fifteen halves.

## The Slot of a Row

**Proposition.** The module of a row is irreducible for its copy when its dimension is a power of two, and the slot is then determined by the dimension alone.

*Proof.* The carriers of the copy are labelled by the non-negative half-integers and the carrier of label $j$ has dimension $2j+1$; a dimension of the form $2^{m}$ is odd only at $m=0$, so the module of dimension $4$ or $16$ must be irreducible of the corresponding label, and the label is read from the dimension.

**Corollary.** The module of the second row is the carrier of label $\tfrac32$, of dimension four, and the module of the third row is the carrier of label $\tfrac{15}{2}$, of dimension sixteen.

*Proof.* The dimension formula, at four and at sixteen.

**Corollary.** The two readings of a row, by label and by dimension, agree on the module and disagree on the algebra.

*Proof.* The module is a single carrier and its label is $\tfrac{d-1}{2}$; the algebra is the square of the module and decomposes into several carriers, whose labels run from $d-1$ down to zero.

**The reading.** The slot is a property of the module, and the algebra has no single slot. The phrase the slot of a row always refers to the module, and the carriers of the row are the summands of the algebra.

## The Two Small Rules

**Proposition.** The two first rows obey
$$
\tfrac12\otimes\tfrac12=V_1\oplus V_0,\qquad
\tfrac32\otimes\tfrac32=V_3\oplus V_2\oplus V_1\oplus V_0,
$$
of dimensions $3+1=4$ and $7+5+3+1=16$.

*Proof.* The addition rule for two labels $j,j'$ gives the sum of the carriers of labels $\lvert j-j'\rvert$ to $j+j'$, each once; at $j=j'=\tfrac12$ this is $1,0$ and at $j=j'=\tfrac32$ this is $3,2,1,0$.

**Corollary.** The labels of the second row are the integers from zero to three, and the labels of the first row are zero and one.

*Proof.* The two squares displayed.

**Corollary.** The carrier dimensions of the second row are the odd numbers from one to seven, and their sum is the dimension of the row.

*Proof.* The labels zero to three give dimensions $2j+1$, and $1+3+5+7=16$.

**The reading.** The first two rows are the two smallest instances of one rule. The first has two carriers and the second four, and the number of carriers is the slot of the row plus one.

## The Same Sixteen, Two Copies

**Proposition.** The sixteen of the second row is the same algebra as the operator space of a two-dimensional defining space, and the two descriptions differ in the copy that is read on it.

*Proof.* Both are the endomorphisms of a four-dimensional space: one because the biquaternion algebra is four-dimensional, the other because the defining space of dimension two has a symmetric cube of dimension four. The two algebras are isomorphic, and the isomorphism is not a map of modules for the two copies.

**Corollary.** The same sixteen carries the labels $0,1,2,3$ under one copy and the labels $0,1$ under another.

*Proof.* Under the principal copy, the copy acting by the commutator, the sixteen is $\tfrac32\otimes\tfrac32$ and its labels are $0,1,2,3$. Under the copy acting by left multiplication alone, the sixteen is the algebra tensored with its opposite, on which the left copy acts through the algebra's own module $V_1\oplus V_0$, so the labels are $0$ and $1$, the triplet four times and the singlet four times.

**Corollary.** The dimensions of the carriers coincide under the two readings only for the labels that both readings possess, and the labels themselves do not coincide.

*Proof.* Both readings contain the labels zero and one; the readings differ in that one contains two and three and the other does not.

**The reading.** Two rows may be the same space and not the same representation. The identity of the underlying algebra is not an identity of modules, and every statement about carriers has to name the copy under which it is made.

## The Third Row

**Proposition.** The third row obeys
$$
\tfrac{15}{2}\otimes\tfrac{15}{2}=\bigoplus_{k=0}^{15}V_k ,
$$
with sixteen summands, and the sum of the carrier dimensions is
$$
\sum_{k=0}^{15}(2k+1)=16^{2}=256 .
$$

*Proof.* The addition rule at $j=j'=\tfrac{15}{2}$ gives the labels from zero to fifteen, each once, and the sum of the first sixteen odd numbers is the square of sixteen.

**Corollary.** The number of carriers of a row is the slot plus one, which is $2,4,16$ for the three rows.

*Proof.* The labels run from zero to the slot, and the slot plus one is the dimension of the module.

**Corollary.** The third row contains a carrier of every integer label from zero to fifteen, and its top carrier has dimension thirty-one.

*Proof.* The labels of the sum, and the dimension formula at $k=15$.

**The reading.** The arithmetic of the third row is the arithmetic of the second, applied to a module four times as large. The rule has sixteen terms, the top carrier has dimension thirty-one, and the sum is the square of the row's module.

## Further Reading

- [The Law of the Module and the Chain of Carriers at Every Order](the-law-of-the-module-and-the-chain-of-carriers-at-every-order.html), for the general form of the law.
- [The Spin Content: Spin $\tfrac32$ on the Module and $0,1,2,3$ on the Algebra](the-spin-content-of-the-biquaternion-operators.html), for the second row in one place.
- [The Clebsch–Gordan Decomposition of the Biquaternion Algebra](the-clebsch-gordan-decomposition-of-the-biquaternion-algebra.html), for the first row.
- [$\operatorname{End}(\mathbb{B})$ as an Algebra: the Regular Representation](end-b-as-an-algebra-the-regular-representation.html), for the second row as an algebra.
- [Introduction to the Spin-Three Carrier: the Top of the Chain](introduction-to-the-spin-three-carrier-the-top-of-the-chain.html), for the top carrier of the second row.
