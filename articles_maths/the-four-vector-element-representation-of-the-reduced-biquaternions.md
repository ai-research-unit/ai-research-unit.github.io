# __The Four-Vector Element Representation of the Reduced Biquaternions__

## Introduction

The **four-vector element representation** reads the reduced biquaternion $\breve Q=Q_++jQ_-$ as a quadruple of real numbers, $\breve Q=(q_+,q'_+,q_-,q'_-)$, and at the same time as a pair of complex numbers, $\breve Q=(Q_+,Q_-)$, with $Q_+=q_++iq'_+$ and $Q_-=q_-+iq'_-$. The $j$-part carries one complex coordinate, hence two real ones, so the reading is a real quadruple and a complex pair of the same element. The algebra has no vector part; the name *four-vector* refers to the quadruple of real coordinates, not to a part of the algebra. This article writes the two, the multiplication in each, the four conjugations in coordinates, the remarkable subspaces as coordinate planes, and the four algebraic norms as formulas on the quadruple. The multiplication is **commutative**, which makes the row reading of the element equal to the column one, and it **has zero divisors**, which the unit criterion records.

**Conventions.** The basis is $1,i,j,ij$ with $i^{2}=-1$, $j^{2}=+1$ and $ji=ij$; the generic element is $\breve Q=Q_++jQ_-$ with $Q_+=q_++iq'_+$ and $Q_-=q_-+iq'_-$. The idempotent coordinates are $Q_{++}=Q_++Q_-$ and $Q_{--}=Q_+-Q_-$, and $\breve Q=Q_{++}\Pi_++Q_{--}\Pi_-$ with $\Pi_{\pm}=\tfrac12(1\pm j)$. The multiplication is the general plain product, the only associative and commutative one of the four; the four products and the forms $\langle\cdot,\cdot\rangle, \langle\cdot,\cdot\rangle_{\natural}, \langle\cdot,\cdot\rangle_{*}, \langle\cdot,\cdot\rangle_{\natural*}$ are *The Four Products, Their Forms and Their Algebraic Norms*. The element glyph is $\breve Q$, with the breve and without a tilde.

**Boundaries.** The basis and the two scalar systems are *Reduced Biquaternions as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$*; the multiplication table in the abstract is *Reduced Biquaternion Space*; the involutions and their fixed spaces are *The Two Involutions and the Group of Involutions*; the subspaces read as coordinate planes are *Introduction to the Remarkable Subspaces of the Reduced Biquaternions*; the four algebraic norms are *The Four Products, Their Forms and Their Algebraic Norms* and *The Forms of the Algebra of the Reduced Biquaternions*. The other element representations are *Introduction to Reduced Biquaternion Element Representations*, *Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions*, *Reduced Biquaternion Other Algebraic Element Representations* and *Reduced Biquaternions Polar Element Representation*. The biquaternion counterpart is *The Four-Vector Element Representation of Biquaternions*.

## The Coefficient Space

**The element is a real quadruple on the real basis and a complex pair on the complex basis, the two readings carrying the same four real coordinates.**

**Definition.** The **real four-vector** of $\breve Q=Q_++jQ_-$ is the quadruple $(q_+,q'_+,q_-,q'_-)$ of *Reduced Biquaternions as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$*, read on the real basis in the order
$$
\breve Q=q_+\cdot 1+q'_+\cdot i+q_-\cdot j+q'_-\cdot ij ,
$$
and the **complex pair** is $(Q_+,Q_-)$, read on the complex basis $1,j$ over the scalar field $\mathbb{C}$,
$$
\breve Q=Q_+\cdot 1+Q_-\cdot j,\qquad Q_+=q_++iq'_+,\quad Q_-=q_-+iq'_-.
$$

**Proposition (the two readings carry the same data).** The map $\breve Q\mapsto(q_+,q'_+,q_-,q'_-)$ is an isomorphism of real vector spaces onto $\mathbb{R}^{4}$, and the map $\breve Q\mapsto(Q_+,Q_-)$ is an isomorphism of complex vector spaces onto $\mathbb{C}^{2}$; the two are the same map read through $Q_+=q_++iq'_+$ and $Q_-=q_-+iq'_-$, so the real quadruple and the complex pair are two alphabets of one set of four real coordinates.

*Proof.* The four basis elements are linearly independent over $\mathbb{R}$ and every element is a real linear combination of them, which is the first isomorphism; the two elements $1,j$ are linearly independent over $\mathbb{C}$ and every element is a complex combination, which is the second. The passage $Q_+=q_++iq'_+$, $Q_-=q_-+iq'_-$ rewrites the two complex coordinates as the four real ones and back, with no loss.

### Real and Imaginary Parts of the Coordinates

**Each complex coordinate splits into a real part and an imaginary part, and the prime marks the second.**

The real part of $Q_+$ is $q_+$ and its imaginary part is $q'_+$; the real part of $Q_-$ is $q_-$ and its imaginary part is $q'_-$. The two parts share the letter of the coordinate, the imaginary part carrying the prime, by *Conventions in Mathematics*, §*The Elements and their Coefficients*. The reader must not confuse the prime of a coefficient with a derivative: no function is being differentiated in this article. The element is written either as $\breve Q=q_++iq'_++q_-j+iq'_-j$ or as $\breve Q=Q_++jQ_-$, and the choice of alphabet is a choice of the representation, not of the element.

## The Column and the Row

**The element is a column and a row, and because the multiplication is commutative the row reading is the column reading.**

**Definition.** The **column** of $\breve Q$ is the complex vector $\binom{Q_+}{Q_-}$ on the basis $1,j$, and the real column is $\bigl(q_+,q'_+,q_-,q'_-\bigr)^{\mathsf T}$ on the basis $1,i,j,ij$. The **row** is the transposed quadruple. The left multiplication by $\breve Q$ acts on the column, $\breve Q_{2}\mapsto \breve Q \breve Q_{2}$, and the right multiplication acts on the row, $\breve Q_{2}\mapsto \breve Q_{2}\breve Q$.

**Proposition (the row equals the column).** The matrix of the left multiplication $L_{\breve Q}$ and the matrix of the right multiplication $R_{\breve Q}$ on the complex basis $1,j$ coincide, both being
$$
L_{\breve Q}=R_{\breve Q}=\begin{pmatrix}Q_+&Q_-\\ Q_-&Q_+\end{pmatrix},
$$
so that $\breve Q_{1}\breve Q_{2}=\breve Q_{2}\breve Q_{1}$ in the representation is the commutativity of the multiplication read as the equality of the two operators.

*Proof.* On the basis, $L_{\breve Q}(1)=\breve Q=Q_++jQ_-$ and $L_{\breve Q}(j)=\breve Q j=Q_-+Q_+j$, giving the columns $\binom{Q_+}{Q_-}$ and $\binom{Q_-}{Q_+}$, hence the displayed matrix; and $R_{\breve Q}(1)=\breve Q$, $R_{\breve Q}(j)=j\breve Q=Q_-+Q_+j$ give the same two columns, so $R_{\breve Q}=L_{\breve Q}$. The equality $L_{\breve Q}=R_{\breve Q}$ is the statement that every element commutes with $\breve Q$, which is the commutativity of the algebra; in the non-commutative companion the two matrices differ.

## Multiplication in Four-Vector Form

**The multiplication is a real $4\times4$ matrix on the quadruple and a complex $2\times2$ matrix on the pair, and the two are the real and complex forms of the same operator.**

**Theorem (the real four-vector matrix).** For $\breve Q=q_++iq'_++q_-j+iq'_-j$, the left multiplication $\breve Q_{2}\mapsto \breve Q \breve Q_{2}$ on the real basis $1,i,j,ij$ has the matrix
$$
L_{\breve Q}=\begin{pmatrix}
q_+&-q'_+&q_-&-q'_-\\
q'_+&q_+&q'_-&q_-\\
q_-&-q'_-&q_+&-q'_+\\
q'_-&q_-&q'_+&q_+
\end{pmatrix}
=\begin{pmatrix}A_+&A_-\\ A_-&A_+\end{pmatrix},
\qquad
A_+=\begin{pmatrix}q_+&-q'_+\\ q'_+&q_+\end{pmatrix},\quad A_-=\begin{pmatrix}q_-&-q'_-\\ q'_-&q_-\end{pmatrix},
$$
where $A_+$ and $A_-$ are the real $2\times2$ matrices of the multiplication by the complex numbers $Q_+$ and $Q_-$.

*Proof.* Apply $L_{\breve Q}$ to the four basis elements and read the coefficients. On $1$: $\breve Q=q_+\cdot1+q'_+\cdot i+q_-\cdot j+q'_-\cdot ij$ gives the first column. On $i$: $i\breve Q=iQ_++iQ_-j=(iq_+-q'_+)+(iq_--q'_-)j=-q'_+\cdot1+q_+\cdot i-q'_-\cdot j+q_-\cdot ij$, the second column; on $j$: $j\breve Q=Q_+j+Q_-=q_-\cdot1+q'_-\cdot i+q_+\cdot j+q'_+\cdot ij$, the third column; on $ij$: $ij\breve Q=iQ_+j+iQ_-=(iq_+-q'_+)j+(iq_--q'_-)=-q'_-\cdot1+q_-\cdot i-q'_+\cdot j+q_+\cdot ij$, the fourth. The block form is read off the display: the two diagonal blocks are both $A_+$ and the two off-diagonal blocks both $A_-$, because the two coordinates $Q_+$ and $Q_-$ play the symmetric roles in the product $\breve Q_{1}\breve Q_{2}=(Q_{1+}Q_{2+}+Q_{1-}Q_{2-})+(Q_{1+}Q_{2-}+Q_{1-}Q_{2+})j$.

**Corollary (the trace and the determinant).** The real matrix has trace $4q_+=2\operatorname{Re}(Q_{++}+Q_{--})$ and determinant
$$
\det L_{\breve Q}=\bigl|Q_+^{2}-Q_-^{2}\bigr|^{2}=\lvert \langle \breve Q\rangle_{\natural}\rvert^{2}=\lvert Q_{++}\rvert^{2}\lvert Q_{--}\rvert^{2},
$$
so the element is a unit exactly when the real matrix of its multiplication is invertible, and the zero divisors are exactly the non-zero elements whose matrix is singular. The complex matrix $\begin{smallmatrix}Q_+&Q_-\\ Q_-&Q_+\end{smallmatrix}$ has trace $2Q_+$ and determinant $\langle \breve Q\rangle_{\natural}=Q_{++}Q_{--}$.

*Proof.* The trace is the sum of the four diagonal entries $q_++q_++q_++q_+$. The determinant of $\begin{smallmatrix}A_+&A_-\\ A_-&A_+\end{smallmatrix}$ with commuting blocks $A_+,A_-$ is $\det(A_+^{2}-A_-^{2})=\det(A_++A_-)\det(A_+-A_-)$; and $\det(A_++A_-)=\lvert Q_++Q_-\rvert^{2}=\lvert Q_{++}\rvert^{2}$, $\det(A_+-A_-)=\lvert Q_+-Q_-\rvert^{2}=\lvert Q_{--}\rvert^{2}$, giving the display. The complex matrix has the two real $2\times2$ blocks combined into the complex entries $Q_+,Q_-$, whence trace $2Q_+$ and determinant $Q_+^{2}-Q_-^{2}=\langle \breve Q\rangle_{\natural}=Q_{++}Q_{--}$. The unit and zero-divisor readings are the criterion $\langle \breve Q\rangle_{\natural}\neq0$ of *Norm and Invertibility in the Algebra of the Reduced Biquaternions*.

**Corollary (multiplicativity).** The four-vector matrices multiply, $L_{\breve Q_{1}}L_{\breve Q_{2}}=L_{\breve Q_{1}\breve Q_{2}}$, so the map $\breve Q\mapsto L_{\breve Q}$ is a faithful representation of the algebra by real $4\times4$ matrices with the block structure $\begin{smallmatrix}A_+&A_-\\ A_-&A_+\end{smallmatrix}$; the map $\breve Q\mapsto\begin{smallmatrix}Q_+&Q_-\\ Q_-&Q_+\end{smallmatrix}$ is the same representation over $\mathbb{C}$.

*Proof.* $L_{\breve Q_{1}}L_{\breve Q_{2}}=L_{\breve Q_{1}\breve Q_{2}}$ is the associativity of the multiplication, and the injectivity is the theorem of *Introduction to Reduced Biquaternion Element Representations*.

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

**Theorem (the coordinates of the conjugations).** For $\breve Q=q_++iq'_++q_-j+iq'_-j$,
$$
\bar{\breve Q}=q_+-iq'_++q_-j-iq'_-j=(q_+,-q'_+,q_-,-q'_-),
$$
$$
\breve Q^{\natural}=q_++iq'_+-q_-j-iq'_-j=(q_+,q'_+,-q_-,-q'_-),
$$
$$
\breve Q^{*}=q_+-iq'_+-q_-j+iq'_-j=(q_+,-q'_+,-q_-,q'_-),
$$
and $\breve Q^{\flat}=-\breve Q^{*}=(-q_+,q'_+,q_-,-q'_-)$.

*Proof.* The bar conjugates the two complex coordinates, $Q_+\mapsto\bar Q_+=q_+-iq'_+$ and $Q_-\mapsto\bar Q_-=q_--iq'_-$; the natural sign sends $Q_++jQ_-$ to $Q_+-jQ_-$, that is negates $Q_-$; the star is the composite $\bar{\cdot}\circ{}^{\natural}$, conjugating $Q_+$ and negating $Q_-$; the flat is the negative of the star. Reading on the basis gives the quadruples.

**Corollary (the three flips).** The bar flips the second and the fourth coordinates, the natural sign the third and the fourth, and the star the second and the third; the three flips are the three ways of choosing a pair of the three non-scalar coordinates, and their product is the identity on the scalar coordinate. This is the coordinate form of the Klein group of *The Two Involutions and the Group of Involutions*.

*Proof.* Read the three displays: the first coordinate $q_+$ is fixed by all three, and each of the three remaining coordinates is negated by exactly two of the three maps, the pairs being those displayed.

## The Remarkable Subspaces

**The coordinate planes of the four-vector representation are the remarkable subspaces.**

The fixed and anti-fixed spaces of the three conjugations are the coordinate planes of the real basis: the complex line $\mathbb{C}=\mathbb{R}\{1,i\}$ and its companion $\mathbb{C}j=\mathbb{R}\{j,ij\}$ of the natural sign, the planes $\mathbb{R}\{1,j\}$ and $\mathbb{R}\{i,ij\}$ of the bar, and the planes $\mathbb{R}\{1,ij\}$ and $\mathbb{R}\{i,j\}$ of the star. Their defining equations, bases, dimensions and closure under the multiplication are the tables of *Introduction to the Remarkable Subspaces of the Reduced Biquaternions*, *Decompositions Along the Remarkable Subspaces* and *Comparison of the Remarkable Subspaces*, and the four lines $\mathbb{R}$, $\mathbb{R}i$, $\mathbb{R}j$ and $\mathbb{R}ij$ are the **atoms** of the quadruple, the common eigenlines of the two involutions.

## The Algebraic Norms in Coordinates

**The four algebraic norms are the four quadratic forms of the quadruple below.**

**Theorem (the norms on the quadruple).** For $\breve Q=Q_++jQ_-=q_++iq'_++q_-j+iq'_-j$,
$$
\langle \breve Q\rangle=Q_+^{2}+Q_-^{2}=\bigl(q_+^{2}-(q'_+)^{2}+q_-^{2}-(q'_-)^{2}\bigr)+2i\bigl(q_+q'_++q_-q'_-\bigr),
$$
$$
\langle \breve Q\rangle_{\natural}=Q_+^{2}-Q_-^{2}=\bigl(q_+^{2}-(q'_+)^{2}-q_-^{2}+(q'_-)^{2}\bigr)+2i\bigl(q_+q'_+-q_-q'_-\bigr),
$$
$$
\langle \breve Q\rangle_{*}=\lvert Q_+\rvert^{2}-\lvert Q_-\rvert^{2}=q_+^{2}+(q'_+)^{2}-q_-^{2}-(q'_-)^{2},
$$
$$
\langle \breve Q\rangle_{\natural*}=\lvert Q_+\rvert^{2}+\lvert Q_-\rvert^{2}=q_+^{2}+(q'_+)^{2}+q_-^{2}+(q'_-)^{2}.
$$

*Proof.* Expand $Q_+^{2}=(q_++iq'_+)^{2}=q_+^{2}-(q'_+)^{2}+2iq_+q'_+$ and $Q_-^{2}=(q_-+iq'_-)^{2}=q_-^{2}-(q'_-)^{2}+2iq_-q'_-$; their sum is $\langle \breve Q\rangle$ and their difference is $\langle \breve Q\rangle_{\natural}$. The two sesquilinear norms are the sums of the squared real coordinates with the signs of the two complex coordinates, $\langle\cdot\rangle_{*}$ subtracting the $Q_-$-block and $\langle\cdot\rangle_{\natural*}$ adding it.

**Corollary (the multiplicative one).** Only $\langle\cdot\rangle_{\natural}$ is multiplicative, $\langle \breve Q_{1}\breve Q_{2}\rangle_{\natural}=\langle \breve Q_{1}\rangle_{\natural}\langle \breve Q_{2}\rangle_{\natural}$, and its vanishing set is the set of zero divisors; the two coordinates $Q_{++}=Q_++Q_-$ and $Q_{--}=Q_+-Q_-$ give the factored form
$$
\langle \breve Q\rangle_{\natural}=Q_{++}Q_{--},\qquad \lvert Q_{++}\rvert^{2}=(q_++q_-)^{2}+(q'_++q'_-)^{2},\qquad \lvert Q_{--}\rvert^{2}=(q_+-q_-)^{2}+(q'_+-q'_-)^{2}.
$$
The complex-valued $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\natural}$ are the bilinear pair, the real-valued $\langle\cdot\rangle_{*}$ and $\langle\cdot\rangle_{\natural*}$ the sesquilinear pair; $\langle\cdot\rangle_{\natural*}$ is the sum of the four squared coordinates, and $\langle\cdot\rangle_{*}$ is the same sum with the last two negated. The metrical reading of $\langle\cdot\rangle_{\natural*}$ — its square root as the Euclidean norm and the metric it defines — belongs to *Topology and Metric for Each of the Operations* and *The Euclidean Topology of the Reduced Biquaternion Algebra*, and is not taken here.

*Proof.* The multiplicativity $\langle \breve Q_{1}\breve Q_{2}\rangle_{\natural}=\langle \breve Q_{1}\rangle_{\natural}\langle \breve Q_{2}\rangle_{\natural}$ is *The Four Products, Their Forms and Their Algebraic Norms*; $\langle \breve Q\rangle_{\natural}=Q_+^{2}-Q_-^{2}=(Q_++Q_-)(Q_+-Q_-)=Q_{++}Q_{--}$; and the two moduli are the sums of the two squared coordinates of $Q_{++}$ and of $Q_{--}$. The vanishing of $\langle\cdot\rangle_{\natural}$ with $\breve Q\neq0$ is the zero-divisor condition of *Zero Divisors of the Algebra of the Reduced Biquaternions*.

### The Unit Criterion in Coordinates

**The element is a unit exactly when both idempotent coordinates are non-zero, and the two conditions are read on the quadruple.**

**Theorem (the unit criterion).** $\breve Q$ is a unit if and only if $\langle \breve Q\rangle_{\natural}=Q_{++}Q_{--}\neq0$, equivalently
$$
(q_++q_-,q'_++q'_-)\neq(0,0)\quad\text{and}\quad(q_+-q_-,q'_+-q'_-)\neq(0,0),
$$
that is $\lvert Q_{++}\rvert^{2}\neq0$ and $\lvert Q_{--}\rvert^{2}\neq0$; the two failure conditions are the two idempotent lines, $\lvert Q_{++}\rvert^{2}=0$ and $\lvert Q_{--}\rvert^{2}=0$, whose union is the zero-divisor set. The inverse in coordinates is
$$
\breve Q^{-1}=\frac{Q_+-jQ_-}{\langle \breve Q\rangle_{\natural}}=Q_{++}^{-1}\Pi_++Q_{--}^{-1}\Pi_-,
$$
with $Q_{++}^{-1}$ and $Q_{--}^{-1}$ the complex inverses.

*Proof.* The criterion $Q_{++}Q_{--}\neq0$ is that of *Norm and Invertibility in the Algebra of the Reduced Biquaternions*; the two factors are $Q_{++}=Q_++Q_-=(q_++q_-)+i(q'_++q'_-)$ and $Q_{--}=Q_+-Q_-=(q_+-q_-)+i(q'_+-q'_-)$, whose moduli are the displayed sums of two squares, and a complex number vanishes exactly when its two real coordinates do. The inverse is the idempotent inverse of *The Group of Units of the Algebra of the Reduced Biquaternions*, read in the two coordinates.

## Summary

The reduced biquaternion element is a real quadruple $\breve Q=(q_+,q'_+,q_-,q'_-)$ on the basis $1,i,j,ij$ and a complex pair $\breve Q=(Q_+,Q_-)$ on the basis $1,j$, with $Q_+=q_++iq'_+$ and $Q_-=q_-+iq'_-$. The left multiplication is the real $4\times4$ matrix with the $\begin{smallmatrix}A_+&A_-\\ A_-&A_+\end{smallmatrix}$ block structure and the complex $2\times2$ matrix $\begin{smallmatrix}Q_+&Q_-\\ Q_-&Q_+\end{smallmatrix}$; the **multiplication is commutative**, so the row and the column readings coincide, and the trace and determinant are $4q_+$ and $\lvert \langle \breve Q\rangle_{\natural}\rvert^{2}$ in the real model, $2Q_+$ and $\langle \breve Q\rangle_{\natural}$ in the complex one. The basis table is symmetric, with the squares $-1,+1,-1$ on the diagonal. The bar flips the second and fourth coordinates, the natural sign the third and fourth, and the star the second and third. The remarkable subspaces are the coordinate planes, and the four algebraic norms on the quadruple are $\langle \breve Q\rangle=\bigl(q_+^{2}-(q'_+)^{2}+q_-^{2}-(q'_-)^{2}\bigr)+2i(q_+q'_++q_-q'_-)$, $\langle \breve Q\rangle_{\natural}=\bigl(q_+^{2}-(q'_+)^{2}-q_-^{2}+(q'_-)^{2}\bigr)+2i(q_+q'_+-q_-q'_-)$, $\langle \breve Q\rangle_{*}=q_+^{2}+(q'_+)^{2}-q_-^{2}-(q'_-)^{2}$ and $\langle \breve Q\rangle_{\natural*}=q_+^{2}+(q'_+)^{2}+q_-^{2}+(q'_-)^{2}$. The element is a unit exactly when both idempotent coordinates $Q_{++}=Q_++Q_-$ and $Q_{--}=Q_+-Q_-$ are non-zero; the multiplication **has zero divisors**, the two idempotent lines, and is **not a division algebra**.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(q_+,q'_+,q_-,q'_-)$ | the real four-vector of $\breve Q$ on the basis $1,i,j,ij$ |
| $(Q_+,Q_-)$ | the complex pair of $\breve Q$ on the basis $1,j$, $Q_+=q_++iq'_+$, $Q_-=q_-+iq'_-$ |
| $A_+,A_-$ | the real $2\times2$ matrices of the multiplication by $Q_+$ and by $Q_-$ |
| $L_{\breve Q}=\begin{smallmatrix}Q_+&Q_-\\ Q_-&Q_+\end{smallmatrix}$ | the matrix of the multiplication, complex form |
| $Q_{++}=Q_++Q_-$, $Q_{--}=Q_+-Q_-$ | the idempotent coordinates |
| $\langle \breve Q\rangle, \langle \breve Q\rangle_{\natural}, \langle \breve Q\rangle_{*}, \langle \breve Q\rangle_{\natural*}$ | the four algebraic norms on the quadruple |

## Further Reading

- [Reduced Biquaternions as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$](reduced-biquaternions-as-a-vector-space-over-r-and-c.html), for the two scalar systems and the two coordinate readings.
- [Reduced Biquaternion Space](reduced-biquaternion-space.html), for the multiplication table in the abstract.
- [The Two Involutions and the Group of Involutions](the-two-involutions-and-the-group-of-involutions-of-the-reduced-biquaternions.html), for the conjugations and their fixed spaces.
- [The Four Products, Their Forms and Their Algebraic Norms](the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.html), for the four products and the norms.
- [Introduction to the Remarkable Subspaces of the Reduced Biquaternions](introduction-to-the-remarkable-subspaces-of-the-reduced-biquaternions.html), for the coordinate planes.
- [The Four-Vector Element Representation of Biquaternions](the-four-vector-element-representation-of-biquaternions.html), for the non-commutative companion, where the row and the column differ.
