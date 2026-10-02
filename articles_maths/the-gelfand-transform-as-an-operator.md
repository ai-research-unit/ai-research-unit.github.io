
# __The Gelfand Transform as an Operator__

## Introduction

A character of a commutative Banach algebra is a nonzero multiplicative linear functional, and the characters are automatically continuous with norm one. Collecting them into a space turns each element of the algebra into a function on that space: the **Gelfand transform** is the map $\Gamma$ that sends $a$ to the function $\hat a(\chi) = \chi(a)$ on the character space. Read as an operator, $\Gamma$ is a bounded unital algebra homomorphism from $A$ into the algebra of continuous functions on the character space, with norm one, and its algebraic and operator-theoretic properties — its kernel, its image, its continuity, its relation to the spectrum and the spectral radius — are the subject of this article. The kernel measures how far the algebra is from semisimple; it is the radical, and the transform is injective exactly for a semisimple algebra.

This article assumes the commutative Banach algebra, its characters, the maximal ideals, the spectrum, the spectral radius and the Gelfand–Mazur theorem from *Topological Algebras and Banach Algebras*; the characters as continuous functionals and the character space from *Operators on a Banach Algebra*; the ideals, the quotient by a closed ideal, the radical and the Jacobson radical from *Rings* and *Ideals and Quotients of Algebras*; and the compact and locally compact spaces, the topology of uniform convergence and the algebra $C_0(\Delta)$ from *Topological Spaces* and *Normed and Banach Spaces*. The involution is the later group of this category and is not used; the isometry and surjectivity of the transform for a commutative $\mathrm{C}^*$-algebra are *Involutive Banach Algebras and the Gelfand–Naimark Theorem* and *The Involution and the Spectral Radius*, and the measure-theoretic spectral theorem is Part III. The transform of a commutative Banach algebra without involution need not be isometric and need not be surjective, and both failures are recorded.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$; $A$ is a commutative Banach algebra over $\mathbb{K}$ with submultiplicative norm $\lVert\cdot\rVert$, unital with unit $1$ where a statement names $1$; $\Delta = \operatorname{Max}(A)$ is the set of nonzero multiplicative linear functionals, the **character space**; $\widehat{a} : \Delta \to \mathbb{K}$ is the **Gelfand transform** of $a$, $\widehat a(\chi) = \chi(a)$, and $\Gamma : A \to C_0(\Delta)$, $a \mapsto \widehat a$, is the transform as an operator. The radical of $A$ is $\operatorname{rad}(A)$.

## The Characters and the Character Space

**Definition.** A **character** of $A$ is a linear functional $\chi : A \to \mathbb{K}$ with $\chi \neq 0$ and $\chi(ab) = \chi(a)\chi(b)$ for all $a,b$; the set of characters is $\Delta = \operatorname{Max}(A)$, the **Gelfand spectrum** or character space of $A$.

**Proposition (characters are bounded and correspond to maximal ideals).** Every character is continuous with $\lVert\chi\rVert = 1$ on a unital algebra, and

$$
\chi \longmapsto \ker\chi
$$

is a bijection of $\Delta$ onto the set of maximal ideals of a unital commutative Banach algebra; the kernel of a character is a closed maximal ideal of codimension one.

**Proof.** Continuity and $\lVert\chi\rVert = 1$ are proved in *Operators on a Banach Algebra*: if $\lvert\chi(a)\rvert > \lVert a\rVert$ then $1 - a/\chi(a)$ is invertible while its image $0$ is not. The kernel of a nonzero multiplicative functional is a proper ideal, of codimension one because $\chi$ is nonzero and onto, hence a maximal ideal, closed as the kernel of a continuous map. Conversely a maximal ideal $M$ of a unital commutative Banach algebra is closed and $A/M$ is a field that is a Banach algebra, hence $\mathbb{K}$ by the Gelfand–Mazur theorem, and the quotient map is a character with kernel $M$. $\square$

**Theorem (the character space is a compact Hausdorff space).** Let $A$ be a unital commutative Banach algebra. Then $\Delta$ is a nonempty compact Hausdorff space in the weak-$*$ topology inherited from the dual $A'$, and the evaluation $\chi \mapsto \chi(a)$ is continuous for every $a$. If $A$ is not unital then $\Delta$ is locally compact Hausdorff but need not be compact, and it is compact exactly when $A$ has a unit.

**Proof.** $\Delta \subseteq \{\chi \in A' : \lVert\chi\rVert = 1\}$, the unit sphere of the dual, which is weak-$*$ compact by the Banach–Alaoglu theorem of *Normed and Banach Spaces*; the multiplicative conditions and $\chi(1) = 1$ are closed, so $\Delta$ is a closed subset of a compact space, hence compact. Nonemptiness is the Gelfand–Mazur theorem applied to a maximal ideal, which exists by Zorn's lemma. In the non-unital case the characters extend to the unitisation and form a locally compact space; the unit may be adjoined, and compactness is recovered exactly when the unit is present. $\square$

**Corollary (evaluation separates points and elements).** For distinct characters $\chi \neq \psi$ there is $a$ with $\chi(a) \neq \psi(a)$; for $a \neq 0$ in a semisimple algebra there is a character with $\chi(a) \neq 0$. Hence $\Delta$ separates the points of $\Delta$ through the functions $\widehat a$, and the transform separates the elements of a semisimple algebra.

**Proof.** Two distinct characters have distinct kernels, and a character with the same values on a maximal ideal and at the unit is determined; the second statement is the definition of semisimplicity. $\square$

## The Transform as an Operator

**Definition.** The **Gelfand transform** is the map

$$
\Gamma : A \longrightarrow C_0(\Delta) , \qquad \Gamma(a) = \widehat a , \qquad \widehat a(\chi) = \chi(a) .
$$

**Theorem ($\Gamma$ is a bounded unital algebra homomorphism of norm one).** The Gelfand transform is a unital algebra homomorphism when $A$ is unital,

$$
\widehat{a+b} = \widehat a + \widehat b , \qquad \widehat{\lambda a} = \lambda\,\widehat a , \qquad \widehat{ab} = \widehat a\,\widehat b , \qquad \widehat 1 = 1 ,
$$

it is bounded with operator norm $\lVert\Gamma\rVert = 1$ on a unital algebra, and its image lies in $C_0(\Delta)$;

$$
\lVert\widehat a\rVert_\infty = \sup_{\chi \in \Delta}\lvert\chi(a)\rvert \leq \lVert a\rVert .
$$

**Proof.** Multiplicativity is $\chi(ab) = \chi(a)\chi(b)$ for each $\chi$, additivity and homogeneity are the linearity of each $\chi$, and $\widehat 1(\chi) = \chi(1) = 1$. The bound is $\lvert\chi(a)\rvert \leq \lVert a\rVert$ for every character, so the sup is at most $\lVert a\rVert$; the element $\widehat a$ is continuous as a pointwise limit of the continuous evaluations, and it vanishes at infinity in the non-unital case. The norm is attained at $\widehat 1 = 1$, so $\lVert\Gamma\rVert = 1$. $\square$

**Theorem (the kernel is the radical).** The kernel of the Gelfand transform is the intersection of the maximal ideals, that is the radical,

$$
\ker\Gamma = \bigcap_{\chi \in \Delta}\ker\chi = \operatorname{rad}(A) ,
$$

and $\Gamma$ is injective if and only if $A$ is semisimple, $\operatorname{rad}(A) = 0$. Consequently $\Gamma$ induces an injective transform on the semisimple quotient $A/\operatorname{rad}(A)$, and the image is a subalgebra of $C_0(\Delta)$ isomorphic to $A/\operatorname{rad}(A)$.

**Proof.** $\widehat a = 0$ means $\chi(a) = 0$ for every character, that is $a$ lies in every maximal ideal, and the intersection of the maximal ideals is the radical by definition; the first isomorphism theorem gives the injectivity on $A/\operatorname{rad}(A)$. $\square$

**Corollary (the radical is a closed ideal and the semisimple quotient is a Banach algebra).** The radical of a commutative Banach algebra is a closed two-sided ideal, and $A/\operatorname{rad}(A)$ is a semisimple commutative Banach algebra isometrically embedded by $\Gamma$ in $C_0(\Delta)$.

**Proof.** $\ker\Gamma$ is closed, being the kernel of the bounded operator $\Gamma$; the quotient of a Banach algebra by a closed ideal is a Banach algebra by *Ideals and Quotients of Algebras*, and it is semisimple by construction. $\square$

## The Spectrum and the Spectral Radius

**Theorem (the spectrum is the image of the element).** For $a$ in a unital commutative Banach algebra,

$$
\sigma(a) = \widehat a(\Delta) = \{\chi(a) : \chi \in \Delta\} ,
$$

so the spectrum of $a$ is exactly the set of values of its Gelfand transform, and the transform is the spectral model of the algebra.

**Proof.** $\lambda \in \sigma(a)$ means $a - \lambda$ is not invertible, so it lies in some maximal ideal $M = \ker\chi$, and then $\chi(a) = \lambda$; conversely if $\chi(a) = \lambda$ then $\chi(a - \lambda) = 0$ so $a - \lambda$ lies in the proper ideal $\ker\chi$ and is not invertible, so $\lambda \in \sigma(a)$. $\square$

**Theorem (the spectral radius formula).** For every $a$,

$$
r(a) = \lVert\widehat a\rVert_\infty = \sup_{\chi\in\Delta}\lvert\chi(a)\rvert = \lim_{n\to\infty}\lVert a^n\rVert^{1/n} ,
$$

so the Gelfand transform computes the spectral radius, and $\Gamma$ is a contraction that is isometric exactly when $\lVert a\rVert = r(a)$ for all $a$.

**Proof.** The spectrum is $\widehat a(\Delta)$, so its supremum modulus is $\lVert\widehat a\rVert_\infty$; the Beurling–Gelfand theorem gives $r(a) = \lim\lVert a^n\rVert^{1/n}$; combining, the transform preserves the value of the spectral radius, and it preserves the norm exactly when the norm is the spectral radius. $\square$

**Corollary (the transform is not isometric in general).** If $A$ is a commutative Banach algebra and $a$ is nilpotent but nonzero, then $\widehat a = 0$ and $a \neq 0$, so $\Gamma$ is not injective; if instead every $a$ satisfies $\lVert a\rVert = r(a)$ then $\Gamma$ is isometric. In general $\lVert\Gamma\rVert = 1$ and $\Gamma$ is not an isometry.

**Proof.** A nilpotent $a$ has $\chi(a)^n = \chi(a^n) = 0$, so $\chi(a) = 0$ for every character; the image of a nonzero nilpotent is zero, and injectivity fails. The second case is the theorem read with $\lVert a\rVert = r(a)$. $\square$

## The Image of the Transform

**Proposition (the image is a separating algebra of continuous functions).** The image $\Gamma(A)$ is a unital subalgebra of $C_0(\Delta)$ that separates the points of $\Delta$, and it is closed under complex conjugation only in the involutive cases treated later. The transform is surjective onto $C_0(\Delta)$ exactly when $A/\operatorname{rad}(A) \cong C_0(\Delta)$ isometrically, which fails in general.

**Proof.** The image is a subalgebra because $\Gamma$ is a homomorphism, and it separates points by the corollary above. Surjectivity is a special property: the disk algebra has character space the closed disk, but its transform lands in the disc algebra of functions continuous on the disk and analytic on its interior, a proper subalgebra of $C(\Delta)$. $\square$

**Corollary (the closed image and the quotient).** $\Gamma(A)$ is a subalgebra of $C_0(\Delta)$ isomorphic to $A/\operatorname{rad}(A)$, and the transform is a bijection onto its image; its closure in the supremum norm is a commutative Banach algebra isometrically isomorphic to the completion of $A/\operatorname{rad}(A)$ for the spectral norm.

**Proof.** The induced map $A/\operatorname{rad}(A) \to \Gamma(A)$ is an injective homomorphism, and the completion in the supremum norm identifies with the closure of the image. $\square$

**Remark (the involutive refinement).** When $A$ carries an involution and satisfies the $\mathrm{C}^*$-identity, the Gelfand transform becomes isometric and surjective, and the abstract commutative $\mathrm{C}^*$-algebra is isometrically ${}^*$-isomorphic to $C_0(\Delta)$; that refinement is *Involutive Banach Algebras and the Gelfand–Naimark Theorem*, later in this category, and *The Involution and the Spectral Radius*. The present article uses no involution, and its transform is only a contraction.

## Examples

**Example (the algebra $C_0(\Delta)$ itself).** If $A = C_0(\Delta)$ for a locally compact Hausdorff $\Delta$, then $\operatorname{Max}(A) = \Delta$ (the evaluations), and the Gelfand transform is the identity, an isometric isomorphism; the algebra is semisimple and its radical is zero.

**Example (the disk algebra).** Let $A$ be the disc algebra of functions continuous on the closed unit disk and holomorphic on its interior, with the supremum norm. Its characters are the evaluations at points of the closed disk, $\Delta$ is the closed disk, and $\Gamma$ is the inclusion of the disc algebra in $C(\Delta)$, injective with closed image that is a proper subalgebra of $C(\Delta)$; the spectral radius of the generator $z$ is $1$, so $\Gamma$ is isometric here, but the image is not all of $C(\Delta)$.

**Example (the Wiener algebra).** Let $A$ be the Wiener algebra of absolutely convergent Fourier series, with the $\ell^1$ norm. Its characters are the evaluations at points of the circle, but the algebra is not a $\mathrm{C}^*$-algebra, and the transform is an injection into $C(\mathbb{T})$ whose image is a dense proper subalgebra: it is not isometric for the $\ell^1$ norm, since $\lVert\widehat a\rVert_\infty \leq \lVert a\rVert_1$ with strict inequality in general.

**Example (a nilpotent radical).** Let $A$ be the algebra of $2 \times 2$ upper triangular matrices of the form $\big(\begin{smallmatrix}\lambda & \mu \\ 0 & \lambda\end{smallmatrix}\big)$, a commutative Banach algebra under a matrix norm. The only character is $\chi\big(\begin{smallmatrix}\lambda & \mu \\ 0 & \lambda\end{smallmatrix}\big) = \lambda$, so $\Delta$ is a point, the transform sends the nilpotent $N = \big(\begin{smallmatrix}0 & 1 \\ 0 & 0\end{smallmatrix}\big)$ to $0$, and the radical is the one-dimensional ideal $\mathbb{K}N$; the transform is not injective and the algebra is not semisimple.

## Summary

For a commutative Banach algebra $A$ the character space $\Delta = \operatorname{Max}(A)$ is a compact Hausdorff space in the weak-$*$ topology when $A$ is unital and a locally compact one otherwise, its points are the continuous multiplicative functionals of norm one, and its points are in bijection with the maximal ideals. The Gelfand transform $\Gamma : A \to C_0(\Delta)$, $\widehat a(\chi) = \chi(a)$, is a bounded unital algebra homomorphism of operator norm one with $\lVert\widehat a\rVert_\infty \leq \lVert a\rVert$; its kernel is the radical, the intersection of the maximal ideals, so $\Gamma$ is injective exactly when $A$ is semisimple, and it induces an isomorphism of $A/\operatorname{rad}(A)$ onto a separating subalgebra of $C_0(\Delta)$. The spectrum of an element is the image of its transform, $\sigma(a) = \widehat a(\Delta)$, and the spectral radius is the supremum norm, $r(a) = \lVert\widehat a\rVert_\infty = \lim\lVert a^n\rVert^{1/n}$. The transform is a contraction that is isometric only when the norm equals the spectral radius and surjective only in special cases; in the involutive $\mathrm{C}^*$-case it becomes an isometric ${}^*$-isomorphism onto $C_0(\Delta)$, which is *Involutive Banach Algebras and the Gelfand–Naimark Theorem*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$, $\lVert\cdot\rVert$ | Commutative Banach algebra and its norm |
| $\Delta = \operatorname{Max}(A)$ | The character space, compact when $A$ is unital |
| $\chi$ | A character: nonzero multiplicative linear functional, $\lVert\chi\rVert=1$ |
| $\ker\chi$, maximal ideals | Bijection of characters with maximal ideals |
| $\widehat a(\chi) = \chi(a)$ | The Gelfand transform of the element $a$ |
| $\Gamma : a \mapsto \widehat a$ | The Gelfand transform as an operator, $\lVert\Gamma\rVert = 1$ |
| $\operatorname{rad}(A) = \ker\Gamma$ | The radical, the intersection of the maximal ideals |
| $\sigma(a) = \widehat a(\Delta)$ | Spectrum as the range of the transform |
| $r(a) = \lVert\widehat a\rVert_\infty = \lim\lVert a^n\rVert^{1/n}$ | Spectral radius formula |
| $C_0(\Delta)$ | Continuous functions vanishing at infinity on $\Delta$ |
| $A/\operatorname{rad}(A)$ | The semisimple quotient, embedded injectively by $\Gamma$ |

## Further Reading

- Israel M. Gelfand and Dmitri A. Raikov, "On the theory of normed rings" (1943), for the Gelfand transform, the character space and the radical.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the Gelfand theory of a commutative Banach algebra and the radical.
- Frank F. Bonsall and John Duncan, *Complete Normed Algebras* (Springer, 1973), for the character space, the transform and the spectral radius formula.
- Garth Warner, *Commutative Banach Algebras* (unpublished lecture notes), for the disc algebra, the Wiener algebra and their character spaces.
- Eberhard Kaniuth, *A Course in Commutative Banach Algebras*, Graduate Texts in Mathematics 246 (Springer, 2009), for the transform, the radical and the structure of the character space.
