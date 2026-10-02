
# __The Adjoint Action of a Lie Algebra__

## Introduction

Every element $x$ of a Lie algebra $\mathrm{G}$ defines the operator $\operatorname{ad}_x$ on $\mathrm{G}$ by $\operatorname{ad}_x(y)=[x,y]$, and the assignment $x\mapsto\operatorname{ad}_x$ is the **adjoint action** of $\mathrm{G}$ on itself. The operators $\operatorname{ad}_x$ are the inner operators of the algebra, and their theory is the operator layer of the structure of $\mathrm{G}$: the Jacobi identity is exactly the statement that each $\operatorname{ad}_x$ is a derivation and that the map $x\mapsto\operatorname{ad}_x$ is a homomorphism of Lie algebras, the centre of $\mathrm{G}$ is exactly its kernel, the ideals of $\mathrm{G}$ are exactly the subspaces stable under all the $\operatorname{ad}_x$, and the inner derivations are exactly the image. The structure theory that uses these facts — the radical, the Killing form, Cartan's criteria, the Levi decomposition — is *Structure of Lie Algebras*; the derivations as a Lie algebra are *Derivations of a Lie Algebra*; the module structure it defines is *Representations of Lie Algebras*.

The base is a field $K$ and $\mathrm{G}$ is finite-dimensional over $K$. The adjoint map is written $\operatorname{ad}:\mathrm{G}\to\operatorname{End}_K(\mathrm{G})$, its value at $x$ by $\operatorname{ad}_x$, the centre by $\mathrm{Z}(\mathrm{G})$, the derivations by $\operatorname{Der}(\mathrm{G})$ and the inner derivations by $\operatorname{Inn}(\mathrm{G})$. The article reasons with the bracket and linear algebra over $K$ only.

## The Adjoint Map

**Definition.** The **adjoint action** of $\mathrm{G}$ on itself is the map

$$
\operatorname{ad}:\mathrm{G}\longrightarrow\operatorname{End}_K(\mathrm{G}),\qquad \operatorname{ad}(x)=\operatorname{ad}_x,\qquad \operatorname{ad}_x(y)=[x,y].
$$

**Proposition.** For each $x$ the operator $\operatorname{ad}_x$ is linear, and the map $\operatorname{ad}$ is linear.

**Proof.** The bracket is bilinear, so $\operatorname{ad}_x$ is linear in $y$; and for scalars $\lambda,\mu$ and elements $x,x'$, $\operatorname{ad}_{\lambda x+\mu x'}(y)=[\lambda x+\mu x',y]=\lambda[x,y]+\mu[x',y]$, so $\operatorname{ad}$ is linear in $x$. $\square$

## The Jacobi Identity as the Derivation Property

**Theorem.** The Jacobi identity is equivalent to the statement that every $\operatorname{ad}_x$ is a derivation of the bracket:

$$
\operatorname{ad}_x([y,z])=[\operatorname{ad}_x y,z]+[y,\operatorname{ad}_x z]\qquad\text{for all }x,y,z .
$$

**Proof.** The displayed identity reads $[x,[y,z]]=[[x,y],z]+[y,[x,z]]$, which is the Jacobi identity rearranged. $\square$

**Theorem.** The Jacobi identity is equivalently the statement that the adjoint map is a homomorphism of Lie algebras:

$$
\operatorname{ad}_{[x,y]}=[\operatorname{ad}_x,\operatorname{ad}_y]\qquad\text{for all }x,y .
$$

**Proof.** Both sides are operators on $\mathrm{G}$; evaluated on $z$, the left is $[[x,y],z]$ and the right is $[x,[y,z]]-[y,[x,z]]$, whose equality is again the Jacobi identity. $\square$

**Corollary.** The image $\operatorname{Inn}(\mathrm{G})=\operatorname{ad}(\mathrm{G})$ is a Lie subalgebra of $\operatorname{End}_K(\mathrm{G})$ with the commutator bracket, and $\operatorname{ad}$ is a homomorphism of Lie algebras onto it, so $\operatorname{ad}$ is a representation of $\mathrm{G}$ on $\mathrm{G}$, the adjoint representation of *Representations of Lie Algebras*. The derivations $\operatorname{Der}(\mathrm{G})$ of *Derivations of a Lie Algebra* contain $\operatorname{Inn}(\mathrm{G})$ as an ideal.

## The Kernel and the Centre

**Theorem.** The kernel of the adjoint map is the centre:

$$
\ker\operatorname{ad}=\{x:\operatorname{ad}_x=0\}=\{x:[x,y]=0\text{ for all }y\}=\mathrm{Z}(\mathrm{G}).
$$

**Proof.** $\operatorname{ad}_x=0$ means $[x,y]=0$ for every $y$, which is the definition of the centre. $\square$

**Corollary.** The adjoint representation is faithful exactly when $\mathrm{G}$ has trivial centre; and $\operatorname{ad}(\mathrm{G})\cong\mathrm{G}/\mathrm{Z}(\mathrm{G})$ as Lie algebras.

**Proposition.** The centre is an ideal and is the smallest ideal $\mathrm{I}$ with $\operatorname{ad}(\mathrm{G})\subseteq\operatorname{Der}(\mathrm{G})$ having $\mathrm{I}$ in its kernel; equivalently, a subspace $\mathrm{I}$ lies in the kernel of every $\operatorname{ad}_x$ exactly when $[\mathrm{G},\mathrm{I}]=0$, which for an ideal $\mathrm{I}$ means $\mathrm{I}\subseteq\mathrm{Z}(\mathrm{G})$ when $\mathrm{G}$ is spanned by $[\mathrm{G},\mathrm{G}]$.

**Proof.** The centre is an ideal because $[[x,y],z]=[x,[y,z]]-[y,[x,z]]\in\mathrm{Z}$ for $z$ central; the span statement is the definition of the bracket. $\square$

## Ideals as Invariant Subspaces

**Theorem.** A subspace $\mathrm{I}\subseteq\mathrm{G}$ is an ideal if and only if it is stable under every operator $\operatorname{ad}_x$, $x\in\mathrm{G}$; it is characteristic if and only if it is stable under every derivation.

**Proof.** Stability under $\operatorname{ad}_x$ means $[x,\mathrm{I}]\subseteq\mathrm{I}$ for every $x$, which is the definition of an ideal; the characteristic statement is the analogous reading with derivations in place of the $\operatorname{ad}_x$. $\square$

**Corollary.** The sum and the intersection of ideals are ideals, the quotient $\mathrm{G}/\mathrm{I}$ is a Lie algebra with the induced bracket, and the induced map on the quotient is the adjoint action of the quotient; the correspondence between ideals and invariant subspaces is the linear-algebraic form of the isomorphism theorems.

## The Operators and the Bracket

**Proposition.** The operators $\operatorname{ad}_x$ satisfy

$$
[\operatorname{ad}_x,\operatorname{ad}_y]=\operatorname{ad}_{[x,y]},
$$

so $\operatorname{ad}$ is a representation; the operators $\operatorname{ad}_x$ are the inner elements of the normaliser of $\operatorname{ad}(\mathrm{G})$ in $\operatorname{End}_K(\mathrm{G})$, and they act on $\operatorname{End}_K(\mathrm{G})$ by the commutator.

**Proof.** The first is the homomorphism property; the second is the Jacobi identity in the associative algebra $\operatorname{End}_K(\mathrm{G})$. $\square$

**Proposition (the transpose action).** The transpose operators $\operatorname{ad}_x^{*}$ on $\mathrm{G}^*$ define the **coadjoint action**, and it is again a representation, $\operatorname{ad}_{[x,y]}^{*}=[\operatorname{ad}_x^{*},\operatorname{ad}_y^{*}]$; with respect to the pairing $\mathrm{G}^*\times\mathrm{G}\to K$ the coadjoint and adjoint actions are transposed, $\langle\operatorname{ad}_x^{*}\xi,y\rangle=-\langle\xi,\operatorname{ad}_x y\rangle$ in the convention in which the pairing is $\xi(y)$.

**Proof.** Transposition reverses the commutator, so the homomorphism property is preserved; the sign in the pairing is the definition of the transpose. $\square$

## Worked Case: $\mathrm{sl}(2,K)$

Let $\mathrm{G}=\mathrm{sl}(2,K)$ with basis $e,h,f$ and $[h,e]=2e$, $[h,f]=-2f$, $[e,f]=h$. The adjoint operators are

$$
\operatorname{ad}_h=\begin{pmatrix}2&0&0\\0&0&0\\0&0&-2\end{pmatrix},\qquad
\operatorname{ad}_e=\begin{pmatrix}0&-2&0\\0&0&1\\0&0&0\end{pmatrix},\qquad
\operatorname{ad}_f=\begin{pmatrix}0&0&0\\-1&0&0\\0&2&0\end{pmatrix},
$$

the centre is zero, so the adjoint representation is faithful and $\operatorname{ad}(\mathrm{G})\cong\mathrm{sl}(2,K)$; the image is the three-dimensional Lie algebra spanned by the displayed matrices, with $[\operatorname{ad}_h,\operatorname{ad}_e]=2\operatorname{ad}_e$ and $[\operatorname{ad}_e,\operatorname{ad}_f]=\operatorname{ad}_h$, the same brackets as $\mathrm{G}$. The operators have trace zero, as they must, and each is a derivation of the bracket by the Jacobi identity.

**Verified.** The three matrices were recomputed from the brackets, the brackets of the matrices were checked to reproduce $[h,e]=2e$, $[h,f]=-2f$, $[e,f]=h$, and $\ker\operatorname{ad}=0$ was confirmed by the rank $3$ of the adjoint map.

## Summary

The **adjoint action** is the map $\operatorname{ad}:\mathrm{G}\to\operatorname{End}_K(\mathrm{G})$, $x\mapsto\operatorname{ad}_x$ with $\operatorname{ad}_x(y)=[x,y]$. The Jacobi identity is exactly the statement that each $\operatorname{ad}_x$ is a derivation of the bracket, equivalently that $\operatorname{ad}_{[x,y]}=[\operatorname{ad}_x,\operatorname{ad}_y]$, so $\operatorname{ad}$ is a homomorphism of Lie algebras onto the inner derivations, an ideal of the derivations. The kernel of $\operatorname{ad}$ is the centre $\mathrm{Z}(\mathrm{G})$, so the adjoint representation is faithful exactly when the centre is zero and $\operatorname{ad}(\mathrm{G})\cong\mathrm{G}/\mathrm{Z}(\mathrm{G})$. A subspace is an ideal exactly when it is stable under every $\operatorname{ad}_x$, and characteristic exactly when stable under every derivation. The transpose operators on the dual define the coadjoint action, another representation, transposed to the adjoint action with the sign of the pairing. For $\mathrm{sl}(2,K)$ the adjoint operators are the displayed matrices, the representation is faithful, and the image is a copy of $\mathrm{sl}(2,K)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | the base field |
| $\mathrm{G}$ | a finite-dimensional Lie algebra over $K$ |
| $[x,y]$ | the bracket |
| $\operatorname{ad}_x(y)=[x,y]$ | the adjoint operator of $x$ |
| $\operatorname{ad}:\mathrm{G}\to\operatorname{End}_K(\mathrm{G})$ | the adjoint map, the adjoint representation |
| $\operatorname{ad}_x^{*}$ | the transpose, giving the coadjoint action on $\mathrm{G}^*$ |
| $\mathrm{Z}(\mathrm{G})=\ker\operatorname{ad}$ | the centre |
| $\operatorname{Der}(\mathrm{G})$, $\operatorname{Inn}(\mathrm{G})$ | the derivations and the inner derivations |
| $\langle\cdot,\cdot\rangle$ | the pairing of $\mathrm{G}^*$ with $\mathrm{G}$ |

## Further Reading

- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the adjoint representation and the identification of ideals with invariant subspaces.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Graduate Texts in Mathematics 9 (Springer, 1972), for the adjoint and coadjoint actions and the centre.
- Nicolas Bourbaki, *Lie Groups and Lie Algebras*, Chapters 1–3 (Springer, 1989), for the adjoint action and the ideal correspondence.
- Jean-Pierre Serre, *Lie Algebras and Lie Groups*, Lecture Notes in Mathematics 1500 (Springer, 1992), for the adjoint representation and its properties.
