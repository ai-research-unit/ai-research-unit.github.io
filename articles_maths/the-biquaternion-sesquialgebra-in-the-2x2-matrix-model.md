
# __The Biquaternion Sesquialgebra in the $2\times2$ Matrix Model__

## Introduction

The biquaternion algebra is isomorphic to the full matrix algebra $M_2(\mathbb{C})$, and the model of *Biquaternion $2\times2$ Matrix Element Representation* carries the algebra, the involution and the norm. Under the isomorphism the star-involution becomes the Hermitian transpose, and the sesquilinear multiplication $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ of *Biquaternions as a Sesquialgebra over $\mathbb{C}$* becomes the product with the Hermitian transpose of the second factor:

$$
\Phi(\tilde P\star\tilde Q)=\Phi(\tilde P)\,\Phi(\tilde Q)^{\dagger} , \qquad\text{equivalently}\qquad X\star Y=XY^{\dagger}\ \text{ on the matrices} .
$$

The sesquialgebra is therefore the matrix algebra $M_2(\mathbb{C})$ read with the derived operation of its transpose conjugation, and every object of the batch is an object of the matrix algebra read through one multiplication by a Hermitian transpose: the ternary product is $XY^{\dagger}Z$, the sandwich is $PX^{\dagger}Q^{\dagger}$, the idempotents are the Hermitian projections, the rank of an element is the rank of its matrix, and the trace and the determinant of a value are read from the ordinary trace and determinant of the matrix product.

This is the reason the article is the last of the batch: it collects the model in one place and reads every preceding statement in it. It cites the model article for the isomorphism and the trace and determinant identities, and it reads *Projections of the Biquaternion Sesquialgebra*, *The Squares and the Positive Cone of the Biquaternion Sesquialgebra*, *The Biquaternion Sesquialgebra Is Simple*, *The Ternary Product and the Associator of the Biquaternion Sesquialgebra*, *The Left and Right Multiplications of the Biquaternion Sesquialgebra*, *The Sesquilinear Sandwich on the Biquaternions* and *The Sesquilinear Commutator and the Symmetrised Product on the Biquaternions* in the matrix notation. The general matrix sesquialgebras are *Matrix Sesquialgebras*, where the model $X\star Y=XY^{\dagger}$ is treated for the matrix algebras over an involutive field. The article belongs to the matrix-representation group of the Topology, beside *The Forms in the Matrix Representation of the Biquaternion Algebra* and *The Unit Group and the Frobenius Norm in the Matrix Representation*.

The setting is that of *Biquaternions as a Sesquialgebra over $\mathbb{C}$*: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the unit, ${}^{*}$ the conjugate-linear involution with $Q^{*}_\nu=\varepsilon_\nu\overline{Q_\nu}$ and $\varepsilon=(1,-1,-1,-1)$, the multiplication $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$, the norm $\langle\tilde Q,\tilde Q\rangle_{\natural}=Q_0^2+Q_1^2+Q_2^2+Q_3^2$, and the Hermitian form $\langle\tilde P,\tilde Q\rangle_*=\mathrm{Sc}(\tilde P\tilde Q^{*})=\sum_\mu P_\mu\overline{Q_\mu}$ of *The Hermitian Form on the Biquaternion Algebra*. The isomorphism $\Phi$ is that of *Biquaternion $2\times2$ Matrix Element Representation*, and the standard abbreviations $E_{ij}$ for the matrix units are used throughout.

## The Model

### The Isomorphism

**Theorem.** The map $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ of *Biquaternion $2\times2$ Matrix Element Representation* is an isomorphism of $\mathbb{C}$-algebras,

$$
\Phi(\tilde P\tilde Q)=\Phi(\tilde P)\Phi(\tilde Q) , \qquad \Phi(\lambda\tilde P)=\lambda\Phi(\tilde P) , \qquad \Phi(e_0)=I , \qquad \Phi(e_1)=J_1 , \ \Phi(e_2)=J_2 , \ \Phi(e_3)=J_3 ,
$$

with the images of the three imaginary basis elements the three matrices $J_k=\Phi(e_k)$. In coordinates, for $\tilde Q=Q_0e_0+\mathbf Q$,

$$
\Phi(\tilde Q)=\begin{pmatrix} Q_0-iQ_3 & -iQ_1-Q_2 \\ -iQ_1+Q_2 & Q_0+iQ_3 \end{pmatrix} .
$$

**Proof.** This is the definition and the table of *Introduction to the 2×2 Matrix Representation of Biquaternions*, §*The Representation*; the coordinate display is that table read with $\mathbf Q=(Q_1,Q_2,Q_3)$. The multiplicativity is the isomorphism statement of that article. $\square$

**Remark.** The model is not an accident of dimension: it is the regular representation of the Clifford algebra of the space, and the $4\times4$ operator model of *Biquaternion $4\times4$ Regular Matrix Operator Representation* is its left-regular doubling. The trace and the determinant of $\Phi(\tilde Q)$ are computed in *Introduction to the 2×2 Matrix Representation of Biquaternions*, §*The Trace and the Determinant*, and are the invariants of $\tilde Q$ under the algebra structure.

### The Involution in the Model

**Theorem.** The involution of the sesquialgebra is the Hermitian transpose in the model:

$$
\Phi(\tilde Q^{*})=\Phi(\tilde Q)^{\dagger} .
$$

**Proof.** The four coordinates of $\tilde Q^{*}$ are $(\overline{Q_0},-\overline{Q_1},-\overline{Q_2},-\overline{Q_3})$, and substituting them in the coordinate display gives the conjugate transpose of the display for $\tilde Q$: the diagonal entries $Q_0\mp iQ_3$ become $\overline{Q_0}\pm i\overline{Q_3}$, which are the conjugates of the diagonal entries of the transpose, and the off-diagonal pair is exchanged with a conjugation. This is the statement of *Biquaternion $2\times2$ Matrix Element Representation*, §*The Conjugations in Matrix Form*. $\square$

**Corollary (the two halves).** The Hermitian and anti-Hermitian halves of *Hermitian and Skew-Hermitian Elements* are the Hermitian and the anti-Hermitian matrices, $\Phi(\mathbb{M}_+)$ the Hermitian matrices and $\Phi(\mathbb{M}_-)$ the anti-Hermitian ones.

**Proof.** The involution corresponds to the Hermitian transpose by the theorem, so the fixed space and the anti-fixed space correspond to the Hermitian and the anti-Hermitian matrices. $\square$

### The Multiplication in the Model

**Theorem (the derived operation).** For all $\tilde P,\tilde Q$,

$$
\Phi(\tilde P\star\tilde Q)=\Phi(\tilde P)\,\Phi(\tilde Q)^{\dagger} ,
$$

so the sesquialgebra $(\mathbb{B},\star)$ is isomorphic to the matrix set $M_2(\mathbb{C})$ with the operation $X\star Y=XY^{\dagger}$.

**Proof.** $\Phi(\tilde P\star\tilde Q)=\Phi(\tilde P\tilde Q^{*})=\Phi(\tilde P)\Phi(\tilde Q^{*})=\Phi(\tilde P)\Phi(\tilde Q)^{\dagger}$ by the multiplicativity and the involution theorem. $\square$

**Proposition (the two actions of the unit).** In the model the unit matrix $I$ acts by

$$
I\star Y=IY^{\dagger}=Y^{\dagger} , \qquad Y\star I=YI^{\dagger}=Y ,
$$

so $I$ is a right unit and not a left unit, and the left action of the unit is the Hermitian transpose while the right action is the identity; in the notation of *The Left and Right Multiplications of the Biquaternion Sesquialgebra*, $\Phi(L_{\tilde A}(\tilde X))=\Phi(\tilde A)\Phi(\tilde X)^{\dagger}$ and $\Phi(R_{\tilde A}(\tilde X))=\Phi(\tilde X)\Phi(\tilde A)^{\dagger}$.

**Proof.** $I^{\dagger}=I$, and $Y^{\dagger}\neq Y$ in general; the operator statements are the definitions of the two multiplications read through the model. $\square$

**Remark.** The model makes the failure of the two-sided unit visible as the failure of the Hermitian transpose to be the identity: the multiplication of the model is the ordinary matrix multiplication with one factor transposed, and the transpose is what breaks the symmetry of the two sides. Every asymmetry of the batch has this origin in the model.

## The Sesquilinear Structure in the Model

### The Ternary Product and the Quadratic Representation

**Proposition.** In the model the ternary product of *The Ternary Product and the Associator of the Biquaternion Sesquialgebra* is the matrix product

$$
\Phi\bigl(\{\tilde P,\tilde Q,\tilde R\}\bigr)=\Phi(\tilde P)\,\Phi(\tilde Q)^{\dagger}\,\Phi(\tilde R) ,
$$

so $\{X,Y,Z\}=XY^{\dagger}Z$, the middle model of *Algebraic J\*-Algebras* on the matrix algebra; the quadratic representation is

$$
Z\longmapsto ZY^{\dagger}Z .
$$

**Proof.** $\{\tilde P,\tilde Q,\tilde R\}=\tilde P\tilde Q^{*}\tilde R$, and the multiplicativity and the involution theorem transport it to $\Phi(\tilde P)\Phi(\tilde Q)^{\dagger}\Phi(\tilde R)$. $\square$

**Proposition (the associator).** In the model the associator of *The Ternary Product and the Associator of the Biquaternion Sesquialgebra* is

$$
[X,Y,Z]=X\bigl(Y^{\dagger}Z^{\dagger}-ZY^{\dagger}\bigr) ,
$$

and the two groupings of the product are $(X\star Y)\star Z=XY^{\dagger}Z^{\dagger}$ and $X\star(Y\star Z)=XZY^{\dagger}$.

**Proof.** $(X\star Y)\star Z=(XY^{\dagger})Z^{\dagger}=XY^{\dagger}Z^{\dagger}$ and $X\star(Y\star Z)=X(YZ^{\dagger})^{\dagger}=XZY^{\dagger}$; the difference is the display. $\square$

### The Idempotents and the Projections

**Theorem.** The $\star$-idempotents of the model are the Hermitian projections, that is the matrices $\Pi$ with $\Pi=\Pi^{\dagger}=\Pi^{2}$; they are the trivial pair $0,I$ together with the images of the projections $\tilde\Pi_+(\hat\mu)$ of *Projections of the Biquaternion Sesquialgebra*, and the rank-one ones form the sphere $\mathbb{CP}^{1}$ of the lines of $\mathbb{C}^{2}$.

**Proof.** An idempotent satisfies $\Pi\star\Pi=\Pi\Pi^{\dagger}=\Pi$; applying the Hermitian transpose to this equation gives $\Pi\Pi^{\dagger}=\Pi^{\dagger}$, so $\Pi=\Pi^{\dagger}$ and the element is Hermitian, and then $\Pi^{2}=\Pi\Pi^{\dagger}=\Pi$; conversely a Hermitian idempotent has $\Pi\star\Pi=\Pi\Pi^{\dagger}=\Pi^{2}=\Pi$. The identification with the projections is *Projections of the Biquaternion Sesquialgebra*, §*The Projections*, through the model; the parametrisation by the lines is the rank-one case of the projection $\Phi(\tilde\Pi_+(\hat\mu))=\tfrac12\bigl(I+\ \text{a Hermitian traceless matrix}\bigr)$, which is the orthogonal projection onto a line. $\square$

**Remark.** In the model the idempotents of the multiplication are the Hermitian idempotents and the general idempotents of the algebra are not idempotents of the multiplication, which is *Projections of the Biquaternion Sesquialgebra*, §*The Contrast with the Algebra*, read in the matrix notation: the algebra has idempotents of rank one and of rank two, and only the Hermitian ones survive the transpose. The rank of an element, which is the rank of its matrix in this model, is the invariant that separates the projections from the general idempotents, by *Biquaternion Zero Divisors* and *Biquaternion Idempotents and Projections*.

### The Sandwich, the Adjoint and the Rank

**Proposition.** In the model the sandwich of *The Sesquilinear Sandwich on the Biquaternions* is

$$
\Phi\bigl(S_{\tilde P,\tilde Q}(\tilde X)\bigr)=\Phi(\tilde P)\,\Phi(\tilde X)^{\dagger}\,\Phi(\tilde Q)^{\dagger} ,
$$

the left and the right multiplication are $X\mapsto AX^{\dagger}$ and $X\mapsto XA^{\dagger}$, and the rank of $S_{\tilde P,\tilde Q}$ is $\operatorname{rank}\Phi(\tilde P)\cdot\operatorname{rank}\Phi(\tilde Q)$, the standard rank identity of the matrix algebra.

**Proof.** Read the definitions through the model; the rank identity is $\dim\bigl(\Phi(\tilde P)M_2\Phi(\tilde Q)^{\dagger}\bigr)=\operatorname{rank}\Phi(\tilde P)\operatorname{rank}\Phi(\tilde Q)$. $\square$

**Remark.** The general matrix sesquialgebras are *Matrix Sesquialgebras*, where the same operators are read for $M_n$ over an involutive field and the rank identity is the same; the biquaternion case is the case $n=2$ over $\mathbb{C}$ with the conjugate transpose, and the two-dimensionality is what makes the idempotents a sphere rather than a larger projective space.

## The Trace and the Determinant

### The Trace

**Theorem.** For every $\tilde Q$,

$$
\mathrm{tr}\,\Phi(\tilde Q)=2Q_0=2\,\mathrm{Sc}(\tilde Q) ,
$$

so the trace is twice the scalar part, and it is additive and $\mathbb{C}$-linear; it satisfies

$$
\mathrm{tr}\,\Phi(\tilde Q^{*})=\overline{\mathrm{tr}\,\Phi(\tilde Q)} .
$$

**Proof.** The diagonal entries of the coordinate display are $Q_0-iQ_3$ and $Q_0+iQ_3$, whose sum is $2Q_0$; the scalar part of $\tilde Q$ is $Q_0$, and the additivity and linearity are those of the matrix trace. The last display is $\mathrm{tr}(M^{\dagger})=\overline{\mathrm{tr}M}$. $\square$

**Remark.** The trace is the model form of the scalar part, and hence of the Hermitian form: the form $\langle\cdot,\cdot\rangle_*$ of *The Hermitian Form on the Biquaternion Algebra* is

$$
\langle\tilde P,\tilde Q\rangle_*=\mathrm{Sc}(\tilde P\tilde Q^{*})=\tfrac12\,\mathrm{tr}\bigl(\Phi(\tilde P)\Phi(\tilde Q)^{\dagger}\bigr) ,
$$

the standard Hermitian form of the matrix algebra, the trace pairing of $M_2(\mathbb{C})$.

### The Determinant

**Theorem.** For every $\tilde Q$,

$$
\det\Phi(\tilde Q)=\langle\tilde Q,\tilde Q\rangle_{\natural}=Q_0^2+Q_1^2+Q_2^2+Q_3^2 ,
$$

the norm form of *Biquaternion Norm and Invertibility*; the determinant is multiplicative, so the norm is multiplicative as well, $\langle\tilde P\tilde Q,\tilde P\tilde Q\rangle_{\natural}=\langle\tilde P,\tilde P\rangle_{\natural}\langle\tilde Q,\tilde Q\rangle_{\natural}$, and it satisfies

$$
\det\Phi(\tilde Q^{*})=\overline{\det\Phi(\tilde Q)} .
$$

**Proof.** The determinant of the coordinate display is $(Q_0-iQ_3)(Q_0+iQ_3)-(-iQ_1-Q_2)(-iQ_1+Q_2)=Q_0^{2}+Q_3^{2}+Q_1^{2}+Q_2^{2}$, and the multiplicativity and the conjugate-transpose identity are those of the matrix determinant. $\square$

**Remark.** The determinant is therefore the norm, and the invertibility criterion of *Biquaternion Norm and Invertibility*, that $\tilde Q$ is a unit exactly when $\langle\tilde Q,\tilde Q\rangle_{\natural}\neq0$, is the invertibility of the matrix $\Phi(\tilde Q)$. The determinant is not a trace of a power in the naive sense, but the two are linked by the characteristic polynomial $\lambda^{2}-2Q_0\lambda+\langle\tilde Q,\tilde Q\rangle_{\natural}$ of $\Phi(\tilde Q)$.

### The Trace and the Determinant of a Value

**Theorem.** For the multiplication and for its derived ternary product,

$$
\mathrm{tr}\,\Phi(\tilde P\star\tilde Q)=2\sum_\mu P_\mu\overline{Q_\mu}=2\,\mathrm{Sc}(\tilde P\star\tilde Q) , \qquad
\det\Phi(\tilde P\star\tilde Q)=\langle\tilde P,\tilde P\rangle_{\natural}\,\overline{\langle\tilde Q,\tilde Q\rangle_{\natural}} ,
$$

so the trace of a value is twice the Hermitian form of the two factors and the determinant of a value is the norm of the first factor times the conjugate of the norm of the second.

**Proof.** $\Phi(\tilde P\star\tilde Q)=\Phi(\tilde P)\Phi(\tilde Q)^{\dagger}$; the trace is $2\mathrm{Sc}(\tilde P\star\tilde Q)=2\sum_\mu P_\mu\overline{Q_\mu}$ by the trace theorem, and the determinant is $\det\Phi(\tilde P)\det\Phi(\tilde Q)^{\dagger}=\det\Phi(\tilde P)\overline{\det\Phi(\tilde Q)}$ by the multiplicativity and the determinant theorem. $\square$

**Corollary (the square).** For the square of *The Squares and the Positive Cone of the Biquaternion Sesquialgebra*,

$$
\mathrm{tr}\,\Phi(\tilde Q\star\tilde Q)=2\sum_\mu\lvert Q_\mu\rvert^{2} , \qquad \det\Phi(\tilde Q\star\tilde Q)=\lvert\langle\tilde Q,\tilde Q\rangle_{\natural}\rvert^{2} ,
$$

both real and nonnegative, and the trace vanishes exactly at $\tilde Q=0$ while the determinant vanishes exactly at the zero divisors.

**Proof.** The two displays are the theorem at $\tilde P=\tilde Q$, using $\langle\tilde Q,\tilde Q\rangle_{\natural}\overline{\langle\tilde Q,\tilde Q\rangle_{\natural}}=\lvert\langle\tilde Q,\tilde Q\rangle_{\natural}\rvert^{2}$; the nonnegativity is that of a modulus square and of a sum of modulus squares, the trace vanishing only at the zero element, and the determinant at the elements with $\langle\tilde Q,\tilde Q\rangle_{\natural}=0$, which are the zero divisors. $\square$

**Remark.** The corollary is the matrix form of the positivity of the square and of the positive cone of *The Squares and the Positive Cone of the Biquaternion Sesquialgebra*: the trace of the square is twice the squared Euclidean norm of the eight real coordinates, and the determinant of the square is the squared modulus of the norm. The trace is the quantity that is strictly positive off zero, and the determinant is the quantity that detects the zero divisors; the two together are the invariant pair of the square.

## The Batch in the Model

The model collects the statements of the batch in one table. The multiplication is $X\star Y=XY^{\dagger}$ and the involution is the Hermitian transpose; the ternary product is the middle model.

| object of the batch | matrix model |
|---|---|
| element $\tilde Q=Q_0e_0+\mathbf Q$ | $\Phi(\tilde Q)=\begin{pmatrix} Q_0-iQ_3 & -iQ_1-Q_2 \\ -iQ_1+Q_2 & Q_0+iQ_3 \end{pmatrix}$ |
| involution $\tilde Q^{*}$ | Hermitian transpose $\Phi(\tilde Q)^{\dagger}$ |
| multiplication $\tilde P\star\tilde Q$ | $XY^{\dagger}$ |
| ternary product $\{\tilde P,\tilde Q,\tilde R\}$ | $XY^{\dagger}Z$ |
| associator $[\tilde P,\tilde Q,\tilde R]$ | $X(Y^{\dagger}Z^{\dagger}-ZY^{\dagger})$ |
| idempotents of the multiplication | Hermitian projections; the rank-one ones are the sphere $\mathbb{CP}^{1}$ |
| simplicity | $M_2(\mathbb{C})$ is simple, centre $\mathbb{C}I$ |
| left and right multiplications | $Y\mapsto AY^{\dagger}$, $Y\mapsto YA^{\dagger}$ |
| sandwich $S_{\tilde P,\tilde Q}$ | $X\mapsto PX^{\dagger}Q^{\dagger}$ |
| commutator $[\tilde P,\tilde Q]_\varsigma$ | $XY^{\dagger}-YX^{\dagger}$ |
| symmetrised product $\tilde P\circ\tilde Q$ | $\tfrac12(XY^{\dagger}+YX^{\dagger})$ |
| norm $\langle\tilde Q,\tilde Q\rangle_{\natural}$ | $\det\Phi(\tilde Q)$ |
| scalar part $\mathrm{Sc}(\tilde Q)$ | $\tfrac12\mathrm{tr}\,\Phi(\tilde Q)$ |
| Hermitian form $\langle\tilde P,\tilde Q\rangle_*$ | $\tfrac12\mathrm{tr}(XY^{\dagger})$ |
| rank of an element | rank of the matrix |

**Remark.** The table is the reading of the batch in the model: every operation on $\mathbb{B}$ becomes one of the elementary operations of the matrix algebra with a transpose, and the two products that carry the transpose are the derived operation and the ternary model. The ordinary matrix algebra, with no transpose, is the bilinear reading of *Biquaternions as an Algebra over $\mathbb{C}$* and of *Biquaternion Jordan Algebras*; the table is the sesquilinear reading, and the transpose is the whole difference between the two columns.

**Remark (the simplicity in the model).** The simplicity of the sesquialgebra is the simplicity of $M_2(\mathbb{C})$ read with the derived operation: the two-sided ideals of the multiplication are the two-sided ideals of the matrix algebra, by *The Biquaternion Sesquialgebra Is Simple*, and the matrix algebra has the two trivial ones because a nonzero two-sided ideal contains a matrix unit and hence the identity. The centre is $\mathbb{C}I$, which is $\mathbb{C}e_0$, and the only central idempotents are $0$ and $I$, in agreement with *Central Simple Algebras and the Brauer Group*.

## Summary

In the model of *Biquaternion $2\times2$ Matrix Element Representation* the biquaternion sesquialgebra is the matrix algebra $M_2(\mathbb{C})$ with the derived operation $X\star Y=XY^{\dagger}$ of the Hermitian transpose, the involution is the transpose, the unit matrix is a right unit alone, and the left action of the unit is the transpose. The ternary product is the middle model $XY^{\dagger}Z$, the associator is $X(Y^{\dagger}Z^{\dagger}-ZY^{\dagger})$, the sandwich is $X\mapsto PX^{\dagger}Q^{\dagger}$, and the idempotents of the multiplication are the Hermitian projections, that is $0$, $I$ and the orthogonal projections onto the lines of $\mathbb{C}^{2}$; the rank of an element is the rank of its matrix, and the rank of a sandwich is the product of the ranks of its parameters.

The trace of an element is twice its scalar part, the determinant is the norm, the trace of a product is twice the Hermitian form of its factors, and the determinant of a product is the norm of the first factor times the conjugate of the norm of the second; the square has both invariants real and nonnegative, its trace twice the squared Euclidean norm and its determinant the squared modulus of the norm. The whole batch is the matrix algebra read through one transpose, and the ordinary matrix algebra is the bilinear reading without it.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ | the isomorphism of *Biquaternion $2\times2$ Matrix Element Representation* |
| $X\star Y=XY^{\dagger}$ | the multiplication in the model |
| $\Phi(\tilde Q^{*})=\Phi(\tilde Q)^{\dagger}$ | the involution is the Hermitian transpose |
| $\{X,Y,Z\}=XY^{\dagger}Z$ | the ternary product, the middle model |
| $[X,Y,Z]=X(Y^{\dagger}Z^{\dagger}-ZY^{\dagger})$ | the associator in the model |
| $\Pi=\Pi^{\dagger}=\Pi^{2}$ | the idempotents of the multiplication, the Hermitian projections |
| $Y\mapsto AY^{\dagger}$, $Y\mapsto YA^{\dagger}$ | the left and the right multiplication |
| $X\mapsto PX^{\dagger}Q^{\dagger}$ | the sandwich |
| $\mathrm{tr}\,\Phi(\tilde Q)=2\mathrm{Sc}(\tilde Q)$ | the trace is twice the scalar part |
| $\det\Phi(\tilde Q)=\langle\tilde Q,\tilde Q\rangle_{\natural}$ | the determinant is the norm |
| $\mathrm{tr}\,\Phi(\tilde P\star\tilde Q)=2\langle\tilde P,\tilde Q\rangle_*$ | the trace of a value |
| $\det\Phi(\tilde P\star\tilde Q)=\langle\tilde P,\tilde P\rangle_{\natural}\overline{\langle\tilde Q,\tilde Q\rangle_{\natural}}$ | the determinant of a value |
| $\mathrm{tr}\,\Phi(\tilde Q\star\tilde Q)=2\sum_\mu\lvert Q_\mu\rvert^{2}$ | the trace of a square |
| $\det\Phi(\tilde Q\star\tilde Q)=\lvert\langle\tilde Q,\tilde Q\rangle_{\natural}\rvert^{2}$ | the determinant of a square |
| $E_{ij}$ | the matrix units of the model |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Graduate Texts in Mathematics 88, Springer, 1982), for the algebra $M_2(\mathbb{C})$, its idempotents, its one-sided ideals and the rank identity.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the matrix algebras with an involution and the Hermitian transpose as the standard example.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society Colloquium Publications 37, 1956), for the simplicity of a full matrix ring, the centre and the trace.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, second edition, 2013), for the trace, the determinant, the rank identity and the Hermitian forms of a matrix algebra.
- Irving Kaplansky, *Rings of Operators* (Benjamin, 1968), for the middle model $XY^{\dagger}Z$, its quadratic representation and the associated triple systems.
