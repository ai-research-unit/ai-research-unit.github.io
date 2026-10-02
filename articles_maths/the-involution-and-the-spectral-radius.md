
# __The Involution and the Spectral Radius__

## Introduction

The spectral radius of an element of a Banach algebra is the radius of the smallest disc centred at the origin that contains the spectrum, and in a $\mathrm{C}^*$-algebra the involution computes it: the $\mathrm{C}^*$-identity $\lVert a^*a\rVert = \lVert a\rVert^2$ says that $r(a^*a) = \lVert a\rVert^2$, so the norm is recovered from the spectrum of the self-adjoint element $a^*a$, and the spectral radius becomes an algebraic invariant, defined by invertibility, that determines the analytic norm. This is the source of the rigidity of the $\mathrm{C}^*$-algebras: the involution is isometric, every $*$-homomorphism is contractive, every $*$-isomorphism is isometric, and a $*$-algebra carries at most one $\mathrm{C}^*$-norm. This article gathers the identities that tie the involution to the spectral radius and derives the consequences for the maps between $\mathrm{C}^*$-algebras.

The article assumes the involutive Banach algebra, the $\mathrm{C}^*$-identity and the Gelfand–Naimark theorem from *Involutive Banach Algebras and the Gelfand–Naimark Theorem*; the reality of the spectrum, the norm formula $\lVert a\rVert = r(a)$ for a self-adjoint element and the spectral mapping from *The Spectrum of a Self-Adjoint Element* and *The Functional Calculus of a Self-Adjoint Element*; the spectral radius, the spectral radius formula and Gelfand duality from *Topological Algebras and Banach Algebras*; the positive cone and the order from *Hermitian and Self-Adjoint Elements of a Banach Algebra*; and the operator form of the identities from *Operator Algebras*. The grade involution $\alpha$ is not used.

Throughout, $A$ is a unital $\mathrm{C}^*$-algebra over $\mathbb{C}$ with involution $a \mapsto a^*$; $\sigma(a)$ is the spectrum, $r(a) = \max\{\lvert\lambda\rvert : \lambda \in \sigma(a)\}$ the spectral radius, and $r(a) = \lim_n\lVert a^n\rVert^{1/n}$ the Gelfand–Beurling formula; an element is self-adjoint, normal, positive or unitary as in the preceding articles.

## The Identities

**Theorem (the $\mathrm{C}^*$-identity and the spectral radius).** For every $a \in A$,

$$
\lVert a\rVert^2 = \lVert a^*a\rVert = r(a^*a) = r(a)^2 \;\;\text{for normal } a , \qquad \lVert a\rVert = r(a^*a)^{1/2} \;\;\text{in general} .
$$

For a normal $a$, $\lVert a\rVert = r(a)$; for a self-adjoint $a$, likewise $\lVert a\rVert = r(a)$.

**Proof.** The first equality is the $\mathrm{C}^*$-identity; $a^*a$ is self-adjoint, so $\lVert a^*a\rVert = r(a^*a)$ by *The Spectrum of a Self-Adjoint Element*; if $a$ is normal then $a^*a$ and the commuting $a$ satisfy $r(a^*a) = r(a)^2$, and $\lVert a\rVert^2 = r(a)^2$ gives $\lVert a\rVert = r(a)$. $\square$

**Proposition (the involution and the spectrum).** For every $a$,

$$
\sigma(a^*) = \overline{\sigma(a)} , \qquad r(a^*) = r(a) , \qquad r(a^*a) = r(a)^2 ,
$$

and the involution is isometric, $\lVert a^*\rVert = \lVert a\rVert$.

**Proof.** $\lambda \in \sigma(a)$ iff $\bar\lambda \in \sigma(a^*)$, because $a - \lambda$ is invertible iff $a^* - \bar\lambda = (a-\lambda)^*$ is; hence the spectra are conjugate and the spectral radii agree. For the third identity, $\lVert a^*a\rVert = \lVert a\rVert^2$ and $a^*a$ is self-adjoint, so $r(a^*a) = \lVert a\rVert^2 = r(a)^2$ read from the first identity and the spectral radius formula $r(a) \leq \lVert a\rVert$ (with equality in the normal case). The isometry of the involution is the proposition of *Involutive Banach Algebras and the Gelfand–Naimark Theorem*. $\square$

**Corollary (the radius bounds the norm, and the involution recovers the norm).** For every $a$, $r(a) \leq \lVert a\rVert$, with equality exactly for the normal elements among the elements of a $\mathrm{C}^*$-algebra; and

$$
\lVert a\rVert = r(a^*a)^{1/2} = r(aa^*)^{1/2} .
$$

**Proof.** The Gelfand–Beurling formula gives $r(a) \leq \lVert a\rVert$ for every Banach algebra element; the equality case is the theorem; the displayed identity is the $\mathrm{C}^*$-identity combined with the norm formula for the self-adjoint $a^*a$. $\square$

## Rigidity

**Theorem (the unique $\mathrm{C}^*$-norm and the isometric maps).** A $*$-algebra carries at most one $\mathrm{C}^*$-norm; every $*$-isomorphism of $\mathrm{C}^*$-algebras is isometric; and every unital $*$-homomorphism $\varphi : A \to B$ of unital $\mathrm{C}^*$-algebras is contractive, with

$$
\lVert\varphi(a)\rVert = r\bigl(\varphi(a^*a)\bigr)^{1/2} \leq r(a^*a)^{1/2} = \lVert a\rVert .
$$

An injective unital $*$-homomorphism is isometric.

**Proof.** Uniqueness: the norm is $\lVert a\rVert = r(a^*a)^{1/2}$, and the spectral radius is defined by invertibility, an algebraic notion, so two $\mathrm{C}^*$-norms on the same $*$-algebra agree; a $*$-isomorphism preserves invertibility, hence the spectral radius of $a^*a$, hence the norm. Contractivity: $\sigma(\varphi(a^*a)) \subseteq \sigma(a^*a)$ under a unital homomorphism, so $r(\varphi(a^*a)) \leq r(a^*a)$; the displayed chain follows. For an injective unital $*$-homomorphism the spectra agree by the same argument applied to the range, so the inequality is an equality. $\square$

**Corollary (the $\mathrm{C}^*$-identity characterises the $\mathrm{C}^*$-norm).** A complete norm $\lVert\cdot\rVert$ on a $*$-algebra is a $\mathrm{C}^*$-norm if and only if $\lVert a^*a\rVert = \lVert a\rVert^2$ for all $a$; among the Banach $*$-norms the $\mathrm{C}^*$-norm is the unique one with this property, and it is the smallest complete algebra $\ast$-norm in which the involution is isometric when such exists.

**Proof.** The "if" is the definition; the uniqueness is the theorem; the last statement is the standard comparison of a $\mathrm{C}^*$-norm with an isometric Banach $*$-norm. $\square$

## Examples

**Example (the Hermitian matrix).** For $A = M_n(\mathbb{C})$ with the operator norm, $\lVert X\rVert^2 = \lVert X^*X\rVert = r(X^*X) = \max_i\lvert\lambda_i(X^*X)\rvert$, the largest singular value squared; for a normal $X$ this is $r(X)^2 = \max_i\lvert\lambda_i(X)\rvert^2$. The identity is the operator-norm statement that the norm of a matrix is its largest singular value.

**Example (the continuous functions).** For $A = C(X,\mathbb{C})$ the norm is $\lVert f\rVert_\infty = r(f)$, and the involution is isometric: $\lVert\bar f\rVert_\infty = \lVert f\rVert_\infty$. The spectral radius is the sup norm, and the $\mathrm{C}^*$-identity is the pointwise identity $\lvert\bar ff\rvert = \lvert f\rvert^2$.

**Example (the convolution algebra).** For $A = L^1(\mathbb{R})$ with the convolution product and the involution $f^*(t) = \overline{f(-t)}$, the involution is not isometric for the $L^1$-norm, $\lVert f^*\rVert_1 = \lVert f\rVert_1$ is true but the norm is not a $\mathrm{C}^*$-norm, since the $\mathrm{C}^*$-identity fails; the $\mathrm{C}^*$-envelope is the reduced $\mathrm{C}^*$-algebra of $\mathbb{R}$, on which the $\mathrm{C}^*$-identity holds.

## The Involution and the Banach *-Norms

**Proposition (comparison of the norms).** Let $A$ be a $*$-algebra carrying a $\mathrm{C}^*$-norm $\lVert\cdot\rVert$ and a complete algebra `*`-norm $\lvert\cdot\rvert$ for which the involution is isometric. Then

$$
\lVert a\rVert \leq \lvert a\rvert \qquad (a \in A) ,
$$

so the $\mathrm{C}^*$-norm is the smallest complete algebra `*`-norm with an isometric involution; the identity map from $(A,\lvert\cdot\rvert)$ to $(A,\lVert\cdot\rVert)$ has closed graph and is therefore bounded.

**Proof.** Both norms make the algebra operations continuous, and the $\mathrm{C}^*$-norm is determined by the spectral radius, $\lVert a\rVert^2 = r(a^*a)$, which is computed from the invertibility of the elements $a^*a - \lambda$, a `*`-algebraic condition continuous for the norm $\lvert\cdot\rvert$; hence the identity has closed graph and is bounded. $\square$

**Proposition (the spectral radius is not subadditive).** On a $\mathrm{C}^*$-algebra the spectral radius is not a seminorm: for

$$
a = \begin{pmatrix}0 & 1\\ 0 & 0\end{pmatrix} , \qquad b = \begin{pmatrix}0 & 0\\ 1 & 0\end{pmatrix} ,
$$

one has $r(a) = r(b) = 0$ while $a + b = \begin{pmatrix}0&1\\1&0\end{pmatrix}$ has eigenvalues $\pm1$ and $r(a+b) = 1 > r(a) + r(b)$. The radius is nevertheless a norm on the normal elements, where $\lVert a\rVert = r(a)$.

**Proof.** The matrices are nilpotent, so $r(a) = r(b) = 0$; their sum is the symmetry exchanging the coordinates, with eigenvalues $\pm1$, so $r(a+b) = 1$. The last statement is the normal-element theorem. $\square$

## Summary

In a $\mathrm{C}^*$-algebra the involution computes the spectral radius: $\lVert a^*a\rVert = r(a^*a) = \lVert a\rVert^2$, so $\lVert a\rVert = r(a^*a)^{1/2}$, and for a normal (in particular self-adjoint) element $\lVert a\rVert = r(a)$. The involution moves the spectrum by conjugation, $\sigma(a^*) = \overline{\sigma(a)}$, it preserves the spectral radius, $r(a^*) = r(a)$, and $r(a^*a) = r(a)^2$. These identities make the norm algebraic: a $*$-algebra carries at most one $\mathrm{C}^*$-norm, every $*$-isomorphism is isometric, and every unital $*$-homomorphism is contractive with $\lVert\varphi(a)\rVert^2 = r(\varphi(a^*a)) \leq r(a^*a) = \lVert a\rVert^2$, an injective one isometrically. The $\mathrm{C}^*$-identity thus characterises the $\mathrm{C}^*$-norm among the Banach $*$-norms. The positivity and the order are *Hermitian and Self-Adjoint Elements of a Banach Algebra*, and the operator formulation is *Operator Algebras*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\lVert a^*a\rVert = \lVert a\rVert^2$ | The $\mathrm{C}^*$-identity |
| $r(a) = \lim\lVert a^n\rVert^{1/n}$ | Gelfand–Beurling formula |
| $\lVert a\rVert = r(a^*a)^{1/2}$ | Norm recovered from the involution |
| $\lVert a\rVert = r(a)$ | Normal (self-adjoint) case |
| $\sigma(a^*) = \overline{\sigma(a)}$, $r(a^*) = r(a)$ | Involution and spectrum |
| $\lVert\varphi(a)\rVert \leq \lVert a\rVert$ | Contractivity of a unital $*$-homomorphism |
| Unique $\mathrm{C}^*$-norm | At most one such norm on a $*$-algebra |
| $\lVert a\rVert \leq \lvert a\rvert$ | C*-norm smallest complete isometric `*`-norm |
| $r$ not subadditive | $r(a+b) > r(a)+r(b)$ in $M_2(\mathbb{C})$ |

## Further Reading

- Gérard J. Murphy, *$\mathrm{C}^*$-Algebras and Operator Theory* (Academic Press, 1990), for the $\mathrm{C}^*$-identity, the spectral radius and the contractivity of the $*$-homomorphisms.
- Jacques Dixmier, *$\mathrm{C}^*$-Algebras* (North-Holland, 1977), for the uniqueness of the $\mathrm{C}^*$-norm and the isometric $*$-isomorphisms.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the spectral radius identity and the uniqueness of the $\mathrm{C}^*$-norm.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the operator form of the identities and the isometry of the involution.
- Theodore W. Palmer, *Banach Algebras and the General Theory of ${}^*$-Algebras, Volume II* (Cambridge University Press, 2001), for the general comparison of the Banach $*$-norms.
