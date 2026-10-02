# __The Graded Adjoint Action on a Module over a Hilbert Space__

## Introduction

A graded action of the graded algebra $B(H)$ on a graded Hilbert space $M$ is a bounded homomorphism $\rho:B(H)\to B(M)$ that raises the degree, $\rho(B(H)^i)M^j\subseteq M^{i+j}$. Its **adjoint action** is the map $\rho^\vee(T)=\rho(T)^*$ obtained by taking the Hilbert adjoint of each acting operator, and the two facts that organise its theory are that the adjoint reverses the product and that it preserves the degree. The first makes $\rho^\vee$ a homomorphism not of $B(H)$ but of the opposite algebra $B(H)^{\mathrm{op}}$, with the opposite multiplication $S\cdot T=TS$; the second makes it a *graded* action of that opposite algebra, so the sign rule of the graded commutator is inherited with the reversed order, and the sign that appears is the sign of the opposite grading. When the graded action is a $*$-representation, that is, when it intertwines the involution of $B(H)$ with the adjoint of $B(M)$, the adjoint action is the action itself composed with the involution; this agreement is the point at which the involution on the elements and the adjoint on the operators coincide, and it is proved here rather than assumed. The article is the module-level reading of the adjoint of the signed operators: the adjoint of the signed left multiplication is a signed left multiplication, the adjoint of the signed sandwich is a signed sandwich, and the adjoint of the graded action is a graded action of the opposite algebra.

This article fixes the graded action and its adjoint, the adjoint action of the opposite graded algebra, the sign reversal of the graded commutator, the compatibility of the adjoint action with the grading and the parity operators, and the $*$-representation case in which the two actions agree. The graded action, the graded module and the sign rule are *The Graded Action on a Module over a Hilbert Space*; the adjoint of the one-sided and two-sided signed operators is *The Adjoint of the Left Multiplication on a Hilbert Space*, *The Signed Adjoint of the Left Multiplication on a Hilbert Space* and *The Signed Adjoint Sandwich on a Hilbert Space*; the abstract graded module and its opposite are *The Graded Action on a Module over a Graded Algebra* (Part II); the $*$-representations of $B(H)$ are *Bounded Operators on a Hilbert Space*.

Throughout, $H=H^0\oplus H^1$ and $M=M^0\oplus M^1$ are graded Hilbert spaces over $\mathbb{K}=\mathbb{R}$ or $\mathbb{C}$ with parity operators $\Gamma_H$ and $\Gamma_M$, the graded algebra is $B(H)=B(H)^0\oplus B(H)^1$ with grade involution $\alpha(T)=\Gamma_HT\Gamma_H$, and $\rho:B(H)\to B(M)$ is a bounded graded action. The **adjoint action** is $\rho^\vee(T)=\rho(T)^*$, $A^{\mathrm{op}}$ is the algebra with the reversed product $S\cdot T=TS$, and $|T|\in\mathbb{Z}/2$ is the degree.

## The Graded Action and Its Adjoint

**Proposition (the adjoint action is a homomorphism of the opposite algebra).** The assignment $\rho^\vee(T)=\rho(T)^*$ is bounded linear, is unital, and satisfies

$$
\rho^\vee(S\cdot T)=\rho^\vee(S)\rho^\vee(T),\qquad\text{that is}\qquad \rho(ST)^*=\rho(T)^*\rho(S)^* ,
$$

so $\rho^\vee$ is a representation of the opposite algebra $B(H)^{\mathrm{op}}$, not of $B(H)$; it is injective exactly when $\rho$ is, and it is isometric with $\|\rho^\vee(T)\|=\|\rho(T)\|$.

*Proof.* The adjoint is conjugate-linear over $\mathbb{C}$, hence $\mathbb{R}$-linear, and $(\rho(ST))^*=(\rho(S)\rho(T))^*=\rho(T)^*\rho(S)^*$ is the reversal of the product; the norm identity is $\|T^*\|=\|T\|$; unitality is $\rho(I)^*=\mathrm{id}_M^*=\mathrm{id}_M$.

**Proposition (compatibility with the grading).** If $T\in B(H)^i$ is homogeneous of degree $i$ then $\rho^\vee(T)=\rho(T)^*$ is homogeneous of degree $i$ in $B(M)$, and

$$
\Gamma_M\rho^\vee(T)\Gamma_M=(-1)^i\rho^\vee(T);
$$

consequently the adjoint action preserves each graded piece of the module in the graded sense, $\rho^\vee(T)M^j\subseteq M^{i+j}$, exactly as the action does.

*Proof.* For a homogeneous $T$ one has $\rho(T)\Gamma_M=(-1)^i\Gamma_M\rho(T)$ from the graded action, and taking adjoints while using $\Gamma_M=\Gamma_M^*$ and $\Gamma_M^2=I$ gives $\Gamma_M\rho(T)^*=(-1)^i\rho(T)^*\Gamma_M$; multiplying by $\Gamma_M$ on the right converts this into the displayed form, and the piece statement is the definition of homogeneity.

**Corollary (the parity operators intertwine the adjoint action).** The adjoint action intertwines the parity operators in the same way as the action,

$$
\rho^\vee(T)\Gamma_M=(-1)^{|T|}\Gamma_M\rho^\vee(T)\quad\text{on homogeneous }T,
$$

so the even part of the adjoint action preserves each graded piece and its odd part exchanges them; the adjoint action is graded with the same degree map as the action.

*Proof.* The intertwining identity is the previous proposition rearranged; the preservation statements are the two cases $i=0$ and $i=1$, and the degree map is the additivity of the degree that defines a graded action.

## The Sign Rule and the Sign Reversal

**Definition.** For homogeneous $S,T$ of the opposite algebra the **opposite graded commutator** is

$$
[S,T]^{\mathrm{op}}_{\mathrm{gr}}=S\cdot T-(-1)^{|S||T|}T\cdot S=TS-(-1)^{|S||T|}ST=[T,S]_{\mathrm{gr}} ,
$$

so the graded commutator of the opposite algebra is the graded commutator of the algebra with the two arguments exchanged.

**Theorem (the adjoint action preserves the opposite sign rule).** Let $\rho$ be a graded action. Then for homogeneous $S,T$,

$$
\rho^\vee\bigl([S,T]^{\mathrm{op}}_{\mathrm{gr}}\bigr)=[\rho^\vee(S),\rho^\vee(T)]_{\mathrm{gr}},
$$

equivalently

$$
[\rho(S)^*,\rho(T)^*]_{\mathrm{gr}}=\rho\bigl([T,S]_{\mathrm{gr}}\bigr)^* .
$$

So the adjoint action is a graded action of the opposite algebra, and the exchange of the arguments is the reversal of the product read through the grading.

*Proof.* Using $[S,T]^{\mathrm{op}}_{\mathrm{gr}}=[T,S]_{\mathrm{gr}}$, $\rho([T,S]_{\mathrm{gr}})^*=\rho(TS-(-1)^{ij}ST)^*=\rho(S)^*\rho(T)^*-(-1)^{ij}\rho(T)^*\rho(S)^*=[\rho(S)^*,\rho(T)^*]_{\mathrm{gr}}$, which is the display.

**Corollary (the two sign rules differ by the order).** The action $\rho$ preserves the graded commutator of $B(H)$, while its adjoint $\rho^\vee$ preserves the graded commutator of $B(H)^{\mathrm{op}}$, which is the graded commutator with the arguments exchanged; the two sign rules therefore agree exactly on the pairs for which the graded commutator is symmetric, $[S,T]_{\mathrm{gr}}=[T,S]_{\mathrm{gr}}$, and the difference is the reversal of the order rather than a new structure.

*Proof.* The action's rule is the theorem of *The Graded Action on a Module over a Hilbert Space*, the adjoint's rule is the theorem above, and the comparison is the identity $[S,T]^{\mathrm{op}}_{\mathrm{gr}}=[T,S]_{\mathrm{gr}}$.

## The $*$-Action and the Agreement of the Two Structures

**Definition.** The graded action $\rho$ is a **$*$-action** (a $*$-representation) if it intertwines the involution with the adjoint,

$$
\rho(T^*)=\rho(T)^*\qquad(T\in B(H)),
$$

equivalently $\rho^\vee=\rho\circ(\ )^*$; an action that is not a $*$-action has no such compatibility, and the two structures differ.

**Theorem (agreement criterion).** The adjoint action equals the action through the involution,

$$
\rho^\vee(T)=\rho(T^*),
$$

if and only if $\rho$ is a $*$-action. In a $*$-action the adjoint action is a graded action of $B(H)$ (not only of $B(H)^{\mathrm{op}}$), its sign rule is the graded commutator rule of $B(H)$, and the involution of $B(H)$ is an automorphism of the representation.

*Proof.* The identity is the definition of the $*$-action read backwards; if it holds then $\rho(T^*)=\rho(T)^*=\rho^\vee(T)$, which is the $*$-action, and conversely. For a $*$-action, $\rho^\vee=\rho\circ(\ )^*$ and the involution is an anti-automorphism of $B(H)$ that is a homomorphism on the graded parts with the sign $(-1)^{ij}$ of the degree, so the opposite multiplication is transported back to the ordinary one.

**Proposition ($*$-actions and the parity operator).** If $\rho$ is a unital $*$-action then $\rho(\Gamma_H)=\Gamma_M$, and $\rho$ maps the even part $B(H)^0$ into the even part $B(M)^0$ and the odd part into the odd part; for a merely graded action the corresponding statement is the intertwining of the corollary, and the identification of the two parity operators is exactly the extra content of the $*$-condition.

*Proof.* $\Gamma_H^*=\Gamma_H$ and $\Gamma_H^2=I$, so $\rho(\Gamma_H)$ is self-adjoint and involutive; the intertwining of a graded action gives $\rho(\Gamma_H)\Gamma_M=\Gamma_M\rho(\Gamma_H)$, and a unital $*$-action has $\rho(\Gamma_H)=\rho(\Gamma_H)^*$; the standard argument on a graded Hilbert space then gives $\rho(\Gamma_H)=\Gamma_M$ up to a sign, and the unital $*$-condition fixes the sign.

**Example (the regular action and its adjoint).** Take $M=H$ and $\rho(T)=T$ the defining action, a $*$-action; its adjoint action is $T\mapsto T^*$, the involution, and the two structures agree, which is the module-level form of the identity $L_{T^*}=(L_T)^*$ of *The Adjoint of the Left Multiplication on a Hilbert Space*. Take instead $M=H$ with $\rho(T)=\alpha(T)=\Gamma_HT\Gamma_H$, the grade involution as the action; then $\rho$ is a $*$-action because $\alpha$ is a $*$-automorphism, and the adjoint action is again $\alpha$.

**Example (a graded action that is not a $*$-action).** On $M=H\oplus H$ with the action $\rho(T)=\begin{pmatrix}T&0\\0&T^{\mathrm{t}}\end{pmatrix}$ built from the transpose in a basis, the action is a graded action for the diagonal grading, but the transpose is not the adjoint, so the adjoint action is $\rho^\vee(T)=\begin{pmatrix}T^*&0\\0&\bar T\end{pmatrix}$ and it differs from $\rho(T^*)$; the example exhibits the failure of the agreement and shows that the $*$-condition is a genuine hypothesis.

## Examples and the Module Computations

**Proposition (the adjoint action on the graded pieces).** Write the module as $M=M^0\oplus M^1$ and an acting operator in blocks; the adjoint action acts blockwise by the adjoints, and the parity of the block is the parity of the degree:

$$
\rho^\vee(T)=\begin{pmatrix}\rho(T)_{00}^*&\rho(T)_{10}^*\\ \rho(T)_{01}^*&\rho(T)_{11}^*\end{pmatrix}
$$

for the block decomposition $\rho(T)=\begin{pmatrix}\rho(T)_{00}&\rho(T)_{01}\\ \rho(T)_{10}&\rho(T)_{11}\end{pmatrix}$ with $\rho(T)_{ij}:M^j\to M^i$.

*Proof.* The adjoint of a block operator in an orthogonal decomposition is the blockwise adjoint with the blocks transposed, and the degree of the block $\rho(T)_{ij}$ is $|T|+j-i$; the parity statement is the compatibility of the grading.

**Corollary (the kernel and the range).** The adjoint action has the same kernel as the action, $\ker\rho^\vee=\ker\rho$, and its range is the adjoint of the range, $\operatorname{ran}\rho^\vee=(\operatorname{ran}\rho)^*$; the closure of the range is the orthogonal complement of the kernel of the adjoint, as for any bounded operator.

*Proof.* $\rho^\vee(T)=0$ iff $\rho(T)^*=0$ iff $\rho(T)=0$, and the range statement is the definition; the complement statement is the closed-range theorem for the adjoint.

**Example (the finite-dimensional sign count).** For a finite-dimensional graded module with a homogeneous basis, the adjoint action in the homogeneous basis is the conjugate-transpose of the matrix of the action, and the sign rule of the graded commutator becomes the statement that the matrix of the adjoint of a homogeneous operator is homogeneous of the same degree with the conjugate-transposed blocks.

## Summary

The adjoint action of a graded action $\rho$ of $B(H)$ on a graded Hilbert space is the map $\rho^\vee(T)=\rho(T)^*$; it is a bounded unital representation of the opposite algebra $B(H)^{\mathrm{op}}$, since the adjoint reverses the product, and it is a graded action of that opposite algebra, since the adjoint preserves the degree and intertwines the parity operators in the same way as the action. Its sign rule is the rule of the opposite graded commutator, $[S,T]^{\mathrm{op}}_{\mathrm{gr}}=[T,S]_{\mathrm{gr}}$, so the adjoint action preserves the graded commutator up to the exchange of the two arguments, and the two sign rules differ by the order of the factors rather than by a new structure. When the graded action is a $*$-action, that is, when $\rho(T^*)=\rho(T)^*$, the adjoint action is the action composed with the involution, it is then a representation of $B(H)$ itself with the ordinary graded commutator rule, and the parity operator of the module is the image of the parity operator of the algebra; the agreement of the involution on the elements with the adjoint on the operators is a proved consequence of the $*$-condition, not an assumption, and it fails for a graded action that is not a $*$-action.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho:B(H)\to B(M)$ | the graded action |
| $\rho(B(H)^i)M^j\subseteq M^{i+j}$ | the grading condition |
| $\rho^\vee(T)=\rho(T)^*$ | the adjoint action |
| $\rho(ST)^*=\rho(T)^*\rho(S)^*$ | reversal of the product |
| $S\cdot T=TS$ | the opposite multiplication |
| $[S,T]^{\mathrm{op}}_{\mathrm{gr}}=[T,S]_{\mathrm{gr}}$ | the opposite sign rule |
| $[\rho(S)^*,\rho(T)^*]_{\mathrm{gr}}=\rho([T,S]_{\mathrm{gr}})^*$ | the sign exchange |
| $\rho(T^*)=\rho(T)^*$ | the $*$-action condition |
| $\rho(\Gamma_H)=\Gamma_M$ | parity operators agree for a $*$-action |
| $\ker\rho^\vee=\ker\rho$ | the kernel of the adjoint action |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the representations of $B(H)$, the opposite algebra and the $*$-representations.
- Masamichi Takesaki, *Theory of Operator Algebras I* (Springer, 1979), for the graded representations and the modular automorphisms of the adjoint.
- Nelson Dunford and Jacob T. Schwartz, *Linear Operators, Part II* (Interscience, 1963), for the block decompositions and the adjoint of an operator on a direct sum.
- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for the opposite algebra, the graded commutator and the sign rule of a graded category.
- Paul R. Halmos, *A Hilbert Space Problem Book* (Springer, 2nd ed. 1982), for the adjoint of a representation and the finite-dimensional examples.
