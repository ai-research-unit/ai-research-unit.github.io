
# __The Adjoint Representation and the Involution__

## Introduction

The **adjoint representation** of a Lie algebra $\mathrm{G}$ is the map

$$
\operatorname{ad}:\mathrm{G}\longrightarrow\mathfrak{gl}(\mathrm{G}),\qquad \operatorname{ad}_x(y)=[x,y],
$$

and an involution $\theta$ of $\mathrm{G}$ acts on both sides of it: on $\mathrm{G}$ by $\theta$ itself and on the operators by conjugation, $\Theta(T)=\theta T\theta^{-1}$. The two actions are **compatible**, $\operatorname{ad}_{\theta x}=\Theta\operatorname{ad}_x\Theta^{-1}$, so $\operatorname{ad}$ is a morphism of algebras-with-involution, and the adjoint representation carries the involution to the operator algebra. This article, the fourth of the `- * Operator Theory` group of the category, treats the adjoint representation under an involution: its equivariance, the induced decomposition of the endomorphism algebra along the eigenspaces of $\theta$, the **self-duality** of the adjoint representation through the Killing form, the **orthogonal** and **symplectic** types that a self-dual representation takes according to the symmetry of its invariant form, and the **self-dual representations** as the objects fixed by the duality. The adjoint action as an operator is *The Adjoint Action of a Lie Algebra*; the extension $\Theta$ and the module theory are *Representations of Lie Algebras*; the symmetric pair and the Cartan involution are *The Cartan Involution and the Cartan Decomposition* and *Symmetric Pairs of a Lie Algebra*; the analysis of unitarity belongs to a later Part and is named only.

The base is a field $K$ of characteristic not two; $\mathrm{G}$ is a finite-dimensional Lie algebra with Killing form $B$, $\theta$ an involution, $\Theta$ the conjugation action on $\mathfrak{gl}(\mathrm{G})$, and $B_\theta(x,y)=-B(x,\theta y)$ the twisted form. The article uses the bracket, the operator algebra and the form algebraically, and forms no length from $B$.

## The Equivariance of the Adjoint Representation

**Theorem.** Let $\theta$ be an involution of $\mathrm{G}$ and let $\Theta$ be the conjugation $T\mapsto\theta T\theta^{-1}$ on $\mathfrak{gl}(\mathrm{G})$. Then

$$
\operatorname{ad}_{\theta x}=\Theta\operatorname{ad}_x\Theta^{-1}
$$

for every $x\in\mathrm{G}$; equivalently $\operatorname{ad}\circ\theta=\Theta\circ\operatorname{ad}$, so the adjoint representation intertwines the involution of $\mathrm{G}$ with the involution of the operator algebra.

**Proof.** For $y\in\mathrm{G}$, $\Theta\operatorname{ad}_x\Theta^{-1}(y)=\theta[x,\theta^{-1}y]=[\theta x,y]=\operatorname{ad}_{\theta x}(y)$, because $\theta$ is an algebra automorphism and $\theta^{-1}=\theta$. The second form is the same statement. $\square$

**Corollary.** $\Theta$ is an involution of $\mathfrak{gl}(\mathrm{G})$ (the conjugation by an involution), and $\operatorname{ad}$ carries the $\pm1$-eigenspaces of $\theta$ into the $\pm1$-eigenspaces of $\Theta$: $\operatorname{ad}(\mathrm{K})\subseteq\mathfrak{gl}(\mathrm{G})^{+}$ and $\operatorname{ad}(\mathrm{P})\subseteq\mathfrak{gl}(\mathrm{G})^{-}$, where $\mathrm{G}=\mathrm{K}\oplus\mathrm{P}$ is the decomposition of $\theta$.

**Proposition.** The image $\operatorname{ad}(\mathrm{G})$ is $\Theta$-stable, and the kernel of $\operatorname{ad}$ is the centre $\mathrm{Z}(\mathrm{G})$, which is $\theta$-stable; hence the isomorphism $\mathrm{G}/\mathrm{Z}(\mathrm{G})\cong\operatorname{ad}(\mathrm{G})$ is an isomorphism of algebras with involution.

**Proof.** Stability of the image follows from the equivariance, and stability of the centre because $\theta$ is an automorphism; the isomorphism is the first isomorphism theorem, and it respects the involutions because $\operatorname{ad}\circ\theta=\Theta\circ\operatorname{ad}$. $\square$

## The Induced Decomposition of the Operator Algebra

**Theorem.** The decomposition $\mathrm{G}=\mathrm{K}\oplus\mathrm{P}$ induces a decomposition of the adjoint image,

$$
\operatorname{ad}(\mathrm{G})=\operatorname{ad}(\mathrm{K})\oplus\operatorname{ad}(\mathrm{P}),
$$

with $\operatorname{ad}(\mathrm{K})$ a Lie subalgebra of $\mathfrak{gl}(\mathrm{G})$, $\operatorname{ad}(\mathrm{P})$ a module over it, and the brackets $[\operatorname{ad}(\mathrm{K}),\operatorname{ad}(\mathrm{K})]\subseteq\operatorname{ad}(\mathrm{K})$, $[\operatorname{ad}(\mathrm{K}),\operatorname{ad}(\mathrm{P})]\subseteq\operatorname{ad}(\mathrm{P})$, $[\operatorname{ad}(\mathrm{P}),\operatorname{ad}(\mathrm{P})]\subseteq\operatorname{ad}(\mathrm{K})$; the involution $\Theta$ acts by $+1$ on the first summand and by $-1$ on the second.

**Proof.** The image is $\operatorname{ad}(\mathrm{G})$, and $\operatorname{ad}$ is linear with $\theta$-invariant kernel, so $\operatorname{ad}(\mathrm{G})=\operatorname{ad}(\mathrm{K})+\operatorname{ad}(\mathrm{P})$ and the sum is direct because $\operatorname{ad}$ is injective on $\mathrm{K}\cap\mathrm{P}=0$ modulo the centre; the brackets are the images of the brackets of $\mathrm{K}$ and $\mathrm{P}$, and the eigenvalue statement is the equivariance. $\square$

**Corollary.** The pair $(\operatorname{ad}(\mathrm{G}),\operatorname{ad}(\mathrm{K}))$ is a symmetric pair, the image of $(\mathrm{G},\mathrm{K})$ under $\operatorname{ad}$, and the $\Theta$-grading of the operator algebra restricts to the grading of the adjoint image.

**Proposition.** The fixed algebra of $\Theta$ on the whole of $\mathfrak{gl}(\mathrm{G})$ is the centraliser of the decomposition, consisting of the operators preserving $\mathrm{K}$ and $\mathrm{P}$ separately, and the anti-fixed part consists of the operators exchanging them; the adjoint image lies in the even part when $\mathrm{G}$ is a symmetric pair.

**Proof.** An operator $T$ commutes with $\Theta$ exactly when it preserves the two eigenspaces, and anticommutes exactly when it exchanges them; for $T=\operatorname{ad}_x$ with $x\in\mathrm{K}$ the operator preserves $\mathrm{K}$ and $\mathrm{P}$ by the bracket relations, while for $x\in\mathrm{P}$ it exchanges them. $\square$

## Self-Duality through the Killing Form

**Definition.** A representation $V$ of $\mathrm{G}$ is **self-dual** when it carries a nondegenerate bilinear form $\phi$ invariant under the action, $\phi(x\cdot u,v)+\phi(u,x\cdot v)=0$; the form is then unique up to a scalar when $V$ is irreducible, and the representation is **orthogonal** when $\phi$ is symmetric and **symplectic** when $\phi$ is antisymmetric.

**Theorem.** The adjoint representation is self-dual, with the invariant form the Killing form:

$$
B(\operatorname{ad}_x y,z)+B(y,\operatorname{ad}_x z)=0 .
$$

**Proof.** The invariance $B([x,y],z)+B(y,[x,z])=0$ is the associativity of the Killing form; it is exactly the displayed relation. $\square$

**Corollary.** The Killing form is symmetric, $B(y,z)=B(z,y)$, so the adjoint representation is of **orthogonal** type; the isomorphism $\mathrm{G}\to\mathrm{G}^{*}$, $x\mapsto B(x,\cdot)$, intertwines the adjoint action with the negative transpose action, $\operatorname{ad}_x^{*}=-\operatorname{ad}_x$ for the contragredient action on the dual, which is the self-duality expressed on the dual.

**Proposition.** When $\theta$ is an involution, the twisted form $B_\theta(x,y)=-B(x,\theta y)$ is invariant under the $\theta$-twisted action, $B_\theta(\theta x,\theta y)=B_\theta(x,y)$; it pairs the two eigenspaces $\mathrm{K},\mathrm{P}$ with themselves and $\mathrm{K}$ with $\mathrm{P}$ according to the parity, and it is symmetric because $B$ and $\theta$ commute with the symmetry.

**Proof.** The invariance of $B_\theta$ is the invariance of $B$ composed with the automorphism $\theta$; the parity of the pairing is read off the eigenvalues of $\theta$ on the two arguments. $\square$

## The Two Types and the Self-Dual Representations

**Theorem.** Let $V$ be an irreducible self-dual representation with invariant form $\phi$. Then either $\phi$ is symmetric or $\phi$ is antisymmetric, and the two cases are exclusive; in the first case $V$ is orthogonal, in the second symplectic. The symmetric resp. antisymmetric form on $V\oplus V$ defined by $\phi$ pairs the two summands in the respective ways, and an irreducible representation that is not self-dual occurs in pairs $V,V^{*}$ with no invariant form on $V$.

**Proof.** The form $\phi$ is determined up to a scalar by irreducibility (Schur's lemma applied to the isomorphism $V\to V^{*}$); a scalar multiple of a symmetric form is symmetric and of an antisymmetric form antisymmetric, so the type is well defined; non-self-dual irreducible representations have $V\not\cong V^{*}$ and admit no invariant form. $\square$

**Corollary.** The adjoint representation is orthogonal, since its invariant form the Killing form is symmetric; the fundamental representation of $\mathrm{sl}(2,K)$ is symplectic, its invariant form being the determinant pairing $\det(u,v)$; the two types occur among the self-dual representations of a semisimple algebra, and the type of an irreducible is its **Frobenius–Schur type**, named and computed by the analysis of a later Part.

**Proposition (the involution on the self-dual representations).** An involution $\theta$ of $\mathrm{G}$ acts on the set of isomorphism classes of self-dual representations by twisting the action through $\theta$, and it fixes the adjoint representation; a self-dual representation is **$\theta$-self-dual** when the twist is isomorphic to the original, equivalently when the invariant form can be chosen $\theta$-invariant.

**Proof.** The twist $V^\theta$ is the module with action $x\cdot_\theta v=\theta(x)\cdot v$; its isomorphism class is well defined, and the adjoint representation is fixed because $\operatorname{ad}\circ\theta=\Theta\circ\operatorname{ad}$ exhibits the isomorphism; the invariant form is $\theta$-invariant exactly when the twist is isomorphic to $V$ via that form. $\square$

**Corollary.** The self-dual representations of a symmetric pair $(\mathrm{G},\mathrm{K})$ split according to their behaviour under $\theta$; the adjoint representation splits as $\operatorname{ad}(\mathrm{K})\oplus\operatorname{ad}(\mathrm{P})$, the fixed and the twisted parts, and the two summands are the components of the adjoint representation as a $\mathrm{K}$-module.

## Worked Case: $\mathrm{sl}(2,K)$

Let $\mathrm{G}=\mathrm{sl}(2,K)$ with basis $e,h,f$, brackets $[h,e]=2e$, $[h,f]=-2f$, $[e,f]=h$, and Killing form $B$ with $B(e,f)=B(h,h)/2=4$ up to a normalisation, $B(e,e)=B(f,f)=0$. The adjoint representation has dimension three and is irreducible; it is self-dual and orthogonal, the invariant form being $B$; in the basis $(e,h,f)$ the form has matrix proportional to $\begin{pmatrix}0&0&4\\0&8&0\\4&0&0\end{pmatrix}$, symmetric with nonzero determinant.

The involution $\theta(x)=-x^{t}$ acts by $\theta(e)=-f$, $\theta(f)=-e$, $\theta(h)=-h$; the induced involution $\Theta$ on the adjoint image fixes $\operatorname{ad}_h$ up to the sign convention and exchanges $\operatorname{ad}_e$ and $\operatorname{ad}_f$ up to signs; the fixed part $\operatorname{ad}(\mathrm{K})=\langle\operatorname{ad}_{e-f}\rangle$ is one-dimensional and the anti-fixed part $\operatorname{ad}(\mathrm{P})=\langle\operatorname{ad}_h,\operatorname{ad}_{e+f}\rangle$ is two-dimensional, matching $\dim\mathrm{K}=1$, $\dim\mathrm{P}=2$. The twisted form $B_\theta$ pairs $\mathrm{K}$ with itself and $\mathrm{P}$ with itself and is nondegenerate on each, as the Cartan decomposition requires.

**Verified.** For $\mathrm{sl}(2,K)$ the equivariance $\operatorname{ad}_{\theta x}=\Theta\operatorname{ad}_x\Theta^{-1}$ was checked on the three generators and their brackets; the invariance of $B$ and of $B_\theta$ was checked on the basis; the dimensions of the fixed and anti-fixed parts of the adjoint image were checked to be $1$ and $2$.

## Summary

The **adjoint representation** $\operatorname{ad}$ of a Lie algebra is **equivariant** under an involution $\theta$: with $\Theta$ the conjugation $T\mapsto\theta T\theta^{-1}$ on the operator algebra, $\operatorname{ad}_{\theta x}=\Theta\operatorname{ad}_x\Theta^{-1}$, so $\operatorname{ad}$ is a morphism of algebras with involution and carries the eigenspace decomposition $\mathrm{G}=\mathrm{K}\oplus\mathrm{P}$ to the decomposition of the adjoint image, a symmetric pair with $\Theta$ acting by $\pm1$. The adjoint representation is **self-dual**, its invariant form the symmetric Killing form, and it is therefore of **orthogonal** type; the **symplectic** type is the other possibility for a self-dual irreducible representation and is exemplified by the fundamental representation of $\mathrm{sl}(2,K)$. Self-dual representations are those carrying an invariant nondegenerate form, unique up to a scalar for an irreducible, and an **involution** acts on them by twisting; those fixed by the twist are the $\theta$-self-dual representations, the adjoint being one of them. For $\mathrm{sl}(2,K)$ the adjoint representation is three-dimensional, orthogonal, and splits under the Cartan involution into a one-dimensional fixed part and a two-dimensional anti-fixed part, matching the Cartan decomposition. The analytic determination of the type and the unitarity belong to a later Part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | the base field, of characteristic not two |
| $\mathrm{G}$ | a finite-dimensional Lie algebra |
| $\operatorname{ad}_x(y)=[x,y]$ | the adjoint representation |
| $\theta,\Theta$ | the involution of $\mathrm{G}$ and the conjugation on the operators |
| $B$ | the Killing form |
| $B_\theta(x,y)=-B(x,\theta y)$ | the twisted form |
| $\mathrm{K},\mathrm{P}$ | the $\pm1$-eigenspaces of $\theta$ |
| $\phi$ | an invariant form on a self-dual representation |

## Further Reading

- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Graduate Texts in Mathematics 9 (Springer, 1972), for the adjoint representation, the Killing form and self-dual representations.
- Jean-Pierre Serre, *Complex Semisimple Lie Algebras* (Springer, 2001), for the types of self-dual representations and the invariant forms.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction*, Progress in Mathematics 140 (Birkhäuser, 2nd ed. 2002), for the adjoint representation of a symmetric pair.
- Nicolas Bourbaki, *Lie Groups and Lie Algebras*, Chapters 4–6 (Springer, 2002), for the adjoint representation and its involutions.
