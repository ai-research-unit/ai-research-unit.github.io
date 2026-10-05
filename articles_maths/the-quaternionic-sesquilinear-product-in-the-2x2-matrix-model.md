
# __The Quaternionic Sesquilinear Product in the $2\times2$ Matrix Model__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ is isomorphic to the algebra $M_2(\mathbb{C})$ of $2\times2$ complex matrices, and the isomorphism is held fixed in the corpus as the map $\Phi$ of *Biquaternion 2×2 Matrix Element Representation*. The algebra carries four products on its underlying $\mathbb{C}$-vector space (*The Four Biquaternion Complex Products*), and the fourth of them,

$$
\tilde P \star \tilde Q = \tilde P^{\natural}\tilde Q^{*} ,
$$

is the subject of this group: the rule and the scalar–vector form are *The Four Biquaternion Complex Products* §*The Complex Quaternionic Sesquilinear Product*; the sesquialgebra it defines is *Biquaternions as a Quaternionic Sesquialgebra over $\mathbb{C}$*; and the associator, the ternary product and the multiplication operators are *The Associator of the Quaternionic Sesquilinear Product*, *The Ternary Product and the Failure of the Jordan Triple Identity* and *The Left and Right Multiplications of the Quaternionic Sesquilinear Product*. The symbols are those of the group: ${}^{\natural}$ is the natural conjugation, ${}^{*}$ the star conjugation, and the bar the coefficientwise complex conjugation.

The subject of this article is the **matrix form** of the product and of the objects attached to it. The isomorphism $\Phi$ carries the two conjugations to the two classical matrix operations: the natural conjugation becomes the **adjugate** and the star conjugation becomes the **conjugate transpose**,

$$
\Phi(\tilde P^{\natural}) = \operatorname{adj}\Phi(\tilde P) , \qquad \Phi(\tilde P^{*}) = \Phi(\tilde P)^{\dagger} , \qquad \Phi(\overline{\tilde P}) = \operatorname{adj}\bigl(\Phi(\tilde P)^{\dagger}\bigr) ,
$$

and the norm becomes the determinant, $\det\Phi(\tilde P) = \langle\tilde P,\tilde P\rangle_{\natural}$. The product therefore reads

$$
\Phi(\tilde P \star \tilde Q) = \operatorname{adj}\Phi(\tilde P)\,\Phi(\tilde Q)^{\dagger} ,
$$

the adjugate of the first factor followed by the conjugate transpose of the second. The article establishes three things. First, the four products take the four simplest matrix forms, and the table is the matrix counterpart of the comparison table of *Comparison Between the Four Biquaternion Products*. Second, the idempotent sphere of *Idempotents of the Quaternionic Sesquilinear Product* is the unitary conjugacy class of the diagonal matrix $\operatorname{diag}(\omega,\omega^{2})$ with the two nontrivial cube roots of unity on the diagonal, which identifies the sphere of idempotents with a familiar orbit of $U(2)$. Third, the associator and the left multiplication take the matrix forms

$$
\operatorname{adj}\bigl(M(Q)^{\dagger}\bigr)M(P)M(R)^{\dagger} - \operatorname{adj}M(P)\,M(R)\,\operatorname{adj}\bigl(M(Q)^{\dagger}\bigr) ,
\qquad
\tilde X \longmapsto \operatorname{adj}M(\tilde A)\,M(\tilde X)^{\dagger} ,
$$

which are the matrix readings of the two articles of the group.

The article owns the matrix forms of the conjugations, of the four products, of the norm, of the idempotents, of the associator and of the operators, and it belongs to the matrix-representation group of the Topology, beside *The Forms in the Matrix Representation of the Biquaternion Algebra* and *The Unit Group and the Frobenius Norm in the Matrix Representation*. It cites the isomorphism $\Phi$, the trace, the determinant and the matrix form of the four conjugations to *Biquaternion 2×2 Matrix Element Representation*; it cites the four products to *The Four Biquaternion Complex Products*; it cites the idempotent sphere to *Idempotents of the Quaternionic Sesquilinear Product* and the classification of the zero divisors to *Biquaternion Zero Divisors*; and it does not treat the 4×4 regular representation, which is *Biquaternion 4×4 Regular Matrix Element Representation*, nor the module theory, which is *Modules over the Biquaternion Algebra*.

## The Matrix Model

### The Isomorphism

**Definition.** The **matrix realization** of $\mathbb{B}$ is the algebra isomorphism

$$
\Phi : \mathbb{B} \longrightarrow M_2(\mathbb{C}) , \qquad
\Phi(e_0) = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} , \quad
\Phi(e_1) = \begin{pmatrix} 0 & -i \\ -i & 0 \end{pmatrix} , \quad
\Phi(e_2) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} , \quad
\Phi(e_3) = \begin{pmatrix} -i & 0 \\ 0 & i \end{pmatrix} ,
$$

with $\Phi(i e_\mu) = i\Phi(e_\mu)$. On a general element it reads

$$
\Phi(\tilde Q) = \begin{pmatrix} Q_0 - iQ_3 & -iQ_1 - Q_2 \\ -iQ_1 + Q_2 & Q_0 + iQ_3 \end{pmatrix} .
$$

This is the choice of *Introduction to the 2×2 Matrix Representation of Biquaternions* §*The Representation*, held fixed so that the matrix statements below agree with that article, with *The Clifford Structure of the Biquaternion Algebra* and with *Biquaternion 2×2 Matrix Operator Representation*.

**Theorem (the isomorphism).** The map $\Phi$ is a $\mathbb{C}$-algebra isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$; the trace is $\operatorname{tr}\Phi(\tilde Q) = 2Q_0$ and the determinant is $\det\Phi(\tilde Q) = Q_0^{2} + Q_1^{2} + Q_2^{2} + Q_3^{2} = \langle\tilde Q,\tilde Q\rangle_{\natural}$.

**Proof.** The isomorphism, the trace and the determinant are *Introduction to the 2×2 Matrix Representation of Biquaternions*, §*The Representation Is an Algebra Isomorphism* and §*The Trace and the Determinant*; the identification of the determinant with the norm form is *Biquaternion Norm and Invertibility*. $\square$

**Remark.** The determinant being the norm is the first matrix statement of the article: the singular matrices are exactly the zero divisors of $\mathbb{B}$ (*Biquaternion Zero Divisors*), and $\Phi$ carries invertibility to invertibility. In the matrix model the norm of an element is the determinant of its matrix, and the multiplicativity of the determinant is the multiplicativity of the norm.

### The Conjugations in Matrices

**Theorem (the three conjugations).** For every $\tilde P$,

$$
\Phi(\tilde P^{\natural}) = \operatorname{adj}\Phi(\tilde P) , \qquad
\Phi(\tilde P^{*}) = \Phi(\tilde P)^{\dagger} , \qquad
\Phi(\overline{\tilde P}) = \operatorname{adj}\bigl(\Phi(\tilde P)^{\dagger}\bigr) = \varepsilon\,\overline{\Phi(\tilde P)}\,\varepsilon^{-1} ,
$$

where $\operatorname{adj}X = \begin{pmatrix} X_{22} & -X_{12} \\ -X_{21} & X_{11} \end{pmatrix}$ is the adjugate, $X^{\dagger}$ the conjugate transpose and $\varepsilon = \Phi(-e_2)$.

**Proof.** The first two are the matrix forms of the conjugations of *Biquaternion 2×2 Matrix Element Representation* §*The Conjugations in Matrix Form*: quaternion conjugation is the adjugate and Hermitian conjugation is the conjugate transpose. The third follows from the first two and ${}^{*} = \overline{\cdot}\circ{}^{\natural}$, together with $\operatorname{adj}(X^{\dagger}) = \operatorname{adj}(X)^{\dagger}$, the adjugate having integer coefficients; it agrees with the $\varepsilon$-form of that article because $\operatorname{adj}(X) = \varepsilon X^{\mathsf{T}}\varepsilon^{-1}$ for every $2\times2$ matrix. $\square$

**Remark.** The three operations are the three classical involutions of $2\times2$ matrices: the adjugate is $\mathbb{C}$-linear and anti-multiplicative, the conjugate transpose is conjugate-linear and anti-multiplicative, and their composite is conjugate-linear and multiplicative. The adjugate of a $2\times2$ matrix is the cofactor matrix, $\operatorname{adj}(X) = \det(X)X^{-1}$ for invertible $X$, and the natural conjugation is therefore the matrix form of the quaternion conjugation on the $\mathbb{H}$ factor. The star being the conjugate transpose is the matrix form of the standard sesquilinear structure, and it is the reason the fourth product has a sesquilinear matrix form. The coefficientwise conjugation is the one that is not entrywise, as *Biquaternion 2×2 Matrix Element Representation* §*The Conjugations in Matrix Form* stresses, and it is presented here in the two equivalent forms above.

### The Norm in Matrices

**Corollary.** The norm, the trace and the adjugate satisfy

$$
\operatorname{adj}X = \langle\Phi^{-1}(X),\Phi^{-1}(X)\rangle_{\natural}\,X^{-1} , \qquad \det(\operatorname{adj}X) = \det X = \langle\Phi^{-1}(X),\Phi^{-1}(X)\rangle_{\natural} , \qquad \operatorname{tr}(\operatorname{adj}X) = 2Q_0
$$

for invertible $X = \Phi(\tilde Q)$.

**Proof.** The first is the identity $\operatorname{adj}X = \det(X)X^{-1}$ with $\det X = \langle\Phi^{-1}(X),\Phi^{-1}(X)\rangle_{\natural}$, the second is $\det(\operatorname{adj}X) = (\det X)^{2-1} = \det X$ for a $2\times2$ matrix, and the third is the trace of the adjugate, which is $Q_0$ from each diagonal entry by the display above. $\square$

**Remark.** On the norm-one elements the adjugate is the inverse, and this is the computational form of the natural conjugation that the idempotent section below uses. The adjugate also gives the criterion of *Biquaternion Norm and Invertibility* in matrix form: $\tilde Q$ is a unit if and only if $\Phi(\tilde Q)$ is invertible, that is if and only if $\operatorname{adj}\Phi(\tilde Q) \neq 0$.

## The Four Products in Matrices

### The Table

**Theorem (the four matrix forms).** Under $\Phi$ the four products of *The Four Biquaternion Complex Products* read

| product | rule on $\mathbb{B}$ | matrix form |
|---|---|---|
| plain | $\tilde P\tilde Q$ | $M(P)M(Q)$ |
| natural-bilinear | $\tilde P^{\natural}\tilde Q$ | $\operatorname{adj}M(P)\,M(Q)$ |
| complex sesquilinear (sibling) | $\tilde P\tilde Q^{*}$ | $M(P)M(Q)^{\dagger}$ |
| complex quaternionic sesquilinear | $\tilde P^{\natural}\tilde Q^{*}$ | $\operatorname{adj}M(P)\,M(Q)^{\dagger}$ |

where $M(\tilde X) = \Phi(\tilde X)$.

**Proof.** The first row is the isomorphism. The second is the first row with the first factor conjugated, $\Phi(\tilde P^{\natural}\tilde Q) = \operatorname{adj}M(P)\,M(Q)$. The third is the first row with the second factor starred, $\Phi(\tilde P\tilde Q^{*}) = M(P)M(Q)^{\dagger}$. The fourth combines the two, $\Phi(\tilde P^{\natural}\tilde Q^{*}) = \operatorname{adj}M(P)M(Q)^{\dagger}$. $\square$

**Remark.** The four products are the four ways of inserting the two conjugations into the two slots of the matrix product, and the table is the matrix counterpart of the comparison table of *Comparison Between the Four Biquaternion Products*: the four products differ by which slot carries the adjugate and which carries the conjugate transpose, and the fourth product carries both. The matrix form shows directly that the fourth product is the "$(\natural,{}^{*})$-twisted" matrix product, the twist being one adjugate and one conjugate transpose.

### The Sesquilinear Product in Matrices

**Corollary.** The fourth product is sesquilinear in the matrix model,

$$
\Phi\bigl((\lambda\tilde P)\star\tilde Q\bigr) = \lambda\,\Phi(\tilde P\star\tilde Q) , \qquad
\Phi\bigl(\tilde P\star(\lambda\tilde Q)\bigr) = \bar\lambda\,\Phi(\tilde P\star\tilde Q) ,
$$

the first factor linear and the second conjugate-linear, and it is not the matrix product.

**Proof.** The adjugate is $\mathbb{C}$-linear and the conjugate transpose is conjugate-linear, so $\operatorname{adj}(\lambda A) = \lambda\operatorname{adj}(A)$ and $(\lambda B)^{\dagger} = \bar\lambda B^{\dagger}$; the parities follow. The last statement is the difference between the fourth row and the first row of the table, and it is the matrix form of *The Product Is Not the Derived Operation* of the group article. $\square$

**Remark.** The matrix model makes the sesquilinearity visible as the presence of one adjugate and one dagger: a product with two adjugates would be $\mathbb{C}$-bilinear, and a product with two daggers would be conjugate-bilinear, and only the mixed pair is sesquilinear. The fourth product has the mixed pair, and it is the only one of the four in the last column of the table that is sesquilinear in the strong sense of the group (the sibling shares the property but not the adjugate).

**Corollary (the transpose form).** Since $\operatorname{adj}(X) = \varepsilon X^{\mathsf{T}}\varepsilon^{-1}$ with $\varepsilon = \Phi(-e_2) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, the fourth product in matrices is

$$
\Phi(\tilde P \star \tilde Q) = \varepsilon\,\Phi(\tilde P)^{\mathsf{T}}\,\varepsilon^{-1}\,\Phi(\tilde Q)^{\dagger} ,
$$

the **transpose** inserted in the first factor and the **conjugate transpose** in the second.

**Proof.** Substituting the adjugate identity $\operatorname{adj}(X) = \varepsilon X^{\mathsf{T}}\varepsilon^{-1}$ (which holds for every $2\times2$ matrix, $\varepsilon$ being the matrix of the symplectic form) into the fourth row of the table gives the display. $\square$

**Proposition (the trace and the determinant of a value and of its factors).** For $\tilde P\star\tilde Q$ with matrix $Z = \Phi(\tilde P\star\tilde Q)$,

$$
\operatorname{tr}Z = 2\,\mathrm{Sc}(\tilde P\star\tilde Q) = 2\bigl(P_0\overline{Q_0} - (\mathbf P,\overline{\mathbf Q})\bigr) , \qquad
\det Z = \langle\tilde P,\tilde P\rangle_{\natural}\overline{\langle\tilde Q,\tilde Q\rangle_{\natural}} ,
$$

while the two factors have $\operatorname{tr}\Phi(\tilde P) = 2P_0$, $\det\Phi(\tilde P) = \langle\tilde P,\tilde P\rangle_{\natural}$, and, for the starred conjugate, $\operatorname{tr}\Phi(\tilde Q)^{\dagger} = 2\overline{Q_0}$, $\det\Phi(\tilde Q)^{\dagger} = \overline{\langle\tilde Q,\tilde Q\rangle_{\natural}}$.

**Proof.** For every pair $X = \Phi(\tilde A)$, $Y = \Phi(\tilde B)$ the trace of the matrix product is twice the scalar part of the product of the elements, $\operatorname{tr}(XY) = 2\,\mathrm{Sc}(\tilde A\tilde B)$, since $\operatorname{tr}\Phi(\tilde C) = 2C_0$ and $\Phi$ is multiplicative; applying this to $\tilde A = \tilde P^{\natural}$ and $\tilde B = \tilde Q^{*}$ and using $\Phi(\tilde P^{\natural}) = \operatorname{adj}M(P)$, $\Phi(\tilde Q^{*}) = M(Q)^{\dagger}$ gives $\operatorname{tr}Z = 2\,\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*}) = 2\,\mathrm{Sc}(\tilde P\star\tilde Q)$. The scalar part of $\tilde P\star\tilde Q$ is the fourth row of the scalar-parts table of *The Four Biquaternion Complex Products*, that is $P_0\overline{Q_0} - (\mathbf P,\overline{\mathbf Q})$. The determinant is multiplicative and $\det\Phi(\tilde Q)^{\dagger} = \overline{\det\Phi(\tilde Q)}$, so $\det Z = \langle\tilde P,\tilde P\rangle_{\natural}\overline{\langle\tilde Q,\tilde Q\rangle_{\natural}}$ by the fourth norm law. The traces and determinants of the factors are the trace and determinant statements of *Biquaternion 2×2 Matrix Element Representation*. $\square$

**Remark.** The determinant of the value is the product of the norm of the first factor and the conjugate of the norm of the second, so the matrix of a product of norm-one factors again has determinant one; with the adjugate being the inverse there, the product of two unit matrices is computed by the twisted rule and stays in the determinant-one group, which is the matrix form of the fact that the units of the algebra are closed under the product. The trace of the value is twice its scalar part, and the scalar part is the sesquilinear pairing of the fourth row, so the matrix trace computes the sesquilinear form of *The Four Biquaternion Complex Products* on the value.

## The Idempotents in Matrices

### The Matrix Idempotent Equation

**Theorem (the idempotent equation).** An element $\tilde\Pi$ is idempotent for the multiplication if and only if its matrix $M = \Phi(\tilde\Pi)$ satisfies

$$
\operatorname{adj}(M)\,M^{\dagger} = M .
$$

**Proof.** The equation $\tilde\Pi\star\tilde\Pi = \tilde\Pi$ is $\tilde\Pi^{\natural}\tilde\Pi^{*} = \tilde\Pi$; applying the isomorphism and the two conjugation theorems gives $\operatorname{adj}(M)M^{\dagger} = M$. $\square$

**Corollary (the invertible case).** For an invertible idempotent, the equation is equivalent to $\det(M)M^{\dagger} = M^{2}$, and for an idempotent of norm one it is equivalent to $M^{\dagger} = M^{2}$.

**Proof.** For invertible $M$ the adjugate is $\det(M)M^{-1}$, so the equation reads $\det(M)M^{-1}M^{\dagger} = M$, that is $\det(M)M^{\dagger} = M^{2}$; with $\det(M) = \langle\tilde\Pi,\tilde\Pi\rangle_{\natural} = 1$ it reads $M^{\dagger} = M^{2}$. $\square$

**Remark.** The matrix equation is not the ordinary idempotent equation $M^{2} = M$, and the difference is the conjugations: the matrix of an idempotent of the product is not a projection in general, and the matrix of a projection is not an idempotent of the product in general. For example $\operatorname{diag}(1,\omega)$ satisfies $M^{2} = M^{\dagger}$ but not the idempotent equation, so $M^{2} = M^{\dagger}$ alone is not the criterion; the adjugate is essential.

### The Sphere of Idempotents

**Theorem (the sphere as an orbit).** The nontrivial idempotents of the multiplication are exactly the elements whose matrices are the unitary conjugates of the diagonal matrix $\operatorname{diag}(\omega,\omega^{2})$, where $\omega = e^{2\pi i/3}$,

$$
\tilde\Pi \longleftrightarrow M = U\operatorname{diag}(\omega,\omega^{2})U^{\dagger} , \qquad U \in U(2) ,
$$

and this set is the two-sphere $-\frac12 e_0 + \mu$ with $\lvert\mu\rvert^{2} = \frac34$ of *Idempotents of the Quaternionic Sesquilinear Product*.

**Proof.** An idempotent of norm one satisfies $M^{\dagger} = M^{2}$ by the corollary. Applying the dagger to both sides gives $(M^{\dagger})^{\dagger} = (M^{2})^{\dagger}$, that is $(M^{\dagger})^{2} = M$, and substituting $M^{\dagger} = M^{2}$ gives $M^{4} = M$; the norm-one matrix is invertible, so $M^{3} = I$. Then $MM^{\dagger} = MM^{2} = M^{3} = I$ and $M^{\dagger}M = I$, so $M$ is unitary, and $\det(M) = \langle\tilde\Pi,\tilde\Pi\rangle_{\natural} = 1$. A unitary matrix with $M^{3} = I$ and $\det M = 1$ has eigenvalues among the cube roots of unity with product $1$, so its spectrum is either $\{1,1\}$ or $\{\omega,\omega^{2}\}$; the first case is $M = I$, the identity $\tilde\Pi = e_0$, and the second, by the spectral theorem, is the displayed unitary conjugacy class. Conversely, for $M = U\operatorname{diag}(\omega,\omega^{2})U^{\dagger}$ one has $M^{\dagger} = M^{2}$, $M^{3} = I$ and $\det M = 1$, whence $\operatorname{adj}(M)M^{\dagger} = \det(M)M^{-1}M^{2} = M$, so every matrix of the class is the matrix of an idempotent. The trace of $\operatorname{diag}(\omega,\omega^{2})$ is $\omega + \omega^{2} = -1$, so $Q_0 = -\frac12$ for the matrices of the class; the relation $\operatorname{adj}(M^{\dagger}) = \operatorname{adj}(M^{2}) = \operatorname{adj}(M)^{2} = M^{-2} = M$ gives $\Phi(\overline{\tilde\Pi}) = \Phi(\tilde\Pi)$, so the three vector coordinates are real; and the unitarity of $M$ gives $\lvert Q_0\rvert^{2} + \lvert Q_1\rvert^{2} + \lvert Q_2\rvert^{2} + \lvert Q_3\rvert^{2} = 1$, hence $\lvert Q_1\rvert^{2} + \lvert Q_2\rvert^{2} + \lvert Q_3\rvert^{2} = \frac34$. The class is connected, has real dimension two, and is the two-sphere of the idempotent article. $\square$

**Remark.** The sphere of idempotents is therefore a familiar orbit of the unitary group, the class of a matrix whose eigenvalues are the two primitive cube roots of unity. The identification explains the two-sphere topologically, gives a second proof that every nontrivial idempotent is a unit (the class consists of unitary matrices), and shows that the idempotents are the order-three rotations in the unitary group of the algebra. In the other three products the idempotents are the trivial ones or the zero divisors, and the matrix criterion for those is the ordinary $M^{2} = M$ or the Hermitian projection condition; the fourth product is the only one with nontrivial idempotents that are not projections.

**Corollary.** The matrix of a nontrivial idempotent satisfies $M^{3} = I$, $M^{\dagger} = M^{2} = M^{-1}$ and $\det M = 1$; consequently $\operatorname{tr}M = -1$ and the characteristic polynomial of $M$ is $\lambda^{2} + \lambda + 1$.

**Proof.** The first two are the proof of the theorem, and the trace and the spectrum follow. $\square$

### The Zero Divisors in Matrices

**Proposition.** The zero divisors of the algebra are the elements whose matrices are singular, and the zero divisors of the fourth product coincide with the zero divisors of the algebra.

**Proof.** By the determinant–norm identity, $\Phi(\tilde Q)$ is singular if and only if $\langle\tilde Q,\tilde Q\rangle_{\natural} = 0$, which is the criterion of *Biquaternion Zero Divisors*; the zero divisors of the fourth product are those of the algebra because the fourth product is the algebra product with two bijections inserted (*The Isotope Reading* of the group article), and inserting bijections does not change the set of zero divisors. $\square$

**Remark.** The nontrivial idempotents of the fourth product are units, so they are not zero divisors, and this is the sharpest contrast of the batch: in the matrix model they are unitary matrices of order three, while the zero divisors are the singular matrices, and the two sets are disjoint. In the sibling complex sesquilinear product the nontrivial idempotents are the rank-one Hermitian projections, which are singular, so there the nontrivial idempotents are zero divisors; the matrix model makes the difference visible as the difference between a unitary matrix of order three and a projection.

## The Associator and the Operators in Matrices

### The Associator in Matrices

**Theorem (the associator).** For $M(\tilde X) = \Phi(\tilde X)$, the associator of *The Associator of the Quaternionic Sesquilinear Product* has the matrix form

$$
\Phi\bigl([\tilde P,\tilde Q,\tilde R]\bigr)
= \operatorname{adj}\bigl(M(Q)^{\dagger}\bigr)M(P)M(R)^{\dagger}
- \operatorname{adj}M(P)\,M(R)\,\operatorname{adj}\bigl(M(Q)^{\dagger}\bigr) .
$$

**Proof.** The associator is $\overline{\tilde Q}\tilde P\tilde R^{*} - \tilde P^{\natural}\tilde R\overline{\tilde Q}$. By the conjugation theorems, $\Phi(\overline{\tilde Q}) = \operatorname{adj}(M(Q)^{\dagger})$, $\Phi(\tilde P) = M(P)$, $\Phi(\tilde R^{*}) = M(R)^{\dagger}$, and $\Phi(\tilde P^{\natural}) = \operatorname{adj}M(P)$, $\Phi(\tilde R) = M(R)$. Substituting gives the display. $\square$

**Corollary (the vanishing condition).** The associator vanishes if and only if

$$
\operatorname{adj}\bigl(M(Q)^{\dagger}\bigr)M(P)M(R)^{\dagger} = \operatorname{adj}M(P)\,M(R)\,\operatorname{adj}\bigl(M(Q)^{\dagger}\bigr) ,
$$

the matrix condition for the two groupings to agree.

**Proof.** The matrix of the associator vanishes if and only if the two terms of the display are equal, the isomorphism being injective. $\square$

**Remark.** The matrix form of the associator is the difference of two products of three matrices, each product mixing the adjugate and the dagger, and it exhibits the failure of associativity as the failure of two matrix products to agree. The associator is not the commutator of any single pair, since the two products differ both in the placement of the adjugate and the dagger and in the order of the three factors, the first reading them as $Q,P,R$ and the second as $P,R,Q$; the matrix model makes this non-commutator structure explicit.

### The Operators in Matrices

**Theorem (the multiplication operators).** For every $\tilde A$ and $\tilde X$,

$$
\Phi\bigl(L_{\tilde A}(\tilde X)\bigr) = \operatorname{adj}M(\tilde A)\,M(\tilde X)^{\dagger} , \qquad
\Phi\bigl(R_{\tilde A}(\tilde X)\bigr) = \operatorname{adj}M(\tilde X)\,M(\tilde A)^{\dagger} .
$$

**Proof.** The left multiplication is $\tilde A\star\tilde X = \tilde A^{\natural}\tilde X^{*}$, whose matrix is $\operatorname{adj}M(A)M(X)^{\dagger}$; the right multiplication is $\tilde X\star\tilde A = \tilde X^{\natural}\tilde A^{*}$, whose matrix is $\operatorname{adj}M(X)M(A)^{\dagger}$. $\square$

**Corollary (the composition in matrices).** The composition of two left multiplications has the matrix form

$$
\Phi\bigl(L_{\tilde A}L_{\tilde B}(\tilde X)\bigr) = \operatorname{adj}M(A)\,M(X)\,\bigl(\operatorname{adj}M(B)\bigr)^{\dagger} ,
$$

with the middle factor $M(X)$ linear, the matrix counterpart of the composition law $L_{\tilde A}L_{\tilde B} = T_{\tilde A^{\natural},\overline{\tilde B}}$.

**Proof.** The matrix of the composition is the composition of the two matrix operators, and

$$
\operatorname{adj}M(A)\Bigl(\operatorname{adj}M(B)\,M(X)^{\dagger}\Bigr)^{\dagger}
= \operatorname{adj}M(A)\,M(X)\,\bigl(\operatorname{adj}M(B)\bigr)^{\dagger} ,
$$

using the involutivity of the dagger and the anti-multiplicativity of the adjugate. $\square$

**Remark.** The composition is a matrix product with $M(X)$ in the middle, which is the matrix form of the ordinary two-sided multiplication $T_{\tilde P,\tilde Q}$ and the reason the composition leaves the class of the multiplication operators: the left multiplication carries a dagger on $M(X)$ and the composition does not. Since $(\operatorname{adj}M(B))^{\dagger} = \operatorname{adj}(M(B)^{\dagger}) = M(\overline{\tilde B})$, the matrix form agrees with the value $T_{\tilde A^{\natural},\overline{\tilde B}} = \operatorname{adj}M(A)\,M(X)\,M(\overline{\tilde B})$ predicted by the composition law of *The Left and Right Multiplications of the Quaternionic Sesquilinear Product*.

## Summary

The isomorphism $\Phi : \mathbb{B} \to M_2(\mathbb{C})$ of *Biquaternion 2×2 Matrix Element Representation* carries the natural conjugation to the adjugate, the star conjugation to the conjugate transpose, the coefficientwise conjugation to the adjugate of the conjugate transpose, and the norm to the determinant. The four products take the four matrix forms $M(P)M(Q)$, $\operatorname{adj}M(P)M(Q)$, $M(P)M(Q)^{\dagger}$ and $\operatorname{adj}M(P)M(Q)^{\dagger}$, the fourth being the sesquilinear one with one adjugate and one dagger. The idempotents of the fourth product are the matrices satisfying $\operatorname{adj}(M)M^{\dagger} = M$; the nontrivial ones have norm one and satisfy $M^{\dagger} = M^{2}$, hence $M^{3} = I$, and they are exactly the unitary conjugates of $\operatorname{diag}(\omega,\omega^{2})$, the two-sphere of *Idempotents of the Quaternionic Sesquilinear Product*. The zero divisors are the singular matrices, and they are disjoint from the nontrivial idempotents, which are units. The associator is the difference $\operatorname{adj}(M(Q)^{\dagger})M(P)M(R)^{\dagger} - \operatorname{adj}M(P)M(R)\operatorname{adj}(M(Q)^{\dagger})$, and the left and right multiplications are $\operatorname{adj}M(A)M(X)^{\dagger}$ and $\operatorname{adj}M(X)M(A)^{\dagger}$; the composition of two left multiplications is a matrix product with $M(X)$ in the middle, which is the matrix form of the failure of closure. The matrix model thus presents the whole group as the theory of the twisted matrix product $\operatorname{adj}M(P)M(Q)^{\dagger}$ and of its two classical factors.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\Phi : \mathbb{B} \to M_2(\mathbb{C})$ | the matrix isomorphism of *Biquaternion 2×2 Matrix Element Representation*, with $\Phi(e_0) = I$ and $J_k = \Phi(e_k)$ the three images of the imaginary units |
| $\varepsilon = \Phi(-e_2) = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ | the matrix of the transpose-conjugation, $\operatorname{adj}(X) = \varepsilon X^{\mathsf{T}}\varepsilon^{-1}$ |
| $\Phi(\tilde Q) = \begin{pmatrix} Q_0 - iQ_3 & -iQ_1 - Q_2 \\ -iQ_1 + Q_2 & Q_0 + iQ_3 \end{pmatrix}$ | the matrix of a biquaternion |
| $\det\Phi(\tilde Q) = \langle\tilde Q,\tilde Q\rangle_{\natural}$ | the norm is the determinant |
| $\Phi(\tilde P^{\natural}) = \operatorname{adj}\Phi(\tilde P)$ | the natural conjugation is the adjugate |
| $\Phi(\tilde P^{*}) = \Phi(\tilde P)^{\dagger}$ | the star is the conjugate transpose |
| $\Phi(\overline{\tilde P}) = \operatorname{adj}(\Phi(\tilde P)^{\dagger})$ | the bar is the adjugate of the dagger |
| $\operatorname{adj}M(P)M(Q)^{\dagger}$ | the fourth product in matrices |
| $\operatorname{adj}(M)M^{\dagger} = M$ | the matrix idempotent equation |
| $U\operatorname{diag}(\omega,\omega^{2})U^{\dagger}$ | the sphere of idempotents as a unitary orbit |
| $\operatorname{adj}(M(Q)^{\dagger})M(P)M(R)^{\dagger} - \operatorname{adj}M(P)M(R)\operatorname{adj}(M(Q)^{\dagger})$ | the associator in matrices |
| $\operatorname{adj}M(A)M(X)^{\dagger}$ | the left multiplication in matrices |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (2nd ed., Cambridge University Press, 2012), for the adjugate, the determinant and the unitary group.
- Nicolas Bourbaki, *Algebra I, Chapters 1–3* (Springer, 1998), for the structure of $M_2(\mathbb{C})$ and its involutions.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the classification of the involutions of a matrix algebra and the orthosymplectic forms.
- Barry Simon, *Representations of Finite and Compact Groups* (American Mathematical Society, 1996), for the conjugacy classes of $U(2)$ and the orbits of the unitary group.
