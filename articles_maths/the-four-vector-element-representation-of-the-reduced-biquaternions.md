# __The Four-Vector Element Representation of the Reduced Biquaternions__

## Introduction

The **four-vector element representation** reads the reduced biquaternion $T=A+Bj$ as a quadruple of real numbers, $T=(a,a',b,b')$, and at the same time as a pair of complex numbers, $T=(A,B)$, with $A=a+ia'$ and $\langle\cdot\rangle=b+ib'$. The vector part is one-dimensional in the complex reading and two-dimensional in the real one, so the reading is a real quadruple and a complex pair of the same element. This article writes the two, the multiplication in each, the four conjugations in coordinates, the remarkable subspaces as coordinate planes, and the four algebraic norms as formulas on the quadruple. The multiplication is **commutative**, which makes the row reading of the element equal to the column one, and it **has zero divisors**, which the unit criterion records.

**Conventions.** The basis is $1,i,j,ij$ with $i^{2}=-1$, $j^{2}=+1$ and $ji=ij$; the generic element is $T=A+Bj$ with $A=a+ia'$ and $\langle\cdot\rangle=b+ib'$. The idempotent coordinates are $q_1=A+B$ and $q_2=A-B$, and $T=q_1\Pi_{1}+q_2\Pi_{2}$ with $\Pi_{1,2}=\tfrac12(1\pm j)$. The multiplication is the general plain product, the only associative and commutative one of the four; the four products and the forms $\langle\cdot,\cdot\rangle, \langle\cdot,\cdot\rangle_{\natural}, \langle\cdot,\cdot\rangle_{*}, \langle\cdot,\cdot\rangle_{\natural*}$ are *The Four Products, Their Forms and Their Algebraic Norms*. The element glyph is $T$, without a tilde.

**Boundaries.** The basis and the two scalar systems are *Reduced Biquaternions as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$*; the multiplication table in the abstract is *Reduced Biquaternion Space*; the involutions and their fixed spaces are *The Two Involutions and the Group of Involutions*; the subspaces read as coordinate planes are *Introduction to the Remarkable Subspaces of the Reduced Biquaternions*; the four algebraic norms are *The Four Products, Their Forms and Their Algebraic Norms* and *The Forms of the General Plain Algebra of the Reduced Biquaternions*. The other element representations are *Introduction to Reduced Biquaternion Element Representations*, *Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions*, *Reduced Biquaternion Other Algebraic Element Representations* and *Reduced Biquaternions Polar Element Representation*. The biquaternion counterpart is *The Four-Vector Element Representation of Biquaternions*.

## The Coefficient Space

**The element is a real quadruple on the real basis and a complex pair on the complex basis, the two readings carrying the same four real coordinates.**

**Definition.** The **real four-vector** of $T=A+Bj$ is the quadruple $(a,a',b,b')$ of *Reduced Biquaternions as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$*, read on the real basis in the order
$$
T=a\cdot 1+a'\cdot i+b\cdot j+b'\cdot ij ,
$$
and the **complex pair** is $(A,B)$, read on the complex basis $1,j$ over the scalar field $\mathbb{C}$,
$$
T=A\cdot 1+B\cdot j,\qquad A=a+ia',\quad B=b+ib'.
$$

**Proposition (the two readings carry the same data).** The map $T\mapsto(a,a',b,b')$ is an isomorphism of real vector spaces onto $\mathbb{R}^{4}$, and the map $T\mapsto(A,B)$ is an isomorphism of complex vector spaces onto $\mathbb{C}^{2}$; the two are the same map read through $A=a+ia'$ and $\langle\cdot\rangle=b+ib'$, so the real quadruple and the complex pair are two alphabets of one set of four real coordinates.

*Proof.* The four basis elements are linearly independent over $\mathbb{R}$ and every element is a real linear combination of them, which is the first isomorphism; the two elements $1,j$ are linearly independent over $\mathbb{C}$ and every element is a complex combination, which is the second. The passage $A=a+ia'$, $\langle\cdot\rangle=b+ib'$ rewrites the two complex coordinates as the four real ones and back, with no loss.

### Real and Imaginary Parts of the Coordinates

**Each complex coordinate splits into a real part and an imaginary part, and the prime marks the second.**

The real part of $A$ is $a$ and its imaginary part is $a'$; the real part of $\langle\cdot\rangle$ is $b$ and its imaginary part is $b'$. The two parts share the letter of the coordinate, the imaginary part carrying the prime, by *Conventions in Mathematics*, §*The Elements and their Coefficients*. The reader must not confuse the prime of a coefficient with a derivative: no function is being differentiated in this article. The element is written either as $T=a+ia'+bj+ib'j$ or as $T=A+Bj$, and the choice of alphabet is a choice of the representation, not of the element.

## The Column and the Row

**The element is a column and a row, and because the multiplication is commutative the row reading is the column reading.**

**Definition.** The **column** of $T$ is the complex vector $\binom{A}{B}$ on the basis $1,j$, and the real column is $\bigl(a,a',b,b'\bigr)^{\mathsf T}$ on the basis $1,i,j,ij$. The **row** is the transposed quadruple. The left multiplication by $T$ acts on the column, $W\mapsto TW$, and the right multiplication acts on the row, $W\mapsto WT$.

**Proposition (the row equals the column).** The matrix of the left multiplication $L_{T}$ and the matrix of the right multiplication $R_{T}$ on the complex basis $1,j$ coincide, both being
$$
L_{T}=R_{T}=\begin{pmatrix}A&B\\ B&A\end{pmatrix},
$$
so that $TW=WT$ in the representation is the commutativity of the multiplication read as the equality of the two operators.

*Proof.* On the basis, $L_{T}(1)=T=A+Bj$ and $L_{T}(j)=Tj=B+Aj$, giving the columns $\binom{A}{B}$ and $\binom{B}{A}$, hence the displayed matrix; and $R_{T}(1)=T$, $R_{T}(j)=jT=B+Aj$ give the same two columns, so $R_{T}=L_{T}$. The equality $L_{T}=R_{T}$ is the statement that every element commutes with $T$, which is the commutativity of the algebra; in the non-commutative companion the two matrices differ.

## Multiplication in Four-Vector Form

**The multiplication is a real $4\times4$ matrix on the quadruple and a complex $2\times2$ matrix on the pair, and the two are the real and complex forms of the same operator.**

**Theorem (the real four-vector matrix).** For $T=a+ia'+bj+ib'j$, the left multiplication $W\mapsto TW$ on the real basis $1,i,j,ij$ has the matrix
$$
L_{T}=\begin{pmatrix}
a&-a'&b&-b'\\
a'&a&b'&b\\
b&-b'&a&-a'\\
b'&b&a'&a
\end{pmatrix}
=\begin{pmatrix}\tilde A&\tilde B\\ \tilde B&\tilde A\end{pmatrix},
\qquad
\tilde A=\begin{pmatrix}a&-a'\\ a'&a\end{pmatrix},\quad \tilde B=\begin{pmatrix}b&-b'\\ b'&b\end{pmatrix},
$$
where $\tilde A$ and $\tilde B$ are the real $2\times2$ matrices of the multiplication by the complex numbers $A$ and $\langle\cdot\rangle$.

*Proof.* Apply $L_{T}$ to the four basis elements and read the coefficients. On $1$: $T=a\cdot1+a'\cdot i+b\cdot j+b'\cdot ij$ gives the first column. On $i$: $iT=iA+iBj=(ia-a')+(ib-b')j=-a'\cdot1+a\cdot i-b'\cdot j+b\cdot ij$, the second column; on $j$: $jT=Aj+B=b\cdot1+b'\cdot i+a\cdot j+a'\cdot ij$, the third column; on $ij$: $ijT=iAj+iB=(ia-a')j+(ib-b')=-b'\cdot1+b\cdot i-a'\cdot j+a\cdot ij$, the fourth. The block form is read off the display: the two diagonal blocks are both $\tilde A$ and the two off-diagonal blocks both $\tilde B$, because the two coordinates $A$ and $\langle\cdot\rangle$ play the symmetric roles in the product $TW=(AC+BD)+(AD+BC)j$.

**Corollary (the trace and the determinant).** The real matrix has trace $4a=2\operatorname{Re}(q_1+q_2)$ and determinant
$$
\det L_{T}=\bigl|A^{2}-B^{2}\bigr|^{2}=\lvert \langle T\rangle_{\natural}\rvert^{2}=\lvert q_1\rvert^{2}\lvert q_2\rvert^{2},
$$
so the element is a unit exactly when the real matrix of its multiplication is invertible, and the zero divisors are exactly the non-zero elements whose matrix is singular. The complex matrix $\begin{smallmatrix}A&B\\ B&A\end{smallmatrix}$ has trace $2A$ and determinant $\langle T\rangle_{\natural}=q_1q_2$.

*Proof.* The trace is the sum of the four diagonal entries $a+a+a+a$. The determinant of $\begin{smallmatrix}\tilde A&\tilde B\\ \tilde B&\tilde A\end{smallmatrix}$ with commuting blocks $\tilde A,\tilde B$ is $\det(\tilde A^{2}-\tilde B^{2})=\det(\tilde A+\tilde B)\det(\tilde A-\tilde B)$; and $\det(\tilde A+\tilde B)=\lvert A+B\rvert^{2}=\lvert q_1\rvert^{2}$, $\det(\tilde A-\tilde B)=\lvert A-B\rvert^{2}=\lvert q_2\rvert^{2}$, giving the display. The complex matrix has the two real $2\times2$ blocks combined into the complex entries $A,B$, whence trace $2A$ and determinant $A^{2}-B^{2}=\langle T\rangle_{\natural}=q_1q_2$. The unit and zero-divisor readings are the criterion $\langle T\rangle_{\natural}\neq0$ of *Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions*.

**Corollary (multiplicativity).** The four-vector matrices multiply, $L_{T}L_{W}=L_{TW}$, so the map $T\mapsto L_{T}$ is a faithful representation of the algebra by real $4\times4$ matrices with the block structure $\begin{smallmatrix}\tilde A&\tilde B\\ \tilde B&\tilde A\end{smallmatrix}$; the map $T\mapsto\begin{smallmatrix}A&B\\ B&A\end{smallmatrix}$ is the same representation over $\mathbb{C}$.

*Proof.* $L_{T}L_{W}=L_{TW}$ is the associativity of the multiplication, and the injectivity is the theorem of *Introduction to Reduced Biquaternion Element Representations*.

### The Multiplication Table of the Basis

**The products of the four basis elements are the table below.**

| $\cdot$ | $1$ | $i$ | $j$ | $ij$ |
|---|---|---|---|---|
| $1$ | $1$ | $i$ | $j$ | $ij$ |
| $i$ | $i$ | $-1$ | $ij$ | $-j$ |
| $j$ | $j$ | $ij$ | $+1$ | $i$ |
| $ij$ | $ij$ | $-j$ | $i$ | $-1$ |

**Theorem (the table).** The table is symmetric, the multiplication being commutative, and its diagonal is $1,-1,+1,-1$, the three entries past the corner being $i^{2}=-1$, $j^{2}=+1$ and $(ij)^{2}=-1$, the two products $i\cdot j=ij$ and $i\cdot ij=-j$ following from $j^{2}=+1$ and $i^{2}=-1$.

*Proof.* Each entry is the product of two basis elements computed from the relations; the symmetry is the commutativity $ji=ij$ and the equalities read in the table, and the three diagonal entries are the displayed squares.

## The Conjugations in Coordinates

**The three conjugations act on the quadruple by independent sign flips, and the flat is the negative of the star.**

**Theorem (the coordinates of the conjugations).** For $T=a+ia'+bj+ib'j$,
$$
\bar{T}=a-ia'+bj-ib'j=(a,-a',b,-b'),
$$
$$
T^{\natural}=a+ia'-bj-ib'j=(a,a',-b,-b'),
$$
$$
T^{*}=a-ia'-bj+ib'j=(a,-a',-b,b'),
$$
and $T^{\flat}=-T^{*}=(-a,a',b,-b')$.

*Proof.* The bar conjugates the two complex coordinates, $A\mapsto\bar A=a-ia'$ and $B\mapsto\bar B=b-ib'$; the natural sign sends $A+Bj$ to $A-Bj$, that is negates $\langle\cdot\rangle$; the star is the composite $\bar{\cdot}\circ{}^{\natural}$, conjugating $A$ and negating $\langle\cdot\rangle$; the flat is the negative of the star. Reading on the basis gives the quadruples.

**Corollary (the three flips).** The bar flips the second and the fourth coordinates, the natural sign the third and the fourth, and the star the second and the third; the three flips are the three ways of choosing a pair of the three non-scalar coordinates, and their product is the identity on the scalar coordinate. This is the coordinate form of the Klein group of *The Two Involutions and the Group of Involutions*.

*Proof.* Read the three displays: the first coordinate $a$ is fixed by all three, and each of the three remaining coordinates is negated by exactly two of the three maps, the pairs being those displayed.

## The Remarkable Subspaces

**The coordinate planes of the four-vector representation are the remarkable subspaces.**

The fixed and anti-fixed spaces of the three conjugations are the coordinate planes of the real basis: the complex line $\mathbb{C}=\mathbb{R}\{1,i\}$ and its companion $\mathbb{C}j=\mathbb{R}\{j,ij\}$ of the natural sign, the planes $\mathbb{R}\{1,j\}$ and $\mathbb{R}\{i,ij\}$ of the bar, and the planes $\mathbb{R}\{1,ij\}$ and $\mathbb{R}\{i,j\}$ of the star. Their defining equations, bases, dimensions and closure under the multiplication are the tables of *Introduction to the Remarkable Subspaces of the Reduced Biquaternions*, *Decompositions Along the Remarkable Subspaces* and *Comparison of the Remarkable Subspaces*, and the four lines $\mathbb{R}$, $\mathbb{R}i$, $\mathbb{R}j$ and $\mathbb{R}ij$ are the **atoms** of the quadruple, the common eigenlines of the two involutions.

## The Algebraic Norms in Coordinates

**The four algebraic norms are the four quadratic forms of the quadruple below.**

**Theorem (the norms on the quadruple).** For $T=A+Bj=a+ia'+bj+ib'j$,
$$
\langle T\rangle=A^{2}+B^{2}=\bigl(a^{2}-a'^{2}+b^{2}-b'^{2}\bigr)+2i\bigl(aa'+bb'\bigr),
$$
$$
\langle T\rangle_{\natural}=A^{2}-B^{2}=\bigl(a^{2}-a'^{2}-b^{2}+b'^{2}\bigr)+2i\bigl(aa'-bb'\bigr),
$$
$$
\langle T\rangle_{*}=\lvert A\rvert^{2}-\lvert B\rvert^{2}=a^{2}+a'^{2}-b^{2}-b'^{2},
$$
$$
\langle T\rangle_{\natural*}=\lvert A\rvert^{2}+\lvert B\rvert^{2}=a^{2}+a'^{2}+b^{2}+b'^{2}.
$$

*Proof.* Expand $A^{2}=(a+ia')^{2}=a^{2}-a'^{2}+2iaa'$ and $B^{2}=(b+ib')^{2}=b^{2}-b'^{2}+2ibb'$; their sum is $\langle T\rangle$ and their difference is $\langle T\rangle_{\natural}$. The two sesquilinear norms are the sums of the squared real coordinates with the signs of the two complex coordinates, $\langle\cdot\rangle_{*}$ subtracting the $\langle\cdot\rangle$-block and $\langle\cdot\rangle_{\natural*}$ adding it.

**Corollary (the multiplicative one).** Only $\langle\cdot\rangle_{\natural}$ is multiplicative, $\langle TW\rangle_{\natural}=\langle T\rangle_{\natural}\langle W\rangle_{\natural}$, and its vanishing set is the set of zero divisors; the two coordinates $q_1=A+B$ and $q_2=A-B$ give the factored form
$$
\langle T\rangle_{\natural}=q_1q_2,\qquad \lvert q_1\rvert^{2}=(a+b)^{2}+(a'+b')^{2},\qquad \lvert q_2\rvert^{2}=(a-b)^{2}+(a'-b')^{2}.
$$
The complex-valued $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\natural}$ are the bilinear pair, the real-valued $\langle\cdot\rangle_{*}$ and $\langle\cdot\rangle_{\natural*}$ the sesquilinear pair; $\langle\cdot\rangle_{\natural*}$ is the sum of the four squared coordinates, and $\langle\cdot\rangle_{*}$ is the same sum with the last two negated. The metrical reading of $\langle\cdot\rangle_{\natural*}$ — its square root as the Euclidean norm and the metric it defines — belongs to *Topology and Metric for Each of the Operations* and *The Euclidean Topology of the Reduced Biquaternion Algebra*, and is not taken here.

*Proof.* The multiplicativity $\langle TW\rangle_{\natural}=\langle T\rangle_{\natural}\langle W\rangle_{\natural}$ is *The Four Products, Their Forms and Their Algebraic Norms*; $\langle T\rangle_{\natural}=A^{2}-B^{2}=(A+B)(A-B)=q_1q_2$; and the two moduli are the sums of the two squared coordinates of $q_1$ and of $q_2$. The vanishing of $\langle\cdot\rangle_{\natural}$ with $T\neq0$ is the zero-divisor condition of *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*.

### The Unit Criterion in Coordinates

**The element is a unit exactly when both idempotent coordinates are non-zero, and the two conditions are read on the quadruple.**

**Theorem (the unit criterion).** $T$ is a unit if and only if $\langle T\rangle_{\natural}=q_1q_2\neq0$, equivalently
$$
(a+b,a'+b')\neq(0,0)\quad\text{and}\quad(a-b,a'-b')\neq(0,0),
$$
that is $\lvert q_1\rvert^{2}\neq0$ and $\lvert q_2\rvert^{2}\neq0$; the two failure conditions are the two idempotent lines, $\lvert q_1\rvert^{2}=0$ and $\lvert q_2\rvert^{2}=0$, whose union is the zero-divisor set. The inverse in coordinates is
$$
T^{-1}=\frac{A-Bj}{\langle T\rangle_{\natural}}=q_1^{-1}\Pi_{1}+q_2^{-1}\Pi_{2},
$$
with $q_1^{-1}$ and $q_2^{-1}$ the complex inverses.

*Proof.* The criterion $q_1q_2\neq0$ is that of *Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions*; the two factors are $q_1=A+B=(a+b)+i(a'+b')$ and $q_2=A-B=(a-b)+i(a'-b')$, whose moduli are the displayed sums of two squares, and a complex number vanishes exactly when its two real coordinates do. The inverse is the idempotent inverse of *The Group of Units of the General Plain Algebra of the Reduced Biquaternions*, read in the two coordinates.

## Summary

The reduced biquaternion element is a real quadruple $T=(a,a',b,b')$ on the basis $1,i,j,ij$ and a complex pair $T=(A,B)$ on the basis $1,j$, with $A=a+ia'$ and $\langle\cdot\rangle=b+ib'$. The left multiplication is the real $4\times4$ matrix with the $\begin{smallmatrix}\tilde A&\tilde B\\ \tilde B&\tilde A\end{smallmatrix}$ block structure and the complex $2\times2$ matrix $\begin{smallmatrix}A&B\\ B&A\end{smallmatrix}$; the **multiplication is commutative**, so the row and the column readings coincide, and the trace and determinant are $4a$ and $\lvert \langle T\rangle_{\natural}\rvert^{2}$ in the real model, $2A$ and $\langle T\rangle_{\natural}$ in the complex one. The basis table is symmetric, with the squares $-1,+1,-1$ on the diagonal. The bar flips the second and fourth coordinates, the natural sign the third and fourth, and the star the second and third. The remarkable subspaces are the coordinate planes, and the four algebraic norms on the quadruple are $\langle\cdot\rangle=\bigl(a^{2}-a'^{2}+b^{2}-b'^{2}\bigr)+2i(aa'+bb')$, $\langle\cdot\rangle_{\natural}=\bigl(a^{2}-a'^{2}-b^{2}+b'^{2}\bigr)+2i(aa'-bb')$, $\langle\cdot\rangle_{*}=a^{2}+a'^{2}-b^{2}-b'^{2}$ and $\langle\cdot\rangle_{\natural*}=a^{2}+a'^{2}+b^{2}+b'^{2}$. The element is a unit exactly when both idempotent coordinates $q_1=A+B$ and $q_2=A-B$ are non-zero; the multiplication **has zero divisors**, the two idempotent lines, and is **not a division algebra**.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(a,a',b,b')$ | the real four-vector of $T$ on the basis $1,i,j,ij$ |
| $(A,B)$ | the complex pair of $T$ on the basis $1,j$, $A=a+ia'$, $\langle\cdot\rangle=b+ib'$ |
| $\tilde A,\tilde B$ | the real $2\times2$ matrices of the multiplication by $A$ and by $\langle\cdot\rangle$ |
| $L_{T}=\begin{smallmatrix}A&B\\ B&A\end{smallmatrix}$ | the matrix of the multiplication, complex form |
| $q_1=A+B$, $q_2=A-B$ | the idempotent coordinates |
| $\langle\cdot,\cdot\rangle, \langle\cdot,\cdot\rangle_{\natural}, \langle\cdot,\cdot\rangle_{*}, \langle\cdot,\cdot\rangle_{\natural*}$ | the four algebraic norms on the quadruple |

## Further Reading

- *Reduced Biquaternions as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$* (`articles_maths/reduced-biquaternions-as-a-vector-space-over-r-and-c.md`), for the two scalar systems and the two coordinate readings.
- *Reduced Biquaternion Space* (`articles_maths/reduced-biquaternion-space.md`), for the multiplication table in the abstract.
- *The Two Involutions and the Group of Involutions* (`articles_maths/the-two-involutions-and-the-group-of-involutions-of-the-reduced-biquaternions.md`), for the conjugations and their fixed spaces.
- *The Four Products, Their Forms and Their Algebraic Norms* (`articles_maths/the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.md`), for the four products and the norms.
- *Introduction to the Remarkable Subspaces of the Reduced Biquaternions* (`articles_maths/introduction-to-the-remarkable-subspaces-of-the-reduced-biquaternions.md`), for the coordinate planes.
- *The Four-Vector Element Representation of Biquaternions* (`articles_maths/the-four-vector-element-representation-of-biquaternions.md`), for the non-commutative companion, where the row and the column differ.
