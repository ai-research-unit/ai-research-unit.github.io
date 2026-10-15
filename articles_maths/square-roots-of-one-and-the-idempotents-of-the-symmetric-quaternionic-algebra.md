# __Square Roots of One and the Idempotents of the Symmetric Quaternionic Algebra__

## Introduction

The symmetric quaternionic product is the pairing $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$ on $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the product of the block (*Introduction to the Symmetric Quaternionic Algebra of Biquaternions*), and it is the product read throughout this article. A root of a central value $\lambda$ is a nonzero element with $\tilde\Xi\star\tilde\Xi=\lambda e_0$ (*Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* §*Powers, the Square and the Roots*). The square is always central, $\tilde\Xi\star\tilde\Xi=N(\tilde\Xi)e_0$, so the equation for a central value is the single scalar equation $N(\tilde\Xi)=\lambda$ for the quadratic form $N(\tilde\Xi)=\sum_{\mu=0}^{3}\Xi_\mu^2$, and the root sets of the block are level sets of one form (*Norm and Invertibility in the Symmetric Quaternionic Algebra*).

The article treats two subjects, and in this order. The first is the square roots of the central value $+1$, the elements $\tilde\Xi\in\mathbb{B}$ with

$$
\tilde\Xi\star\tilde\Xi=e_0 .
$$

The second is the idempotents of the product, the elements $\tilde\Pi$ with $\tilde\Pi\star\tilde\Pi=\tilde\Pi$. The two subjects are one subject in an associative unital product, where the **halving map**

$$
\tilde\Xi\longmapsto\tilde\Pi=\tfrac12(e_0+\tilde\Xi),\qquad \tilde\Xi\star\tilde\Xi=e_0,
$$

is a bijection from the roots of $+1$ onto the idempotents, with inverse $\tilde\Xi=2\tilde\Pi-e_0$. In this block it is not, and the failure is structural: the product is central valued, it has neither a unit nor an associativity, and the square of an element can never restore its vector part. The article states the roots of $+1$, states the two idempotents, and states the failure of the halving map as the correction it is; the idempotents are classified on their own equation, and on nothing else.

**The results.** The roots of $+1$ are the level set $N=1$ of the diagonal form $N(\tilde\Xi)=\Xi_0^2+(\vec\Xi,\vec\Xi)$, an affine hyperquadric of complex dimension three containing the two central roots $\pm e_0$ and the four basis elements $e_0,e_1,e_2,e_3$. The scaling $\tilde\Xi\mapsto\mu\tilde\Xi$ carries the level $\lambda$ onto the level $\mu^2\lambda$, so the levels are pairwise disjoint and the non-central ones form one orbit. The idempotents are exactly $0$ and $e_0$: the equation $\tilde\Pi\star\tilde\Pi=N(\tilde\Pi)e_0=\tilde\Pi$ forces the vector part to vanish and the scalar part to satisfy $\Pi_0^2=\Pi_0$. The halving map carries the two central roots of $+1$ onto the two idempotents and carries no other root of $+1$ to an idempotent, so the bijection of the parent is false here and not merely unproved; the idempotent $e_0$ acts by the projection $E$ onto the centre along the vector subspace, which is not the identity; and the block has no Peirce decomposition and no classification of its zero divisors by idempotents.

The article is algebraic. It does not treat the roots of $0$ and the nilpotents, which are *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Algebra*; the roots of a general element, which are *Square Roots of a General Element in the Symmetric Quaternionic Algebra*; the isotropic cone and its two families, which are *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*; the structure of the zero-divisor set, which is *Zero Divisors of the Symmetric Quaternionic Algebra*; or the operators of the block and its idempotent endomorphisms, which are *The Multiplication Operators of the Symmetric Quaternionic Algebra* and *The Specificities of the Symmetric Quaternionic Algebra*. The last paragraph of §*The Roots of One* records how the roots of $-1$ are read off the roots of $+1$; it is a remark, it is used nowhere, and it opens nothing.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has basis $e_0,e_1,e_2,e_3$ with $e_1e_2=e_3$, and central scalar imaginary $i$, $i^2=-1$. A general element is $\tilde\Xi=\Xi_0e_0+\vec\Xi$ with $\Xi_\mu\in\mathbb{C}$ and $\vec\Xi=\Xi_1e_1+\Xi_2e_2+\Xi_3e_3$, and $(\vec\Xi,\vec\Xi)=\sum_{k=1}^{3}\Xi_k^2$ may vanish without $\vec\Xi$ vanishing. The **symmetric quaternionic multiplication** is

$$
\tilde\Xi\star\tilde Q=N(\tilde\Xi,\tilde Q)e_0,\qquad N(\tilde\Xi,\tilde Q)=\Xi_0Q_0+(\vec\Xi,\vec Q),
$$

and its diagonal is $N(\tilde\Xi)=N(\tilde\Xi,\tilde\Xi)=\sum_{\mu=0}^{3}\Xi_\mu^2$; the operation is also written $\bullet$. The centre is $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$, the vector subspace is $\mathrm{Vect}(\mathbb{B})=\mathbb{C}e_1+\mathbb{C}e_2+\mathbb{C}e_3$, and $E$ is the projection $\tilde Y\mapsto Y_0e_0$ of the space onto its centre along the vector subspace. The natural conjugation is $\tilde\Xi^{\natural}=\Xi_0-\vec\Xi$, and the star and the Hermitian conjugation are those of *Conventions in Mathematics* §*The Conjugations and the Adjoint*. A root of a central value is written $\tilde\Xi$ (§*The Root Convention*), an idempotent $\tilde\Pi$ (§*The Idempotent Convention*), and a generic element $\tilde P$.

The equations name a product, so the roots and the idempotents are relative to it. The general definition of the power, the square and the root of a central value is *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*Powers, the Square and the Roots*, and the general definition of an idempotent, with the orthogonal, complete and primitive families, the projection and the Peirce decomposition, is the same article. Throughout this article the square is the one of the symmetric quaternionic product; the roots of a value and the idempotents of the other products of the space are read product by product in *Square Roots of Minus One, Zero and Plus One in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* and *Idempotents in the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*.

## The Roots of One

**The roots of $+1$ are exactly the elements with $N(\tilde\Xi)=\Xi_0^2+(\vec\Xi,\vec\Xi)=1$: the level set of the diagonal form at $1$, an affine hyperquadric of complex dimension three and real dimension six, containing the two central roots $\pm e_0$ and the four basis elements $e_0,e_1,e_2,e_3$, and containing no isotropic element.**

A **root of $+1$** is an element $\tilde\Xi\in\mathbb{B}$ with $\tilde\Xi\star\tilde\Xi=e_0$, the square being the one of the symmetric quaternionic product.

### The Reduction

**For every central value $\lambda$ the equation $\tilde\Xi\star\tilde\Xi=\lambda e_0$ reduces to the single scalar equation $N(\tilde\Xi)=\Xi_0^2+(\vec\Xi,\vec\Xi)=\lambda$, so that each root set is a level set of the diagonal form: the natural conjugation and the sign leave each level set in place, while the star and the Hermitian conjugation carry the level set of $\lambda$ onto the level set of $\overline{\lambda}$.**

**Theorem (the reduction).** For every $\lambda\in\mathbb{C}$, the equation $\tilde\Xi\star\tilde\Xi=\lambda e_0$ is equivalent to the single scalar equation

$$
N(\tilde\Xi)=\Xi_0^2+(\vec\Xi,\vec\Xi)=\lambda .
$$

The natural conjugation and the sign leave each level set in place, and the star and the Hermitian conjugation carry the level set of $\lambda$ onto the level set of $\overline{\lambda}$.

*Proof.* The square is $N(\tilde\Xi)e_0$ by the definition of the product, and comparing with $\lambda e_0$ gives the scalar equation, since $N$ depends only on the four coefficients squared and not on their order. The natural conjugation replaces $\vec\Xi$ by $-\vec\Xi$ and leaves the scalar part, so $N(\tilde\Xi^{\natural})=N(\tilde\Xi)$; the star conjugates the four coefficients and negates the vector part, and the Hermitian conjugation conjugates all four, so both give $N(\tilde\Xi^{*})=N(\overline{\tilde\Xi})=\overline{N(\tilde\Xi)}$.

The reduction is total in the block: the vector part enters only through the single scalar $(\vec\Xi,\vec\Xi)$ and never through a vector equation, so the root problem is a problem of a quadratic form and not of a multiplication.

### The Level Set of Plus One

**Theorem (the roots of $+1$).** The roots of $+1$ are the elements with

$$
N(\tilde\Xi)=\Xi_0^2+(\vec\Xi,\vec\Xi)=1 ,
$$

that is the level set of the diagonal form at $1$. The set is an affine hyperquadric of $\mathbb{C}^4$, of complex dimension three and real dimension six; it contains the two central roots $\pm e_0$ and the four basis elements $e_0,e_1,e_2,e_3$, and it contains no isotropic element.

*Proof.* The reduction gives the equation; the level $1$ is non-central and the polynomial $N-1$ is nonsingular, so the set is an affine hyperquadric. The basis elements have $N(e_\mu)=1$ by the table $N(e_\mu,e_\nu)=\delta_{\mu\nu}$, and $\pm e_0$ likewise. An isotropic root would satisfy $N(\tilde\Xi)=0\neq1$.

**Parametrisation.** Over each vector part $\vec\Xi$ the roots are the elements

$$
\tilde\Xi=\Xi_0e_0+\vec\Xi,\qquad \Xi_0^2=1-(\vec\Xi,\vec\Xi),
$$

so the solutions over a fixed $\vec\Xi$ are the two square roots of $1-(\vec\Xi,\vec\Xi)$ when $(\vec\Xi,\vec\Xi)\neq1$, and the single value $\Xi_0=0$ when $(\vec\Xi,\vec\Xi)=1$. The exceptional vector parts exist, for instance $\vec\Xi=e_1$.

### The Trivial Roots

**The only central roots of $+1$ are $\pm e_0$, since a central element is $\lambda e_0$ with $\lambda^2=1$; they are the two roots the halving map uses, and §*The Halving Map and the Failure of the Bijection* shows that they are the only ones that survive the passage to the idempotents.**

**Examples.** $e_0\star e_0=e_0$ and $e_k\star e_k=e_0$, so the four basis elements are roots. $N(e_0+e_1)=1+1=2$, so $e_0+e_1$ is not a root of $+1$. $N(e_0+ie_1)=1-1=0$, so $e_0+ie_1$ is isotropic and is not a root of $+1$ either.

**The Hermitian subspaces.** On the Hermitian subspace $\mathbb{M}_+$, an element $q_0e_0+i(q_1e_1+q_2e_2+q_3e_3)$ with real $q$ has $N=q_0^2-q_1^2-q_2^2-q_3^2$, so the roots of $+1$ there are the elements of the level set of that form, and the roots of $0$ the light cone. The two subspaces are those of *Remarkable Subspaces under the Symmetric Quaternionic Algebra of Biquaternions*.

### The Three Level Sets

**On every complex line through the origin the equation for a central value reads $t^2N(\tilde A)=\lambda$; a line with $N(\tilde A)=0$ lies in the level $0$ and meets no nonzero level, a line with $N(\tilde A)\neq0$ meets a nonzero level in the two points $t=\pm\sqrt{\lambda/N(\tilde A)}$, and the scaling $\tilde\Xi\mapsto\mu\tilde\Xi$ carries the level $\lambda$ onto the level $\mu^2\lambda$, so the levels are pairwise disjoint and the non-central ones form one orbit of the scalings.**

**Proposition (the levels in one display).** On a complex line $\mathbb{C}\tilde A$ through the origin the equation $N(t\tilde A)=\lambda$ reads $t^2N(\tilde A)=\lambda$, since $N(t\tilde A)=t^2N(\tilde A)$:

- if $N(\tilde A)=0$ the line lies in the level $0$ and meets no level $\lambda\neq0$;
- if $N(\tilde A)\neq0$ and $\lambda\neq0$ the line meets the level $\lambda$ in the two points $t=\pm\sqrt{\lambda/N(\tilde A)}$;
- if $N(\tilde A)\neq0$ and $\lambda=0$ the line meets the level $0$ only at the origin.

The scaling $\tilde\Xi\mapsto\mu\tilde\Xi$ therefore carries the level $\lambda$ onto the level $\mu^2\lambda$, the two nonzero levels are pairwise disjoint, and each nonzero level is carried onto the level $1$ by some scaling.

*Proof.* The display is the homogeneity of the diagonal; the two solutions of $t^2=\lambda/N(\tilde A)$ are distinct unless $\lambda=0$; the disjointness is that a scalar has one of the two values and not both.

**Remark (the shape of the levels).** The level $1$ is an affine hyperquadric of complex dimension three, and the level $0$ is the isotropic cone of the form, a quadric cone with vertex $0$ of the same dimension. The level $0$ is the one invariant under every scaling, and it is *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Algebra*. The levels of real value are pairwise disjoint and each is invariant under the three conjugations, because a real value is fixed by the conjugation.

### Verification

The reduction and the tables were recomputed on a pure-Python model of $\mathbb{B}$ as complex quadruples with $N(\tilde Q)=\sum_\mu Q_\mu^2$, on the four basis elements, on $10^3$ random elements, and on the constructed roots $e_0,e_1,e_2,e_3$, $\pm e_0$, the elements $\pm\mu e_0$ with $\mu^2=1$, and $ie_1$. The identity $\tilde\Xi\star\tilde\Xi=N(\tilde\Xi)e_0$ held at every one of them, the level $1$ was met by $e_0,e_1,e_2,e_3$ and by no element of the cone, and $(i\tilde\Xi)\star(i\tilde\Xi)=-e_0$ held at every root tested.

### Status of the Roots

**The roots of $+1$ are units of the parent algebra and are not units of the block: $N(\tilde\Xi)=1\neq0$ makes $\tilde\Xi^{\natural}/N(\tilde\Xi)=\tilde\Xi^{\natural}$ the inverse of $\tilde\Xi$ in the parent, while the block has no unit and no group of units.**

The natural conjugation carries the level $1$ onto itself, and the star and the Hermitian conjugation carry it onto itself too, because the value $1$ is real; so the whole root set of $+1$ is stable under the three conjugations. The root set of $+1$ is the level set of the diagonal read in *Norm and Invertibility in the Symmetric Quaternionic Algebra* as the analogue of the group of the elements of algebraic norm one of an associative unital product; it is not a group here, because the block has no unit to be the identity of it.

**The roots of minus one.** The central imaginary turns the roots of $+1$ into the roots of $-1$: if $\tilde\Xi\star\tilde\Xi=e_0$ then $(i\tilde\Xi)\star(i\tilde\Xi)=-e_0$, because $i$ is central and the product is two-sidedly linear, and since $i$ is invertible the map $\tilde\Xi\mapsto i\tilde\Xi$ is a bijection from the level set $N=1$ onto the level set $N=-1$, whose two central elements are $\pm ie_0$. The mechanism needs the centrality of the scalar and the two-sided linearity of the product, and it is not universal.**

For this product the mechanism applies. The product is $\mathbb{C}$-bilinear with the central scalar $i$, so the map $\tilde\Xi\mapsto i\tilde\Xi$ is invertible and

$$
(i\tilde\Xi)\star(i\tilde\Xi)=i^2\,(\tilde\Xi\star\tilde\Xi)=-e_0
$$

for every root $\tilde\Xi$ of $+1$; the inverse sends a root of $-1$ to $-i$ times it. The roots of $-1$ are therefore nonempty, and they are the level set $N=-1$,

$$
\{\tilde\Xi:N(\tilde\Xi)=-1\}=\Bigl\{\Xi_0e_0+\vec\Xi:\Xi_0^2=-1-(\vec\Xi,\vec\Xi)\Bigr\},
$$

an affine hyperquadric of complex dimension three, containing the two central roots $\pm ie_0$ and no isotropic element, and invariant under the three conjugations because the value $-1$ is real.

The mechanism is not universal. It needs a central scalar of square $-1$ that can be moved past the two slots of the product; in a sesquilinear product, where the second slot conjugates, the scalar multiplication cannot flip the sign this way, and the roots of $-1$ are then read from the roots of $+1$ by no such map, or are absent altogether.

## The Idempotents

**The idempotents of the block are exactly $0$ and $e_0$; the equation $\tilde\Pi\star\tilde\Pi=N(\tilde\Pi)e_0=\tilde\Pi$ forces the vector part to vanish and the scalar part to satisfy $\Pi_0^2=\Pi_0$.**

### The Definition

**Definition (idempotent of a product).** Let $\star$ be a product on $\mathbb{B}$. An element $\tilde\Pi$ is an **idempotent of $\star$** when

$$
\tilde\Pi\star\tilde\Pi=\tilde\Pi ,
$$

and it is **nontrivial** when it is neither the element $0$ nor the two-sided unit, when a unit exists. Idempotents of an associative product are **orthogonal** when $\tilde\Pi\star\tilde\Pi'=\tilde\Pi'\star\tilde\Pi=0$, **complete** when in addition their sum is the unit, and **primitive** when not a sum of two nonzero orthogonal idempotents.

Throughout this article an idempotent, written without qualification, is an idempotent of the **symmetric quaternionic product**, and the square is read in that product.

### The Classification of the Idempotents

**Theorem (the two idempotents).** The idempotents of the block are exactly $0$ and $e_0$.

*Proof.* The equation is $\tilde\Pi\star\tilde\Pi=N(\tilde\Pi)e_0=\tilde\Pi$, and its right side must be central, so $\tilde\Pi=\Pi_0e_0$ has vanishing vector part. The equation then reads $\Pi_0^2=\Pi_0$, whose solutions are $\Pi_0=0$ and $\Pi_0=1$; both are realized, since $0\star0=0$ and $e_0\star e_0=e_0$.

**Corollary (the pair).** The two idempotents are orthogonal, $0\star e_0=e_0\star0=0$, and their sum is $e_0$, which acts as the identity on the image $\mathbb{C}e_0$ of the block without being a unit of the algebra, since the block has none (*Norm and Invertibility in the Symmetric Quaternionic Algebra*). Neither is primitive in the sense of the corner algebra, because no associative structure and no Peirce decomposition exists in the block, and the words *trivial* and *nontrivial* are used only in the ambient sense.

**Comparison with the parent.** In the parent plain algebra the idempotents are the halving images $\tilde\Pi=\tfrac12(e_0+\tilde\Xi)$ of its roots $\tilde\Xi$ of $+1$, a set of real dimension four (*Square Roots of One and the Idempotents of the General Plain Algebra*). In the block the whole continuum disappears and exactly the two trivial idempotents survive; the block shares them with every other product of the twelve, since $0$ and $e_0$ are idempotents of each of the twelve operations whose square at $e_0$ is $e_0$.

### The Halving Map and the Failure of the Bijection

**The halving map $\tilde P\mapsto\tilde\Pi=\tfrac12(e_0+\tilde P)$ carries the two central roots of $+1$, $\tilde P=\pm e_0$, onto the two idempotents $e_0$ and $0$, and carries no other root of $+1$ to an idempotent; so the bijection of the parent is not merely unproved in the block but false in it, the root sets being of complex dimension three and the idempotent set being two points.**

**Theorem (the bijection fails).** There is no bijection between the roots of $+1$ of the block and its idempotents. What survives is the following: the halving map

$$
\tilde P\ \longmapsto\ \tilde\Pi=\tfrac12(e_0+\tilde P)
$$

carries the **central** roots of $+1$, that is $\tilde P=\pm e_0$, onto the two idempotents $e_0$ and $0$, and carries no other root of $+1$ to an idempotent.

*Proof.* $\tilde\Pi\star\tilde\Pi=\tfrac14\bigl(1+2P_0+N(\tilde P)\bigr)e_0$ by the definition of the product, while $\tilde\Pi=\tfrac12e_0+\tfrac12\tilde P$. The two are equal only if $\tilde P$ is central, and then the equality reads $\tfrac14(1+2P_0+P_0^2)=\tfrac12(1+P_0)$, that is $P_0^2=1$. For a central root of $+1$ the value $P_0=1$ gives $\tilde\Pi=e_0$ and $P_0=-1$ gives $\tilde\Pi=0$; for any other root of $+1$, of which the level set is full, the vector part of $\tilde\Pi$ is nonzero and cannot be cancelled.

**Remark (the reason, in one sentence).** In the parent the vector part of a halved element is cancelled by the equation $\tilde\Xi\star\tilde\Xi=e_0$ through the associativity and the unit; in the block the product is central valued, the square $\tilde\Pi\star\tilde\Pi$ can only be a scalar multiple of $e_0$, and the vector part of $\tilde\Pi$ can never be cancelled. The root sets are three-dimensional and the idempotent set is two points, and no map can match them.

### Idempotents as Projections

**The multiplication by $e_0$ is the projection $L_{e_0}:\tilde Y\mapsto Y_0e_0=E(\tilde Y)$ onto the centre along the vector subspace, and it is not the identity; the multiplication by $0$ is the zero operator; and the block has no Peirce decomposition, the available splitting $\mathbb{B}=\mathbb{C}e_0\oplus\mathrm{Vect}(\mathbb{B})$ being the image–kernel splitting of $E$.**

**Theorem (the operator of $e_0$ is the projection onto the centre).** The left multiplication by the idempotent $e_0$,

$$
L_{e_0}:\tilde Y\longmapsto e_0\star\tilde Y=Y_0e_0=E(\tilde Y),
$$

is the projection of $\mathbb{B}$ onto its centre along its vector subspace; the multiplication by $0$ is the zero operator; and $L_{e_0}$ is not the identity, since it fixes the centre and annihilates the vector subspace — the block having no unit.

*Proof.* $e_0\star\tilde Y=N(e_0,\tilde Y)e_0=Y_0e_0$ by the definition of the product; the operator thus has image the centre and kernel the vector subspace, and it is idempotent, $L_{e_0}^2=L_{e_0}$. The operator theory of the block, including its other idempotent endomorphisms, is *The Specificities of the Symmetric Quaternionic Algebra*.

**Corollary (the absent Peirce decomposition).** The block has **no Peirce decomposition**: the construction presupposes that the product is associative with a unit, and the block is neither (*Introduction to the Symmetric Quaternionic Algebra of Biquaternions*). The decomposition that is available is the elementary splitting of the operator $L_{e_0}$,

$$
\mathbb{B}=\mathbb{C}e_0\oplus\mathrm{Vect}(\mathbb{B})=\operatorname{im}L_{e_0}\oplus\ker L_{e_0},
$$

which is a direct sum decomposition of the space under the projection $E$ and not a Peirce decomposition: the two summands are not corner algebras, and the vector subspace is not stable under the product, since $e_1\star e_1=e_0$ leaves it.

**Remark (the two idempotents as projections).** With the ambient involution the two idempotents are self-adjoint, $e_0^{*}=e_0$ and $0^{*}=0$, so both are projections of the ambient $*$-algebra, and the splitting above is the orthogonal direct sum for the form $N$, the centre and the vector subspace being mutually orthogonal. No other element of the block is an idempotent, so the block carries no other projection, Hermitian or not.

### Idempotents and the Zero Divisors

**The block has no classification of its zero divisors by idempotents: it has no nontrivial idempotent, and its zero-divisor set is the whole punctured space, so no subfamily of idempotents can index it; the idempotent endomorphisms are a larger family than the idempotent elements, and the two are told apart in the Specificities entry.**

**Theorem (no classification of the zero divisors by the idempotents).** In the parent every non-pure zero divisor is the complex multiple $2Q_0\tilde\Pi$ of a nontrivial idempotent $\tilde\Pi$, which is the way the parent classifies its zero divisors (*Zero Divisors of the General Plain Algebra*). In the block the statement has no analogue: the block has no nontrivial idempotent, and its zero-divisor set is the whole punctured space (*Zero Divisors of the Symmetric Quaternionic Algebra*), so no subfamily of idempotents can index it.

*Proof.* The parent's statement presupposes its continuum of idempotents; the block's idempotents are the two of the classification theorem, so the only multiples available are the central elements $\lambda e_0$, a one-dimensional family inside the zero-divisor set of the block, which is of real dimension eight.

**Remark (the idempotent endomorphisms).** The idempotent **endomorphisms** of the block are a strictly larger family than its idempotent **elements**: by the identity $L_{\tilde X}^2=X_0L_{\tilde X}$ of *The Specificities of the Symmetric Quaternionic Algebra* the idempotent multiplications are the $L_{\tilde X}$ with $X_0=1$, a hyperplane of pairwise distinct rank-one projections onto the central line, together with the zero operator, while the idempotent elements are $0$ and $e_0$ alone. The idempotent endomorphisms of the block and the idempotents of the product are therefore two different sets.

## Summary

The roots of $+1$ of the symmetric quaternionic product are the level set $N=1$ of the form $N(\tilde\Xi)=\Xi_0^2+(\vec\Xi,\vec\Xi)$: an affine hyperquadric of complex dimension three containing the two central roots $\pm e_0$ and the four basis elements $e_0,e_1,e_2,e_3$. The roots of $-1$ are read from them by multiplication by the central imaginary, $\tilde\Xi\mapsto i\tilde\Xi$, because the product is two-sidedly linear and $i$ is central: the map is a bijection onto the level set $N=-1$, which is nonempty and contains the two central roots $\pm ie_0$; in a sesquilinear product the mechanism fails, and the roots of $-1$ are then not read this way. The roots of $0$ are the punctured isotropic cone and are *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Algebra*.

The idempotents of the block are exactly $0$ and $e_0$: the equation $\tilde\Pi\star\tilde\Pi=N(\tilde\Pi)e_0=\tilde\Pi$ forces the vector part to vanish, and the scalar part satisfies $\Pi_0^2=\Pi_0$. The continuum of idempotents of the parent plain algebra, the halving image of its roots of $+1$, dissolves in the block: the halving map $\tilde\Pi=\tfrac12(e_0+\tilde P)$ carries only the two central roots of $+1$ to idempotents, because the centrality of the product prevents the vector part of $\tilde\Pi$ from being cancelled. The idempotent $e_0$ acts by the projection $E$ onto the centre along the vector subspace, which is not the identity — the block having no unit — and the block has no Peirce decomposition, the available splitting $\mathbb{B}=\mathbb{C}e_0\oplus\mathrm{Vect}(\mathbb{B})$ being the image–kernel splitting of $E$ and not a decomposition into corner algebras. The parent's classification of the zero divisors by nontrivial idempotents has no analogue, since the block has neither the idempotents nor a proper zero-divisor set; the idempotent endomorphisms of the block are a different, larger family, treated in the Specificities entry.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde P\star\tilde Q=N(\tilde P,\tilde Q)e_0$ | the symmetric quaternionic multiplication |
| $N(\tilde Q)=\sum_\mu Q_\mu^2=\Xi_0^2+(\vec\Xi,\vec\Xi)$ | the form at the two equal arguments |
| $N=1$ | the roots of $+1$ |
| $\pm e_0$ | the central roots of $+1$ |
| $e_0,e_1,e_2,e_3$ | the four roots of $+1$ of the basis |
| $\tilde\Pi=\tfrac12(e_0+\tilde\Xi)$ | the halving map, defined but not bijective in the block |
| $0$, $e_0$ | the two idempotents of the block |
| $E(\tilde Y)=Y_0e_0$ | the projection onto the centre, the operator of $e_0$ |
| $\mathbb{B}=\mathbb{C}e_0\oplus\mathrm{Vect}(\mathbb{B})$ | the image–kernel splitting of $E$, not a Peirce decomposition |

## Further Reading

- *Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/definitions-for-the-study-of-the-algebraic-structures-over-the-biquaternioid-c-space.md`), for the general definitions of a root of a central value, of an idempotent, of a projection and of the Peirce decomposition.
- *Square Roots of One and the Idempotents of the General Plain Algebra* (`articles_maths/square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.md`), for the parent's classification, where the roots of $+1$ and the idempotents are in bijection.
- *Square Roots of Zero and the Nilpotents of the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-symmetric-quaternionic-algebra.md`), for the roots of $0$ and the nilpotents of the block.
- *Square Roots of a General Element in the Symmetric Quaternionic Algebra* (`articles_maths/square-roots-of-a-general-element-in-the-symmetric-quaternionic-algebra.md`), for the radicands that are not central.
- *Norm and Invertibility in the Symmetric Quaternionic Algebra* (`articles_maths/norm-and-invertibility-in-the-symmetric-quaternionic-algebra.md`), for the diagonal, the non-isotropic class and the group of units of the parent.
- *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra* (`articles_maths/the-radical-and-the-isotropic-elements-of-the-symmetric-quaternionic-algebra.md`), for the cone and its two families.
- *Zero Divisors of the Symmetric Quaternionic Algebra* (`articles_maths/zero-divisors-of-the-symmetric-quaternionic-algebra.md`), for the maximal zero-divisor set of the block.
- *The Specificities of the Symmetric Quaternionic Algebra* (`articles_maths/the-specificities-of-the-symmetric-quaternionic-algebra.md`), for the idempotent endomorphisms and the operator theory.
