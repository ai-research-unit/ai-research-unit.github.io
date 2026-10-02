
# __Involutive Fréchet Algebras__

## Introduction

A **Fréchet algebra** is a complete metrisable locally convex topological algebra, and an **involutive Fréchet algebra** is one with a continuous involution. It is the natural home of the algebras of smooth and holomorphic functions, which are not Banach algebras in any natural norm but are complete for a countable sequence of seminorms, and it is the projective limit of the Banach $*$-algebras its seminorm quotients. The involution of a Fréchet algebra is required to be continuous for the Fréchet topology, and the spectral theory extends from the Banach case with one change of language: the spectrum of an element is defined by invertibility as before, and the involution moves it by conjugation, but the norm no longer bounds the spectrum, and the place of the norm is taken by the family of seminorms. This article develops the involutive Fréchet algebras, the continuity of the involution, the projective limit description and the spectral theory.

The article assumes the Fréchet algebra, the sequence of seminorms, the projective limit and the spectrum from *Locally Convex and Fréchet Algebras*, which owns the topological algebra and the spectral theory of a Fréchet algebra; the topological algebra, the submultiplicative norm and the Banach algebras from *Topological Algebras and Banach Algebras*; the involutive Banach algebra, the $\mathrm{C}^*$-identity and the Hermitian elements from *Involutive Banach Algebras and the Gelfand–Naimark Theorem* and *Hermitian and Self-Adjoint Elements of a Banach Algebra*; the continuous involution and the fixed and skew parts from *Involutive Topological Linear Algebras*; and the abstract involution from *Involutive Linear Algebras*. The grade involution $\alpha$ of the signed block is not used.

Throughout, $A$ is a unital commutative-compatible associative Fréchet algebra over $\mathbb{C}$ with a countable increasing family of submultiplicative seminorms $(p_n)_{n\geq0}$ defining the topology, $p_0 \leq p_1 \leq \cdots$, and with a **continuous involution** $a \mapsto a^*$; $A_n = A/\ker p_n$ is the Banach algebra completion of the quotient and $A \cong \varprojlim_n A_n$; $\sigma(a)$ is the spectrum, the complement of the set of $\lambda$ for which $a - \lambda$ is invertible; $A^+ = \{a : a^* = a\}$ is the Hermitian part; and an **A*-algebra** is an involutive Fréchet algebra in which the Hermitian elements are real and span the algebra.

## The Involution and the Seminorms

**Definition.** An **involutive Fréchet algebra** is a Fréchet algebra $A$ with an involution $a \mapsto a^*$, $(ab)^* = b^*a^*$, $(\lambda a)^* = \bar\lambda a^*$, $a^{**} = a$, that is **continuous** for the Fréchet topology. A morphism is a continuous unital $*$-homomorphism.

**Proposition (continuity of the involution and the seminorms).** The involution of an involutive Fréchet algebra is continuous if and only if for every $n$

$$
p_n(a^*) \leq C_n\,p_m(a) \qquad (a \in A)
$$

for some $m = m(n)$ and some constant $C_n$. In that case the involution is a homeomorphism, it is an isomorphism of the topological algebra onto its topological opposite, and it descends to each quotient $A_n$ and to the limit.

**Proof.** The continuity of a linear map of a Fréchet space is the existence, for every continuous seminorm $p_n$, of a continuous seminorm $p_m$ and a constant $C_n$ with $p_n(\sigma(a)) \leq C_n p_m(a)$; the seminorms $p_m$ generate the topology, giving the criterion. An involutive homeomorphism is its own inverse, and the conjugate-linear anti-automorphism descends to the quotient because the kernel of $p_n$ is stable under $\sigma$ when $p_n$ is $\sigma$-subordinate to a $p_m$ for the reverse inequality also holds by symmetry. $\square$

**Example (a discontinuous involution).** Let $A = C^\infty(\mathbb{R})$ and let $\varphi : C^\infty(\mathbb{R}) \to C^\infty(\mathbb{R})$ be a discontinuous derivation composed with the identity; the map $f \mapsto \overline{f} + \varphi(f)$ is a linear involution that is not continuous for the Fréchet topology. The example shows that continuity is a genuine hypothesis and not a consequence of the algebra structure.

## The Fréchet *-Algebras as Projective Limits

**Theorem (the projective limit description).** Let $A$ be an involutive Fréchet algebra. Then each quotient $A_n = A/\ker p_n$ is a normed (and, completed, Banach) $*$-algebra, and

$$
A \;\cong\; \varprojlim_n A_n
$$

is the projective limit of the Banach $*$-algebras $A_n$ along the continuous unital $*$-homomorphisms $A_{n} \to A_{m}$ for $m \leq n$. Conversely the projective limit of a countable system of Banach $*$-algebras with continuous connecting $*$-homomorphisms is an involutive Fréchet algebra.

**Proof.** The kernel $\ker p_n$ is a closed two-sided ideal stable under the involution, so the quotient is a normed $*$-algebra and its completion a Banach $*$-algebra; the quotients are linked by the natural maps and the algebra is their projective limit by the standard description of a Fréchet space as the limit of its seminorm quotients. The converse is the standard construction of a Fréchet topology from a countable projective system of Banach spaces, with the involution defined componentwise. $\square$

**Theorem (the m-convex case and the spectrum).** If the seminorms $p_n$ are submultiplicative and the algebra is **m-convex**, then $A$ is a projective limit of Banach algebras and the spectrum of an element is the set of $\lambda$ with $a - \lambda$ non-invertible; for each $n$ the spectrum of the image $\pi_n(a)$ in $A_n$ contains $\sigma(a)$, and

$$
\sigma(a) = \bigcup_n \sigma_{A_n}\bigl(\pi_n(a)\bigr) ,
$$

a compact subset of $\mathbb{C}$. The involution moves the spectrum by conjugation, $\sigma(a^*) = \overline{\sigma(a)}$, and the Hermitian elements are those with real spectrum in the $A_n$.

**Proof.** The spectrum of $a$ is the complement of the invertible set, mapped onto the sets of inverses of the $\sigma_{A_n}(\pi_n(a))$; the union description and compactness are standard for a Fréchet algebra, and the conjugation of the spectrum is the involution order two argument as in the Banach case. A Hermitian element has Hermitian image in each $A_n$, hence real spectrum in each, hence in $A$. $\square$

## The Spectral Geometry

**Definition.** Let $A$ be an involutive Fréchet algebra. The **Hermitian part** is $A^+ = \{a : a^* = a\}$, and the **skew part** $A^-$; the **spectrum** $\Sigma(A)$ is the space of continuous characters, and an involution is **Hermitian** when every Hermitian element has real image in each $\sigma_{A_n}$, and **A*** when, in addition, $A^+$ spans $A$ over $\mathbb{C}$.

**Proposition (Hermitian involutions and real spectra).** An involution is Hermitian if and only if every self-adjoint element has real spectrum; it is then continuous when the topology is m-convex. For an A*-algebra the self-adjoint part $A^+$ is a real Fréchet space with $A = A^+ \oplus iA^+$, and the algebra is the complexification of its Hermitian part.

**Proof.** Hermitian means real images in every quotient; real images for all self-adjoint elements is real spectrum for every quotient; conversely real spectrum forces the Hermitian part real. The continuity under m-convexity is the standard automatic-continuity statement for a Hermitian involution on an m-convex Fréchet algebra. The decomposition is the real-form statement extended to the Fréchet case. $\square$

## Examples

**Example (the smooth functions).** Let $A = C^\infty(X)$ for a smooth compact manifold $X$, with the family of seminorms $p_\alpha(f) = \sup_X\lvert\partial^\alpha f\rvert$; the involution $f \mapsto \bar f$ is continuous, the algebra is the projective limit of the Banach algebras $C^k(X)$, and the Hermitian elements are the real-valued smooth functions.

**Example (the holomorphic functions).** Let $A = \mathcal{O}(\Omega)$ be the algebra of holomorphic functions on an open $\Omega \subseteq \mathbb{C}$ with the topology of compact convergence, and the involution $f \mapsto f^*$ with $f^*(z) = \overline{f(\bar z)}$. It is an involutive Fréchet algebra; the projective limit is over the Banach algebras of functions continuous on $\bar K$ and holomorphic on $K$ for the compact $K \subseteq \Omega$.

**Example (a nuclear Fréchet *-algebra).** The algebra $\mathcal{S}(\mathbb{R})$ of rapidly decreasing functions with convolution and the involution $f^*(t) = \overline{f(-t)}$ is an involutive Fréchet algebra. It is not a Banach algebra, it is nuclear and m-convex, and its spectrum is the real line; the Fourier transform exchanges the convolution with the multiplication and turns the involution into conjugation, and the algebra is the base of the nuclear spectral theory.

## Automatic Continuity and the Hermitian Involution

**Theorem (automatic continuity, cited).** Let $A$ be an m-convex Fréchet `*`-algebra whose involution is **Hermitian**, that is every self-adjoint element has real image in each Banach quotient $A_n$. Then the involution is automatically continuous; the result is standard for m-convex Fréchet `*`-algebras (Bhatt–Karia) and rests on the real spectra rather than on the continuity hypothesis.

**Theorem (characters and the Gelfand transform).** For a commutative Hermitian involutive Fréchet algebra every character $\chi$ is a `*`-homomorphism, $\chi(a^*) = \overline{\chi(a)}$, because the self-adjoint elements have real images and every element is $h + ik$ with $h,k$ self-adjoint; hence the Gelfand transform is a `*`-homomorphism onto a subalgebra of $C(\Sigma(A))$, where $\Sigma(A)$ is the spectrum of continuous characters, and it is injective when the quotients $A_n$ are semisimple. The Fréchet topology and the Gelfand theory are *Locally Convex and Fréchet Algebras*.

**Proposition (comparison with the Banach case).** A Banach `*`-algebra is the special case of an involutive Fréchet algebra whose topology is defined by a single norm, $A_n = A$ for all $n$; the union-of-spectra formula then reproduces the Banach spectrum of *Involutive Banach Algebras and the Gelfand–Naimark Theorem*, and the Hermitian involutions include the $\mathrm{C}^*$-involutions.

## Summary

An involutive Fréchet algebra is a complete metrisable locally convex algebra with a continuous involution, the continuity of the involution being the condition $p_n(a^*) \leq C_n p_m(a)$ for a suitable $m$; it is the projective limit of the Banach $*$-algebras $A_n = A/\ker p_n$, and conversely a countable projective limit of Banach $*$-algebras is an involutive Fréchet algebra. The spectrum of an element is the union of its spectra in the quotients, so it is a compact subset of $\mathbb{C}$, and the involution moves it by conjugation, $\sigma(a^*) = \overline{\sigma(a)}$; a Hermitian involution is one for which every self-adjoint element has real spectrum in each quotient, and an A*-algebra is one whose Hermitian part spans the algebra and is its real form. The Fréchet topology and the spectral theory of the algebra without the involution are *Locally Convex and Fréchet Algebras*; the Banach case is the earlier theory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$, $(p_n)$, $A_n = A/\ker p_n$ | Fréchet algebra, seminorms, quotient Banach algebras |
| $a \mapsto a^*$ | Continuous involution |
| $p_n(a^*) \leq C_n p_m(a)$ | Criterion for the continuity of the involution |
| $A \cong \varprojlim_n A_n$ | Projective limit description |
| $\sigma(a)$, $\sigma_{A_n}(\pi_n(a))$ | Spectra in the algebra and the quotients |
| $\sigma(a) = \bigcup_n\sigma_{A_n}(\pi_n(a))$ | The spectrum as a union |
| $A^+$, $A^-$ | Hermitian and skew parts |
| Hermitian / A* involution | Real spectra; Hermitian part spans |
| $\chi(a^*) = \overline{\chi(a)}$ | Characters are `*`-homomorphisms (Hermitian case) |

## Further Reading

- Alexandre Grothendieck, *Topological Vector Spaces* (Gordon and Breach, 1973), for the Fréchet spaces and the projective limits.
- Lucien Waelbroeck, *Topological Vector Spaces and Algebras*, Lecture Notes in Mathematics 230 (Springer, 1971), for the Fréchet algebras and their spectral theory.
- Theodore W. Palmer, *Banach Algebras and the General Theory of ${}^*$-Algebras, Volume II* (Cambridge University Press, 2001), for the involutive topological algebras and the continuous involutions.
- S. J. Bhatt and D. J. Karia, "Uniqueness of the topology on a topological algebra", *Proceedings of the American Mathematical Society* 143 (2015), for the continuity hypotheses on the involutions of Fréchet algebras.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the comparison with the Banach and $\mathrm{C}^*$ cases.
