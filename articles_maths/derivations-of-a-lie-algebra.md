
# __Derivations of a Lie Algebra__

## Introduction

A **derivation** of a Lie algebra $\mathrm{G}$ is a linear operator $D:\mathrm{G}\to\mathrm{G}$ that satisfies the Leibniz rule for the bracket, $D([x,y])=[Dx,y]+[x,Dy]$. The Jacobi identity says that every adjoint operator $\operatorname{ad}_x=[x,-]$ is a derivation, and the derivations of this special form are the **inner** ones; the others, read modulo the inner ones, are the **outer** derivations. This article studies the derivation algebra $\operatorname{Der}(\mathrm{G})$ as a Lie algebra of operators on $\mathrm{G}$: the Leibniz rule as a commutation relation with the adjoint operators, the description of $\operatorname{Der}(\mathrm{G})$ as the normaliser of $\operatorname{ad}(\mathrm{G})$ with a matching induced operator, the exact sequence that separates the centre, the inner and the outer derivations, the identification of the outer derivations with the first cohomology group, the behaviour under direct sums, the restricted structure in positive characteristic, and the exact dimensions in the examples.

The structural facts are established in *Structure of Lie Algebras* and are cited, not reproved: that the derivations form a Lie subalgebra of $\operatorname{End}_K(\mathrm{G})$, that the inner derivations are an ideal, that $\operatorname{Out}(\mathrm{G})=\operatorname{Der}(\mathrm{G})/\operatorname{Inn}(\mathrm{G})$ is the quotient, and that a semisimple Lie algebra over a field of characteristic zero has no outer derivations. The bracket, the Jacobi identity, the centre and the adjoint map are *Lie Algebras*; the Chevalley–Eilenberg complex and its first cohomology are *Lie Algebra Cohomology*; the derivation of an associative algebra is *Automorphisms and Derivations of Algebras*.

The article stays inside Part I and reasons with no form and no distance: the Killing form is not used, and the semisimplicity criterion it carries is not invoked. The Lie algebra of the automorphism group, the exponential of a derivation and the correspondence between derivations and one-parameter subgroups are named as forward references and belong to Part II. The base is a field $K$, and $\mathrm{G}$ is a Lie algebra of finite dimension over $K$; the characteristic is arbitrary and every characteristic-dependent statement is flagged.

## The Leibniz Rule as an Operator Identity

### The Definition, Recalled

**Definition.** A **derivation** of $\mathrm{G}$ is a $K$-linear map $D:\mathrm{G}\to\mathrm{G}$ with

$$
D([x,y])=[Dx,y]+[x,Dy]\qquad\text{for all }x,y\in\mathrm{G}.
$$

The set of derivations is a subspace of $\operatorname{End}_K(\mathrm{G})$, written $\operatorname{Der}(\mathrm{G})$, and a Lie subalgebra under the commutator $[D,E]=D\circ E-E\circ D$; the **inner derivations** are the operators $\operatorname{ad}_x$, forming the image $\operatorname{Inn}(\mathrm{G})=\operatorname{ad}(\mathrm{G})$. Both statements are from *Structure of Lie Algebras*, together with the fact that $\operatorname{Inn}(\mathrm{G})$ is an ideal, so that $\operatorname{Out}(\mathrm{G})=\operatorname{Der}(\mathrm{G})/\operatorname{Inn}(\mathrm{G})$ is a Lie algebra.

**Remark.** The identity operator is a derivation exactly when $\mathrm{G}$ is abelian: the Leibniz rule for $\operatorname{id}$ reads $[x,y]=[x,y]+[x,y]$, that is $[x,y]=0$ for all $x,y$.

### The Commutation Form

**Proposition (the operator form of the Leibniz rule).** Let $D\in\operatorname{End}_K(\mathrm{G})$. Then $D$ is a derivation if and only if

$$
[D,\operatorname{ad}_x]=\operatorname{ad}_{Dx}\qquad\text{for all }x\in\mathrm{G},
$$

the bracket of operators being the commutator in $\operatorname{End}_K(\mathrm{G})$.

**Proof.** For every $y$, $[D,\operatorname{ad}_x](y)=D([x,y])-[x,Dy]$; the Leibniz rule says exactly that this equals $[Dx,y]=\operatorname{ad}_{Dx}(y)$ for all $x,y$. $\square$

**Corollary.** A derivation $D$ commutes with $\operatorname{ad}_x$ exactly when $Dx$ is central; in particular $D(\mathrm{Z}(\mathrm{G}))\subseteq\mathrm{Z}(\mathrm{G})$.

**Proof.** $[D,\operatorname{ad}_x]=0$ is $\operatorname{ad}_{Dx}=0$, whose kernel is the centre; apply this to a central $z$. $\square$

### The Derivation Algebra as a Normaliser

**Definition.** The **normaliser** of the subspace $\operatorname{ad}(\mathrm{G})\subseteq\operatorname{End}_K(\mathrm{G})$ is

$$
\mathrm{N}=\{\,T\in\operatorname{End}_K(\mathrm{G}) : [T,\operatorname{ad}(\mathrm{G})]\subseteq\operatorname{ad}(\mathrm{G})\,\}.
$$

It is the largest subspace of $\operatorname{End}_K(\mathrm{G})$ in which $\operatorname{ad}(\mathrm{G})$ is an ideal, and it is a Lie subalgebra.

**Theorem.** $\operatorname{Der}(\mathrm{G})\subseteq\mathrm{N}$, and a member $T$ of $\mathrm{N}$ lies in $\operatorname{Der}(\mathrm{G})$ if and only if $[T,\operatorname{ad}_x]=\operatorname{ad}_{Tx}$ for all $x$.

**Proof.** A derivation satisfies this by the proposition, hence lies in $\mathrm{N}$. Conversely a member of $\mathrm{N}$ satisfies $[T,\operatorname{ad}_x]=\operatorname{ad}_{\varphi(x)}$ for some linear $\varphi$ determined up to an element of the centre; the displayed condition says $\varphi=T$, which by the proposition is the Leibniz rule. $\square$

**Proposition (the inclusion is proper).** If $\mathrm{G}$ is not abelian and has nonzero centre then $\operatorname{Der}(\mathrm{G})\neq\mathrm{N}$.

**Proof.** The identity lies in $\mathrm{N}$, because $[\operatorname{id},\operatorname{ad}_x]=0$, and it is not a derivation by the remark. $\square$

**Example.** In the Heisenberg algebra the identity lies in $\mathrm{N}$ and not in $\operatorname{Der}(\mathrm{G})$; the discrepancy measures the centre, through which every operator commutes with $\operatorname{ad}(\mathrm{G})$.

## Inner and Outer Derivations

### The Adjoint Map and the Exact Sequence

**Proposition (the basic exact sequence).** The adjoint map $\operatorname{ad}:\mathrm{G}\to\operatorname{Der}(\mathrm{G})$ is a Lie algebra homomorphism with kernel $\mathrm{Z}(\mathrm{G})$, hence $\operatorname{Inn}(\mathrm{G})\cong\mathrm{G}/\mathrm{Z}(\mathrm{G})$ and

$$
0\longrightarrow\mathrm{Z}(\mathrm{G})\longrightarrow\mathrm{G}\xrightarrow{\operatorname{ad}}\operatorname{Der}(\mathrm{G})\longrightarrow\operatorname{Out}(\mathrm{G})\longrightarrow0 .
$$

**Proof.** The homomorphism property is $\operatorname{ad}_{[x,y]}=[\operatorname{ad}_x,\operatorname{ad}_y]$, which is the Jacobi identity; the kernel is the centre; the image is $\operatorname{Inn}(\mathrm{G})$; the quotient is $\operatorname{Out}(\mathrm{G})$. $\square$

**Corollary.** $\operatorname{Inn}(\mathrm{G})\cong\mathrm{G}$ exactly when $\mathrm{G}$ has trivial centre, and $\operatorname{Inn}(\mathrm{G})=0$ exactly when $\mathrm{G}$ is abelian.

### The Identification with the First Cohomology

**Theorem.** With coefficients in the adjoint module $\mathrm{G}$,

$$
\operatorname{Der}(\mathrm{G})=Z^1(\mathrm{G};\mathrm{G}),\qquad
\operatorname{Inn}(\mathrm{G})=B^1(\mathrm{G};\mathrm{G}),\qquad
\operatorname{Out}(\mathrm{G})=H^1(\mathrm{G};\mathrm{G}).
$$

**Proof.** The differential on a one-cochain $\delta:\mathrm{G}\to\mathrm{G}$ is $d\delta(x,y)=[x,\delta(y)]-[y,\delta(x)]-\delta([x,y])$; its vanishing is the Leibniz rule read with one argument transposed. The coboundaries are the inner derivations, by the identification recorded in *Lie Algebra Cohomology*, and the quotient is $\operatorname{Out}(\mathrm{G})$. $\square$

**Corollary.** $\operatorname{Out}(\mathrm{G})=0$ for a semisimple $\mathrm{G}$ over a field of characteristic zero, by the vanishing of the first cohomology with coefficients in the adjoint module, which is the first Whitehead lemma of *Lie Algebra Cohomology* and the cohomological form of the theorem of *Structure of Lie Algebras* that every derivation of such an algebra is inner.

## Derivations and the Operations

### Direct Sums

**Proposition.** Let $\mathrm{G}_1$ and $\mathrm{G}_2$ be Lie algebras. Then $\operatorname{Der}(\mathrm{G}_1\oplus\mathrm{G}_2)$ contains $\operatorname{Der}(\mathrm{G}_1)\oplus\operatorname{Der}(\mathrm{G}_2)$, and in addition contains the operators with a single cross component $\phi:\mathrm{G}_1\to\mathrm{G}_2$ or $\psi:\mathrm{G}_2\to\mathrm{G}_1$ that kills the derived subalgebra of the source and takes values in the centre of the target.

**Proof.** A derivation $D$ of the direct sum has four components, and the diagonal ones are derivations of the summands. For a single cross component $D(x_1,x_2)=(0,\phi(x_1))$ the Leibniz rule reads $\phi([x_1,y_1])=[\phi(x_1),y_2]+[x_2,\phi(y_1)]$; taking $x_2=y_2=0$ forces $\phi([x_1,y_1])=0$, so $\phi$ kills the derived subalgebra, and then the right-hand side must vanish for all $x_2,y_2$, so $\phi$ takes values in the centre. The converse is immediate. $\square$

**Corollary.** If both summands are perfect with trivial centre then $\operatorname{Der}(\mathrm{G}_1\oplus\mathrm{G}_2)=\operatorname{Der}(\mathrm{G}_1)\oplus\operatorname{Der}(\mathrm{G}_2)$.

### The Restricted Structure in Characteristic $p$

**Proposition (the iterated Leibniz rule).** For a derivation $D$ and all $x,y$ and all $n\geq0$,

$$
D^n([x,y])=\sum_{i=0}^{n}\binom{n}{i}\,[D^ix,D^{n-i}y],
$$

with $D^0=\operatorname{id}$.

**Proof.** Induction on $n$ using $D([u,v])=[Du,v]+[u,Dv]$ and Pascal's rule. $\square$

**Corollary (the $p$-th power of a derivation).** Let $K$ have characteristic $p>0$. If $D$ is a derivation then $D^p$ is a derivation.

**Proof.** With $n=p$ the binomial coefficient $\binom{p}{i}$ is divisible by $p$, hence zero in $K$, for $0<i<p$, so only the end terms survive: $D^p([x,y])=[D^px,y]+[x,D^py]$. $\square$

**Remark.** The corollary makes $\operatorname{Der}(\mathrm{G})$ a restricted Lie algebra under the $p$-map $D\mapsto D^p$ when $K$ has characteristic $p$; the restricted structure is treated with the graded Lie algebras in characteristic $p$, later in this Part. If a derivation is nilpotent then $\exp(D)$ is an automorphism, the nilpotent instance of the correspondence between the derivation algebra and the automorphism group of Part II.

## Worked Cases

### The Abelian Algebra

**Proposition.** If $\mathrm{G}$ is abelian then every linear operator is a derivation and

$$
\operatorname{Der}(\mathrm{G})=\operatorname{End}_K(\mathrm{G}),\qquad
\operatorname{Inn}(\mathrm{G})=0,\qquad
\operatorname{Out}(\mathrm{G})=\operatorname{End}_K(\mathrm{G}).
$$

**Proof.** The bracket vanishes identically, so the Leibniz rule is vacuous; the adjoint operators are all zero. $\square$

**Verified.** In dimensions $2$ and $3$ the derivation algebra has dimensions $4$ and $9$, in agreement with $\dim\operatorname{End}_K(K^n)=n^2$, and the adjoint image has dimension $0$.

### The Two-Dimensional Non-Abelian Algebra

Let $\mathrm{L}$ have basis $x,y$ with $[x,y]=x$. Then $\mathrm{L}$ has trivial centre and every derivation is inner.

**Proposition.** $\operatorname{Der}(\mathrm{L})=\operatorname{Inn}(\mathrm{L})$ has dimension $2$, so $\operatorname{Out}(\mathrm{L})=0$.

**Proof.** For $Dx=ax+cy$ and $Dy=bx+dy$ the Leibniz rule on the single bracket gives $Dx=(a+d)x$, so $c=d=0$; the derivations form the two-dimensional space killing $y$ and sending $x$ into $\operatorname{span}(x,y)$. The inner derivations $\operatorname{ad}_x,\operatorname{ad}_y$ are independent and span this space. $\square$

**Verified.** Solved as a linear system in the four matrix entries, the derivation space has dimension $2$, equal to the rank of the adjoint image.

### The Heisenberg Algebra

Let $\mathrm{H}$ have basis $x,y,z$ with $[x,y]=z$ and $z$ central.

**Proposition.** $\operatorname{Der}(\mathrm{H})$ has dimension $6$, $\operatorname{Inn}(\mathrm{H})$ has dimension $2$, and $\operatorname{Out}(\mathrm{H})$ has dimension $4$.

**Proof.** Write $Dx=a_1x+a_2y+a_3z$, $Dy=b_1x+b_2y+b_3z$, $Dz=c_1x+c_2y+c_3z$. The Leibniz rule on $[x,y]=z$ reads $Dz=[Dx,y]+[x,Dy]=a_1z+b_2z$, so $c_1=c_2=0$ and $c_3=a_1+b_2$, the six remaining coefficients being free. The inner derivations $\operatorname{ad}_x(y)=z$ and $\operatorname{ad}_y(x)=-z$ have dimension $2$ and kill $z$, so $\dim\operatorname{Out}(\mathrm{H})=6-2=4$. $\square$

**Example.** The derivation $D_0=\operatorname{diag}(1,1,2)$ is not inner, since every inner derivation kills $z$; its class is a nonzero outer derivation.

**Verified.** Solved as a linear system in the nine matrix entries: $\dim\operatorname{Der}(\mathrm{H})=6$ and the adjoint image has rank $2$.

### The Lie Algebra $\mathrm{SL}(2,K)$

Let $\mathrm{SL}(2,K)$ have basis $e,h,f$ with $[e,f]=h$, $[h,e]=2e$ and $[h,f]=-2f$; the notation is that of *Structure of Lie Algebras*, where the Lie algebra carries the name of the group.

**Proposition.** Every derivation of $\mathrm{SL}(2,K)$ is inner, $\operatorname{Der}(\mathrm{SL}(2,K))=\operatorname{Inn}(\mathrm{SL}(2,K))$ has dimension $3$, and $\operatorname{Out}(\mathrm{SL}(2,K))=0$.

**Proof.** This is the semisimple case of the theorem of *Structure of Lie Algebras*; the inner derivations already have dimension $3$ because the centre is zero, and direct solution of the derivation equations gives dimension $3$ as well. $\square$

**Verified.** Solved as a linear system in the nine matrix entries, the derivation space has dimension $3$, equal to the rank of the adjoint image; in particular $\operatorname{id}$ is not a derivation.

## Summary

A **derivation** of a Lie algebra $\mathrm{G}$ is a linear operator satisfying the Leibniz rule for the bracket, equivalently an operator with $[D,\operatorname{ad}_x]=\operatorname{ad}_{Dx}$ for every $x$. In this form the Leibniz rule says that $D$ normalises the subspace $\operatorname{ad}(\mathrm{G})$ with the induced operator equal to $D$ itself; the normaliser is a Lie subalgebra containing the derivations and strictly larger as soon as $\mathrm{G}$ is non-abelian with nonzero centre, the identity being the witness. The derivations form a Lie subalgebra of $\operatorname{End}_K(\mathrm{G})$, the inner derivations are an ideal, and $\operatorname{Out}(\mathrm{G})=\operatorname{Der}(\mathrm{G})/\operatorname{Inn}(\mathrm{G})$ is the quotient. The adjoint map is a homomorphism with kernel the centre, giving $\operatorname{Inn}(\mathrm{G})\cong\mathrm{G}/\mathrm{Z}(\mathrm{G})$ and the exact sequence $0\to\mathrm{Z}(\mathrm{G})\to\mathrm{G}\to\operatorname{Der}(\mathrm{G})\to\operatorname{Out}(\mathrm{G})\to0$. The derivations are the one-cocycles of the Chevalley–Eilenberg complex with coefficients in the adjoint module, the inner ones are the one-coboundaries, and $\operatorname{Out}(\mathrm{G})=H^1(\mathrm{G};\mathrm{G})$; in particular a semisimple $\mathrm{G}$ over a field of characteristic zero has no outer derivations.

A derivation carries the centre into itself. In characteristic $p$ the iterated Leibniz rule makes the $p$-th power $D^p$ a derivation, so $\operatorname{Der}(\mathrm{G})$ is restricted. The abelian algebra has $\operatorname{Der}=\operatorname{End}_K$ and $\operatorname{Inn}=0$; the two-dimensional non-abelian algebra is complete, with $\operatorname{Der}=\operatorname{Inn}$ of dimension $2$; the Heisenberg algebra has $\operatorname{Der}$ of dimension $6$, $\operatorname{Inn}$ of dimension $2$ and $\operatorname{Out}$ of dimension $4$; and $\mathrm{SL}(2,K)$ has dimension $3$ in both $\operatorname{Der}$ and $\operatorname{Inn}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | the base field, of arbitrary characteristic |
| $\mathrm{G}$ | a finite-dimensional Lie algebra over $K$ |
| $[x,y]$ | the bracket |
| $\operatorname{ad}_x(y)=[x,y]$ | the adjoint operator |
| $\mathrm{Z}(\mathrm{G})$ | the centre, the kernel of $\operatorname{ad}$ |
| $D,E$ | derivations |
| $\operatorname{Der}(\mathrm{G})$ | the Lie algebra of derivations |
| $\operatorname{Inn}(\mathrm{G})=\operatorname{ad}(\mathrm{G})$ | the inner derivations |
| $\operatorname{Out}(\mathrm{G})=\operatorname{Der}(\mathrm{G})/\operatorname{Inn}(\mathrm{G})$ | the outer derivations |
| $\mathrm{N}$ | the normaliser of $\operatorname{ad}(\mathrm{G})$ in $\operatorname{End}_K(\mathrm{G})$ |
| $Z^1,B^1,H^1$ | cocycles, coboundaries and cohomology of the adjoint module |
| $D^p$ | the $p$-th power, a derivation in characteristic $p$ |
| $\mathrm{L}$, $\mathrm{H}$ | the two-dimensional non-abelian algebra and the Heisenberg algebra |

## Further Reading

- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the derivation algebra, the inner and outer derivations and the restricted structure in positive characteristic.
- Nicolas Bourbaki, *Lie Groups and Lie Algebras*, Chapters 1–3 (Springer, 1989), for derivations as the infinitesimal automorphisms and the exact sequence of the adjoint map.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory*, Graduate Texts in Mathematics 9 (Springer, 1972), for the theorem that a semisimple Lie algebra over a field of characteristic zero has no outer derivations.
- Jean-Pierre Serre, *Lie Algebras and Lie Groups*, Lecture Notes in Mathematics 1500 (Springer, 1992), for the identification of the outer derivations with the first cohomology of the adjoint module.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the derivation algebra of an associative algebra, its normaliser and the Leibniz rule in operator form.
- Charles A. Weibel, *An Introduction to Homological Algebra*, Cambridge Studies in Advanced Mathematics 38 (Cambridge University Press, 1994), for the Chevalley–Eilenberg complex and the low-degree identifications.
