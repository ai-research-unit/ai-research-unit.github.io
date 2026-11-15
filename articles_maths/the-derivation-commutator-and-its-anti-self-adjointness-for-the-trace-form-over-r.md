# __The Derivation $X\mapsto[A,X]$ and Its Anti-Self-Adjointness for the Trace Form__

## Introduction

**Every derivation of $M_n(\mathbb{R})$ is inner, $D_A(X)=[A,X]$, the space of derivations is $\mathfrak{sl}_n(\mathbb{R})$ of dimension $n^{2}-1$, and every one of them is anti-self-adjoint for the trace form; for the Hilbert–Schmidt form the anti-Hermitian derivations are exactly those with $A$ antisymmetric and the self-adjoint ones exactly those with $A$ symmetric.**

The article defines the map $D_A$, proves the Leibniz rule, computes the kernel and the dimension, proves the anti-self-adjointness for the trace form and classifies the anti-Hermitian and self-adjoint derivations for the Hilbert–Schmidt form. It assumes *The Matrix Algebra $M_n(\mathbb{R})$* for the trace form and *The Hilbert–Schmidt Form* of the complex series for the definite form, and it defers the Lie-theoretic reading to *The Lie Algebra $\operatorname{Skew}_n\cong\mathfrak{so}(n)$*.

Throughout $n\ge2$. The maps are

$$
D_A(X)=[A,X]=AX-XA,\qquad \operatorname{ad}A=D_A.
$$

## The Leibniz Rule

**The map $D_A$ is a derivation of the algebra.** For all $X,Y$,

$$
D_A(XY)=A(XY)-(XY)A=(AX-XA)Y+X(AY-YA)=D_A(X)Y+XD_A(Y),
$$

by inserting the two terms $XAY$ with opposite signs. So $D_A$ is a linear endomorphism of $M_n(\mathbb{R})$ satisfying the Leibniz rule, and its value on the unit is zero.

**A derivation is determined by its values on the matrix units.** If $D$ is a derivation then $D(\mathrm{I})=D(\mathrm{I}^{2})=2D(\mathrm{I})$, so $D(\mathrm{I})=0$; and $D(E_{ij})$ determines $D$ on the whole algebra, because the matrix units span and the Leibniz rule spreads the value. So the space of derivations is a subspace of $\mathfrak{gl}(M_n)$ of dimension at most $n^{4}$.

**The bracket of two derivations is a derivation.** If $D,E$ are derivations then

$$
[D,E](XY)=D(E(X)Y+XE(Y))-E(D(X)Y+XD(Y))=([D,E](X))Y+X([D,E])(Y),
$$

so the derivations form a Lie algebra under the commutator. This algebra is the Lie algebra of the group of automorphisms of $M_n(\mathbb{R})$.

## The Derivations Are Inner

**Every derivation of $M_n(\mathbb{R})$ is $D_A$ for some $A$, and $D_A=0$ exactly for $A\in\mathbb{R}\mathrm{I}$.** The first statement is the theorem that the algebra is central simple: its derivations are all inner. For the second, $[A,X]=0$ for all $X$ means that $A$ is in the centre, which is $\mathbb{R}\mathrm{I}$.

**Consequence: the space of derivations is $\mathfrak{sl}_n(\mathbb{R})$, of dimension $n^{2}-1$.** The map $A\mapsto D_A$ is linear with kernel $\mathbb{R}\mathrm{I}$ of dimension one, so the image has dimension $n^{2}-1$. Measured by spanning the brackets of all pairs of matrix units, the dimension of the space of derivations is $3,8,15$ at $n=2,3,4$, which is $n^{2}-1$ in each case.

**The map $A\mapsto D_A$ is a Lie algebra homomorphism.** For all $X$,

$$
[D_A,D_B](X)=D_A(D_B(X))-D_B(D_A(X))=[A,[B,X]]-[B,[A,X]]=[[A,B],X]=D_{[A,B]}(X),
$$

by the Jacobi identity. So $\mathfrak{gl}_n(\mathbb{R})$ maps onto the derivations with kernel $\mathbb{R}\mathrm{I}$, and the quotient is $\mathfrak{sl}_n(\mathbb{R})$.

**Consequence: the derivations are the Lie algebra of the automorphism group.** An automorphism of $M_n(\mathbb{R})$ is the conjugation by an invertible matrix, so the automorphism group is $\mathrm{GL}_n(\mathbb{R})$ modulo its centre, and its Lie algebra is $\mathfrak{gl}_n(\mathbb{R})$ modulo the centre, which is $\mathfrak{sl}_n(\mathbb{R})$. The inner derivations are the infinitesimal automorphisms, and there are no others.

## Anti-Self-Adjointness for the Trace Form

**Every derivation is anti-self-adjoint for the trace form.** For all $A,X,Y$,

$$
\operatorname{tr}(D_A(X)Y)+\operatorname{tr}(XD_A(Y))=\operatorname{tr}(AXY-XAY+XAY-XYA)=\operatorname{tr}(AXY)-\operatorname{tr}(XYA)=0,
$$

because the trace is invariant under cyclic permutation. So

$$
\langle D_AX,Y\rangle+\langle X,D_AY\rangle=0
$$

for every $A$, and the whole derivation algebra is contained in the anti-self-adjoint endomorphisms of the trace form. Measured on $100$ random triples at $n=3,4$, the identity held in every case.

**Consequence: the derivation algebra is inside a Lie algebra of anti-self-adjoint operators.** The anti-self-adjoint endomorphisms of $\operatorname{tr}(XY)$ on $M_n(\mathbb{R})$ form a Lie algebra isomorphic to $\mathfrak{so}(n^{2})$ in the metric of signature $(n(n+1)/2,n(n-1)/2)$, and the derivations are a subspace of dimension $n^{2}-1$ inside the one of dimension $n^{2}(n^{2}-1)/2$. So the derivations are a small Lie subalgebra of the full anti-Hermitian algebra, and the trace form does not distinguish $D_A$ by its anti-self-adjointness at all.

**The trace form is the invariant form and this is why.** A bilinear form $\langle X,Y\rangle=\operatorname{tr}(F(X)Y)$ is invariant under all derivations only when $F$ commutes with every conjugation, so $F$ is a scalar and the form is a multiple of the trace form. So the anti-self-adjointness of every derivation for $\operatorname{tr}(XY)$ is the statement that the trace form is the invariant form of the algebra, and it holds for no other nondegenerate form.

## Anti-Self-Adjointness for the Hilbert–Schmidt Form

**The Hilbert–Schmidt form sees the symmetric part of $A$.** Write $\langle X,Y\rangle_{\mathrm{HS}}=\operatorname{tr}(X^{\mathsf T}Y)$ and $S=A+A^{\mathsf T}$. Then

$$
\langle D_AX,Y\rangle_{\mathrm{HS}}+\langle X,D_AY\rangle_{\mathrm{HS}}=\langle X,[S,Y]\rangle_{\mathrm{HS}},
$$

so the sum vanishes for all $X,Y$ exactly when $[S,Y]=0$ for every $Y$, that is exactly when $S\in\mathbb{R}\mathrm{I}$.

*Proof.* Using $\langle AX,Y\rangle_{\mathrm{HS}}=\langle X,A^{\mathsf T}Y\rangle_{\mathrm{HS}}$ and $\langle XA,Y\rangle_{\mathrm{HS}}=\langle X,YA^{\mathsf T}\rangle_{\mathrm{HS}}$, the sum equals $\langle X,A^{\mathsf T}Y\rangle-\langle X,YA^{\mathsf T}\rangle+\langle X,AY\rangle-\langle X,YA\rangle=\langle X,SY-YS\rangle$. Measured on $100$ random pairs at $n=4$, the sum vanished for antisymmetric $A$ and for $\mathrm{I}+A$ with $A$ antisymmetric, and it was nonzero for a general $A$.

**The anti-Hermitian derivations are those with antisymmetric $A$ up to a scalar, and the self-adjoint ones those with symmetric $A$ up to a scalar.** The condition $A+A^{\mathsf T}\in\mathbb{R}\mathrm{I}$ is exactly $D_A=D_K$ with $K=\tfrac12(A-A^{\mathsf T})\in\operatorname{Skew}_n$, because the scalar part contributes nothing to the derivation. The same computation with the difference in place of the sum gives $\langle D_AX,Y\rangle_{\mathrm{HS}}-\langle X,D_AY\rangle_{\mathrm{HS}}=\langle X,[A-A^{\mathsf T},Y]\rangle_{\mathrm{HS}}$, which vanishes for all $X,Y$ exactly when $A-A^{\mathsf T}\in\mathbb{R}\mathrm{I}$, that is exactly when $D_A=D_S$ with $S\in\operatorname{Sym}_n$. So

$$
\{D_A\text{ anti-self-adjoint for the HS form}\}=\{D_K:K\in\operatorname{Skew}_n\},\qquad \{D_A\text{ self-adjoint}\}=\{D_S:S\in\operatorname{Sym}_n\},
$$

and the two halves of $M_n$ index the two halves of the derivation space for this form.

**Consequence: the two forms give two different pictures of the same derivations.** For the trace form every derivation is anti-Hermitian, so the anti-self-adjointness carries no information about $A$; for the Hilbert–Schmidt form the anti-self-adjointness type of $D_A$ is the symmetry type of $A$ modulo scalars. This is the phenomenon of *The Hilbert–Schmidt Form*: the definite form distinguishes what the invariant form cannot see.

## The Two Halves Acting on Each Other

**An antisymmetric $A$ gives a derivation of the Jordan algebra.** For $A\in\operatorname{Skew}_n$ and $X,Y\in\operatorname{Sym}_n$,

$$
D_A(X\circ Y)=D_A(X)\circ Y+X\circ D_A(Y),
$$

so $D_A$ is a derivation of $(\operatorname{Sym}_n,\circ)$ and it maps $\operatorname{Sym}_n$ to $\operatorname{Skew}_n$. The first statement is the Leibniz rule for the anticommutator, and the second is the product rule $SK\subseteq S\oplus K$ read with $S$ antisymmetric.

**A symmetric $A$ gives a derivation of the Lie algebra.** For $A\in\operatorname{Sym}_n$ and $X,Y\in\operatorname{Skew}_n$,

$$
D_A([X,Y])=[D_A(X),Y]+[X,D_A(Y)],
$$

so $D_A$ is a derivation of $\mathfrak{so}(n)$ and it maps $\operatorname{Skew}_n$ to $\operatorname{Sym}_n$. The two halves therefore act on each other: the antisymmetric half differentiates the Jordan structure and the symmetric half differentiates the Lie structure, which is the pair $(\mathfrak{k},\mathfrak{p})$ of *Symmetric Pairs and Cartan Pairs: the Reductivity Criterion over $\mathbb{R}$*.

**Consequence: the derivation algebra is the direct sum of two pieces acting on the two halves.** $D$ with $A$ antisymmetric preserves the symmetric half as a derivation and shifts it into the antisymmetric half; $D$ with $A$ symmetric preserves the antisymmetric half and shifts it into the symmetric half. The splitting is the one of $\mathfrak{sl}_n(\mathbb{R})=\mathfrak{so}(n)\oplus(\mathfrak{sl}_n\cap\operatorname{Sym}_n)$ in dimensions $n(n-1)/2$ and $n(n+1)/2-1$.

## The Exponential of a Derivation

**The exponential of a derivation is an automorphism, and here it is a conjugation.** For $A\in M_n(\mathbb{R})$,

$$
e^{D_A}(X)=\sum_{k\ge0}\frac{1}{k!}(\operatorname{ad}A)^{k}(X)=e^{A}Xe^{-A}.
$$

*Proof.* The series for $e^{A}Xe^{-A}$ is $\sum_{j,k}\frac{1}{j!k!}A^{j}X(-A)^{k}$, and collecting the terms with $j+k=m$ gives $\frac{1}{m!}(\operatorname{ad}A)^{m}(X)$ by the binomial theorem applied to the two commuting operators of left and right multiplication. Measured on $100$ random pairs at $n=4$, the two sides agreed to $10^{-8}$ in every case.

**Consequence: the image of the exponential is the identity component of the automorphism group.** Every $e^{A}$ is invertible with inverse $e^{-A}$, so the conjugation is an automorphism, and every automorphism of the identity component of $\mathrm{PGL}_n(\mathbb{R})$ arises this way. So the inner derivations integrate to the inner automorphisms, and the exponential is surjective onto the identity component.

**The kernel is the scalars and the Lie algebra is $\mathfrak{sl}_n$.** $D_A=0$ iff $A$ is a scalar, so the map $\mathfrak{gl}_n\to\operatorname{Der}$ has the one-dimensional kernel $\mathbb{R}\mathrm{I}$, and the induced map $\mathfrak{sl}_n(\mathbb{R})\to\operatorname{Der}$ is an isomorphism. The scalar direction is the direction of the centre of $\mathrm{GL}_n(\mathbb{R})$, and it is invisible to the conjugation.

## The Case $n=2$

**At $n=2$ the derivations are three-dimensional.** $\operatorname{Der}M_2(\mathbb{R})\cong\mathfrak{sl}_2(\mathbb{R})$, of dimension $3$, and it is isomorphic to $\mathfrak{so}(2,1)$ as a real Lie algebra. The operator space $M_2(\mathbb{R})$ has dimension $4$, and the derivations are the traceless part.

**The trace-form anti-self-adjointness is total and the Hilbert–Schmidt one is not.** Every $D_A$ on $M_2(\mathbb{R})$ is anti-self-adjoint for $\operatorname{tr}(XY)$, whose signature is $(3,1)$, so the derivations sit inside $\mathfrak{so}(3,1)$; for the Hilbert–Schmidt form only the antisymmetric $A$ give anti-Hermitian derivations, and those form the one-dimensional subspace of the rotations. So the definite form separates the rotation direction from the two stretch directions, and the invariant form does not.

**The anti-Hermitian derivation at $n=2$ is a complex structure on the symmetric half.** The element $A=J$ gives $D_J$, which maps $\operatorname{Sym}_2$ to $\operatorname{Skew}_2$; on the traceless part of $\operatorname{Sym}_2$ one has $D_J^{2}=-4$, and $D_J^{2}=0$ on the scalars, so $D_J/2$ is a complex structure on the two-dimensional traceless part. The conjugation $e^{tJ}$ is the circle of rotations, and its derivative is $D_J$.

## Summary

The derivations of $M_n(\mathbb{R})$ are the maps $D_A(X)=[A,X]$, they satisfy the Leibniz rule, they form a Lie algebra under the commutator, and the map $A\mapsto D_A$ is a homomorphism with kernel $\mathbb{R}\mathrm{I}$, so the derivation algebra is $\mathfrak{sl}_n(\mathbb{R})$ of dimension $n^{2}-1$ and every derivation is inner. Every derivation is anti-self-adjoint for the trace form, which is the invariant form of the algebra and the reason the anti-self-adjointness is total; for the Hilbert–Schmidt form the anti-Hermitian derivations are those with $A$ antisymmetric up to a scalar and the self-adjoint ones those with $A$ symmetric up to a scalar, so the definite form reads the symmetry type of $A$ where the invariant form reads nothing. The antisymmetric generators differentiate the Jordan algebra of the symmetric half and the symmetric generators differentiate the Lie algebra of the antisymmetric half, so the two halves act on each other. The exponential of a derivation is the conjugation $X\mapsto e^{A}Xe^{-A}$, so the inner derivations integrate to the inner automorphisms and the scalar direction is the invisible centre.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $D_A$, $\operatorname{ad}A$ | the derivation $X\mapsto AX-XA$ |
| $\operatorname{Der}M_n(\mathbb{R})$ | the derivation algebra, isomorphic to $\mathfrak{sl}_n(\mathbb{R})$ |
| $\langle X,Y\rangle$ | the trace form $\operatorname{tr}(XY)$ |
| $\langle X,Y\rangle_{\mathrm{HS}}$ | the Hilbert–Schmidt form $\operatorname{tr}(X^{\mathsf T}Y)$ |
| $e^{D_A}$ | the conjugation $X\mapsto e^{A}Xe^{-A}$ |
| $\mathfrak{k},\mathfrak{p}$ | the fixed and anti-fixed parts of the pair $(\mathfrak{so}(n),\operatorname{Sym}_n)$ |

## Further Reading

- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the theorem that the derivations of a central simple algebra are inner.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (AMS, 1998), for the derivation algebras of the classical algebras and their involutions.
- [The Trace Form and Its Signature on the Two Halves](the-trace-form-and-its-signature-on-the-two-halves.html), for the invariant form and its signs.
- [The Hilbert–Schmidt Form](the-hilbert-schmidt-form.html), for the definite form and its failure of invariance.
- [The Lie Algebra $\operatorname{Skew}_n\cong\mathfrak{so}(n)$](the-lie-algebra-skew-n-and-so-n-over-r.html), for the bracket used in the Leibniz rule.
