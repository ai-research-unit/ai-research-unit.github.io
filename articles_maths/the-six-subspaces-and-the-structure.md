# __The Six Subspaces and the Structure__

## Introduction

An element of the biquaternion algebra is an **idempotent** if $\tilde\Pi^2 = \tilde\Pi$, and a **left ideal** of $\mathbb{B}$ is a $\mathbb{C}$-subspace $I$ with $\mathbb{B}I \subseteq I$, where the product of a subspace with a subspace is the span of the products; a **right ideal** is a subspace $J$ with $J\mathbb{B} \subseteq J$, and a **two-sided ideal** is both. The two notions are two faces of one object: an idempotent splits the algebra as

$$
\mathbb{B} = \mathbb{B}\tilde\Pi \oplus \mathbb{B}(e_0 - \tilde\Pi) ,
$$

its complement $e_0 - \tilde\Pi$ is the complementary projection, and when the idempotent is primitive the two summands are minimal one-sided ideals. This article records what the classification of the idempotents and the classification of the ideals see of the six distinguished subspaces of *Introduction to the Six Subspaces*. The classifications themselves are the business of *Biquaternion Idempotents and Projections* and *Biquaternion Ideals and Peirce Decomposition*; what is added here is their restriction to the six.

**The idempotents.** Every idempotent of $\mathbb{B}$ is $0$, or $e_0$, or of the form

$$
\tilde\Pi = \tfrac{1}{2}\left(e_0 + \xi i\right) , \qquad \xi^2 = -1 ,
$$

with $\xi$ a root of minus one; there are no others. Writing the idempotent as $\tilde\Pi = \Pi_0e_0 + \mathbf{q}$, with $\Pi_0$ the scalar part and $\mathbf{q}$ the vector part, and using $\mathbf{q}^2 = -(\mathbf{q},\mathbf{q})e_0$, the equation $\tilde\Pi^2 = \tilde\Pi$ is the pair

$$
\Pi_0^2 - (\mathbf{q},\mathbf{q}) = \Pi_0 , \qquad 2\Pi_0\mathbf{q} = \mathbf{q} ,
$$

and the solutions in the six subspaces are the following. Of the six, only three contain a nonzero idempotent, and the nontrivial ones all lie in one of them.

| subspace | its idempotents |
|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $0$ and $e_0$ |
| $\mathrm{Vect}(\mathbb{B})$ | $0$ only |
| $\mathbb{H}_{\mathbb{B}}$ | $0$ and $e_0$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $0$ only |
| $\mathbb{M}_+$ | $0$, $e_0$, and $\tfrac{1}{2}(e_0 + i\mathbf{u})$ for real unit vectors $\mathbf{u}$ |
| $\mathbb{M}_-$ | $0$ only |

**Theorem (the idempotents of the six).** The idempotents of $\mathbb{C}_{\mathbb{B}}$ are $0$ and $e_0$; those of $\mathbb{H}_{\mathbb{B}}$ are $0$ and $e_0$; those of $\mathbb{M}_+$ are $0$, $e_0$ and the two-sphere of elements $\tfrac{1}{2}(e_0 + i\mathbf{u})$ with $\mathbf{u}$ a real vector of $(\mathbf{u},\mathbf{u}) = 1$; and $0$ is the only idempotent of $\mathrm{Vect}(\mathbb{B})$, of $i\mathbb{H}_{\mathbb{B}}$ and of $\mathbb{M}_-$.

**Proof.** Read the two equations of the display above on each subspace, whose elements are enumerated in *Introduction to the Six Subspaces*. The second equation, $2\Pi_0\mathbf{q} = \mathbf{q}$, is the one that does the work: it forces $\mathbf{q} = 0$ unless the scalar part is exactly $\tfrac{1}{2}$, and the scalar part is real only on the centre and in the Hermitian subspace. *Centre:* $\mathbf{q} = 0$ and $\Pi_0^2 = \Pi_0$, so $\Pi_0 \in \{0,1\}$. *Vector:* $\Pi_0 = 0$, and $2\Pi_0\mathbf{q} = \mathbf{q}$ gives $\mathbf{q} = 0$ directly, whatever the first equation would allow. *Quaternion:* $\Pi_0 = h_0$ real and $\mathbf{q}$ a real vector; $2h_0\mathbf{q} = \mathbf{q}$ gives $\mathbf{q} = 0$ or $h_0 = \tfrac{1}{2}$, and $h_0 = \tfrac{1}{2}$ in the first equation gives $(\mathbf{q},\mathbf{q}) = -\tfrac{1}{4}$, impossible for a real vector, so $\mathbf{q} = 0$ and $h_0 \in \{0,1\}$. *Anti-quaternion:* $\Pi_0$ is purely imaginary and $\mathbf{q}$ is real; $2\Pi_0\mathbf{q} = \mathbf{q}$ forces $\mathbf{q} = 0$ since $2\Pi_0 \neq 1$, and the first equation then gives $\Pi_0^2 = \Pi_0$ with $\Pi_0$ purely imaginary, so $\Pi_0 = 0$. *Hermitian:* $\Pi_0 = a_0$ real and $\mathbf{q} = i\mathbf{p}$ with $\mathbf{p}$ real, so $(\mathbf{q},\mathbf{q}) = -(\mathbf{p},\mathbf{p})$; the second equation gives $\mathbf{p} = 0$ or $a_0 = \tfrac{1}{2}$, and with $\mathbf{p} = 0$ the first gives $a_0 \in \{0,1\}$ while with $a_0 = \tfrac{1}{2}$ it gives $(\mathbf{p},\mathbf{p}) = \tfrac{1}{4}$. *Anti-Hermitian:* $\Pi_0$ is purely imaginary and $\mathbf{q}$ is real; the second equation forces $\mathbf{q} = 0$, and the first gives $\Pi_0 = 0$. $\square$

**Corollary.** The nontrivial idempotents present in the six are exactly the **Hermitian idempotents** $\tfrac{1}{2}(e_0 + i\mathbf{u})$, and they all lie in the Hermitian subspace. Each is a zero divisor, since its norm is $\tfrac{1}{4}(1 - (\mathbf{u},\mathbf{u})) = 0$; so is its complement $\tfrac{1}{2}(e_0 - i\mathbf{u})$, and the two are orthogonal and sum to $e_0$,

$$
\tfrac{1}{2}(e_0 + i\mathbf{u}) \cdot \tfrac{1}{2}(e_0 - i\mathbf{u}) = 0 , \qquad \tfrac{1}{2}(e_0 + i\mathbf{u}) + \tfrac{1}{2}(e_0 - i\mathbf{u}) = e_0 .
$$

Every idempotent of the algebra not of this form — every idempotent built on a non-Hermitian root of minus one — lies in none of the six, its vector part mixing a real and an imaginary direction. The six therefore see exactly one nontrivial family of idempotents, and they see it in exactly one subspace.

**Corollary (the orthogonal partner).** Let $\tilde\Pi = \tfrac{1}{2}(e_0 + i\mathbf{u})$ be a Hermitian idempotent of the Hermitian subspace, with $\mathbf{u}$ a real unit vector. The only idempotents of the algebra orthogonal to $\tilde\Pi$ are $0$ and its complement $e_0 - \tilde\Pi$.

**Proof.** If $\tilde\Pi\tilde{X} = \tilde{X}\tilde\Pi = 0$, then

$$
(e_0-\tilde\Pi)\tilde{X}(e_0-\tilde\Pi) = \tilde{X} - \tilde\Pi\tilde{X} - \tilde{X}\tilde\Pi + \tilde\Pi\tilde{X}\tilde\Pi = \tilde{X} ,
$$

so every element orthogonal to $\tilde\Pi$ lies in the **corner** $(e_0-\tilde\Pi)\mathbb{B}(e_0-\tilde\Pi)$. Put $\mathbf{A} = 2(e_0-\tilde\Pi) = e_0 - i\mathbf{u}$; then $\mathbf{A}^2 = 2\mathbf{A}$, since $(i\mathbf{u})^2 = -i^2(\mathbf{u},\mathbf{u})e_0 = (\mathbf{u},\mathbf{u})e_0 = e_0$. The corner is a complex subspace because $i$ is central, and it contains $\mathbf{A}/2$, so it contains the complex line $\mathbb{C}\mathbf{A}$; its real dimension is $2$ — for $\mathbf{u} = e_1$ it is spanned by $e_0-ie_1$ and $ie_0+e_1$, and in general by the primitivity of $\tilde\Pi$, in *Biquaternion Ideals and Peirce Decomposition* — so it *is* that line. An idempotent in it is $z\mathbf{A}$ with $(z\mathbf{A})^2 = z\mathbf{A}$, that is $z(2z-1)\mathbf{A} = 0$, giving $z = 0$ or $z = \tfrac{1}{2}$; the idempotents orthogonal to $\tilde\Pi$ are therefore $0$ and $\tfrac{1}{2}\mathbf{A} = e_0-\tilde\Pi$. $\square$

**The ideals.** $\mathbb{B}$ is **simple**, its only two-sided ideals being $0$ and $\mathbb{B}$, and it has **length two** as a left module over itself, so that every nonzero proper left ideal is **minimal**, of real dimension $4$, and dually every nonzero proper right ideal is a minimal right ideal of real dimension $4$. Two consequences are immediate and both are flat. Since the only two-sided ideals are $0$ and $\mathbb{B}$, **no subspace of the six is a two-sided ideal**: no proper nonzero subspace of a simple algebra can be one. And each of the six **generates the whole algebra on both sides**,

$$
\mathbb{B}\mathbb{S} = \mathbb{S}\mathbb{B} = \mathbb{B} \qquad \text{for each of the six subspaces } \mathbb{S} ,
$$

because a left ideal containing a unit is everything — if $\tilde U \in I$ is invertible then $\tilde U^{-1}\tilde U = e_0 \in I$ — and each of the six contains a unit: $e_0$ is in the centre, in the quaternion subspace and in $\mathbb{M}_+$, the element $e_1$ is in the vector subspace and in $\mathbb{M}_-$, and $ie_0$ is in the anti-quaternion subspace. So the six are not ideals, and each is as far from being one as a subspace can be.

The interest is in between: the **minimal** one-sided ideals, which are exactly the ones the six do determine, through their zero divisors. Two statements carry the article.

**Theorem (the annihilators of the zero divisors).** Let $\tilde Q \neq 0$ be a zero divisor of $\mathbb{B}$, so that $N(\tilde Q) = 0$. Write $I_{\tilde Q}$ for the set of $\tilde X$ with $\tilde X\tilde Q = 0$ and $J_{\tilde Q}$ for the set of $\tilde X$ with $\tilde Q\tilde X = 0$. Then $I_{\tilde Q}$ is a minimal left ideal, $J_{\tilde Q}$ is a minimal right ideal, and each has real dimension $4$.

**Theorem (the ideal generated against the annihilator).** For a nonzero **nilpotent** of the vector subspace, $\mathbf{P}^2 = 0$, the ideal generated and the annihilator coincide,

$$
\mathbb{B}\mathbf{P} = I_{\mathbf{P}} , \qquad \mathbf{P}\mathbb{B} = J_{\mathbf{P}} ;
$$

for every other zero divisor $\tilde Q$ the two are distinct and therefore complementary,

$$
\mathbb{B} = \mathbb{B}\tilde Q \oplus I_{\tilde Q} = \tilde Q\mathbb{B} \oplus J_{\tilde Q} .
$$

The subspaces of the six that carry a zero divisor are the vector subspace, $\mathbb{M}_+$ and $\mathbb{M}_-$, by *The Six Subspaces and the Elements*; the other three, the centre, the quaternion subspace and the anti-quaternion subspace, consist of $0$ and units, and determine no minimal ideal at all. So the ideal content of the six is carried by three of them:

| subspace | left ideal generated | right ideal generated | units in it | minimal one-sided ideals determined |
|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\mathbb{B}$ | $\mathbb{B}$ | all $Ae_0$ with $A \neq 0$ | none |
| $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{B}$ | $\mathbb{B}$ | $e_1$ | $\mathbb{B}\mathbf{P} = I_{\mathbf{P}}$ and $\mathbf{P}\mathbb{B} = J_{\mathbf{P}}$, $\mathbf{P}$ a nonzero nilpotent |
| $\mathbb{H}_{\mathbb{B}}$ | $\mathbb{B}$ | $\mathbb{B}$ | $e_0$ | none |
| $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{B}$ | $\mathbb{B}$ | $ie_0$ | none |
| $\mathbb{M}_+$ | $\mathbb{B}$ | $\mathbb{B}$ | $e_0$ | $\mathbb{B}\tilde\Pi$, $I_{\tilde\Pi} = \mathbb{B}(e_0-\tilde\Pi)$ and their right-hand twins, $\tilde\Pi$ a Hermitian idempotent |
| $\mathbb{M}_-$ | $\mathbb{B}$ | $\mathbb{B}$ | $e_1$ | the same four, unchanged |

## The Centre Subspace

A central element is $Ae_0$, and $A^2 = A$ forces $A \in \{0,1\}$:

$$
0 , \qquad e_0 .
$$

The centre is a field, so it carries no nontrivial idempotent, and the only idempotent of it that is not the unit is the zero element. It is one of the three subspaces of the theorem, and the only one of them that is commutative: the trivial pair $0$ and $e_0$ is all the centre has, and it is the same trivial pair that the quaternion subspace has for a different reason.

On the ideal side a central element is invertible exactly when $A \neq 0$, so the centre is a field, contains no zero divisor, determines no minimal ideal, and the left ideal it generates is $\mathbb{B}$, by $e_0 \in \mathbb{C}_{\mathbb{B}}$.

The centre is worth one remark on the Peirce side. A **central** idempotent $e$ gives the Peirce decomposition $\mathbb{B} = \mathbb{B}e \oplus \mathbb{B}(e_0-e)$, and this is more than a direct sum: the two summands are two-sided ideals and the decomposition is a product of algebras, $\mathbb{B} = \mathbb{B}e \times \mathbb{B}(e_0-e)$, as *Biquaternion Ideals and Peirce Decomposition* records. For the biquaternion algebra that is impossible unless one factor is zero, because $\mathbb{B}$ is simple; and indeed the only central idempotents are $0$ and $e_0$, the two cases in which one factor is $\mathbb{B}$ and the other is $0$. **The Peirce decomposition relative to a central idempotent is trivial for $\mathbb{B}$**, and this is the same fact as simplicity, read through the centre.

## The Vector Subspace

The vector subspace has one idempotent, $0$. A pure vector with $\mathbf{P}^2 = \mathbf{P}$ would have $\mathbf{P}^2 = -(\mathbf{P},\mathbf{P})e_0$ central and equal to the pure vector $\mathbf{P}$, so $\mathbf{P} \in \mathbb{C}_{\mathbb{B}} \cap \mathrm{Vect}(\mathbb{B}) = 0$. In the language of the two equations of the Introduction it is the second, $2\Pi_0\mathbf{q} = \mathbf{q}$, that rules the case out, since the first, $(\mathbf{P},\mathbf{P}) = 0$, has nonzero solutions — the square-zero elements of *The Six Subspaces and the Elements*. The vector subspace therefore has square-zero elements and no idempotent; an element of the algebra that is a projection never has a pure vector part without a scalar part.

The vector subspace is also the one of the six in which the two opposite kinds of element meet. Its roots of $-1$ are the pure roots, by *The Six Subspaces and the Elements*, and those are units; its nilpotents are the nonzero solutions of $(\mathbf{P},\mathbf{P}) = 0$, and those are zero divisors. The units generate $\mathbb{B}$, as above; the nilpotents generate minimal ideals, and for them the ideal and the annihilator are the same set.

**Proof of the nilpotent case of the second theorem.** If $\mathbf{P}^2 = 0$ then $(\tilde X\mathbf{P})\mathbf{P} = \tilde X\mathbf{P}^2 = 0$ for every $\tilde X$, so $\mathbb{B}\mathbf{P} \subseteq I_{\mathbf{P}}$, and $\mathbb{B}\mathbf{P}$ contains $\mathbf{P} \neq 0$ while $I_{\mathbf{P}}$ is proper, so both are nonzero proper left ideals; by the length-two statement they are both minimal of real dimension $4$, hence equal. The right-hand statement is the mirror image, using $(\mathbf{P}\tilde X)\mathbf{P} = 0$ on the left instead. $\square$

An explicit case is $\mathbf{P} = e_1 + ie_2$, with $\mathbf{P}^2 = 0$ and

$$
\mathbb{B}\mathbf{P} = I_{\mathbf{P}} = \operatorname{span}_{\mathbb{R}}\left\{e_1 + ie_2,\; e_2 - ie_1,\; e_0 - ie_3,\; e_3 + ie_0\right\},
$$

where the first two elements are further nilpotents of the vector subspace and the last two are a Hermitian element and $i$ times it — $e_0 - ie_3 = 2\cdot\tfrac{1}{2}(e_0 - ie_3)$ and $e_3 + ie_0 = i(e_0 - ie_3) = 2i\cdot\tfrac{1}{2}(e_0 - ie_3)$. So this minimal ideal is the sum of a complex line of the vector subspace, a real line of $\mathbb{M}_+$ and a real line of $\mathbb{M}_-$; it contains no basis element of the algebra, so it is not a sum of coordinate blocks, and it is not one of the six.

## The Quaternion Subspace

The quaternion subspace has the two trivial idempotents and no others:

$$
0 , \qquad e_0 .
$$

For $h \in \mathbb{H}_{\mathbb{B}}$, the equation $h^2 = h$ reads $h(h - e_0) = 0$, and the quaternion subspace is a division algebra, so $h = 0$ or $h = e_0$. This is the argument that the anti-quaternion subspace cannot use — it is not a division algebra, nor even closed under the product — and it is the reason the two quaternion subspaces reach the same trivial answer by different routes.

On the ideal side the quaternion subspace is the sharpest of the three negative cases: not merely the subspace as a whole, but **every single nonzero element** of $\mathbb{H}_{\mathbb{B}}$ is a unit, so every one of them generates the whole algebra on both sides, and the ideal theory sees nothing of the subspace beyond the identity element it shares with the centre and $\mathbb{M}_+$.

The quaternion subspace is closed under the product, one of the two among the six that are (the centre being the other), but it is not an ideal: $ie_1 \in \mathbb{B}$ and $\mathbb{H}_{\mathbb{B}} \ni e_1$ give $ie_1e_1 = -i \notin \mathbb{H}_{\mathbb{B}}$, so left multiplication by an element of $\mathbb{B}$ already leaves it.

## The Anti-Quaternion Subspace

The anti-quaternion subspace has one idempotent, $0$. An element of it is $ih$ with $h$ real, and $(ih)^2 = -h^2$ is a real quaternion; an idempotent there would satisfy $\tilde\Pi = \tilde\Pi^2 \in \mathbb{H}_{\mathbb{B}}$ and therefore lie in $i\mathbb{H}_{\mathbb{B}} \cap \mathbb{H}_{\mathbb{B}} = 0$. The subspace consists of units and zero, by *The Six Subspaces and the Elements*, and its idempotents are correspondingly the fewest possible: it contributes nothing to the projection theory of the algebra, and its interest for the idempotents is exactly that the products it produces land in, and only in, the two quaternion and Hermitian subspaces.

For the ideals the subspace is $i\mathbb{H}_{\mathbb{B}}$, and multiplication by the central unit $i$ carries $\mathbb{H}_{\mathbb{B}}$ bijectively to it and preserves products and linear combinations. So everything said of the quaternion subspace holds of it verbatim: every nonzero element is a unit, no zero divisor lies in it, and every nonzero element generates $\mathbb{B}$ on both sides. It is not an ideal: $e_1 \in \mathbb{B}$ and $ie_1 \in i\mathbb{H}_{\mathbb{B}}$ give $e_1 \cdot ie_1 = -i \notin i\mathbb{H}_{\mathbb{B}}$.

## The Hermitian Subspace

The Hermitian subspace is the one subspace of the six that carries a nontrivial family of idempotents. Besides $0$ and $e_0$,

$$
\tilde\Pi = \tfrac{1}{2}\left(e_0 + i\mathbf{u}\right) , \qquad \mathbf{u} \in \mathbb{R}^3 , \quad (\mathbf{u},\mathbf{u}) = 1 .
$$

The parameter $\mathbf{u}$ runs over a two-sphere, so the nontrivial idempotents of the Hermitian subspace form a two-parameter family; each is a Hermitian idempotent of the algebra and a projection, and the family is the one that occurs in the spectral theorem, treated in *Biquaternion Spectral Theory*. Three properties hold for every member, and they are the ones the projection theory uses.

**First, the norm vanishes, so every nontrivial idempotent of the Hermitian subspace is a zero divisor.** The norm of $\tfrac{1}{2}(e_0 + i\mathbf{u})$ is $\tfrac{1}{4}(1 - (\mathbf{u},\mathbf{u})) = 0$, and by *The Six Subspaces and the Elements* the nontrivial idempotents are exactly the zero divisors of the Hermitian subspace with scalar part $\tfrac{1}{2}$, every other zero divisor of the subspace being a real multiple of one of them. So an idempotent of the Hermitian subspace is either the unit $e_0$, or $0$, or a zero divisor of norm $0$; there is nothing in between, and the only idempotent of the subspace that is a unit is $e_0$.

**Second, the complement and the orthogonality.** The complement $e_0 - \tilde\Pi = \tfrac{1}{2}(e_0 - i\mathbf{u})$ is again a nontrivial idempotent of the Hermitian subspace, $\tilde\Pi$ and $e_0 - \tilde\Pi$ are orthogonal, and they are the only two nontrivial idempotents of the algebra orthogonal to each other in the pair:

$$
\tilde\Pi\left(e_0 - \tilde\Pi\right) = \left(e_0 - \tilde\Pi\right)\tilde\Pi = 0 , \qquad \tilde\Pi + \left(e_0 - \tilde\Pi\right) = e_0 .
$$

The pair is a complete orthogonal pair of idempotents, a **frame** of the algebra, and each member is primitive, generating a minimal right ideal; the proof that the ideals are minimal, and the resulting Peirce decomposition, are in *Biquaternion Ideals and Peirce Decomposition*. What belongs here is the concrete shape: a Hermitian idempotent cuts the algebra into the four pieces $\tilde\Pi\mathbb{B}\tilde\Pi$, $\tilde\Pi\mathbb{B}(e_0-\tilde\Pi)$, $(e_0-\tilde\Pi)\mathbb{B}\tilde\Pi$ and $(e_0-\tilde\Pi)\mathbb{B}(e_0-\tilde\Pi)$, each of real dimension $2$, so that the eight-dimensional algebra splits into four pieces of dimension two. None of the four is a sum of coordinate blocks: for $\tilde\Pi = \tfrac{1}{2}(e_0 + ie_1)$ the pieces mix the eight basis elements, in contrast with the six subspaces, every one of which is a sum of blocks.

**Third, the projection.** The idempotent is the projection onto $\mathbb{B}\tilde\Pi$ along $\mathbb{B}(e_0 - \tilde\Pi)$, and on the two summands it acts as the identity and as zero:

$$
\tilde\Pi\tilde{X}\tilde\Pi = \tilde{X}\tilde\Pi \quad (\tilde{X} \in \mathbb{B}\tilde\Pi) , \qquad \tilde\Pi\tilde{Y}\tilde\Pi = 0 \quad (\tilde{Y} \in \mathbb{B}(e_0 - \tilde\Pi)) .
$$

This is the statement that the idempotent is a projection, and it is the same statement in the algebra and in the matrix representation, whose projections are the images of these under the isomorphism.

The Hermitian subspace carries the idempotents, and with them the minimal ideals. Let $\tilde\Pi = \tfrac{1}{2}(e_0 + i\mathbf{u})$ be a Hermitian idempotent and $f = e_0 - \tilde\Pi = \tfrac{1}{2}(e_0 - i\mathbf{u})$ its complement. The annihilators are the complement ideals themselves, in the plain sense

$$
I_{\tilde\Pi} = \left\{\tilde X : \tilde X\tilde\Pi = 0\right\} = \left\{\tilde X\,f : \tilde X \in \mathbb{B}\right\} = \mathbb{B}f , \qquad J_{\tilde\Pi} = f\mathbb{B} ,
$$

the first because $\tilde X\tilde\Pi = 0$ leaves $\tilde X = \tilde X(\tilde\Pi + f) = \tilde X f$, and conversely $(\tilde X f)\tilde\Pi = \tilde X f\tilde\Pi = 0$. Here $\tilde\Pi$ is not nilpotent, its square being $2\tilde\Pi$, so the second theorem applies with its second alternative and

$$
\mathbb{B} = \mathbb{B}\tilde\Pi \oplus \mathbb{B}f = \tilde\Pi\mathbb{B} \oplus f\mathbb{B} ,
$$

four nonzero proper one-sided ideals, all minimal, all of real dimension $4$, arranged in two complementary pairs.

The four are the halves of the Peirce decomposition. Expanding $\tilde X$ as $\tilde\Pi\tilde X\tilde\Pi + \tilde\Pi\tilde X f + f\tilde X\tilde\Pi + f\tilde X f$ gives

$$
\mathbb{B} = \tilde\Pi\mathbb{B}\tilde\Pi \oplus \tilde\Pi\mathbb{B}f \oplus f\mathbb{B}\tilde\Pi \oplus f\mathbb{B}f ,
$$

and each of the four Peirce spaces is a complex line, so that the decomposition is

$$
\mathbb{B} = \mathbb{C}\tilde\Pi \oplus \mathbb{C}\tilde R \oplus \mathbb{C}\tilde T \oplus \mathbb{C}f , \qquad \mathbb{C}\tilde R = \tilde\Pi\mathbb{B}f , \quad \mathbb{C}\tilde T = f\mathbb{B}\tilde\Pi .
$$

For $\tilde\Pi = \tfrac{1}{2}(e_0 + ie_1)$ the lines are spanned by

$$
\tilde\Pi\mathbb{B}\tilde\Pi = \mathbb{C}\tilde\Pi , \quad \tilde\Pi\mathbb{B}f = \mathbb{C}(e_3 - ie_2) , \quad f\mathbb{B}\tilde\Pi = \mathbb{C}(e_3 + ie_2) , \quad f\mathbb{B}f = \mathbb{C}f ,
$$

and the same four, grouped in pairs, are the four minimal one-sided ideals:

$$
\mathbb{B}\tilde\Pi = \mathbb{C}\tilde\Pi \oplus \mathbb{C}(e_3 + ie_2) , \quad \mathbb{B}f = \mathbb{C}f \oplus \mathbb{C}(e_3 - ie_2) , \quad \tilde\Pi\mathbb{B} = \mathbb{C}\tilde\Pi \oplus \mathbb{C}(e_3 - ie_2) , \quad f\mathbb{B} = \mathbb{C}f \oplus \mathbb{C}(e_3 + ie_2) .
$$

Two of the four lines are the **idempotent lines** $\mathbb{C}\tilde\Pi$ and $\mathbb{C}f$, each meeting $\mathbb{M}_+$ and $\mathbb{M}_-$ in one real dimension — $\tilde\Pi$ is Hermitian and $i\tilde\Pi$ is anti-Hermitian — and two are the **nilpotent lines** $\mathbb{C}(e_3 \mp ie_2)$, lying wholly in the vector subspace, since $e_3 \pm ie_2$ is a nilpotent and $i$ times a nilpotent is again pure. So each minimal ideal is the sum of a complex line of the vector subspace, a real line of $\mathbb{M}_+$ and a real line of $\mathbb{M}_-$, and of nothing else.

## The Anti-Hermitian Subspace

The anti-Hermitian subspace has one idempotent, $0$. Every product of two of its elements lies in the Hermitian subspace: for $\tilde{Q} = ib_0e_0 + \mathbf{q}$ with $b_0$ real and $\mathbf{q}$ real, the square is $\tilde{Q}^2 = -(b_0^2 + (\mathbf{q},\mathbf{q}))e_0 + 2ib_0\mathbf{q}$, real in its scalar part and imaginary in its vector part, which is the shape of $\mathbb{M}_+$. So an idempotent there would satisfy $\tilde\Pi = \tilde\Pi^2 \in \mathbb{M}_+$ and lie in $\mathbb{M}_+ \cap \mathbb{M}_- = 0$. The subspace has zero divisors, by *The Six Subspaces and the Elements*, and no idempotent: its nonzero elements are the purely imaginary multiples of the Hermitian subspace's idempotents, and a central multiple $c\tilde\Pi$ of an idempotent is an idempotent only when $c(c-1) = 0$, that is when $c = 0$ or $c = 1$.

For the ideals the subspace is $i\mathbb{M}_+$: multiplication by the central unit $i$ is a bijection of $\mathbb{M}_+$ onto $\mathbb{M}_-$ that preserves products and linear combinations and therefore preserves ideals. So the zero divisors of $\mathbb{M}_-$ are the purely imaginary multiples of the Hermitian idempotents, by *The Six Subspaces and the Elements*, and the minimal ideals they determine are the very same four, $\mathbb{B}\tilde\Pi$, $\mathbb{B}f$, $\tilde\Pi\mathbb{B}$ and $f\mathbb{B}$, with the same elements. **The subspace $\mathbb{M}_-$ adds no ideal to those already determined by $\mathbb{M}_+$**, and the same relation holds between $i\mathbb{H}_{\mathbb{B}}$ and $\mathbb{H}_{\mathbb{B}}$, and between the centre and itself, so that up to the central unit $i$ the ideal theory of the six is carried by the three subspaces $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$ and $\mathbb{M}_+$.

## Summary

An idempotent of the biquaternion algebra is $0$, $e_0$, or $\tfrac{1}{2}(e_0 + \xi i)$ for a root $\xi$ of minus one, and the algebra is simple, its only two-sided ideals being $0$ and $\mathbb{B}$, with length two, so that every nonzero proper one-sided ideal is minimal of real dimension $4$. Of the six distinguished subspaces, only three contain a nonzero idempotent: the centre and the quaternion subspace contain $0$ and $e_0$ and nothing else, and the Hermitian subspace contains, besides those, the two-sphere of Hermitian idempotents $\tfrac{1}{2}(e_0 + i\mathbf{u})$ over real unit vectors $\mathbf{u}$. The vector, anti-quaternion and anti-Hermitian subspaces contain only $0$, in each case because a product of two of their elements cannot come back into the subspace as an idempotent would have to. The nontrivial idempotents of the six are therefore exactly the Hermitian idempotents, all in the Hermitian subspace, each a zero divisor of norm $0$, each paired with the orthogonal complement $e_0 - \tilde\Pi$ and with no other nontrivial orthogonal partner; the pair is a frame, and it cuts the algebra into four pieces of real dimension $2$, none of them a sum of coordinate blocks. An idempotent built on a root of minus one that is not Hermitian lies in none of the six, its vector part mixing a real and an imaginary direction, so a generic projection of the algebra is invisible to the six.

On the ideal side, no subspace of the six is a two-sided ideal and each of the six generates $\mathbb{B}$ on both sides, since each contains a unit. Through its zero divisors each of the six determines minimal ideals, and there are none unless the subspace carries a zero divisor, by *The Six Subspaces and the Elements*: none from the centre, the quaternion subspace or the anti-quaternion subspace, which consist of $0$ and units; from the vector subspace, the minimal ideal $\mathbb{B}\mathbf{P} = I_{\mathbf{P}}$ of any nonzero nilpotent, which coincides with its own annihilator; and from either Hermitian subspace, the four minimal ideals $\mathbb{B}\tilde\Pi$, $\mathbb{B}f$, $\tilde\Pi\mathbb{B}$, $f\mathbb{B}$ of a Hermitian idempotent, which come in two complementary pairs summing to $\mathbb{B}$. For a non-nilpotent zero divisor the ideal generated and the annihilator are distinct and complementary; for a nilpotent they coincide. The four minimal ideals of a Hermitian idempotent are the four Peirce spaces, which are complex lines: the two idempotent lines and the two nilpotent lines, the latter inside the vector subspace. Every one of the minimal ideals determined by the six meets the six in the same way, two real dimensions in the vector subspace, one in $\mathbb{M}_+$ and one in $\mathbb{M}_-$,

| minimal ideal | $\mathbb{C}_{\mathbb{B}}$ | $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
|---|---|---|---|---|---|---|
| each $\mathbb{B}\mathbf{P}$, $\mathbf{P}\mathbb{B}$, $\mathbb{B}\tilde\Pi$, $\mathbb{B}f$, $\tilde\Pi\mathbb{B}$, $f\mathbb{B}$ | $0$ | $2$ | $0$ | $0$ | $1$ | $1$ |

the entries being real dimensions; so the minimal ideals meet exactly the three subspaces that carry zero divisors, and avoid the other three entirely. The classification and the Peirce decomposition are the business of *Biquaternion Ideals and Peirce Decomposition*; what is added here is their restriction to the six.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra |
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B})$ | the centre and the vector subspace |
| $\mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces |
| $\mathbb{M}_+, \mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces |
| $\tilde\Pi$ | an idempotent, $\tilde\Pi^2 = \tilde\Pi$ |
| $e_0 - \tilde\Pi, f$ | the complementary idempotent |
| $\mathbf{u}, \mathbf{v}$ | real unit vectors, the parameters of the Hermitian idempotents |
| $I_{\tilde Q}, J_{\tilde Q}$ | the sets of $\tilde X$ with $\tilde X\tilde Q = 0$ and with $\tilde Q\tilde X = 0$ |
| $\mathbf{P}$ | a nonzero nilpotent of the vector subspace |

## Further Reading

- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the six subspaces themselves, one to a section
- *Biquaternion Idempotents and Projections* (`articles_maths/biquaternion-idempotents-and-projections.md`), for the classification of the idempotents of the whole algebra, the bijection with the roots of minus one and the projection reading
- *Biquaternion Ideals and Peirce Decomposition* (`articles_maths/biquaternion-ideals-and-peirce-decomposition.md`), for simplicity, the length, the minimal ideals and the Peirce decomposition in the whole algebra
- *The Six Subspaces and the Elements* (`articles_maths/the-six-subspaces-and-the-elements.md`), for the zero divisors whose annihilators the minimal ideals are, and for the roots of minus one the idempotents are built from
- *The Six Subspaces and the Norms* (`articles_maths/the-six-subspaces-and-the-norms.md`), for the theorem that the minimal one-sided ideals are the maximal totally isotropic one-sided ideals of the bilinear form, and for the Peirce basis in which that form is hyperbolic
- *The Four Biquaternion Complex Products* (`articles_maths/the-four-biquaternion-complex-products.md`), for the product formula
