# __Idempotents of the General Plain Sesqualgebra__

## Introduction

The general plain sesquilinear product $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ of *The Four General Products of the Biquaternion $\mathbb{C}$ Space* is the multiplication of the sesqualgebra $(\mathbb{B},\star)$ of *Introduction to the General Plain Sesqualgebra of Biquaternions*, and its idempotents are the solutions of the equation $\tilde Q\star\tilde Q=\tilde Q$. This article solves that equation. The answer is exact: **an element is idempotent for the sesquilinear multiplication if and only if it is a Hermitian idempotent of the algebra**, so the idempotents of the multiplication are the trivial pair $0,e_0$ together with the family of the elements

$$
\tilde\Pi_1(\hat\mu)=\tfrac12\bigl(e_0+i\hat\mu\bigr) ,
$$

indexed by the real unit vectors $\hat\mu$ of the vector subspace. The whole of the article is the move that makes the equation collapse to that family: applying the involution ${}^{*}$ to the equation shows that an idempotent of $\star$ is its own conjugate, and a Hermitian element whose $\star$-square is itself is an idempotent of the ordinary product.

The result is the element theory of the batch, and it is the sharpest of the three ways in which the sesquilinear multiplication separates the elements. The algebra's own idempotents, classified in *Idempotents of the General Plain Algebra*, are the elements $\tfrac12(e_0+\tilde\Xi i)$ over all roots $\tilde\Xi$ of $-e_0$, and the root $\tilde\Xi$ may be trivial, real or mixed; apart from the trivial pair, the Hermitian ones are exactly those with a real root, and they are the projections above. The others are not idempotent for the multiplication, and the failure is computed here rather than quoted. The same separation is read in the comparison of the four general products, *Comparison Between the Four General Products*, §*The Squares, the Idempotents and the Roots*, where the four idempotent sets are tabulated and the sesquilinear column is the family of the projections.

The setting is that of *Introduction to the General Plain Sesqualgebra of Biquaternions* and *Sesqualgebras*: $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_0$ the unit and $e_k^{2}=-e_0$; a general element is $\tilde Q=\sum_\mu Q_\mu e_\mu=Q_0e_0+\mathbf Q$ with $Q_\mu\in\mathbb{C}$; the conjugations are the natural one ${}^{\natural}$, $\tilde Q^{\natural}=Q_0-\mathbf Q$, and the star, $\tilde Q^{*}=\overline{Q_0}-\overline{\mathbf Q}$, the conjugate-linear involution of the algebra, with ${}^{*}=\bar{\cdot}\circ{}^{\natural}$; and the multiplication is $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$. The two halves of the involution are the remarkable subspaces $\mathbb{M}_+$ and $\mathbb{M}_-$ of *Hermitian and Skew-Hermitian Elements*. The idempotents of the algebra, the roots of $-e_0$ and the zero divisors that the nontrivial ones determine are *Idempotents of the General Plain Algebra*, *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* and *Zero Divisors of the General Plain Algebra*.

## The Idempotent Equation

### The Definition

**Definition.** An element $\tilde Q$ is **idempotent for the multiplication** $\star$, or a **$\star$-idempotent**, when

$$
\tilde Q\star\tilde Q=\tilde Q .
$$

The equation names a product, so the notion is relative to it; the general definition, with the orthogonal and primitive families, the projection and the Peirce decomposition, is *Definitions for the Study of the 12 Algebraic Structures*, §*The Idempotent, the Projection and the Peirce Decomposition*, and throughout this article the product is the general plain sesquilinear product $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ of the block. The idempotents of the associative product $\tilde P\tilde Q$ are called the **idempotents of the algebra**, and they are written $\tilde\Pi$ with $\tilde\Pi^{2}=\tilde\Pi$.

**Remark.** The two equations differ only in the second factor, $\tilde Q\tilde Q^{*}=\tilde Q$ against $\tilde Q\tilde Q=\tilde Q$, and the whole of the article is the consequence of that one difference. The $\star$-equation is the algebra equation with the conjugate read on the second factor, so its solutions are the algebra idempotents on which the involution makes no difference.

### Every $\star$-Idempotent Is Hermitian

**Theorem.** Let $\tilde Q$ satisfy $\tilde Q\star\tilde Q=\tilde Q$. Then $\tilde Q$ is Hermitian,

$$
\tilde Q^{*}=\tilde Q .
$$

**Proof.** The equation reads $\tilde Q\tilde Q^{*}=\tilde Q$. The square $\tilde Q\tilde Q^{*}$ is fixed by the involution for every $\tilde Q$, by *Introduction to the General Plain Sesqualgebra of Biquaternions*, §*The Squares and the Positive Cone*: $(\tilde Q\tilde Q^{*})^{*}=\tilde Q\tilde Q^{*}$. Applying ${}^{*}$ to the equation therefore gives

$$
\tilde Q\tilde Q^{*}=\tilde Q^{*} .
$$

The left-hand sides of the equation and of its conjugate are the same, so the right-hand sides are equal, $\tilde Q=\tilde Q^{*}$.

**Remark.** The proof uses two things and no more: the square is Hermitian, and the involution is injective. The self-adjointness is therefore forced on every solution of the $\star$-equation, and it is the reason the equation reduces to the algebra's: a Hermitian element has $\tilde Q^{*}=\tilde Q$, hence $\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}=\tilde Q\tilde Q=\tilde Q^{2}$, and the two squares coincide.

### The Reduction

**Corollary.** An element is idempotent for the multiplication $\star$ if and only if it is a Hermitian idempotent of the algebra:

$$
\tilde Q\star\tilde Q=\tilde Q \quad\Longleftrightarrow\quad \tilde Q=\tilde Q^{*}\ \text{ and }\ \tilde Q^{2}=\tilde Q .
$$

**Proof.** If $\tilde Q\star\tilde Q=\tilde Q$ then $\tilde Q$ is Hermitian by the theorem, and $\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}=\tilde Q^{2}$, so $\tilde Q^{2}=\tilde Q$. Conversely a Hermitian idempotent has $\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*}=\tilde Q\tilde Q=\tilde Q^{2}=\tilde Q$.

**Remark.** The reduction is the whole content of the element theory: the $\star$-idempotents are cut out of the algebra's idempotents by the single condition of Hermitianness. The three families of the algebra's idempotents of *Idempotents of the General Plain Algebra* are then separated by that condition, and the next sections carry out the separation.

**Proposition (the scalar part of the equation).** Let $\tilde Q$ satisfy $\tilde Q\star\tilde Q=\tilde Q$. Then the scalar part of $\tilde Q$ is the sum of the modulus squares of its coordinates,

$$
Q_0=\mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr)=\sum_{\mu=0}^{3}Q_\mu\overline{Q_\mu}=\sum_{\mu=0}^{3}\lvert Q_\mu\rvert^{2} ,
$$

a real number, and it is nonzero unless $\tilde Q=0$.

**Proof.** The scalar part of the square is $\sum_\mu\lvert Q_\mu\rvert^{2}$ by *Introduction to the General Plain Sesqualgebra of Biquaternions*, §*The Squares and the Positive Cone*; taking the scalar part of $\tilde Q\star\tilde Q=\tilde Q$ gives $Q_0=\sum_\mu\lvert Q_\mu\rvert^{2}$. The sum of the modulus squares is a nonnegative real number, and it vanishes only when every coordinate vanishes.

**Remark.** The display is a constraint and not a definition: it rules out at once the algebra idempotents with a non-real scalar part, and it is the first appearance of the nonnegativity of the sesquilinear square that *The Squares and the Positive Cone of the Biquaternion Sesqualgebra* develops.

## The Projections

### The Classification

**Theorem (the idempotents of the multiplication).** The idempotents of the sesquilinear multiplication $\star$ are $0$, $e_0$ and the elements

$$
\tilde\Pi_1(\hat\mu)=\tfrac12\bigl(e_0+i\hat\mu\bigr) , \qquad \hat\mu\in\mathbb{R}^{3},\ (\hat\mu,\hat\mu)=1 ,
$$

where $\hat\mu=\sum_{k=1}^{3}\hat\mu_k e_k$ ranges over the real vectors of the vector subspace with $(\hat\mu,\hat\mu)=\sum_k\hat\mu_k^{2}=1$. There are no others.

**Proof.** By the corollary, the $\star$-idempotents are the Hermitian idempotents of the algebra. The idempotents of the algebra are classified in *Idempotents of the General Plain Algebra*: every idempotent is either trivial or of the form $\tfrac12(e_0+\tilde\Xi i)$ with $\tilde\Xi$ a root of $-e_0$, and every root falls into one of the three families of *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*. The idempotent is Hermitian exactly when $\tilde\Xi^{*}=-\tilde\Xi$: indeed $\tilde\Pi(\tilde\Xi)^{*}=\tfrac12(e_0+\tilde\Xi^{*}i^{*})=\tfrac12(e_0-\tilde\Xi^{*}i)$, which is $\tilde\Pi(\tilde\Xi)$ exactly when $-\tilde\Xi^{*}=\tilde\Xi$. The roots with $\tilde\Xi^{*}=-\tilde\Xi$ are the trivial roots $\pm i$, whose idempotents are the trivial pair $0$ and $e_0$, and the real roots $\tilde\Xi=\pm\mu$ over the real vectors $\mu$ with $(\mu,\mu)=1$; a mixed root $\tilde\Xi=\boldsymbol p+i\boldsymbol p'$ has $\boldsymbol p'\neq0$, so $\tilde\Xi^{*}=-\boldsymbol p+i\boldsymbol p'\neq-\boldsymbol p-i\boldsymbol p'=-\tilde\Xi$, and its idempotent is not Hermitian. Writing $\hat\mu=\pm\mu$ absorbs the sign, and $\tfrac12(e_0+\mu i)=\tfrac12(e_0+i\mu)=\tilde\Pi_1(\hat\mu)$ because $i$ is central, while the trivial roots give $0$ and $e_0$.

**Remark.** The word **projection** is used here for a Hermitian idempotent of the algebra and for nothing else, and the $\star$-idempotents are exactly the projections. The two families of *Idempotents of the General Plain Algebra* that are not Hermitian are the ones the multiplication discards, and they are treated in the next section.

### The Coordinates

**Proposition (the coordinate form).** For a real vector $\hat\mu$ with $(\hat\mu,\hat\mu)=1$ and coordinates $\hat\mu_k\in\mathbb{R}$,

$$
\tilde\Pi_1(\hat\mu)=\tfrac12 e_0+\tfrac{i}{2}\sum_{k=1}^{3}\hat\mu_k e_k ,
$$

so its scalar part is $\tfrac12$, its vector part is $\tfrac{i}{2}\hat\mu$, and its four coordinates are $\bigl(\tfrac12,\tfrac{i}{2}\hat\mu_1,\tfrac{i}{2}\hat\mu_2,\tfrac{i}{2}\hat\mu_3\bigr)$. Its scalar part is the sum of the modulus squares of its coordinates,

$$
\tfrac12=\tfrac14+\tfrac14\sum_k\hat\mu_k^{2} ,
$$

which is the scalar-part identity of the previous section read on this family.

**Proof.** The coordinates are read from the display, and $\sum_k\hat\mu_k^{2}=1$ gives the scalar-part identity $Q_0=\sum_\mu\lvert Q_\mu\rvert^{2}$.

**Remark.** The scalar part $\tfrac12$ is fixed by $(\hat\mu,\hat\mu)=1$ and is the same for the whole family; the square of the scalar part is $\tfrac14$, the sum of the squares of the vector coordinates is $\tfrac14$, and the two add to the scalar part. The scalar part is therefore not an extra datum: it is forced by the normalisation of the direction, and the family is the whole set of the projections and not a proper subfamily of it.

### The Complement and the Pairing of the Directions

**Proposition (the complement is the antipode).** For every real vector $\hat\mu$ with $(\hat\mu,\hat\mu)=1$,

$$
e_0-\tilde\Pi_1(\hat\mu)=\tilde\Pi_1(-\hat\mu),
$$

and the two are idempotents orthogonal in the algebra and summing to the unit,

$$
\tilde\Pi_1(\hat\mu)\tilde\Pi_1(-\hat\mu)=0 , \qquad \tilde\Pi_1(\hat\mu)+\tilde\Pi_1(-\hat\mu)=e_0 .
$$

**Proof.** The first identity is $e_0-\tfrac12(e_0+i\hat\mu)=\tfrac12(e_0-i\hat\mu)=\tilde\Pi_1(-\hat\mu)$. For the orthogonality, multiply out, using $\hat\mu^{2}=-(\hat\mu,\hat\mu)e_0=-e_0$:

$$
\tilde\Pi_1(\hat\mu)\tilde\Pi_1(-\hat\mu)=\tfrac14\bigl(e_0+i\hat\mu\bigr)\bigl(e_0-i\hat\mu\bigr)=\tfrac14\bigl(e_0-\hat\mu^{2}\bigr)=\tfrac14\bigl(e_0+e_0\bigr)=0 ,
$$

and the sum is immediate.

**Remark.** The complementary pair of a projection is the projection at the antipodal direction, exactly as in the classification of *Idempotents of the General Plain Algebra*, where the pair is indexed by the class $\{\tilde\Xi,-\tilde\Xi\}$ of the root.

**Proposition (when two projections are orthogonal).** For real vectors $\hat\mu,\hat\nu$ with $(\hat\mu,\hat\mu)=(\hat\nu,\hat\nu)=1$,

$$
\tilde\Pi_1(\hat\mu)\tilde\Pi_1(\hat\nu)=0 \quad\Longleftrightarrow\quad \hat\nu=-\hat\mu .
$$

**Proof.** Multiplying out and using $\hat\mu\hat\nu=-(\hat\mu,\hat\nu)e_0+\hat\mu\times\hat\nu$ for the product of two pure real vectors gives

$$
\tilde\Pi_1(\hat\mu)\tilde\Pi_1(\hat\nu)=\tfrac14\Bigl(\bigl(1+(\hat\mu,\hat\nu)\bigr)e_0-\hat\mu\times\hat\nu+i\bigl(\hat\mu+\hat\nu\bigr)\Bigr) .
$$

The scalar part vanishes when $(\hat\mu,\hat\nu)=-1$, and for two real vectors with $(\hat\mu,\hat\mu)=(\hat\nu,\hat\nu)=1$ this forces $\hat\nu=-\hat\mu$, because then $(\hat\mu+\hat\nu,\hat\mu+\hat\nu)=(\hat\mu,\hat\mu)+2(\hat\mu,\hat\nu)+(\hat\nu,\hat\nu)=0$, and a real vector whose square vanishes is zero. With $\hat\nu=-\hat\mu$ the vector part is $-\hat\mu\times(-\hat\mu)+i(\hat\mu-\hat\mu)=0$ as well. Conversely $\hat\nu=-\hat\mu$ gives $0$ by the previous proposition.

**Remark.** Orthogonality is therefore as sparse as it can be: a projection is orthogonal, as an algebra idempotent, to one other projection of the family and to no third one, so the family is not an orthogonal set but a family of complementary pairs. The Peirce decomposition of the algebra relative to the standard pair is *Ideals and Peirce Decomposition of the General Plain Algebra*.

### The Standard Pair

**Example.** The two projections at the directions $\pm e_3$ are the standard idempotents of the algebra of *Idempotents of the General Plain Algebra*,

$$
\tilde\Pi_1(\hat e_3)=\tfrac12(e_0+ie_3)=\tilde\Pi_1 , \qquad \tilde\Pi_1(-\hat e_3)=\tfrac12(e_0-ie_3)=\tilde\Pi_2 ,
$$

and they are the images under $\mathsf{M}_2$ of the two diagonal matrix units of the matrix model: $\tilde\Pi_1(\hat e_3)$ corresponds to $E_{11}$ and $\tilde\Pi_1(-\hat e_3)$ to $E_{22}$, as the transport of *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* records. Since the equalities are equalities in the algebra, they hold for the multiplication $\star$ as well, a Hermitian element having the same square in the two products.

## The Contrast with the Algebra

### The Idempotents of the Algebra

The classification of the algebra's idempotents is *Idempotents of the General Plain Algebra*: every idempotent is either trivial or of the form

$$
\tilde\Pi(\tilde\Xi)=\tfrac12\bigl(e_0+\tilde\Xi i\bigr) , \qquad \tilde\Xi^{2}=-e_0 ,
$$

and the map $\tilde\Xi\mapsto\tilde\Pi(\tilde\Xi)$ is a bijection from the roots of $-e_0$ onto the idempotents of $\mathbb{B}$. The roots fall into three families, by *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*: the trivial roots $\pm i$, whose idempotents are $0$ and $e_0$; the real roots $\pm\mu$ over the real vectors $\mu$ with $(\mu,\mu)=1$, whose idempotents are the projections $\tilde\Pi_1(\pm\mu)$ of the previous section; and the mixed roots $\tilde\Xi=\boldsymbol p+i\boldsymbol p'$, whose idempotents are Hermitian for no value of the pair of real vectors.

### The Non-Hermitian Idempotents Are Not Idempotent for the Multiplication

**Proposition (the contrapositive).** Let $\tilde\Pi$ be an idempotent of the algebra. If $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ then $\tilde\Pi$ is Hermitian; equivalently, an idempotent of the algebra that is not Hermitian is not idempotent for the multiplication.

**Proof.** A solution of $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ satisfies $\tilde\Pi^{*}=\tilde\Pi$ by the theorem of §*The Idempotent Equation*, applied to an element that is already idempotent for the algebra. Conversely a Hermitian idempotent has $\tilde\Pi\star\tilde\Pi=\tilde\Pi\tilde\Pi^{*}=\tilde\Pi^{2}=\tilde\Pi$, so the $\star$-idempotents among the idempotents of the algebra are exactly the Hermitian ones.

**Example (the simplest non-Hermitian idempotent).** Take the real orthonormal pair $(\mu,\nu)=(e_1,e_2)$ and the real pair $(b,d)=(\sqrt2,1)$, so that $b^{2}-d^{2}=1$ and

$$
\tilde\Xi=b\mu+d\nu i=\sqrt2\,e_1+ie_2
$$

is a mixed root of $-e_0$ of *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra*, the two conditions of that classification being $b^{2}-d^{2}=1$ and $\mu\perp\nu$. Then

$$
\tilde\Pi(\tilde\Xi)=\tfrac12(e_0+\tilde\Xi i)=\tfrac12 e_0+\tfrac12\bigl(\sqrt2\,ie_1-e_2\bigr)
$$

is an idempotent of the algebra, and it is not Hermitian. Its square in the multiplication is

$$
\tilde\Pi(\tilde\Xi)\star\tilde\Pi(\tilde\Xi)=\tilde\Pi(\tilde\Xi)\tilde\Pi(\tilde\Xi)^{*}=e_0+\tfrac{\sqrt2}{2}\,ie_1+\tfrac{\sqrt2}{2}\,ie_3\neq\tilde\Pi(\tilde\Xi) .
$$

**Proof.** The idempotence for the algebra is that of *Idempotents of the General Plain Algebra*, and the failure of Hermitianness is read from $\tilde\Pi(\tilde\Xi)^{*}=\tfrac12(e_0-\tilde\Xi^{*}i)$ with $\tilde\Xi^{*}=-\sqrt2 e_1+ie_2\neq\tilde\Xi$, where ${}^{*}$ acts on the central $i$ as $i^{*}=-i$ because $i$ sits among the coefficients. For the square, multiply out,

$$
\tilde\Pi(\tilde\Xi)\tilde\Pi(\tilde\Xi)^{*}=\tfrac14\bigl(e_0+\tilde\Xi i\bigr)\bigl(e_0-\tilde\Xi^{*}i\bigr)=\tfrac14\bigl(e_0+(\tilde\Xi-\tilde\Xi^{*})i+\tilde\Xi\tilde\Xi^{*}\bigr) ,
$$

using $i^{*}=-i$ and $i^{2}=-1$. Here $\tilde\Xi-\tilde\Xi^{*}=2\sqrt2\,e_1$, and

$$
\tilde\Xi\tilde\Xi^{*}=\bigl(\sqrt2 e_1+ie_2\bigr)\bigl(-\sqrt2 e_1+ie_2\bigr)=3e_0+2\sqrt2\,ie_3 ,
$$

by the multiplication of the basis, so the sum is $\tfrac14(4e_0+2\sqrt2\,ie_1+2\sqrt2\,ie_3)=e_0+\tfrac{\sqrt2}{2}ie_1+\tfrac{\sqrt2}{2}ie_3$, which differs from $\tilde\Pi(\tilde\Xi)$.

**Remark.** The element is the one recorded in *Introduction to the General Plain Sesqualgebra of Biquaternions* as the distinguishing case of the proposition: it is idempotent for the bilinear product and not for the sesquilinear one. Its scalar part is $\tfrac12$, but $\mathrm{Sc}(\tilde\Pi\star\tilde\Pi)=1$, so the scalar-part identity of §*The Idempotent Equation* fails at the same element, which is a second reading of the same failure.

### The Two Sets Compared

| idempotent set | description | size |
|---|---|---|
| of the associative multiplication $\tilde P\tilde Q$ | the elements $\tilde\Pi(\tilde\Xi)=\tfrac12(e_0+\tilde\Xi i)$ over the roots $\tilde\Xi$ of $-e_0$ | a real four-dimensional family together with two isolated points |
| of the sesquilinear multiplication $\star$ | the trivial pair and the projections $\tilde\Pi_1(\hat\mu)$ over the real vectors with $(\hat\mu,\hat\mu)=1$ | a real two-dimensional family together with two isolated points |
| in common | the trivial pair $0,e_0$ and the projections | the sesquilinear set |

**Theorem.** The idempotents of the two multiplications agree exactly on the trivial pair and the projections, so the common set is the sesquilinear set, and every idempotent of the algebra that is not Hermitian is dropped in the passage to $\star$.

**Proof.** The idempotents of the algebra are the elements $\tilde\Pi(\tilde\Xi)$ over the roots $\tilde\Xi$ of $-e_0$; those that are Hermitian are the trivial pair together with the real-root family, by the classification theorem of §*The Projections*; and the idempotents of $\star$ are the trivial pair together with the Hermitian idempotents, by the same theorem. The two sets therefore meet in the trivial pair and the projections, which is the whole of the $\star$ set.

**Remark.** The passage from the algebra to the sesqualgebra keeps one half of the idempotents and loses the other, and it keeps the half that the algebra's own element theory singles out as the projections. The two sets agree on $0$ and $e_0$ because the trivial idempotents are Hermitian and central; they disagree on every nontrivial non-Hermitian idempotent, of which the element of the example above is the one the group article records.

## The Matrix Model

**Proposition.** Under the isomorphism $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ of *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$*, which satisfies $\mathsf{M}_2(\tilde Q^{*})=\mathsf{M}_2(\tilde Q)^{\dagger}$ and $\mathsf{M}_2(\tilde P\tilde Q^{*})=\mathsf{M}_2(\tilde P)\mathsf{M}_2(\tilde Q)^{\dagger}$, the projections are the rank-one Hermitian idempotents of the matrix algebra,

$$
\mathsf{M}_2\bigl(\tilde\Pi_1(\hat\mu)\bigr)=\tfrac12\bigl(I+i\mathsf{M}_2(\hat\mu)\bigr) ,
$$

and the family is the set of the rank-one Hermitian idempotents of $M_2(\mathbb{C})$.

**Proof.** The image of a Hermitian idempotent is Hermitian, $\mathsf{M}_2(\tilde\Pi)^{\dagger}=\mathsf{M}_2(\tilde\Pi^{*})=\mathsf{M}_2(\tilde\Pi)$, and idempotent, $\mathsf{M}_2(\tilde\Pi)^{2}=\mathsf{M}_2(\tilde\Pi^{2})=\mathsf{M}_2(\tilde\Pi)$. The image of $\tilde\Pi_1(\hat\mu)$ is computed from $\mathsf{M}_2(\tilde Q)=\sum_\mu Q_\mu\mathsf{M}_2(e_\mu)$ on the coordinates of §*The Projections*, and $\mathsf{M}_2(i\hat\mu)=i\mathsf{M}_2(\hat\mu)$ because $\mathsf{M}_2$ is $\mathbb{C}$-linear. The matrices $i\mathsf{M}_2(e_1),i\mathsf{M}_2(e_2),i\mathsf{M}_2(e_3)$ are Hermitian, traceless and $i\mathsf{M}_2(e_k)^{2}=I$, and they form a real basis of the traceless Hermitian matrices; hence $i\mathsf{M}_2(\hat\mu)=\sum_k\hat\mu_k\,i\mathsf{M}_2(e_k)$ is traceless Hermitian with square $(\hat\mu,\hat\mu)I$, and for $(\hat\mu,\hat\mu)=1$ the element $\tfrac12(I+i\mathsf{M}_2(\hat\mu))$ is a Hermitian idempotent of rank one because its trace is one. Conversely every rank-one Hermitian idempotent of $M_2(\mathbb{C})$ is $\tfrac12(I+H)$ with $H$ traceless Hermitian and $H^{2}=I$, and every such $H$ is $i\mathsf{M}_2(\hat\mu)$ for a real vector $\hat\mu$ with $(\hat\mu,\hat\mu)=1$.

**Remark.** The matrix image is the standard rank-one projection of a two-dimensional space, and the parametrisation by the real vectors $\hat\mu$ with $(\hat\mu,\hat\mu)=1$ is the parametrisation of those projections by the traceless Hermitian involutions. The standard pair is $\mathsf{M}_2(\tilde\Pi_1)=E_{11}$ and $\mathsf{M}_2(\tilde\Pi_2)=E_{22}$.

## The Operator Reading

The idempotents of the block are a class of **elements**, and they must not be confused with the projectors of the block, which are a class of **operators**. The distinction is the one the specificities article states: an element idempotent for the multiplication gives a projector under its right multiplication, and the converse fails, because the right projectors are the idempotents of the **plain** product; on the left the only projector is the zero operator. The two classes are different.

**Corollary (idempotent elements and their operators).** An element $\tilde\Pi$ that is idempotent for $\star$ has $R^{\star}_{\tilde\Pi}$ a projector, because $\tilde\Pi\star\tilde\Pi=\tilde\Pi$ gives $R^{\star}_{\tilde\Pi}{}^{2}=R^{\star}_{\tilde\Pi}$. The left multiplication is **not** a projector unless $\tilde\Pi=0$. But the elements whose right multiplication is a projector are the idempotents of the **plain** product, a family of complex dimension two, and they strictly contain the idempotents of the block.

*Proof.* The operator statement on the right is the right-composition law $R^{\star}_{\tilde P}R^{\star}_{\tilde Q}=R^{\star}_{\tilde P\tilde Q}$ read at $\tilde P=\tilde Q=\tilde\Pi$. The class of the projectors is the projector criterion of *The Specificities of the General Plain Sesqualgebra*: $R^{\star}_{\tilde P}$ is a projector exactly when $\tilde P$ is a plain idempotent, and the plain idempotents $\tfrac12(e_0+\eta)$ over the pure elements $\eta$ with $\eta^{2}=e_0$ form a complex quadric, of which the block's idempotents are the Hermitian subfamily of real-dimension two. On the left there is no composition law, and a conjugate-linear projector is the zero operator, so $L^{\star}_{\tilde\Pi}$ is a projector only for $\tilde\Pi=0$.

**Remark (the half that the multiplication keeps).** On the element level the multiplication keeps the Hermitian idempotents and drops the rest; on the operator level the right multiplications recover the whole plain idempotent set, read at the conjugated index. The gap between the two is the gap between the block's element theory and its right-operator theory, and it is the mirror of the gap that the general quaternionic product shows on its left side (*The Specificities of the General Quaternionic Algebra*). The projectors themselves, their images and their kernels, are treated in the operator articles of the block.

## Summary

An element is idempotent for the sesquilinear multiplication $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ exactly when it is a Hermitian idempotent of the algebra, because applying the involution ${}^{*}$ to the equation $\tilde Q\tilde Q^{*}=\tilde Q$ forces $\tilde Q^{*}=\tilde Q$, and a Hermitian element has the same square in the two products. The idempotents of the multiplication are therefore the trivial pair $0,e_0$ and the **projections**

$$
\tilde\Pi_1(\hat\mu)=\tfrac12\bigl(e_0+i\hat\mu\bigr) , \qquad \hat\mu\in\mathbb{R}^{3},\ (\hat\mu,\hat\mu)=1 ,
$$

a family parametrised by the real unit vectors, whose scalar part is the sum of the modulus squares of its coordinates and whose complement is the antipodal projection $\tilde\Pi_1(-\hat\mu)$. Against the idempotents of the associative multiplication, which are the elements $\tilde\Pi(\tilde\Xi)=\tfrac12(e_0+\tilde\Xi i)$ over all roots $\tilde\Xi$ of $-e_0$ and form a real four-dimensional family, the $\star$-idempotents are the same trivial pair together with the Hermitian idempotents, and every non-Hermitian idempotent of the algebra is not idempotent for the multiplication. The two sets agree exactly on the projections, which is the sense in which the multiplication picks out the half of the algebra's idempotent set that the algebra itself calls the projections.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $e_0,e_1,e_2,e_3$ | the basis, $e_0$ the unit, $e_k^{2}=-e_0$ |
| $\tilde Q=Q_0e_0+\mathbf Q$ | an element, $Q_\mu\in\mathbb{C}$ complex coordinates |
| $\mathbf Q=\sum_kQ_ke_k$ | the vector part |
| ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ | the conjugate-linear involution, $\tilde Q^{*}=\overline{Q_0}-\overline{\mathbf Q}$ |
| ${}^{\natural}$ | the natural conjugation, $\tilde Q^{\natural}=Q_0-\mathbf Q$ |
| $\tilde P\star\tilde Q=\tilde P\tilde Q^{*}$ | the sesquilinear multiplication |
| $\tilde Q\star\tilde Q=\tilde Q$ | the idempotent equation of the multiplication |
| $\tilde\Pi_1(\hat\mu)=\tfrac12(e_0+i\hat\mu)$ | the projections, $\hat\mu$ a real vector with $(\hat\mu,\hat\mu)=1$ |
| $\hat\mu=\sum_k\hat\mu_ke_k$, $(\hat\mu,\hat\mu)=\sum_k\hat\mu_k^{2}=1$ | a real unit vector and its square |
| $\mathbb{M}_+,\mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces |
| $\tilde\Pi(\tilde\Xi)=\tfrac12(e_0+\tilde\Xi i)$, $\tilde\Xi^{2}=-e_0$ | the idempotents of the algebra |
| $0,\ e_0$ | the trivial idempotents, common to the two products |
| $\mathsf{M}_2$ | the isomorphism $\mathbb{B}\to M_2(\mathbb{C})$, $\mathsf{M}_2(\tilde Q^{*})=\mathsf{M}_2(\tilde Q)^{\dagger}$ |
| $E_{11},E_{22}$ | the diagonal matrix units, $\mathsf{M}_2(\tilde\Pi_1),\mathsf{M}_2(\tilde\Pi_2)$ |

## Further Reading

- *Introduction to the General Plain Sesqualgebra of Biquaternions* (`articles_maths/introduction-to-the-general-plain-sesqualgebra-of-biquaternions.md`), for the product, its class, its two slot involutions and the positive cone of the square that the reduction uses.
- *Idempotents of the General Plain Algebra* (`articles_maths/idempotents-of-the-general-plain-algebra.md`), for the idempotents $\tilde\Pi(\tilde\Xi)=\tfrac12(e_0+\tilde\Xi i)$ of the associative product over the roots $\tilde\Xi$ of $-e_0$, whose Hermitian half is the set computed here.
- *Square Roots of Minus One, Zero and Plus One in the General Plain Algebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-algebra.md`), for the three families of roots $\tilde\Xi$ of $-e_0$ that the Hermitian condition separates.
- *Square Roots of Minus One, Zero and Plus One in the General Plain Sesqualgebra* (`articles_maths/square-roots-of-minus-one-zero-and-plus-one-in-the-general-plain-sesqualgebra.md`), for the block's own root sets, whose root of $+1$ is the family $\tilde\Pi_1(\hat\mu)$ met here.
- *Zero Divisors of the General Plain Sesqualgebra* (`articles_maths/zero-divisors-of-the-general-plain-sesqualgebra.md`), for the non-pure zero divisors among which the idempotents $\tilde\Pi_1(\hat\mu)$ sit.
- *The Specificities of the General Plain Sesqualgebra* (`articles_maths/the-specificities-of-the-general-plain-sesqualgebra.md`), for the projector criterion of the right multiplications, whose projector family is the whole plain idempotent set and therefore strictly larger than the block's idempotent set computed here.
- *The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation $M_2(\mathbb{C})$* (`articles_maths/the-general-plain-sesqualgebra-in-the-2x2-matrix-element-representation.md`), for the model in which the idempotents are the rank-one Hermitian projections $E_{11},E_{22}$ and their conjugates.
- *Definitions for the Study of the 12 Algebraic Structures* (`articles_maths/definitions-for-the-study-of-the-12-algebraic-structures.md`), for the general definition of an idempotent, the projection and the Peirce decomposition.
