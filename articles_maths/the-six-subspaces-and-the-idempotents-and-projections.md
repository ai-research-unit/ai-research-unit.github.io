# __The Six Subspaces and the Idempotents and Projections__

## Introduction

An element of the biquaternion algebra is an **idempotent** if $\tilde{\Pi}^2 = \tilde{\Pi}$. Idempotents are the algebraic form of a projection: an idempotent splits the algebra as $\mathbb{B} = \mathbb{B}\tilde{\Pi} \oplus \mathbb{B}(e_0 - \tilde{\Pi})$, its complement $e_0 - \tilde{\Pi}$ is the complementary projection, and the two pieces are the two summands. The algebra's own treatment is in *Biquaternion Idempotents and Projections*, where the classification is that every idempotent is $0$, or $e_0$, or of the form

$$
\tilde{\Pi} = \tfrac{1}{2}\left(e_0 + \xi i\right), \qquad \xi^2 = -1 ,
$$

with $\xi$ a root of minus one; there are no others. This article records which idempotents lie in the six distinguished subspaces, and what they do there.

Writing the idempotent as $\tilde{\Pi} = \Pi_0e_0 + \mathbf{q}$, with $\Pi_0$ the scalar part and $\mathbf{q}$ the vector part, and using $\mathbf{q}^2 = -(\mathbf{q},\mathbf{q})e_0$, the equation $\tilde{\Pi}^2 = \tilde{\Pi}$ is the pair

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

**Proof.** Read the two equations of the display on each subspace, whose elements are enumerated in *Introduction to the Six Subspaces*. The second equation, $2\Pi_0\mathbf{q} = \mathbf{q}$, is the one that does the work: it forces $\mathbf{q} = 0$ unless the scalar part is exactly $\tfrac{1}{2}$, and the scalar part is real only on the centre and in the Hermitian subspace. *Centre:* $\mathbf{q} = 0$ and $\Pi_0^2 = \Pi_0$, so $\Pi_0 \in \{0,1\}$. *Vector:* $\Pi_0 = 0$, and $2\Pi_0\mathbf{q} = \mathbf{q}$ gives $\mathbf{q} = 0$ directly, whatever the first equation would allow. *Quaternion:* $\Pi_0 = h_0$ real and $\mathbf{q}$ a real vector; $2h_0\mathbf{q} = \mathbf{q}$ gives $\mathbf{q} = 0$ or $h_0 = \tfrac{1}{2}$, and $h_0 = \tfrac{1}{2}$ in the first equation gives $(\mathbf{q},\mathbf{q}) = -\tfrac{1}{4}$, impossible for a real vector, so $\mathbf{q} = 0$ and $h_0 \in \{0,1\}$. *Anti-quaternion:* $\Pi_0$ is purely imaginary and $\mathbf{q}$ is real; $2\Pi_0\mathbf{q} = \mathbf{q}$ forces $\mathbf{q} = 0$ since $2\Pi_0 \neq 1$, and the first equation then gives $\Pi_0^2 = \Pi_0$ with $\Pi_0$ purely imaginary, so $\Pi_0 = 0$. *Hermitian:* $\Pi_0 = a_0$ real and $\mathbf{q} = i\mathbf{p}$ with $\mathbf{p}$ real, so $(\mathbf{q},\mathbf{q}) = -(\mathbf{p},\mathbf{p})$; the second equation gives $\mathbf{p} = 0$ or $a_0 = \tfrac{1}{2}$, and with $\mathbf{p} = 0$ the first gives $a_0 \in \{0,1\}$ while with $a_0 = \tfrac{1}{2}$ it gives $(\mathbf{p},\mathbf{p}) = \tfrac{1}{4}$. *Anti-Hermitian:* $\Pi_0$ is purely imaginary and $\mathbf{q}$ is real; the second equation forces $\mathbf{q} = 0$, and the first gives $\Pi_0 = 0$. $\square$

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

## The Centre Subspace

A central element is $Ae_0$, and $A^2 = A$ forces $A \in \{0,1\}$:

$$
0 , \qquad e_0 .
$$

The centre is a field, so it carries no nontrivial idempotent, and the only idempotent of it that is not the unit is the zero element. It is one of the three subspaces of the theorem, and the only one of them that is commutative: the trivial pair $0$ and $e_0$ is all the centre has, and it is the same trivial pair that the quaternion subspace has for a different reason.

## The Vector Subspace

The vector subspace has one idempotent, $0$. A pure vector with $\mathbf{P}^2 = \mathbf{P}$ would have $\mathbf{P}^2 = -(\mathbf{P},\mathbf{P})e_0$ central and equal to the pure vector $\mathbf{P}$, so $\mathbf{P} \in \mathbb{C}_{\mathbb{B}} \cap \mathrm{Vect}(\mathbb{B}) = 0$. In the language of the two equations of the Introduction it is the second, $2\Pi_0\mathbf{q} = \mathbf{q}$, that rules the case out, since the first, $(\mathbf{P},\mathbf{P}) = 0$, has nonzero solutions — the square-zero elements of *The Six Subspaces and the Zero Divisors*. The vector subspace therefore has square-zero elements and no idempotent; an element of the algebra that is a projection never has a pure vector part without a scalar part.

## The Quaternion Subspace

The quaternion subspace has the two trivial idempotents and no others:

$$
0 , \qquad e_0 .
$$

For $h \in \mathbb{H}_{\mathbb{B}}$, the equation $h^2 = h$ reads $h(h - e_0) = 0$, and the quaternion subspace is a division algebra, so $h = 0$ or $h = e_0$. This is the argument that the anti-quaternion subspace cannot use — it is not a division algebra, nor even closed under the product — and it is the reason the two quaternion subspaces reach the same trivial answer by different routes.

## The Anti-Quaternion Subspace

The anti-quaternion subspace has one idempotent, $0$. An element of it is $ih$ with $h$ real, and $(ih)^2 = -h^2$ is a real quaternion; an idempotent there would satisfy $\tilde{\Pi} = \tilde{\Pi}^2 \in \mathbb{H}_{\mathbb{B}}$ and therefore lie in $i\mathbb{H}_{\mathbb{B}} \cap \mathbb{H}_{\mathbb{B}} = 0$. The subspace consists of units and zero, by *The Six Subspaces and the Units*, and its idempotents are correspondingly the fewest possible: it contributes nothing to the projection theory of the algebra, and its interest for the idempotents is exactly that the products it produces land in, and only in, the two quaternion and Hermitian subspaces.

## The Hermitian Subspace

The Hermitian subspace is the one subspace of the six that carries a nontrivial family of idempotents. Besides $0$ and $e_0$,

$$
\tilde{\Pi} = \tfrac{1}{2}\left(e_0 + i\mathbf{u}\right) , \qquad \mathbf{u} \in \mathbb{R}^3 , \quad (\mathbf{u},\mathbf{u}) = 1 .
$$

The parameter $\mathbf{u}$ runs over a two-sphere, so the nontrivial idempotents of the Hermitian subspace form a two-parameter family; each is a Hermitian idempotent of the algebra and a projection, and the family is the one that occurs in the spectral theorem, treated in *Biquaternion Spectral Theory*. Three properties hold for every member, and they are the ones the projection theory uses.

**First, the norm vanishes, so every nontrivial idempotent of the Hermitian subspace is a zero divisor.** The norm of $\tfrac{1}{2}(e_0 + i\mathbf{u})$ is $\tfrac{1}{4}(1 - (\mathbf{u},\mathbf{u})) = 0$, and by *The Six Subspaces and the Zero Divisors* the nontrivial idempotents are exactly the zero divisors of the Hermitian subspace with scalar part $\tfrac{1}{2}$, every other zero divisor of the subspace being a real multiple of one of them. So an idempotent of the Hermitian subspace is either the unit $e_0$, or $0$, or a zero divisor of norm $0$; there is nothing in between, and the only idempotent of the subspace that is a unit is $e_0$.

**Second, the complement and the orthogonality.** The complement $e_0 - \tilde{\Pi} = \tfrac{1}{2}(e_0 - i\mathbf{u})$ is again a nontrivial idempotent of the Hermitian subspace, $\tilde{\Pi}$ and $e_0 - \tilde{\Pi}$ are orthogonal, and they are the only two nontrivial idempotents of the algebra orthogonal to each other in the pair:

$$
\tilde{\Pi}\left(e_0 - \tilde{\Pi}\right) = \left(e_0 - \tilde{\Pi}\right)\tilde{\Pi} = 0 , \qquad \tilde{\Pi} + \left(e_0 - \tilde{\Pi}\right) = e_0 .
$$

The pair is a complete orthogonal pair of idempotents, a **frame** of the algebra, and each member is primitive, generating a minimal right ideal; the proof that the ideals are minimal, and the resulting Peirce decomposition, are in *Biquaternion Ideals and Peirce Decomposition*. What belongs here is the concrete shape: a Hermitian idempotent cuts the algebra into the four pieces $\tilde{\Pi}\mathbb{B}\tilde{\Pi}$, $\tilde{\Pi}\mathbb{B}(e_0-\tilde{\Pi})$, $(e_0-\tilde{\Pi})\mathbb{B}\tilde{\Pi}$ and $(e_0-\tilde{\Pi})\mathbb{B}(e_0-\tilde{\Pi})$, each of real dimension $2$, so that the eight-dimensional algebra splits into four pieces of dimension two. None of the four is a sum of coordinate blocks: for $\tilde{\Pi} = \tfrac{1}{2}(e_0 + ie_1)$ the pieces mix the eight basis elements, in contrast with the six subspaces, every one of which is a sum of blocks.

**Third, the projection.** The idempotent is the projection onto $\mathbb{B}\tilde{\Pi}$ along $\mathbb{B}(e_0 - \tilde{\Pi})$, and on the two summands it acts as the identity and as zero:

$$
\tilde{\Pi}\tilde{X}\tilde{\Pi} = \tilde{X}\tilde{\Pi} \quad (\tilde{X} \in \mathbb{B}\tilde{\Pi}) , \qquad \tilde{\Pi}\tilde{Y}\tilde{\Pi} = 0 \quad (\tilde{Y} \in \mathbb{B}(e_0 - \tilde{\Pi})) .
$$

This is the statement that the idempotent is a projection, and it is the same statement in the algebra and in the matrix representation, whose projections are the images of these under the isomorphism.

## The Anti-Hermitian Subspace

The anti-Hermitian subspace has one idempotent, $0$. Every product of two of its elements lies in the Hermitian subspace: for $\tilde{Q} = ib_0e_0 + \mathbf{q}$ with $b_0$ real and $\mathbf{q}$ real, the square is $\tilde{Q}^2 = -(b_0^2 + (\mathbf{q},\mathbf{q}))e_0 + 2ib_0\mathbf{q}$, real in its scalar part and imaginary in its vector part, which is the shape of $\mathbb{M}_+$. So an idempotent there would satisfy $\tilde{\Pi} = \tilde{\Pi}^2 \in \mathbb{M}_+$ and lie in $\mathbb{M}_+ \cap \mathbb{M}_- = 0$. The subspace has zero divisors, by *The Six Subspaces and the Zero Divisors*, and no idempotent: its nonzero elements are the purely imaginary multiples of the Hermitian subspace's idempotents, and a central multiple $c\tilde{\Pi}$ of an idempotent is an idempotent only when $c(c-1) = 0$, that is when $c = 0$ or $c = 1$.

## Summary

An idempotent of the biquaternion algebra is $0$, $e_0$, or $\tfrac{1}{2}(e_0 + \xi i)$ for a root $\xi$ of minus one. Of the six distinguished subspaces, only three contain a nonzero idempotent: the centre and the quaternion subspace contain $0$ and $e_0$ and nothing else, and the Hermitian subspace contains, besides those, the two-sphere of Hermitian idempotents $\tfrac{1}{2}(e_0 + i\mathbf{u})$ over real unit vectors $\mathbf{u}$. The vector, anti-quaternion and anti-Hermitian subspaces contain only $0$, in each case because a product of two of their elements cannot come back into the subspace as an idempotent would have to. The nontrivial idempotents of the six are therefore exactly the Hermitian idempotents, all in the Hermitian subspace, each a zero divisor of norm $0$, each paired with the orthogonal complement $e_0 - \tilde{\Pi}$ and with no other nontrivial orthogonal partner; the pair is a frame, and it cuts the algebra into four pieces of real dimension $2$, none of them a sum of coordinate blocks. An idempotent built on a root of minus one that is not Hermitian lies in none of the six, its vector part mixing a real and an imaginary direction, so a generic projection of the algebra is invisible to the six.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra |
| $\mathbb{C}_{\mathbb{B}}, \mathrm{Vect}(\mathbb{B})$ | the centre and the vector subspace |
| $\mathbb{H}_{\mathbb{B}}, i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces |
| $\mathbb{M}_+, \mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces |
| $\tilde{\Pi}$ | an idempotent, $\tilde{\Pi}^2 = \tilde{\Pi}$ |
| $e_0 - \tilde{\Pi}$ | the complementary idempotent |
| $\mathbf{u}, \mathbf{v}$ | real unit vectors, the parameters of the Hermitian idempotents |

## Further Reading

- *Introduction to the Six Subspaces* (`articles_maths/introduction-to-the-six-subspaces.md`), for the six subspaces themselves, one to a section
- *The Six Subspaces and the Zero Divisors* (`articles_maths/the-six-subspaces-and-the-zero-divisors.md`), for the zero divisors that the nontrivial idempotents of the Hermitian subspace are
- *The Six Subspaces and the Jordan Algebra* (`articles_maths/the-six-subspaces-and-the-jordan-algebra.md`), for the subalgebras of the symmetrized product, among which the Hermitian subspace is the one carrying the idempotents
- *Biquaternion Idempotents and Projections* (`articles_maths/biquaternion-idempotents-and-projections.md`), for the classification of the idempotents of the whole algebra, the bijection with the roots of minus one and the projection reading
- *The Six Subspaces and the Ideals* (`articles_maths/the-six-subspaces-and-the-ideals.md`), for the four minimal one-sided ideals the idempotent determines and for the Peirce decomposition they come from
- *The Six Subspaces and the Roots of Minus One* (`articles_maths/the-six-subspaces-and-the-roots-of-minus-one.md`), for the roots of $-1$ from which the idempotents are built
