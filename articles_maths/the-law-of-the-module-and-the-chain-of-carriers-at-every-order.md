# __The Law of the Module and the Chain of Carriers at Every Order__

## Introduction

**The subject.** One sentence produces every row of the tower: the module of a row is the defining space of its copy, the algebra of a row is the square of that module, and the module of the next row is the algebra of this one. The article states the law without a frame, derives the chain of carriers at the first two orders, and shows how the kernel of the copy's action on the module decides which labels are integral and which are not.

**The order of the article.** The law and its consequences come first. The first row is computed from a two-dimensional spinor space, the second from the four-dimensional module, then the kernel and the two readings, and the behaviour of the half-integer under conjugation closes the article.

**It assumes** *The Clebsch–Gordan Decomposition of the Biquaternion Algebra* and *The Three Rows of the Tower*. **The row of the elements is** the first instance of the law, where a two-dimensional defining space produces a four-dimensional algebra.

**The result in one line.** From a module of dimension $d$ the law produces an algebra of dimension $d^{2}$, a slot $\tfrac{d-1}{2}$ for that algebra read as a module, and a chain of carriers whose dimensions are the odd numbers from one to $2d-1$; at $d=2$ the chain is $3+1$ and at $d=4$ it is $7+5+3+1$.

**Boundaries.** The comparison of the three rows is *The Three Rows of the Tower*; the survey of the second row is *The Spin Content: Spin $\tfrac32$ on the Module and $0,1,2,3$ on the Algebra*; the construction of the spinor space is *The Minimal Left Ideals of the Biquaternion Algebra*.

## The Law

**Definition.** A **row** consists of a defining space, which is a module for a copy of the rotation algebra, and of the endomorphism algebra of that space. The defining space is the **module** of the row and the endomorphism algebra is the **algebra** of the row.

**Law.** Let $d$ be the dimension of the module of a row.
$$
\text{algebra of the row}=\operatorname{End}(\text{module}),\qquad \dim=d^{2},\qquad
\text{module of the next row}=\text{algebra of this row}.
$$
The slot of the row, the label of its module, is $\tfrac{d-1}{2}$, and the carriers of the row are the summands of the addition rule applied to the module with itself.

*Proof.* The endomorphism algebra of a space of dimension $d$ has dimension $d^{2}$. The module of the next row is that algebra by definition of the tower, and its dimension is therefore $d^{2}$. A carrier of label $j$ has dimension $2j+1$, so a module of dimension $d$ that is a single carrier has label $\tfrac{d-1}{2}$; the carriers of the row are the summands of the square of that label.

**Corollary.** The slot determines the chain: a row of slot $j$ has carriers of labels $0,1,\dots,2j$, and the number of carriers is $2j+1=d$.

*Proof.* The addition rule for $j$ with itself gives the labels from zero to $2j$, each once, and there are $2j+1$ of them.

**The reading.** The law is one sentence about an endomorphism algebra and its square, and nothing in it refers to a basis or a frame. It is the reason every row of the tower has the same shape.

## The Chain at the First Row

**Theorem.** At $d=2$ the law produces the algebra of dimension four, the slot $\tfrac12$, and the chain $3+1$.

*Proof.* The module is a minimal left ideal of the algebra, of complex dimension two. Its endomorphism algebra is the algebra itself, of dimension four. Its slot is $\tfrac{2-1}{2}=\tfrac12$, and the addition rule at $j=\tfrac12$ gives
$$
\tfrac12\otimes\tfrac12=V_1\oplus V_0 ,
$$
of dimensions $3+1=4$.

**Corollary.** The two carriers of the first row are the traceless part of the algebra and its centre, and the labels one and zero are placed on them by the projectors built from the quaternion conjugation.

*Proof.* The algebra splits as the vector part and the scalar line, of real dimensions three and one, and the two projectors are the ones attached to the conjugation.

**The reading.** The first row is the smallest instance of the law and the only one in which the module is a spinor space of dimension two. The half-integer label belongs to the module and not to any summand, which is the first appearance of the distinction that governs the whole tower.

## The Chain at the Second Row

**Theorem.** At $d=4$ the law produces the operator space of dimension sixteen, the slot $\tfrac32$, and the chain $7+5+3+1$.

*Proof.* The module of the second row is the algebra of the first, of dimension four. Its endomorphism algebra has dimension sixteen. Its slot is $\tfrac{4-1}{2}=\tfrac32$, and the addition rule gives
$$
\tfrac32\otimes\tfrac32=V_3\oplus V_2\oplus V_1\oplus V_0 ,
$$
of dimensions $7+5+3+1=16$.

**Corollary.** The number of carriers doubles from the first row to the second, from two to four, and the dimensions are the odd numbers from one to seven.

*Proof.* The number of carriers is $d$, which is two at the first row and four at the second; the dimensions are $2k+1$ for $k$ from zero to the slot.

**The reading.** The second row is the row of this batch of articles, and its chain is the one that the carriers of the preceding articles divide among themselves. The law produces the four labels without a computation, and the dimension count $7+5+3+1$ is the check on it.

## The Cube and the Square

**Proposition.** The phrase that the module of the next row is the cube of the module is correct at the first step and not at the second.

*Proof.* The symmetric cube of a two-dimensional space has dimension four, which is the algebra of the first row, so the cube and the algebra agree there. The symmetric cube of a four-dimensional space has dimension twenty, while the algebra of the second row has dimension sixteen; the two differ, and the algebra is the correct module of the third row.

**Corollary.** The law is the statement that the module of the next row is the algebra, and the cube is a coincidence of the first step.

*Proof.* The dimensions four and sixteen are the squares of two and four, and only the first of them is also the symmetric cube of the module.

**The reading.** The correction matters because the third row is otherwise miscomputed: its slot is $\tfrac{15}{2}$ from a module of dimension sixteen, and not the slot that a cube of dimension twenty would give.

## The Kernel and the Two Readings

**Proposition.** The element $-\mathrm I$ of the copy acts as the identity on the algebra and as minus the identity on the module, and this is why the labels of the summands are integers while the label of the module is a half-integer.

*Proof.* The copy acts on the algebra by conjugation, and conjugation by $-\mathrm I$ is the identity map. It acts on the module by multiplication, and $-\mathrm I$ multiplies every module vector by $-1$. A label is integral exactly when the element $-\mathrm I$ of the copy acts trivially, since the weights of the module are shifted by one half under the double cover and those of the algebra are not.

**Corollary.** The half-integer label occurs on the module and on no summand of any row.

*Proof.* The summands are subspaces of an algebra on which $-\mathrm I$ acts trivially, so their weights are integral.

**Corollary.** The two readings of the law, by the module and by the algebra, give the same dimension and different labels.

*Proof.* The module of a row and the algebra of the row have dimensions $d$ and $d^{2}$, with slots $\tfrac{d-1}{2}$ and integral labels; the algebra is not a single carrier.

**The reading.** The kernel of the action is the source of the half-integer. It is trivial on the algebra and nontrivial on the module, and the difference between the two labels is the difference between the two actions.

## The Half-Integer under Conjugation

**Proposition.** Under the quaternion conjugation the half-integer label of the module becomes an integer, and the module and its conjugate are the same carrier.

*Proof.* The conjugation is complex linear on the algebra and sends a weight to its negative; on the module it is antilinear and sends the weight $m$ to $-m$, which leaves the string invariant and preserves the label. The label of the module is therefore unchanged by the conjugation.

**Corollary.** Every label that appears in a row is integral after conjugation, and the half-integer is a property of the reading and not of the carrier.

*Proof.* The conjugation preserves the string of a carrier and reverses the sign of the weights; a half-integer string is invariant as a set and its label is unchanged.

**The reading.** The half-integer is not an anomaly of the tower but its signature: it lives on the defining space and it disappears when the algebra is read. The law is one sentence about the square and the cube, and every table of a row is an instance of it.

## Further Reading

- [The Three Rows of the Tower](the-three-rows-of-the-tower.html), for the comparison of the rows.
- [The Spin Content: Spin $\tfrac32$ on the Module and $0,1,2,3$ on the Algebra](the-spin-content-of-the-biquaternion-operators.html), for the second row in one place.
- [The Clebsch–Gordan Decomposition of the Biquaternion Algebra](the-clebsch-gordan-decomposition-of-the-biquaternion-algebra.html), for the addition rule at the first row.
- [The Minimal Left Ideals of the Biquaternion Algebra](the-minimal-left-ideals-of-the-biquaternion-algebra.html), for the spinor space.
- [From the Spin to the Carriers and the Closures](the-carriers-the-representation-the-spin-and-the-closure.html), for the labels of the algebra.
