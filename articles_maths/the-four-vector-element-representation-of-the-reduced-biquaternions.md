# __The Four-Vector Element Representation of the Reduced Biquaternions__

## Introduction

The **four-vector element representation** reads the reduced biquaternion $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ as a quadruple of real numbers, $\breve Q=(q_{\blacktriangle},q'_{\blacktriangle},q_{\blacktriangledown},q'_{\blacktriangledown})$, and at the same time as a pair of complex numbers, $\breve Q=(Q_{\blacktriangle},Q_{\blacktriangledown})$, with $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$ and $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$. The $j$-part carries one complex coordinate, hence two real ones, so the reading is a real quadruple and a complex pair of the same element. The algebra has no vector part; the name *four-vector* refers to the quadruple of real coordinates, not to a part of the algebra. This article writes the two, the multiplication in each, the four conjugations in coordinates, the remarkable subspaces as coordinate planes, and the four algebraic norms as formulas on the quadruple. The multiplication is **commutative**, which makes the row reading of the element equal to the column one, and it **has zero divisors**, which the unit criterion records.

## The Coefficient Space

**The element is a real quadruple on the real basis and a complex pair on the complex basis, the two readings carrying the same four real coordinates.**

**Definition.** The **real four-vector** of $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ is the quadruple $(q_{\blacktriangle},q'_{\blacktriangle},q_{\blacktriangledown},q'_{\blacktriangledown})$ of *Reduced Biquaternions as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$*, read on the real basis in the order
$$
\breve Q=q_{\blacktriangle}\cdot 1+q'_{\blacktriangle}\cdot i+q_{\blacktriangledown}\cdot j+q'_{\blacktriangledown}\cdot ij ,
$$
and the **complex pair** is $(Q_{\blacktriangle},Q_{\blacktriangledown})$, read on the complex basis $1,j$ over the scalar field $\mathbb{C}$,
$$
\breve Q=Q_{\blacktriangle}\cdot 1+Q_{\blacktriangledown}\cdot j,\qquad Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle},\quad Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}.
$$

**Proposition (the two readings carry the same data).** The map $\breve Q\mapsto(q_{\blacktriangle},q'_{\blacktriangle},q_{\blacktriangledown},q'_{\blacktriangledown})$ is an isomorphism of real vector spaces onto $\mathbb{R}^{4}$, and the map $\breve Q\mapsto(Q_{\blacktriangle},Q_{\blacktriangledown})$ is an isomorphism of complex vector spaces onto $\mathbb{C}^{2}$; the two are the same map read through $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$ and $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$, so the real quadruple and the complex pair are two alphabets of one set of four real coordinates.

*Proof.* The four basis elements are linearly independent over $\mathbb{R}$ and every element is a real linear combination of them, which is the first isomorphism; the two elements $1,j$ are linearly independent over $\mathbb{C}$ and every element is a complex combination, which is the second. The passage $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$, $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$ rewrites the two complex coordinates as the four real ones and back, with no loss.

### Real and Imaginary Parts of the Coordinates

**Each complex coordinate splits into a real part and an imaginary part, and the prime marks the second.**

The real part of $Q_{\blacktriangle}$ is $q_{\blacktriangle}$ and its imaginary part is $q'_{\blacktriangle}$; the real part of $Q_{\blacktriangledown}$ is $q_{\blacktriangledown}$ and its imaginary part is $q'_{\blacktriangledown}$. The two parts share the letter of the coordinate, the imaginary part carrying the prime, by *Conventions in Mathematics*, §*The Elements and their Coefficients*. The reader must not confuse the prime of a coefficient with a derivative: no function is being differentiated in this article. The element is written either as $\breve Q=q_{\blacktriangle}+iq'_{\blacktriangle}+q_{\blacktriangledown}j+iq'_{\blacktriangledown}j$ or as $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$, and the choice of alphabet is a choice of the representation, not of the element.

## The Column and the Row

**The element is a column and a row, and because the multiplication is commutative the row reading is the column reading.**

**Definition.** The **column** of $\breve Q$ is the complex vector $\binom{Q_{\blacktriangle}}{Q_{\blacktriangledown}}$ on the basis $1,j$, and the real column is $\bigl(q_{\blacktriangle},q'_{\blacktriangle},q_{\blacktriangledown},q'_{\blacktriangledown}\bigr)^{\mathsf T}$ on the basis $1,i,j,ij$. The **row** is the transposed quadruple. The left multiplication by $\breve Q$ acts on the column, $\breve Q_{2}\mapsto \breve Q \breve Q_{2}$, and the right multiplication acts on the row, $\breve Q_{2}\mapsto \breve Q_{2}\breve Q$.

**Proposition (the row equals the column).** The matrix of the left multiplication $L_{\breve Q}$ and the matrix of the right multiplication $R_{\breve Q}$ on the complex basis $1,j$ coincide, both being
$$
L_{\breve Q}=R_{\breve Q}=\begin{pmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\ Q_{\blacktriangledown}&Q_{\blacktriangle}\end{pmatrix},
$$
so that $\breve Q_{1}\breve Q_{2}=\breve Q_{2}\breve Q_{1}$ in the representation is the commutativity of the multiplication read as the equality of the two operators.

*Proof.* On the basis, $L_{\breve Q}(1)=\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ and $L_{\breve Q}(j)=\breve Q j=Q_{\blacktriangledown}+Q_{\blacktriangle}j$, giving the columns $\binom{Q_{\blacktriangle}}{Q_{\blacktriangledown}}$ and $\binom{Q_{\blacktriangledown}}{Q_{\blacktriangle}}$, hence the displayed matrix; and $R_{\breve Q}(1)=\breve Q$, $R_{\breve Q}(j)=j\breve Q=Q_{\blacktriangledown}+Q_{\blacktriangle}j$ give the same two columns, so $R_{\breve Q}=L_{\breve Q}$. The equality $L_{\breve Q}=R_{\breve Q}$ is the statement that every element commutes with $\breve Q$, which is the commutativity of the algebra; in the non-commutative companion the two matrices differ.

## Multiplication in Four-Vector Form

**The multiplication is a real $4\times4$ matrix on the quadruple and a complex $2\times2$ matrix on the pair, and the two are the real and complex forms of the same operator.**

**Theorem (the real four-vector matrix).** For $\breve Q=q_{\blacktriangle}+iq'_{\blacktriangle}+q_{\blacktriangledown}j+iq'_{\blacktriangledown}j$, the left multiplication $\breve Q_{2}\mapsto \breve Q \breve Q_{2}$ on the real basis $1,i,j,ij$ has the matrix
$$
\boxed{\;L_{\breve Q}=\begin{pmatrix}
q_{\blacktriangle}&-q'_{\blacktriangle}&q_{\blacktriangledown}&-q'_{\blacktriangledown}\\
q'_{\blacktriangle}&q_{\blacktriangle}&q'_{\blacktriangledown}&q_{\blacktriangledown}\\
q_{\blacktriangledown}&-q'_{\blacktriangledown}&q_{\blacktriangle}&-q'_{\blacktriangle}\\
q'_{\blacktriangledown}&q_{\blacktriangledown}&q'_{\blacktriangle}&q_{\blacktriangle}
\end{pmatrix}
=\begin{pmatrix}A_+&A_-\\ A_-&A_+\end{pmatrix},
\qquad
A_+=\begin{pmatrix}q_{\blacktriangle}&-q'_{\blacktriangle}\\ q'_{\blacktriangle}&q_{\blacktriangle}\end{pmatrix},\quad A_-=\begin{pmatrix}q_{\blacktriangledown}&-q'_{\blacktriangledown}\\ q'_{\blacktriangledown}&q_{\blacktriangledown}\end{pmatrix}\;},
$$
where $A_+$ and $A_-$ are the real $2\times2$ matrices of the multiplication by the complex numbers $Q_{\blacktriangle}$ and $Q_{\blacktriangledown}$.

*Proof.* Apply $L_{\breve Q}$ to the four basis elements and read the coefficients. On $1$: $\breve Q=q_{\blacktriangle}\cdot1+q'_{\blacktriangle}\cdot i+q_{\blacktriangledown}\cdot j+q'_{\blacktriangledown}\cdot ij$ gives the first column. On $i$: $i\breve Q=iQ_{\blacktriangle}+iQ_{\blacktriangledown}j=(iq_{\blacktriangle}-q'_{\blacktriangle})+(iq_{\blacktriangledown}-q'_{\blacktriangledown})j=-q'_{\blacktriangle}\cdot1+q_{\blacktriangle}\cdot i-q'_{\blacktriangledown}\cdot j+q_{\blacktriangledown}\cdot ij$, the second column; on $j$: $j\breve Q=Q_{\blacktriangle}j+Q_{\blacktriangledown}=q_{\blacktriangledown}\cdot1+q'_{\blacktriangledown}\cdot i+q_{\blacktriangle}\cdot j+q'_{\blacktriangle}\cdot ij$, the third column; on $ij$: $ij\breve Q=iQ_{\blacktriangle}j+iQ_{\blacktriangledown}=(iq_{\blacktriangle}-q'_{\blacktriangle})j+(iq_{\blacktriangledown}-q'_{\blacktriangledown})=-q'_{\blacktriangledown}\cdot1+q_{\blacktriangledown}\cdot i-q'_{\blacktriangle}\cdot j+q_{\blacktriangle}\cdot ij$, the fourth. The block form is read off the display: the two diagonal blocks are both $A_+$ and the two off-diagonal blocks both $A_-$, because the two coordinates $Q_{\blacktriangle}$ and $Q_{\blacktriangledown}$ play the symmetric roles in the product $\breve Q_{1}\breve Q_{2}=(Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown})+(Q_{1\blacktriangle}Q_{2\blacktriangledown}+Q_{1\blacktriangledown}Q_{2\blacktriangle})j$.

**Corollary (the trace and the determinant).** The real matrix has trace $4q_{\blacktriangle}=2\operatorname{Re}(Q_{+}+Q_{-})$ and determinant
$$
\boxed{\;\det L_{\breve Q}=\bigl|Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}\bigr|^{2}=\lvert \langle \breve Q\rangle_{\mathrm{ts}}\rvert^{2}=\lvert Q_{+}\rvert^{2}\lvert Q_{-}\rvert^{2}\;},
$$
so the element is a unit exactly when the real matrix of its multiplication is invertible, and the zero divisors are exactly the non-zero elements whose matrix is singular. The complex matrix $\begin{smallmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\ Q_{\blacktriangledown}&Q_{\blacktriangle}\end{smallmatrix}$ has trace $2Q_{\blacktriangle}$ and determinant $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{+}Q_{-}$.

*Proof.* The trace is the sum of the four diagonal entries $q_{\blacktriangle}+q_{\blacktriangle}+q_{\blacktriangle}+q_{\blacktriangle}$. The determinant of $\begin{smallmatrix}A_+&A_-\\ A_-&A_+\end{smallmatrix}$ with commuting blocks $A_+,A_-$ is $\det(A_+^{2}-A_-^{2})=\det(A_++A_-)\det(A_+-A_-)$; and $\det(A_++A_-)=\lvert Q_{\blacktriangle}+Q_{\blacktriangledown}\rvert^{2}=\lvert Q_{+}\rvert^{2}$, $\det(A_+-A_-)=\lvert Q_{\blacktriangle}-Q_{\blacktriangledown}\rvert^{2}=\lvert Q_{-}\rvert^{2}$, giving the display. The complex matrix has the two real $2\times2$ blocks combined into the complex entries $Q_{\blacktriangle},Q_{\blacktriangledown}$, whence trace $2Q_{\blacktriangle}$ and determinant $Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=\langle \breve Q\rangle_{\mathrm{ts}}=Q_{+}Q_{-}$. The unit and zero-divisor readings are the criterion $\langle \breve Q\rangle_{\mathrm{ts}}\neq0$ of *Norm and Invertibility in the Algebra of the Reduced Biquaternions*.

**Corollary (multiplicativity).** The four-vector matrices multiply, $L_{\breve Q_{1}}L_{\breve Q_{2}}=L_{\breve Q_{1}\breve Q_{2}}$, so the map $\breve Q\mapsto L_{\breve Q}$ is a faithful representation of the algebra by real $4\times4$ matrices with the block structure $\begin{smallmatrix}A_+&A_-\\ A_-&A_+\end{smallmatrix}$; the map $\breve Q\mapsto\begin{smallmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\ Q_{\blacktriangledown}&Q_{\blacktriangle}\end{smallmatrix}$ is the same representation over $\mathbb{C}$.

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

**Theorem (the coordinates of the conjugations).** For $\breve Q=q_{\blacktriangle}+iq'_{\blacktriangle}+q_{\blacktriangledown}j+iq'_{\blacktriangledown}j$,
$$
\bar{\breve Q}=q_{\blacktriangle}-iq'_{\blacktriangle}+q_{\blacktriangledown}j-iq'_{\blacktriangledown}j=(q_{\blacktriangle},-q'_{\blacktriangle},q_{\blacktriangledown},-q'_{\blacktriangledown}),
$$
$$
\breve Q_{\mathrm{ts}}=q_{\blacktriangle}+iq'_{\blacktriangle}-q_{\blacktriangledown}j-iq'_{\blacktriangledown}j=(q_{\blacktriangle},q'_{\blacktriangle},-q_{\blacktriangledown},-q'_{\blacktriangledown}),
$$
$$
\breve Q^{*}=q_{\blacktriangle}-iq'_{\blacktriangle}-q_{\blacktriangledown}j+iq'_{\blacktriangledown}j=(q_{\blacktriangle},-q'_{\blacktriangle},-q_{\blacktriangledown},q'_{\blacktriangledown}),
$$
and $\breve Q^{\flat}=-\breve Q^{*}=(-q_{\blacktriangle},q'_{\blacktriangle},q_{\blacktriangledown},-q'_{\blacktriangledown})$.

*Proof.* The bar conjugates the two complex coordinates, $Q_{\blacktriangle}\mapsto\bar Q_{\blacktriangle}=q_{\blacktriangle}-iq'_{\blacktriangle}$ and $Q_{\blacktriangledown}\mapsto\bar Q_{\blacktriangledown}=q_{\blacktriangledown}-iq'_{\blacktriangledown}$; the tessarine sign sends $Q_{\blacktriangle}+jQ_{\blacktriangledown}$ to $Q_{\blacktriangle}-jQ_{\blacktriangledown}$, that is negates $Q_{\blacktriangledown}$; the star is the composite $\bar{\cdot}\circ{}_{\mathrm{ts}}$, conjugating $Q_{\blacktriangle}$ and negating $Q_{\blacktriangledown}$; the flat is the negative of the star. Reading on the basis gives the quadruples.

**Corollary (the three flips).** The bar flips the second and the fourth coordinates, the tessarine sign the third and the fourth, and the star the second and the third; the three flips are the three ways of choosing a pair of the three non-scalar coordinates, and their product is the identity on the scalar coordinate. This is the coordinate form of the Klein group of *The Two Involutions and the Group of Involutions*.

*Proof.* Read the three displays: the first coordinate $q_{\blacktriangle}$ is fixed by all three, and each of the three remaining coordinates is negated by exactly two of the three maps, the pairs being those displayed.

## The Remarkable Subspaces

**The coordinate planes of the four-vector representation are the remarkable subspaces.**

The fixed and anti-fixed spaces of the three conjugations are the coordinate planes of the real basis: the complex line $\mathbb{C}=\mathbb{R}\{1,i\}$ and its companion $\mathbb{C}j=\mathbb{R}\{j,ij\}$ of the tessarine sign, the planes $\mathbb{R}\{1,j\}$ and $\mathbb{R}\{i,ij\}$ of the bar, and the planes $\mathbb{R}\{1,ij\}$ and $\mathbb{R}\{i,j\}$ of the star. Their defining equations, bases, dimensions and closure under the multiplication are the tables of *Introduction to the Remarkable Subspaces of the Reduced Biquaternions*, *The Three Eigenspace Decompositions* and *The Subspaces and Their Relations*, and the four lines $\mathbb{R}$, $\mathbb{R}i$, $\mathbb{R}j$ and $\mathbb{R}ij$ are the **atoms** of the quadruple, the common eigenlines of the two involutions.

## The Algebraic Norms in Coordinates

**The four algebraic norms are the four quadratic forms of the quadruple below.**

**Theorem (the norms on the quadruple).** For $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}=q_{\blacktriangle}+iq'_{\blacktriangle}+q_{\blacktriangledown}j+iq'_{\blacktriangledown}j$,
$$
\langle \breve Q\rangle=Q_{\blacktriangle}^{2}+Q_{\blacktriangledown}^{2}=\bigl(q_{\blacktriangle}^{2}-(q'_{\blacktriangle})^{2}+q_{\blacktriangledown}^{2}-(q'_{\blacktriangledown})^{2}\bigr)+2i\bigl(q_{\blacktriangle}q'_{\blacktriangle}+q_{\blacktriangledown}q'_{\blacktriangledown}\bigr),
$$
$$
\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=\bigl(q_{\blacktriangle}^{2}-(q'_{\blacktriangle})^{2}-q_{\blacktriangledown}^{2}+(q'_{\blacktriangledown})^{2}\bigr)+2i\bigl(q_{\blacktriangle}q'_{\blacktriangle}-q_{\blacktriangledown}q'_{\blacktriangledown}\bigr),
$$
$$
\langle \breve Q\rangle_{*}=\lvert Q_{\blacktriangle}\rvert^{2}-\lvert Q_{\blacktriangledown}\rvert^{2}=q_{\blacktriangle}^{2}+(q'_{\blacktriangle})^{2}-q_{\blacktriangledown}^{2}-(q'_{\blacktriangledown})^{2},
$$
$$
\langle \breve Q\rangle_{\mathrm{ts}*}=\lvert Q_{\blacktriangle}\rvert^{2}+\lvert Q_{\blacktriangledown}\rvert^{2}=q_{\blacktriangle}^{2}+(q'_{\blacktriangle})^{2}+q_{\blacktriangledown}^{2}+(q'_{\blacktriangledown})^{2}.
$$

*Proof.* Expand $Q_{\blacktriangle}^{2}=(q_{\blacktriangle}+iq'_{\blacktriangle})^{2}=q_{\blacktriangle}^{2}-(q'_{\blacktriangle})^{2}+2iq_{\blacktriangle}q'_{\blacktriangle}$ and $Q_{\blacktriangledown}^{2}=(q_{\blacktriangledown}+iq'_{\blacktriangledown})^{2}=q_{\blacktriangledown}^{2}-(q'_{\blacktriangledown})^{2}+2iq_{\blacktriangledown}q'_{\blacktriangledown}$; their sum is $\langle \breve Q\rangle$ and their difference is $\langle \breve Q\rangle_{\mathrm{ts}}$. The two sesquilinear norms are the sums of the squared real coordinates with the signs of the two complex coordinates, $\langle\cdot\rangle_{*}$ subtracting the $Q_{\blacktriangledown}$-block and $\langle\cdot\rangle_{\mathrm{ts}*}$ adding it.

**Corollary (the multiplicative one).** Only $\langle\cdot\rangle_{\mathrm{ts}}$ is multiplicative, $\langle \breve Q_{1}\breve Q_{2}\rangle_{\mathrm{ts}}=\langle \breve Q_{1}\rangle_{\mathrm{ts}}\langle \breve Q_{2}\rangle_{\mathrm{ts}}$, and its vanishing set is the set of zero divisors; the two coordinates $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}$ and $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$ give the factored form
$$
\langle \breve Q\rangle_{\mathrm{ts}}=Q_{+}Q_{-},\qquad \lvert Q_{+}\rvert^{2}=(q_{\blacktriangle}+q_{\blacktriangledown})^{2}+(q'_{\blacktriangle}+q'_{\blacktriangledown})^{2},\qquad \lvert Q_{-}\rvert^{2}=(q_{\blacktriangle}-q_{\blacktriangledown})^{2}+(q'_{\blacktriangle}-q'_{\blacktriangledown})^{2}.
$$
The complex-valued $\langle\cdot\rangle$ and $\langle\cdot\rangle_{\mathrm{ts}}$ are the bilinear pair, the real-valued $\langle\cdot\rangle_{*}$ and $\langle\cdot\rangle_{\mathrm{ts}*}$ the sesquilinear pair; $\langle\cdot\rangle_{\mathrm{ts}*}$ is the sum of the four squared coordinates, and $\langle\cdot\rangle_{*}$ is the same sum with the last two negated. The metrical reading of $\langle\cdot\rangle_{\mathrm{ts}*}$ — its square root as the Euclidean norm and the metric it defines — belongs to *Topology and Metric for Each of the Operations* and *The Euclidean Topology of the Reduced Biquaternion Algebra*, and is not taken here.

*Proof.* The multiplicativity $\langle \breve Q_{1}\breve Q_{2}\rangle_{\mathrm{ts}}=\langle \breve Q_{1}\rangle_{\mathrm{ts}}\langle \breve Q_{2}\rangle_{\mathrm{ts}}$ is *The Four Products, Their Forms and Their Algebraic Norms*; $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=(Q_{\blacktriangle}+Q_{\blacktriangledown})(Q_{\blacktriangle}-Q_{\blacktriangledown})=Q_{+}Q_{-}$; and the two moduli are the sums of the two squared coordinates of $Q_{+}$ and of $Q_{-}$. The vanishing of $\langle\cdot\rangle_{\mathrm{ts}}$ with $\breve Q\neq0$ is the zero-divisor condition of *Zero Divisors of the Algebra of the Reduced Biquaternions*.

### The Unit Criterion in Coordinates

**The element is a unit exactly when both idempotent coordinates are non-zero, and the two conditions are read on the quadruple.**

**Theorem (the unit criterion).** $\breve Q$ is a unit if and only if $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{+}Q_{-}\neq0$, equivalently
$$
(q_{\blacktriangle}+q_{\blacktriangledown},q'_{\blacktriangle}+q'_{\blacktriangledown})\neq(0,0)\quad\text{and}\quad(q_{\blacktriangle}-q_{\blacktriangledown},q'_{\blacktriangle}-q'_{\blacktriangledown})\neq(0,0),
$$
that is $\lvert Q_{+}\rvert^{2}\neq0$ and $\lvert Q_{-}\rvert^{2}\neq0$; the two failure conditions are the two idempotent lines, $\lvert Q_{+}\rvert^{2}=0$ and $\lvert Q_{-}\rvert^{2}=0$, whose union is the zero-divisor set. The inverse in coordinates is
$$
\boxed{\;\breve Q^{-1}=\frac{Q_{\blacktriangle}-jQ_{\blacktriangledown}}{\langle \breve Q\rangle_{\mathrm{ts}}}=Q_{+}^{-1}\Pi_++Q_{-}^{-1}\Pi_-\;},
$$
with $Q_{+}^{-1}$ and $Q_{-}^{-1}$ the complex inverses.

*Proof.* The criterion $Q_{+}Q_{-}\neq0$ is that of *Norm and Invertibility in the Algebra of the Reduced Biquaternions*; the two factors are $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}=(q_{\blacktriangle}+q_{\blacktriangledown})+i(q'_{\blacktriangle}+q'_{\blacktriangledown})$ and $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}=(q_{\blacktriangle}-q_{\blacktriangledown})+i(q'_{\blacktriangle}-q'_{\blacktriangledown})$, whose moduli are the displayed sums of two squares, and a complex number vanishes exactly when its two real coordinates do. The inverse is the idempotent inverse of *The Group of Units of the Algebra of the Reduced Biquaternions*, read in the two coordinates.

## Summary

The reduced biquaternion element is a real quadruple $\breve Q=(q_{\blacktriangle},q'_{\blacktriangle},q_{\blacktriangledown},q'_{\blacktriangledown})$ on the basis $1,i,j,ij$ and a complex pair $\breve Q=(Q_{\blacktriangle},Q_{\blacktriangledown})$ on the basis $1,j$, with $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$ and $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$. The left multiplication is the real $4\times4$ matrix with the $\begin{smallmatrix}A_+&A_-\\ A_-&A_+\end{smallmatrix}$ block structure and the complex $2\times2$ matrix $\begin{smallmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\ Q_{\blacktriangledown}&Q_{\blacktriangle}\end{smallmatrix}$; the **multiplication is commutative**, so the row and the column readings coincide, and the trace and determinant are $4q_{\blacktriangle}$ and $\lvert \langle \breve Q\rangle_{\mathrm{ts}}\rvert^{2}$ in the real model, $2Q_{\blacktriangle}$ and $\langle \breve Q\rangle_{\mathrm{ts}}$ in the complex one. The basis table is symmetric, with the squares $-1,+1,-1$ on the diagonal. The bar flips the second and fourth coordinates, the tessarine sign the third and fourth, and the star the second and third. The remarkable subspaces are the coordinate planes, and the four algebraic norms on the quadruple are $\langle \breve Q\rangle=\bigl(q_{\blacktriangle}^{2}-(q'_{\blacktriangle})^{2}+q_{\blacktriangledown}^{2}-(q'_{\blacktriangledown})^{2}\bigr)+2i(q_{\blacktriangle}q'_{\blacktriangle}+q_{\blacktriangledown}q'_{\blacktriangledown})$, $\langle \breve Q\rangle_{\mathrm{ts}}=\bigl(q_{\blacktriangle}^{2}-(q'_{\blacktriangle})^{2}-q_{\blacktriangledown}^{2}+(q'_{\blacktriangledown})^{2}\bigr)+2i(q_{\blacktriangle}q'_{\blacktriangle}-q_{\blacktriangledown}q'_{\blacktriangledown})$, $\langle \breve Q\rangle_{*}=q_{\blacktriangle}^{2}+(q'_{\blacktriangle})^{2}-q_{\blacktriangledown}^{2}-(q'_{\blacktriangledown})^{2}$ and $\langle \breve Q\rangle_{\mathrm{ts}*}=q_{\blacktriangle}^{2}+(q'_{\blacktriangle})^{2}+q_{\blacktriangledown}^{2}+(q'_{\blacktriangledown})^{2}$. The element is a unit exactly when both idempotent coordinates $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}$ and $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$ are non-zero; the multiplication **has zero divisors**, the two idempotent lines, and is **not a division algebra**.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(q_{\blacktriangle},q'_{\blacktriangle},q_{\blacktriangledown},q'_{\blacktriangledown})$ | the real four-vector of $\breve Q$ on the basis $1,i,j,ij$ |
| $(Q_{\blacktriangle},Q_{\blacktriangledown})$ | the complex pair of $\breve Q$ on the basis $1,j$, $Q_{\blacktriangle}=q_{\blacktriangle}+iq'_{\blacktriangle}$, $Q_{\blacktriangledown}=q_{\blacktriangledown}+iq'_{\blacktriangledown}$ |
| $A_+,A_-$ | the real $2\times2$ matrices of the multiplication by $Q_{\blacktriangle}$ and by $Q_{\blacktriangledown}$ |
| $L_{\breve Q}=\begin{smallmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\ Q_{\blacktriangledown}&Q_{\blacktriangle}\end{smallmatrix}$ | the matrix of the multiplication, complex form |
| $Q_{+}=Q_{\blacktriangle}+Q_{\blacktriangledown}$, $Q_{-}=Q_{\blacktriangle}-Q_{\blacktriangledown}$ | the idempotent coordinates |
| $\langle \breve Q\rangle, \langle \breve Q\rangle_{\mathrm{ts}}, \langle \breve Q\rangle_{*}, \langle \breve Q\rangle_{\mathrm{ts}*}$ | the four algebraic norms on the quadruple |

## Further Reading

- [Reduced Biquaternions as a Vector Space over $\mathbb{R}$ and $\mathbb{C}$](reduced-biquaternions-as-a-vector-space-over-r-and-c.html), for the two scalar systems and the two coordinate readings.
- [Reduced Biquaternion Space](reduced-biquaternion-space.html), for the multiplication table in the abstract.
- [The Two Involutions and the Group of Involutions](the-two-involutions-and-the-group-of-involutions-of-the-reduced-biquaternions.html), for the conjugations and their fixed spaces.
- [The Four Products, Their Forms and Their Algebraic Norms](the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.html), for the four products and the norms.
- [The Six Subspaces](introduction-to-the-remarkable-subspaces-of-the-reduced-biquaternions.html), for the coordinate planes.
