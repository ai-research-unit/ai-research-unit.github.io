
# __Involutive Banach Algebras and the Gelfand–Naimark Theorem__

## Introduction

An **involutive Banach algebra** is a Banach algebra together with an involution, an anti-automorphism $\sigma$ of order two; a **$\mathrm{C}^*$-algebra** is an involutive Banach algebra in which the involution governs the norm through the **$\mathrm{C}^*$-identity**

$$
\lVert a^*a\rVert = \lVert a\rVert^2 .
$$

The identity is a rigidity statement: it makes the involution isometric, it makes every $*$-homomorphism contractive, and it makes the $\mathrm{C}^*$-norm unique on a given $*$-algebra. Its harvest is the **Gelfand–Naimark theorem**, which says that every $\mathrm{C}^*$-algebra is, up to an isometric $*$-isomorphism, an algebra of operators on a Hilbert space; in the commutative case the Gelfand transform is the isometric $*$-isomorphism onto the continuous functions on the spectrum, and the abstract $\mathrm{C}^*$-algebra is recovered from a compact Hausdorff space. This article develops the involutive Banach algebra and the Gelfand–Naimark theorem at the level the rest of the category needs.

This article is the base of the `- * Theory` group of *Topology on Algebras*. It assumes the Banach algebra, the submultiplicative norm, the spectrum, the spectral radius and the Gelfand duality of *Topological Algebras and Banach Algebras*; the continuous involution $\sigma$, its fixed and skew parts and the $\mathrm{C}^*$-case of *Involutive Topological Algebras*; the abstract involution, the symmetric and skew elements and the opposite algebra of *Involutive Algebras*; the bounded operators, the adjoint and the $\mathrm{C}^*$-identity of $B(H)$ from *Operator Algebras*, which owns the von Neumann algebras, the modular theory and the full representation theory; and the operator version from *Operators on a C*-Algebra*, earlier in this category. The states, the positive functionals and the GNS construction are *States and Positive Functionals on an Involutive Algebra*, the article that follows; the positivity and the order are *Hermitian and Self-Adjoint Elements of a Banach Algebra*.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$; $A$ is a unital Banach algebra over $\mathbb{C}$ with a **continuous involution** $\sigma$, written $a^* = \sigma(a)$, so that $(ab)^* = b^*a^*$, $(a+b)^* = a^*+b^*$, $(\lambda a)^* = \bar\lambda a^*$ and $a^{**} = a$; the algebra is **involutive** with or without the continuity of $\sigma$, and a **$\mathrm{C}^*$-algebra** when the $\mathrm{C}^*$-identity holds; $A^+ = \{a : a^* = a\}$ is the set of self-adjoint (Hermitian) elements and $A^-$ the skew elements; a **$*$-homomorphism** $\varphi : A \to B$ is an algebra homomorphism with $\varphi(a^*) = \varphi(a)^*$; and a **$*$-representation** is a $*$-homomorphism into $B(H)$ for a Hilbert space $H$. The grade involution $\alpha$ of the signed block is an automorphism and is not the map $\sigma$ used here.

## Involutive Banach Algebras

**Definition.** An **involutive Banach algebra** is a Banach algebra $A$ with an involution $\sigma$, an additive map of order two with $\sigma(ab) = \sigma(b)\sigma(a)$ and $\sigma(\lambda a) = \bar\lambda\sigma(a)$. It is a **$\mathrm{C}^*$-algebra** when $\lVert a^*a\rVert = \lVert a\rVert^2$ for all $a$.

**Proposition (the involution of a $\mathrm{C}^*$-algebra is isometric).** In a $\mathrm{C}^*$-algebra, $\lVert a^*\rVert = \lVert a\rVert$ for all $a$. Hence the involution is continuous, with $\lVert\sigma\rVert = 1$.

**Proof.** $\lVert a\rVert^2 = \lVert a^*a\rVert \leq \lVert a^*\rVert\lVert a\rVert$, so $\lVert a\rVert \leq \lVert a^*\rVert$; replacing $a$ by $a^*$ and using $a^{**} = a$ gives the reverse, so the two norms are equal, and $\lVert\sigma\rVert = 1$ by definition of the operator norm. $\square$

**Proposition ($*$-homomorphisms are contractive).** A unital $*$-homomorphism $\varphi : A \to B$ of unital $\mathrm{C}^*$-algebras is contractive, $\lVert\varphi(a)\rVert \leq \lVert a\rVert$, and isometric on the positive elements. A $*$-homomorphism of $\mathrm{C}^*$-algebras is continuous.

**Proof.** For a self-adjoint $a$ the spectrum is real and $\sigma(\varphi(a)) \subseteq \sigma(a)$, so $r(\varphi(a)) \leq r(a) = \lVert a\rVert$; for arbitrary $a$ apply this to $a^*a$, noting $\varphi(a^*a) = \varphi(a)^*\varphi(a)$ is self-adjoint: $\lVert\varphi(a)\rVert^2 = \lVert\varphi(a)^*\varphi(a)\rVert = r(\varphi(a)^*\varphi(a)) \leq r(a^*a) = \lVert a\rVert^2$, using the $\mathrm{C}^*$-identity and the spectral radius formula. $\square$

**Theorem (uniqueness of the $\mathrm{C}^*$-norm).** A $*$-algebra carries at most one $\mathrm{C}^*$-norm, and every $*$-isomorphism of $\mathrm{C}^*$-algebras is isometric.

**Proof.** In a $\mathrm{C}^*$-algebra the norm is determined by the algebraic and involutive structure through $\lVert a\rVert^2 = \lVert a^*a\rVert = r(a^*a)$, the spectral radius being defined by invertibility in the $*$-algebra; two $\mathrm{C}^*$-norms on the same $*$-algebra thus agree. A $*$-isomorphism is an isometry by the same formula applied on both sides. $\square$

## The Gelfand–Naimark Theorem

**Theorem (Gelfand–Naimark).** Every $\mathrm{C}^*$-algebra $A$ admits a faithful isometric $*$-representation $\pi : A \to B(H)$ on a Hilbert space $H$; equivalently, $A$ is isometrically $*$-isomorphic to a closed $*$-subalgebra of $B(H)$. In particular $A$ is semisimple.

**Proof (sketch).** The states of $A$ separate the points, and the GNS construction attaches to each state a cyclic $*$-representation whose vector is cyclic; the direct sum of these representations over the states is a $*$-representation, and it is faithful and isometric because for $a \neq 0$ some state reaches $\lVert a\rVert$ on $a^*a$. The construction of the states and of the GNS representation is *States and Positive Functionals on an Involutive Algebra*; the identification of the norm of the image with that of $A$ uses the $\mathrm{C}^*$-identity and the isometry of the involution. $\square$

**Theorem (commutative Gelfand–Naimark).** Let $A$ be a commutative unital $\mathrm{C}^*$-algebra. Then the Gelfand transform $a \mapsto \hat a$ is an isometric $*$-isomorphism onto $C(\operatorname{Max}(A))$, and the assignment $A \mapsto \operatorname{Max}(A)$ is a contravariant equivalence between commutative unital $\mathrm{C}^*$-algebras and compact Hausdorff spaces.

**Proof.** For a character $\chi$ of a $\mathrm{C}^*$-algebra one has $\chi(a^*) = \overline{\chi(a)}$, because $a = h + ik$ with $h,k$ self-adjoint and $\chi(h), \chi(k)$ real; the transform is therefore a $*$-homomorphism. The $\mathrm{C}^*$-identity gives $\lVert\hat a\rVert_\infty^2 = \sup\lvert\chi(a)\rvert^2 = \sup\chi(a^*a) = r(a^*a) = \lVert a\rVert^2$, using the spectral radius formula for the self-adjoint element $a^*a$; hence the transform is isometric, its image is a closed $*$-subalgebra separating points and containing the constants, and it is all of $C(\operatorname{Max}(A))$ by the Stone–Weierstrass theorem. The equivalence is the functoriality of the construction, a unital $*$-homomorphism inducing the continuous map of the spectra by composition. $\square$

## The Spectrum and the Involution

**Proposition (the spectrum of the image).** A unital $*$-homomorphism $\varphi : A \to B$ of $\mathrm{C}^*$-algebras satisfies $\sigma(\varphi(a)) \subseteq \sigma(a)$ and $\lVert\varphi(a)\rVert \leq \lVert a\rVert$; for an injective $\varphi$ the spectra agree. A self-adjoint element has real spectrum and $\lVert a\rVert = r(a)$; a positive element, one of the form $b^*b$, has non-negative spectrum.

**Proof.** The containment of the spectra is the behaviour of the spectrum under a unital homomorphism; the norm inequality is the contractivity above. For self-adjoint $a$ the element $a - \lambda$ is invertible for non-real $\lambda$ by the inequality $\lVert(a-\lambda)^{-1}\rVert \leq \lvert\operatorname{Im}\lambda\rvert^{-1}$ obtained from the $\mathrm{C}^*$-identity, so the spectrum is real, and then $r(a) = \lVert a\rVert$ by Gelfand duality applied to the commutative $\mathrm{C}^*$-algebra generated by $a$. For $b^*b$ the element is self-adjoint and $\sigma(b^*b) \subseteq [0,\infty)$ because $b^*b - \lambda$ is invertible for $\lambda < 0$ by the same inequality. $\square$

**Remark (the boundary with the operator theory).** The Gelfand–Naimark representation, the states and the positivity are proved in full in *Operator Algebras*, which owns the von Neumann algebras, the bicommutant theorem, the weak and strong topologies, the factors, the traces and the modular theory. This article records the involutive Banach algebra and the embedding it needs, and does not redevelop the operator algebra.

## Examples

**Example (the continuous functions).** For a compact Hausdorff space $X$, the algebra $C(X,\mathbb{C})$ with the sup norm and the involution $\sigma(f) = \bar f$ is a commutative unital $\mathrm{C}^*$-algebra: $\lVert\bar f f\rVert_\infty = \lVert f\rVert_\infty^2$. Its Gelfand transform is the identity reading of $X = \operatorname{Max}(C(X))$.

**Example (the matrix algebra).** For $A = M_n(\mathbb{C})$ with the operator norm and the conjugate transpose $X^* = \bar X^{\mathsf{T}}$, the $\mathrm{C}^*$-identity holds because $\lVert X^*X\rVert = \lVert X\rVert^2$; the algebra is the finite-dimensional model of $B(H)$, and its $*$-representations are the unitary equivalence classes of the defining representation.

**Example ($L^1$ of a group).** The convolution algebra $L^1(G)$ of a locally compact group with the involution $f^*(x) = \overline{f(x^{-1})}\Delta(x)^{-1}$ is an involutive Banach algebra; it is a $\mathrm{C}^*$-algebra only after completing to the reduced group $\mathrm{C}^*$-algebra, and its $*$-representations are the unitary representations of $G$. The group algebra is *Group Algebras*.

## The Universal Representation and the Enveloping Algebra

**Theorem (the universal representation).** Let $A$ be a unital $\mathrm{C}^*$-algebra and $\mathcal{S}(A)$ its state space. The direct sum

$$
\pi_u = \bigoplus_{f \in \mathcal{S}(A)} \pi_f : A \longrightarrow B\Bigl(\bigoplus_{f \in \mathcal{S}(A)} H_f\Bigr)
$$

is a faithful isometric `*`-representation, the **universal representation**, and for every $a$ the norm is the supremum of the GNS norms,

$$
\lVert a\rVert = \sup_{f \in \mathcal{S}(A)} \lVert\pi_f(a)\rVert = \sup_{f \in \mathcal{S}(A)} f(a^*a)^{1/2} .
$$

**Proof.** Each $\pi_f$ is a `*`-representation by the GNS construction of *States and Positive Functionals on an Involutive Algebra*, so the direct sum is one and its norm is the supremum of the norms of the summands. For the isometry, $\lVert\pi_f(a)\rVert^2 = \lVert\pi_f(a^*a)\rVert$; the state $f$ with $f(a^*a) = \lVert a^*a\rVert$, which exists because $a^*a$ is self-adjoint, has $\langle\pi_f(a^*a)\xi_f,\xi_f\rangle = \lVert a^*a\rVert$ with $\pi_f(a^*a) \geq 0$, so $\lVert\pi_f(a^*a)\rVert \geq \lVert a^*a\rVert$ and hence $\lVert\pi_f(a^*a)\rVert = \lVert a^*a\rVert$; the supremum is therefore $\lVert a^*a\rVert = \lVert a\rVert^2$. $\square$

**Corollary (the enveloping von Neumann algebra).** The weak closure $\pi_u(A)''$ is the **enveloping von Neumann algebra** $A^{**}$ of $A$; it is the second dual of $A$ with the Arens product, and $A$ sits in it as a weakly dense $\mathrm{C}^*$-subalgebra. The algebra $A^{**}$ and its projections, weights and modular theory are *Operator Algebras* and *Involutive Operator Algebras and the Commutant*.

**Proposition (the norm is an algebraic invariant).** The universal representation shows that a unital `*`-homomorphism $\varphi : A \to B$ of unital $\mathrm{C}^*$-algebras satisfies $\lVert\varphi\rVert \leq 1$ and that an injective one is isometric, because the norm of $A$ is the supremum of the values $f(a^*a)^{1/2}$ over the states, and the states pull back under $\varphi$ when $\varphi$ is unital. This reproves the contractivity of *The Involution and the Spectral Radius* from the states rather than from the spectrum.

## Summary

An involutive Banach algebra is a Banach algebra with an anti-automorphism $\sigma$ of order two; a $\mathrm{C}^*$-algebra adds the $\mathrm{C}^*$-identity $\lVert a^*a\rVert = \lVert a\rVert^2$, which forces the involution to be isometric, $\lVert a^*\rVert = \lVert a\rVert$, and makes every $*$-homomorphism contractive, $\lVert\varphi(a)\rVert \leq \lVert a\rVert$, and every $*$-isomorphism isometric; a $*$-algebra carries at most one $\mathrm{C}^*$-norm, because $\lVert a\rVert^2 = r(a^*a)$. The Gelfand–Naimark theorem embeds every $\mathrm{C}^*$-algebra faithfully and isometrically as a closed $*$-subalgebra of $B(H)$, through the GNS representations of its states, and in the commutative case the Gelfand transform is the isometric $*$-isomorphism $A \to C(\operatorname{Max}(A))$, a contravariant equivalence with compact Hausdorff spaces. A self-adjoint element has real spectrum and $\lVert a\rVert = r(a)$, and a positive element $b^*b$ has non-negative spectrum; the von Neumann algebras and the modular theory are *Operator Algebras*. The states and the GNS construction are developed in *States and Positive Functionals on an Involutive Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$, $\lVert\cdot\rVert$ | Banach algebra, its norm |
| $a^* = \sigma(a)$ | The involution, an anti-automorphism of order two |
| $\lVert a^*a\rVert = \lVert a\rVert^2$ | The $\mathrm{C}^*$-identity |
| $A^+$, $A^-$ | Self-adjoint (Hermitian) and skew elements |
| $\varphi$, $*$-homomorphism | $\varphi(a^*) = \varphi(a)^*$ |
| $\pi : A \to B(H)$ | A $*$-representation |
| $r(a)$, $\operatorname{Max}(A)$, $\hat a$ | Spectral radius, maximal ideal space, Gelfand transform |
| $\lVert a^*\rVert = \lVert a\rVert$, $\lVert\varphi(a)\rVert \leq \lVert a\rVert$ | Isometry of the involution; contractivity |
| $\pi_u = \bigoplus_f \pi_f$, $\mathcal{S}(A)$ | The universal representation, over the state space |
| $A^{**} = \pi_u(A)''$ | The enveloping von Neumann algebra |

## Further Reading

- Jacques Dixmier, *$\mathrm{C}^*$-Algebras* (North-Holland, 1977), for the Gelfand–Naimark theorem, the states and the GNS construction.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the $\mathrm{C}^*$-algebras, the isometry of the involution and the contractivity of the $*$-homomorphisms.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the involutive Banach algebras, the spectral theory and the uniqueness of the $\mathrm{C}^*$-norm.
- Theodore W. Palmer, *Banach Algebras and the General Theory of ${}^*$-Algebras, Volume II* (Cambridge University Press, 2001), for the general theory of the involutive Banach algebras.
- Gérard J. Murphy, *$\mathrm{C}^*$-Algebras and Operator Theory* (Academic Press, 1990), for the functional calculus and the positive elements.
