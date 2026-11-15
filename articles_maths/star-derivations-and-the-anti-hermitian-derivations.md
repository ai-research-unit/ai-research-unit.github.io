
# __Star-Derivations and the Anti-Hermitian Derivations__

## Introduction

A derivation of a ring is an additive map satisfying the Leibniz rule, and on a ring with an involution it is natural to ask how the derivation interacts with the involution. Two classes arise: the **star-derivations**, also called **$\sigma$-derivations** or *-derivations, which commute with the involution, and the **anti-Hermitian derivations**, which anticommute with it. Every derivation splits into a star part and an anti-Hermitian part when $2$ is invertible, the star-derivations preserve the symmetric and the anti-Hermitian elements while the anti-Hermitian derivations exchange them, and the inner derivations $D_a(x) = ax-xa$ realise the Lie structure: $D_a$ is a star-derivation exactly when $a+\sigma(a)$ is central and an anti-Hermitian derivation exactly when $a-\sigma(a)$ is central, so the inner derivations see the symmetric and anti-Hermitian elements through the commutator.

This article defines the two classes, proves the decomposition, computes the action on the symmetric and the anti-Hermitian elements, and derives the Lie structure of the inner derivations and its restriction to the anti-Hermitian elements. It assumes *Derivations of a Ring* for the Leibniz rule and the inner derivations, *Involutive Rings* for the involution and *The Skew Field of a Ring with Involution* for the symmetric and anti-Hermitian elements; the Lie algebra of the derivations is named from the later category and used only through the identity $[D_a,D_b] = D_{[a,b]}$. Throughout, $A$ is a ring with $1 \neq 0$ and an involution $\sigma$, $2$ is invertible when the decompositions are used, $\operatorname{Der}(A)$ is the Lie algebra of the derivations with $[D,E] = DE-ED$, and $\mathrm{sym}$, $\mathrm{Skew}$ are the symmetric and anti-Hermitian elements.

## The Two Classes

**Definition.** A **$\sigma$-derivation** is an additive map $\delta : A\to A$ with

$$
\boxed{\;\delta(ab) = \delta(a)\,b + \sigma(a)\,\delta(b) \qquad \text{for all } a, b \in A\;} ;
$$

when $\sigma = \mathrm{id}$ this is a derivation. A derivation $D$ is a **star-derivation** when

$$
D(\sigma(a)) = \sigma(D(a)) \quad \text{for all } a, \qquad \text{that is } D\sigma = \sigma D,
$$

and a **anti-Hermitian derivation** when

$$
D(\sigma(a)) = -\sigma(D(a)) \quad \text{for all } a, \qquad \text{that is } D\sigma = -\sigma D .
$$

**Proposition (the decomposition).** A derivation $D$ is a star-derivation exactly when $\sigma D\sigma = D$, and an anti-Hermitian derivation exactly when $\sigma D\sigma = -D$, where $\sigma D\sigma$ is the conjugate derivation $a \mapsto \sigma(D(\sigma(a)))$. Every derivation decomposes uniquely as

$$
\boxed{\;D = D_+ + D_-, \qquad D_+ = \tfrac12(D+\sigma D\sigma), \quad D_- = \tfrac12(D-\sigma D\sigma)\;},
$$

with $D_+$ a star-derivation and $D_-$ an anti-Hermitian derivation.

**Proof.** $\sigma D\sigma$ is additive and satisfies the Leibniz rule because $\sigma$ is an anti-automorphism: $\sigma D\sigma(ab) = \sigma D(\sigma(b)\sigma(a)) = \sigma(D\sigma(b)\sigma(a)+\sigma(b)D\sigma(a)) = \sigma(D\sigma(b))\,\sigma(\sigma(a))+\sigma(\sigma(b))\,\sigma(D\sigma(a)) = \sigma D\sigma(b)\,a + b\,\sigma D\sigma(a)$. A derivation $D$ commutes with $\sigma$ exactly when $\sigma D\sigma = D$ and anticommutes exactly when $\sigma D\sigma = -D$; the two projections are computations with $\sigma D\sigma$ and $\sigma^2 = \mathrm{id}$, and uniqueness is the invertibility of $2$.

**Proposition (action on the eigenspaces).** A star-derivation preserves $\mathrm{sym}$ and $\mathrm{Skew}$; an anti-Hermitian derivation exchanges them, $D(\mathrm{sym})\subseteq\mathrm{Skew}$ and $D(\mathrm{Skew})\subseteq\mathrm{sym}$.

**Proof.** For a star-derivation and $a \in \mathrm{sym}$, $\sigma(D(a)) = D(\sigma(a)) = D(a)$; for $a\in\mathrm{Skew}$, $\sigma(D(a)) = D(-a) = -D(a)$. For an anti-Hermitian derivation and $a\in\mathrm{sym}$, $\sigma(D(a)) = -D(\sigma(a)) = -D(a)$; and for $a\in\mathrm{Skew}$, $\sigma(D(a)) = -D(-a) = D(a)$.

## The Inner Derivations

**Theorem.** For $a \in A$ let $D_a$ be the inner derivation $D_a(x) = ax-xa$. Then $D_a$ is a star-derivation exactly when $a+\sigma(a)$ is central, and an anti-Hermitian derivation exactly when $a-\sigma(a)$ is central:

$$
\boxed{\;D_a\sigma = \sigma D_a \iff a+\sigma(a)\in Z(A), \qquad D_a\sigma = -\sigma D_a \iff a-\sigma(a)\in Z(A)\;}.
$$

In particular a central element gives the zero derivation, a **symmetric** element gives a **antisymmetric** derivation, and a **antisymmetric** element gives a **star**-derivation; for a central element both conditions hold and $D_a = 0$.

**Proof.** $\sigma(D_a x) = \sigma(ax-xa) = \sigma(x)\sigma(a)-\sigma(a)\sigma(x)$ and $D_a(\sigma(x)) = a\sigma(x)-\sigma(x)a$. The two agree for all $x$ exactly when $\sigma(x)\sigma(a)+a \sigma(x) = \sigma(a)\sigma(x)+\sigma(x)a$ for all $x$ — the transposition of the equality $\sigma(x)(\sigma(a)+a) = (a+\sigma(a))\sigma(x)$ for all $x$ — which is the centrality of $a+\sigma(a)$. The anti-Hermitian case is the same computation with the sign.

**Theorem (the Lie structure).** The inner derivations form a Lie subalgebra of $\operatorname{Der}(A)$ with $[D_a,D_b] = D_{ab-ba}$, and the assignment $a \mapsto D_a$ is a Lie algebra homomorphism $A \to \operatorname{Der}(A)$ with kernel the centre $Z(A)$, where $A$ is read with the commutator bracket. Under it the symmetric elements map to the anti-Hermitian derivations and the anti-Hermitian elements to the star-derivations, so $\mathrm{sym}(A,\sigma)/(\mathrm{sym}\cap Z)$ embeds as a Lie subalgebra of the anti-Hermitian derivations and $\mathrm{Skew}(A,\sigma)/(\mathrm{Skew}\cap Z)$ as a Lie subalgebra of the star-derivations.

**Proof.** $[D_a,D_b](x) = D_a(D_bx)-D_b(D_ax) = D_{ab-ba}(x)$ by the direct computation $a(bx-xb)-(bx-xb)a-b(ax-xa)+(ax-xa)b = (ab-ba)x-x(ab-ba)$. The kernel of $a\mapsto D_a$ is the centre, because $D_a = 0$ means $a$ commutes with every element. The image classes are those of the previous theorem: a symmetric element $a$ has $a-\sigma(a) = 0$ and so gives an anti-Hermitian derivation, an anti-Hermitian element gives a star-derivation, and in the quotients by the central elements the conditions are the stated ones; the homomorphism property carries the commutator to the commutator, so the images of the two Lie subalgebras are Lie subalgebras of the corresponding classes.

**Corollary (the graded Lie structure).** Under the parity star $= $ even, anti-Hermitian $=$ odd, the commutator satisfies $[\mathrm{star},\mathrm{star}]\subseteq\mathrm{star}$, $[\mathrm{star},\mathrm{anti}]\subseteq\mathrm{anti}$ and $[\mathrm{anti},\mathrm{anti}]\subseteq\mathrm{star}$; the star-derivations form a Lie subalgebra of $\operatorname{Der}(A)$, the anti-Hermitian derivations a module over it, and the commutator of two anti-Hermitian derivations is a star-derivation.

**Proof.** For star $D, E$ one has $[\sigma D\sigma,\sigma E\sigma] = [D,E]$; for star $D$ and anti-Hermitian $E$, $[\sigma D\sigma,\sigma E\sigma] = [D,-E] = -[D,E]$; for anti-Hermitian $D,E$, $[\sigma D\sigma,\sigma E\sigma] = [-D,-E] = [D,E]$. These are the three cases, and the closure of the star-derivations is the first.

## Examples

**(a) The matrix transpose.** $A = M_n(R)$ with the transpose; the inner derivation $D_X$ is a star-derivation exactly when $X+X^{\mathrm t}$ is a scalar matrix and an anti-Hermitian derivation exactly when $X-X^{\mathrm t}$ is scalar. The symmetric matrices therefore give anti-Hermitian derivations and the antisymmetric matrices give star-derivations, and the derivations of the matrix ring are all inner by the matrix case of *Derivations of a Ring*.

**(b) The quaternion conjugation.** For the quaternion algebra with $D_x(y)=xy-yx$, a pure quaternion is an anti-Hermitian element and so gives a star-derivation, while a real scalar is symmetric and gives the zero or an anti-Hermitian derivation according as it is central; the embedding of the pure quaternions in the star-derivations is the three-dimensional Lie algebra of *The Skew Field of a Ring with Involution* read through the adjoint representation $a\mapsto D_a$.

**(c) The differential operator.** On $A = k[x]$ with the involution $\sigma(x) = -x$ and $\sigma|_k = \mathrm{id}$, the derivation $d/dx$ satisfies $D\sigma = -D$, that is it anticommutes with the involution, so it is an anti-Hermitian derivation; it exchanges the even and the odd polynomials, $\mathrm{sym} = k[x^2]$ and $\mathrm{Skew} = xk[x^2]$, exactly as in the proposition.

**(d) The zero case.** Every central element gives the zero inner derivation; the star-derivations and the anti-Hermitian derivations therefore contain the zero derivation, and the decomposition $D = D_++D_-$ is the one of a derivation into its $\sigma$-commuting and $\sigma$-anticommuting parts, the analogue for derivations of the eigenspace decomposition of an element.

## Summary

A **$\sigma$-derivation** satisfies $\delta(ab) = \delta(a)b+\sigma(a)\delta(b)$ and is a derivation when $\sigma = \mathrm{id}$; a derivation is a **star-derivation** when $D\sigma = \sigma D$ and a **anti-Hermitian derivation** when $D\sigma = -\sigma D$, and every derivation decomposes as $D = D_++D_-$ with $D_\pm = \tfrac12(D\pm\sigma D\sigma)$ when $2$ is invertible. Star-derivations preserve the symmetric and the anti-Hermitian elements, anti-Hermitian derivations exchange them, and for the inner derivation $D_a$, $D_a$ is a star-derivation exactly when $a+\sigma(a)$ is central and an anti-Hermitian derivation exactly when $a-\sigma(a)$ is central. The inner derivations obey $[D_a,D_b] = D_{ab-ba}$, so $a\mapsto D_a$ is a Lie homomorphism with kernel the centre, the anti-Hermitian elements embedding as a Lie subalgebra of the anti-Hermitian derivations and the symmetric elements as one of the star-derivations; the star-derivations are closed under the commutator, the anti-Hermitian derivations are a module over them, and the commutator of two anti-Hermitian derivations is a star-derivation, the graded Lie structure of the two classes.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\delta(ab)=\delta(a)b+\sigma(a)\delta(b)$ | $\sigma$-derivation; derivation when $\sigma=\mathrm{id}$ |
| $D\sigma=\sigma D$ | Star-derivation |
| $D\sigma=-\sigma D$ | Anti-Hermitian derivation |
| $D_\pm=\tfrac12(D\pm\sigma D\sigma)$ | Star and anti-Hermitian parts, $2$ invertible |
| $D(\mathrm{sym})\subseteq\mathrm{sym}$, $D(\mathrm{Skew})\subseteq\mathrm{Skew}$ | Star-derivation preserves the eigenspaces |
| $D(\mathrm{sym})\subseteq\mathrm{Skew}$, $D(\mathrm{Skew})\subseteq\mathrm{sym}$ | Anti-Hermitian derivation exchanges them |
| $D_a(x)=ax-xa$ | Inner derivation |
| $a+\sigma(a)\in Z$ / $a-\sigma(a)\in Z$ | $D_a$ star / anti-Hermitian |
| $[D_a,D_b]=D_{ab-ba}$ | Lie homomorphism $a\mapsto D_a$, kernel $Z(A)$ |
| $[\mathrm{star},\mathrm{anti}]\subseteq\mathrm{anti}$ | Graded Lie structure of the two classes |

## Further Reading

- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the star-derivations, the anti-Hermitian derivations and the inner derivations of a ring with involution.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the derivation algebra, the inner derivations and the Lie structure of a simple ring.
- Matej Brešar, *Introduction to Noncommutative Algebra* (Springer, 2014), for the $\sigma$-derivations, the Lie structure of the derivations and the functional identities they satisfy.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for the relation between the derivations and the involutions of a central simple algebra.
