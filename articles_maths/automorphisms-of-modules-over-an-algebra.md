
# __Automorphisms of Modules over an Algebra__

## Introduction

The transformations of a module are its endomorphisms, and the invertible ones form its automorphism group. The object of this article is the pair

$$
\operatorname{End}_A(M) \quad \text{and} \quad \operatorname{Aut}_A(M)
$$

for a module $M$ over a possibly noncommutative algebra $A$. The first is a ring and the second its group of units, and the passage from $A$ to this pair records how much freedom an $A$-linear map retains once the whole algebra is required to commute with it. When $A=F$ is a field the requirement is vacuous, and the pair is the full ring of $F$-linear maps together with the full general linear group; over a larger algebra the condition is severe, and the gap between $A$-linear and merely $R$-linear maps is not covered here.

The conventions are those of the companion article *Modules over an Algebra*: $R$ is a commutative ring with $1 \neq 0$, and $A$ is a unital associative $R$-algebra, generally noncommutative. Modules are left modules unless stated, $A^{\times}$ is the group of units of $A$, and $Z(A)$ is the center. The regular module ${}_A A$ acts on itself by left multiplication, and the endomorphisms of the regular module were identified in the companion article as the right multiplications. That identification is the base case of everything below, and it is the reason the noncommutative case behaves asymmetrically.

Two facts are used throughout and are stated once. The first is that $\operatorname{End}_A(M)$ is the **centralizer** of the action of $A$ in the ring $\operatorname{End}_R(M)$ of $R$-linear maps: an $R$-linear map is $A$-linear precisely when it commutes with every operator of the representation. The second is Schur's lemma, proved in the companion article and recalled here in the form needed: a nonzero homomorphism between simple modules is an isomorphism, so the endomorphism ring of a simple module is a division ring. The second fact is the engine of the theory, and it converts questions about transformations into questions about division rings and matrices over them.

## Endomorphisms and Automorphisms

### Definition

Let $M$ be a left $A$-module. The **endomorphism ring** of $M$ is

$$
\operatorname{End}_A(M)=\{f: M \to M : f \text{ is } A\text{-linear}\},
$$

with addition defined pointwise, $(f+g)(m)=f(m)+g(m)$, and multiplication given by composition, $(fg)(m)=f(g(m))$. Addition makes it an abelian group, composition is associative and distributes over addition, the identity map is a unit, and composition is not commutative in general. Thus $\operatorname{End}_A(M)$ is a unital associative ring. It is an $R$-algebra, since $rf$ defined by $(rf)(m)=r f(m)=f(rm)$ is again $A$-linear and central in the ring.

The **automorphism group** of $M$ is the group of units of this ring,

$$
\operatorname{Aut}_A(M)=\{f \in \operatorname{End}_A(M) : f \text{ is bijective}\}=\operatorname{End}_A(M)^{\times}.
$$

Both are invariant under isomorphism: an isomorphism $u: M \to N$ induces a ring isomorphism $\operatorname{End}_A(M)\to\operatorname{End}_A(N)$, $f \mapsto u f u^{-1}$, and it carries $\operatorname{Aut}_A(M)$ onto $\operatorname{Aut}_A(N)$.

### The centralizer description

Fix the action, that is, the $R$-algebra homomorphism

$$
\rho : A \to \operatorname{End}_R(M), \qquad \rho(a)(m)=am.
$$

An $R$-linear map $f \in \operatorname{End}_R(M)$ is $A$-linear exactly when $f(am)=a f(m)$ for all $a \in A$ and $m \in M$, that is, when $f \rho(a)=\rho(a) f$ for all $a$. Therefore

$$
\operatorname{End}_A(M)=\{f \in \operatorname{End}_R(M) : f \rho(a)=\rho(a) f \text{ for all } a \in A\}=\rho(A)',
$$

the **commutant**, or centralizer, of the image of $A$ in $\operatorname{End}_R(M)$. This is the single most useful description of the endomorphism ring. It shows immediately that $\operatorname{End}_A(M)$ depends only on the image $\rho(A)$, hence only on the faithful quotient $A/\operatorname{Ann}_A(M)$, and that enlarging $A$ shrinks its commutant.

### $A$-linear versus $R$-linear

Because $\rho$ is an $R$-algebra homomorphism, the inclusion

$$
\operatorname{End}_A(M) \subseteq \operatorname{End}_R(M)
$$

always holds, and it is strict in general. If $A=R$ is the base ring acting by scalars, then $\rho(A)=R\cdot\mathrm{id}$ is central in $\operatorname{End}_R(M)$, so $\operatorname{End}_A(M)=\operatorname{End}_R(M)$: over a commutative base ring, and in particular over a field, every $R$-linear map is $A$-linear because there is nothing else for the scalars to impose. As soon as the action of $A$ is larger than the scalars, that is $\rho(A)\supsetneq R\cdot\mathrm{id}_M$, the condition $f\rho(a)=\rho(a) f$ removes maps, and the quotient

$$
\operatorname{End}_R(M)/\operatorname{End}_A(M)
$$

measures the loss. The worked cases over $\mathbb{H}$ and $\mathbb{B}$ below make the loss concrete: over $\mathbb{B}$ the $\mathbb{C}$-linear endomorphisms of the defining module form a four-dimensional algebra, while the $\mathbb{B}$-linear ones are only the scalars.

## The Regular Module

The action of $A$ on itself by left multiplication is the basic example, and its endomorphisms are computed completely. Recall from *Modules over an Algebra* the theorem that right multiplication identifies the opposite algebra with the endomorphism ring of the left regular module.

**Theorem.** The map

$$
A^{\mathrm{op}} \xrightarrow{\ \sim\ } \operatorname{End}_A({}_A A), \qquad a \longmapsto R_a, \quad R_a(b)=ba,
$$

is an isomorphism of $R$-algebras. Consequently

$$
\operatorname{Aut}_A({}_A A) \cong (A^{\mathrm{op}})^{\times} \cong A^{\times}.
$$

*Proof.* The isomorphism is proved in *Modules over an Algebra*, §The Regular Module and Its Endomorphisms. It is $R$-linear in $a$ because right multiplication is $R$-bilinear, and it carries the reversed product of $A^{\mathrm{op}}$ to composition: $R_{a a'}(b)=b(aa')=(ba)a'=R_{a'}(R_a(b))$. Taking units gives the second statement. $\square$

Three consequences deserve emphasis. First, the theorem is asymmetric: it is right multiplication, not left multiplication, that gives $A$-linear endomorphisms of ${}_A A$. Left multiplication by $a$ is the module action itself and is $A$-linear only in the trivial sense that it is the action of an element on the module; as a transformation of $A$ it is not $A$-linear unless $a$ is central. Second, the automorphism group of the regular module is the group of units of $A$, so it is small in a precise sense: for $A=M_n(F)$ it is $GL_n(F)$, and for a division algebra $D$ it is $D^{\times}$. Third, the group $\operatorname{Aut}_A({}_A A)$ is not the group of algebra automorphisms of $A$: the latter consists of the bijective $R$-algebra maps $A \to A$ preserving the product, and it can be strictly larger, as the biquaternion case below shows. Automorphisms of the module and automorphisms of the algebra are different objects, and only the first is discussed here.

## What $A$-Linearity Forces

### The density theorem

The commutant description has a strong structural converse. A simple module is generated by any nonzero element, and the density theorem says that on a finite set of linearly independent elements the action can realise arbitrary prescribed values, as far as the endomorphism division ring permits.

**Theorem (Jacobson density).** Let $S$ be a simple left $A$-module, put $D=\operatorname{End}_A(S)$, and regard $S$ as a left $D$-module. Let $x_1,\dots,x_n \in S$ be $D$-linearly independent and let $y_1,\dots,y_n \in S$ be arbitrary. Then there exists $a \in A$ such that

$$
a x_i=y_i \qquad (i=1,\dots,n).
$$

Equivalently, the image of $A$ in $\operatorname{End}_D(S)$ is dense for the finite topology.

*Proof sketch.* For $n=1$ simplicity gives $Ax_1=S$, so some $a$ carries $x_1$ to $y_1$. For general $n$, consider the submodule $N=\{(ax_1,\dots,ax_n) : a \in A\}$ of $S^{\oplus n}$. If the conclusion failed for some $(y_1,\dots,y_n)$, then $N$ would be a proper submodule of the semisimple module $S^{\oplus n}$ and would miss a simple summand; composing a projection onto that summand with the resulting relation forces a nontrivial $D$-linear dependence among the $x_i$, contradicting independence. $\square$

The theorem is standard and is quoted as such. It has the following corollary, which is the case used most often.

**Corollary.** Let $S$ be a simple left $A$-module with $D=\operatorname{End}_A(S)$ and suppose $S$ is finite-dimensional over $D$. Then the natural map

$$
A/\operatorname{Ann}_A(S) \longrightarrow \operatorname{End}_D(S)
$$

is an isomorphism. In particular, if $A$ is finite-dimensional over a field and $S$ is a finite-dimensional simple module with $D=\operatorname{End}_A(S)$, then $A/\operatorname{Ann}_A(S) \cong M_n(D^{\mathrm{op}})$ for $n=\dim_D S$, the opposite being the computation $\operatorname{End}_D(D^n)\cong M_n(D^{\mathrm{op}})$ of §Over a Division Ring applied to a $D$-basis of $S$.

*Proof.* Density gives surjectivity when the finite topology is discrete, which is the case when $S$ is finite-dimensional over $D$; the kernel is $\operatorname{Ann}_A(S)$; the identification of $\operatorname{End}_D(S)$ with $M_n(D^{\mathrm{op}})$ is the choice of a $D$-basis. $\square$

This corollary is the precise sense in which a finite-dimensional simple module is the defining module of a matrix algebra. It is the double centralizer statement in the form used by representation theory.

## Schur's Lemma and Simple Modules

**Theorem (Schur).** Let $S$ and $T$ be simple left $A$-modules and let $f \in \operatorname{Hom}_A(S,T)$. Then either $f=0$ or $f$ is an isomorphism. Hence

$$
\operatorname{Hom}_A(S,T)=\begin{cases} 0, & S \not\cong T,\\ D, & S \cong T,\end{cases}
$$

where $D=\operatorname{End}_A(S)$ is a division ring. Therefore $\operatorname{Aut}_A(S)=D^{\times}$.

*Proof.* The kernel and image of $f$ are submodules, so each is $0$ or everything; a nonzero $f$ has zero kernel and full image, hence is bijective. An $A$-linear bijection has $A$-linear inverse, and a nonzero endomorphism of $S$ is invertible, so $\operatorname{End}_A(S)$ is a division ring whose units are the automorphisms. $\square$

Consequently, for a simple module the only $A$-linear transformations are zero and invertible, and the invertible ones form the multiplicative group of a division ring. In particular $\operatorname{Aut}_A(S)$ is the unit group of the division ring $D$, not a matrix group, and the size of $D$ depends on the base field: for $A=M_n(\mathbb{C})$ the simple module is $\mathbb{C}^n$ and $D=\mathbb{C}$, so $\operatorname{Aut}_A(\mathbb{C}^n)=\mathbb{C}^{\times}$, while over $\mathbb{R}$ the same matrix algebra has $D=\mathbb{R}$ and automorphism group $\mathbb{R}^{\times}$. Over a non-algebraically-closed field the simple module of a finite-dimensional algebra can have endomorphism ring a larger division algebra.

## The Case $A=M_n(F)$

Let $F$ be a field, let $A=M_n(F)$, and let $S=F^n$ be the defining module of column vectors. Two endomorphism rings arise, one for the simple module and one for the regular module, and their contrast is the heart of the example.

**Theorem.** $\operatorname{End}_{M_n(F)}(S)\cong F$.

*Proof.* Regard $S$ as the space of column vectors and identify $\operatorname{End}_F(S)$ with $M_n(F)$ acting on the left. An element $T=(t_{kl})$ of $\operatorname{End}_F(S)$ is $A$-linear precisely when $XT=TX$ for every $X \in M_n(F)$, that is, when $T$ lies in the center of $M_n(F)$. To compute that center, let $E_{ij}$ be the matrix units and write $E_{ij}T=TE_{ij}$ in coordinates:

$$
\delta_{ki}\,t_{jl}=t_{ki}\,\delta_{jl}.
$$

Taking $i=j$ gives $t_{il}=t_{ii}\delta_{il}$, so $T$ is diagonal; taking $i \neq j$, $k=i$, $l=j$ gives $t_{jj}=t_{ii}$, so all diagonal entries are equal. Hence $T=\lambda I$ with $\lambda \in F$, and every scalar matrix is central. Therefore $\operatorname{End}_{M_n(F)}(S)\cong F$. $\square$

**Corollary.** $\operatorname{Aut}_{M_n(F)}(S)\cong F^{\times}$.

The corollary is the extreme case of Schur's lemma: the only invertible transformations of the defining module commuting with the whole matrix algebra are the nonzero scalars. Passing from $F$-linear to $M_n(F)$-linear therefore discards the whole of $GL_n(F)$ except its center.

**Theorem.** For the regular module,

$$
\operatorname{End}_{M_n(F)}(M_n(F))\cong M_n(F)^{\mathrm{op}}\cong M_n(F), \qquad
\operatorname{Aut}_{M_n(F)}(M_n(F))\cong GL_n(F).
$$

*Proof.* The first isomorphism is the theorem on the regular module, applied to $A=M_n(F)$. The transpose $X \mapsto X^{\mathsf T}$ is an $F$-algebra isomorphism $M_n(F)^{\mathrm{op}}\to M_n(F)$, since $(XY)^{\mathsf T}=Y^{\mathsf T}X^{\mathsf T}$. Taking units gives $\operatorname{Aut}_{M_n(F)}(M_n(F))\cong GL_n(F)$. $\square$

Thus the regular module recovers the full matrix group $GL_n(F)$ as its automorphism group, while the simple module contributes only the scalars. Both statements are instances of the general principle that $\operatorname{Aut}_A(M)$ is large when $M$ is the algebra and small when $M$ is rigid.

## Over a Division Ring

Let $D$ be a division ring and let $M=D^n$ be a free left $D$-module, so that $A=D$ acts by scalars. Choosing a basis $e_1,\dots,e_n$, a $D$-linear endomorphism is described by its matrix, and the correspondence between endomorphisms and matrices is a ring anti-isomorphism onto $M_n(D)$, equivalently a ring isomorphism

$$
\operatorname{End}_D(D^n) \cong M_n(D^{\mathrm{op}}),
$$

as one sees by comparing composition with matrix multiplication, or from the general identity $\operatorname{End}_D(M^n)\cong M_n(\operatorname{End}_D(M))$ with $M=D$ and $\operatorname{End}_D(D)\cong D^{\mathrm{op}}$ by the theorem on the regular module. Since every group is isomorphic to its opposite by $g \mapsto g^{-1}$, and $GL_n(D^{\mathrm{op}})$ is the opposite group of $GL_n(D)$, the automorphism group is unambiguous:

$$
\operatorname{Aut}_D(D^n)\cong GL_n(D).
$$

When $D$ is commutative, $D^{\mathrm{op}}=D$ and the endomorphism ring is $M_n(D)$ without qualification; when $D=\mathbb{H}$, the two are identified by quaternion conjugation in the sense explained below. If instead $A=M_n(D)$ and $M=A$ is the regular module, the theorem of §The Regular Module gives

$$
\operatorname{End}_A(A)\cong A^{\mathrm{op}}, \qquad \operatorname{Aut}_A(A)\cong A^{\times}=GL_n(D),
$$

the last equality being the definition of $GL_n(D)$ as the group of invertible matrices over a division ring. So $GL_n(D)$ appears as the automorphism group of the regular module over $M_n(D)$, and it is the basic noncommutative linear group of this category.

A caution on the opposite. For $D$ a field, transposition identifies $M_n(D)$ with its opposite; for $\mathbb{H}$, quaternion conjugation $q \mapsto \bar{q}$ is an anti-automorphism with $\bar{q}q=N(q)$, and applying it entrywise identifies $M_n(\mathbb{H})$ with $M_n(\mathbb{H})^{\mathrm{op}}$. For a general division ring the two opposites may fail to be isomorphic, and this is why $\operatorname{End}_D(D^n)$ is stated with $D^{\mathrm{op}}$. The group $GL_n(D)$ is unaffected, because a group is isomorphic to its opposite.

## Worked Case: The Quaternions

The quaternions $\mathbb{H}$ are a division algebra over $\mathbb{R}$, so every $\mathbb{H}$-module is free by *Modules* §19. Let $M=\mathbb{H}^n$.

**Proposition.** $\operatorname{End}_{\mathbb{H}}(\mathbb{H}^n)\cong M_n(\mathbb{H}^{\mathrm{op}})$, and $\operatorname{Aut}_{\mathbb{H}}(\mathbb{H}^n)\cong GL_n(\mathbb{H})$. In particular $\operatorname{Aut}_{\mathbb{H}}(\mathbb{H})\cong \mathbb{H}^{\times}$, the nonzero quaternions.

The identification is the one above with $D=\mathbb{H}$, using that $\mathbb{H}^{\mathrm{op}}\cong\mathbb{H}$. For $n=1$ it is instructive to see the asymmetry directly, because it is the prototype of the biquaternion case. Regard $\mathbb{H}$ as a left $\mathbb{H}$-module and as a real vector space of dimension four. The endomorphism ring over $\mathbb{R}$ is $\operatorname{End}_{\mathbb{R}}(\mathbb{H})\cong M_4(\mathbb{R})$, of real dimension $16$. The $\mathbb{H}$-linear endomorphisms are the right multiplications $R_q(x)=xq$, and

$$
\operatorname{End}_{\mathbb{H}}(\mathbb{H})=\{R_q : q \in \mathbb{H}\}\cong \mathbb{H}^{\mathrm{op}}\cong\mathbb{H},
$$

of real dimension $4$. Left multiplication $L_q(x)=qx$ is the module action; it is not $\mathbb{H}$-linear unless $q$ is real, since for non-central $q$ and any $x$, $L_q(q'x)=qq'x$ while $q'L_q(x)=q'qx$, and $qq' \neq q'q$ in general. Thus the image of the algebra inside the $\mathbb{R}$-endomorphism ring is the set of left multiplications, whereas the commutant is the set of right multiplications. This is the simplest visible sign that $\mathbb{H}$ is not commutative, and it says that over a division ring the endomorphism ring of a free module is the matrix ring over the opposite division ring.

## Worked Case: The Biquaternions

Let $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ be the biquaternion algebra, viewed over $\mathbb{C}$, where $\mathbb{B}\cong M_2(\mathbb{C})$. The basis is $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$, the scalar imaginary $i$ is central, and a general element is $\tilde{Q}=\sum_\mu Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$. Since $\mathbb{B}$ is a matrix algebra and not a division algebra, its module theory is that of $M_2(\mathbb{C})$, and the transformations of its modules separate sharply into a $\mathbb{C}$-linear part and a $\mathbb{B}$-linear part.

Let $S=\mathbb{C}^2$ be the defining module. Then $\mathbb{B}\cong M_2(\mathbb{C})$ acts on $S$ by matrices, and:

$$
\operatorname{End}_{\mathbb{B}}(S)\cong\mathbb{C}, \qquad \operatorname{Aut}_{\mathbb{B}}(S)\cong\mathbb{C}^{\times}, \qquad
\operatorname{End}_{\mathbb{C}}(S)=M_2(\mathbb{C})\cong\mathbb{B}.
$$

The first two are Schur's lemma and the computation of §The Case $A=M_n(F)$ with $n=2$, $F=\mathbb{C}$. The third is the statement that every $\mathbb{C}$-linear map of $S$ is given by a biquaternion: $\mathbb{B}$ is exactly the full endomorphism ring of its own simple module, by the double centralizer corollary. The contrast is the point. A $\mathbb{C}$-linear endomorphism of $S$ is an arbitrary $2\times2$ complex matrix, a four-complex-dimensional family, and every such matrix is multiplication by an element of $\mathbb{B}$; a $\mathbb{B}$-linear endomorphism is multiplication by a scalar alone, a one-complex-dimensional family. The intermediate group $GL_2(\mathbb{C})$ therefore contains transformations of $S$ that are not $\mathbb{B}$-linear; only its center $\mathbb{C}^{\times}$ survives the restriction.

For the regular module the theorem on the regular module gives

$$
\operatorname{End}_{\mathbb{B}}(\mathbb{B})\cong\mathbb{B}^{\mathrm{op}}\cong\mathbb{B}\cong M_2(\mathbb{C}), \qquad
\operatorname{Aut}_{\mathbb{B}}(\mathbb{B})\cong\mathbb{B}^{\times}\cong GL_2(\mathbb{C}),
$$

using that $\mathbb{B}$ is isomorphic to its opposite (quaternion conjugation is a $\mathbb{C}$-linear anti-automorphism) and that the group of units of $\mathbb{B}$ is the set of elements of nonzero norm, identified with $GL_2(\mathbb{C})$ under the matrix representative. Equivalently $\operatorname{Aut}_{\mathbb{B}}(\mathbb{B})=GL_2(\mathbb{C})$.

### Why the zero divisors obstruct a basis

The biquaternion algebra has zero divisors: a nonzero $\tilde{Q}$ is a zero divisor exactly when its norm form vanishes, $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}=0$. This has an immediate effect on endomorphisms and on bases. In any free module with basis $B$, a basis element $b$ has trivial annihilator: if $ab=0$ then $a$ must vanish, since the coefficient of $b$ in the expansion of $ab$ is the whole of $a$. But a zero divisor $\tilde{Q}$ has $\operatorname{Ann}_{\mathbb{B}}(\tilde{Q})\neq 0$, so $\tilde{Q}$ cannot occur in a basis. More: the cyclic module $\mathbb{B}\tilde{Q}$ is nonzero and not free. A free module of rank $r$ needs at least $r$ generators, so a free quotient of ${}_\mathbb{B}\mathbb{B}$ generated by one element can have rank at most one; and rank one would give $\mathbb{B}\tilde{Q}\cong\mathbb{B}$ with $\tilde{Q}$ the image of $1_{\mathbb{B}}$, forcing $\operatorname{Ann}_{\mathbb{B}}(\tilde{Q})=0$. Hence

$$
\tilde{Q} \text{ a zero divisor} \implies \mathbb{B}\tilde{Q} \text{ is a nonzero cyclic module that is not free.}
$$

The same argument explains why not every $\mathbb{B}$-module is free and, consequently, why $\operatorname{Aut}_{\mathbb{B}}(M)$ cannot in general be a full linear group. For the regular module the automorphism group is $\mathbb{B}^{\times}$, and the zero divisors are exactly the elements excluded from it: an automorphism is invertible, and an invertible element is never a zero divisor. For the defining module the automorphism group is the scalars, and no zero divisor is a scalar since $N(\lambda)=\lambda^2 \neq 0$ for $\lambda \neq 0$.

### Automorphisms of the module and of the algebra

It is worth recording what $\operatorname{Aut}_{\mathbb{B}}(\mathbb{B})\cong GL_2(\mathbb{C})$ is not. It is the group of $\mathbb{B}$-linear automorphisms of the regular module, and these are the right multiplications by units. The group of $\mathbb{C}$-algebra automorphisms of $\mathbb{B}$ is

$$
\operatorname{Aut}_{\mathbb{C}\text{-alg}}(\mathbb{B})\cong PGL(2,\mathbb{C}),
$$

by the Skolem–Noether theorem, and over $\mathbb{R}$ it is $PGL(2,\mathbb{C})\rtimes\mathbb{Z}/2$; these are computed . The two groups differ: $GL_2(\mathbb{C})$ and $PGL(2,\mathbb{C})$ have different dimensions, and an algebra automorphism need not be a module automorphism of the regular module, nor conversely. The module automorphism group acts on the module and commutes with the algebra; the algebra automorphism group acts on the algebra and preserves its product.

## Transport along Morita Equivalence

An equivalence of module categories carries endomorphism rings and automorphism groups across. Let $A$ and $B$ be $R$-algebras and let

$$
F: \operatorname{Mod}(A) \to \operatorname{Mod}(B)
$$

be an $R$-linear equivalence, as . Because an equivalence is fully faithful and additive, it induces a ring isomorphism

$$
\operatorname{End}_A(M) \xrightarrow{\ \sim\ } \operatorname{End}_B(F(M)), \qquad f \longmapsto F(f),
$$

for every left $A$-module $M$, and therefore a group isomorphism $\operatorname{Aut}_A(M)\cong\operatorname{Aut}_B(F(M))$. In particular the whole representation theory of the endomorphism rings is a Morita invariant, and the examples above transport: the simple module of $M_n(A)$ corresponds under the equivalence to the simple module of $A$, with the same endomorphism division ring, which is why $\operatorname{End}_{M_n(F)}(F^n)\cong F$ agrees with the case $n=1$.

The standard instance is the equivalence between $\operatorname{Mod}(A)$ and $\operatorname{Mod}(M_n(A))$, whose inverse functors are

$$
S \longmapsto A^n \otimes_A S, \qquad T \longmapsto \operatorname{Hom}_{M_n(A)}(A^n, T),
$$

with $A^n$ regarded as an $(M_n(A),A)$-bimodule. Under it the defining module $S=F^n$ of $M_n(F)$ corresponds to $F$ as a module over $F$, and the endomorphism rings match: $\operatorname{End}_F(F)\cong F$. For the biquaternion algebra, this is the algebraic reason the module theory of $\mathbb{B}\cong M_2(\mathbb{C})$ reduces to the module theory of $\mathbb{C}$: the two algebras are Morita equivalent, and $\operatorname{Aut}_{\mathbb{B}}$ of a module is $\operatorname{Aut}_{\mathbb{C}}$ of the corresponding complex vector space.

## Automorphisms and Representations

The original meaning of a representation of an algebra is a homomorphism $\rho: A \to \operatorname{End}_F(V)$ of $F$-algebras. In the language of this category it is the same thing as a left module structure on $V$, and the endomorphism ring is the commutant:

$$
\operatorname{End}_A(V)=\rho(A)'=\{T \in \operatorname{End}_F(V) : T\rho(a)=\rho(a)T \text{ for all } a\}.
$$

The amount by which $\rho$ fails to be surjective is measured exactly by the size of the commutant. If $V$ is finite-dimensional over an algebraically closed field $F$ and is simple, Schur's lemma gives $\operatorname{End}_A(V)=F$, and the density theorem gives that $\rho$ is surjective, so $A/\ker \rho \cong \operatorname{End}_F(V)$: an irreducible finite-dimensional representation over an algebraically closed field is a quotient of the algebra, and the algebra acts as the whole endomorphism ring of its carrier. If $V$ is not simple, the commutant is the ring of intertwiners of the semisimple decomposition and is a product of matrix rings over the endomorphism division rings of the simple constituents.

The group $\operatorname{Aut}_A(V)$ is the group of invertible **intertwining operators**, that is, of equivalences of the representation with itself. For a simple representation it is the unit group of a division ring, by Schur's lemma; for a direct sum $V=S_1\oplus\cdots\oplus S_k$ of pairwise non-isomorphic simple modules it is the product $\prod_i \operatorname{Aut}_A(S_i)$ of division-ring unit groups, since there are no nonzero maps between distinct simple modules; and when repeated simple summands occur, matrices over the division rings appear, by the theorem of §The Case $A=M_n(F)$ applied in each isotypic component. This is the general shape of $\operatorname{Aut}_A(M)$ for a semisimple module, and it is developed .

## Summary

For a left $A$-module $M$, the endomorphisms $\operatorname{End}_A(M)$ form a unital $R$-algebra, and its units are the automorphisms $\operatorname{Aut}_A(M)$. The endomorphism ring is the commutant of the action of $A$ inside $\operatorname{End}_R(M)$, so it depends only on the faithful quotient $A/\operatorname{Ann}_A(M)$; when $A=R$ acts by scalars every $R$-linear map is $A$-linear, and the inclusion $\operatorname{End}_A(M)\subseteq\operatorname{End}_R(M)$ is strict as soon as the action of $A$ is larger than the scalars, that is $\rho(A)\supsetneq R\cdot\mathrm{id}_M$; a module on which $A$ happens to act through the base ring has $\operatorname{End}_A(M)=\operatorname{End}_R(M)$. For the regular module, right multiplication gives $\operatorname{End}_A({}_A A)\cong A^{\mathrm{op}}$ and $\operatorname{Aut}_A({}_A A)\cong A^{\times}$, so right multiplications are the $\mathbb{H}$-linear endomorphisms of $\mathbb{H}$ and the images of the module action (left multiplications) are not, unless central.

Schur's lemma makes $\operatorname{End}_A(S)$ a division ring for simple $S$, with $\operatorname{Aut}_A(S)$ its unit group, and the density theorem gives the converse structure: a finite-dimensional simple module over a finite-dimensional algebra is the defining module of a matrix algebra over the opposite of that division ring, $A/\operatorname{Ann}_A(S)\cong M_n(D^{\mathrm{op}})$. For $A=M_n(F)$ the defining module has commutant $F$ and automorphism group $F^{\times}$, while the regular module has endomorphism ring $M_n(F)^{\mathrm{op}}$ and automorphism group $GL_n(F)$; over a division ring $D$ the free module $D^n$ has automorphism group $GL_n(D)$, and the regular module over $M_n(D)$ also has automorphism group $GL_n(D)$. The worked biquaternion case separates the $\mathbb{C}$-linear from the $\mathbb{B}$-linear: $\operatorname{End}_{\mathbb{C}}(S)=\mathbb{B}$ while $\operatorname{End}_{\mathbb{B}}(S)=\mathbb{C}$, and the zero divisors of $\mathbb{B}$, being exactly the non-units, obstruct bases because a basis element must have trivial annihilator. All of it transports along Morita equivalence, which preserves endomorphism rings and automorphism groups; hence the equivalence of $\operatorname{Mod}(\mathbb{B})$ with $\operatorname{Mod}(\mathbb{C})$ explains the reduction of the biquaternion module theory to complex linear algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | commutative ring with identity, the base ring |
| $F$ | a field |
| $A$ | unital associative $R$-algebra, generally noncommutative |
| $A^{\mathrm{op}}$ | opposite algebra, product $a \cdot_{\mathrm{op}} b=ba$ |
| $A^{\times}$ | group of units of $A$ |
| $Z(A)$ | center of $A$ |
| $M$, $N$, $S$ | left $A$-modules; $S$ simple |
| ${}_A A$ | left regular module |
| $\rho : A \to \operatorname{End}_R(M)$ | the action homomorphism |
| $\rho(A)'$ | commutant, $=\{f : f\rho(a)=\rho(a)f\}$ |
| $\operatorname{End}_A(M)$ | endomorphism ring of $M$ |
| $\operatorname{Aut}_A(M)$ | automorphism group, $=\operatorname{End}_A(M)^{\times}$ |
| $R_a(b)=ba$ | right multiplication, an endomorphism of ${}_A A$ |
| $L_a(b)=ab$ | left multiplication, the module action |
| $M_n(D)$ | matrix ring over a division ring $D$ |
| $GL_n(D)$ | group of invertible $n \times n$ matrices over $D$ |
| $D=\operatorname{End}_A(S)$ | division ring of a simple module |
| $\mathbb{H}$ | quaternions |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | biquaternions, $\cong M_2(\mathbb{C})$ over $\mathbb{C}$ |
| $S=\mathbb{C}^2$ | defining module of $\mathbb{B}$ |
| $N(\tilde{Q})=\tilde{Q}\bar{\tilde{Q}}$ | norm form of $\mathbb{B}$ |
| $\operatorname{Mod}(A)$ | category of left $A$-modules |





## Further Reading

- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 2nd ed. 1992), for endomorphism rings, the density theorem, and the structure of the regular module.
- Nicolas Bourbaki, *Algebra I* (Springer, 1989), for the density and double centralizer theorems in the module setting.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for the endomorphism ring of a free module over a division ring and linear algebra over a skew field.
- I. N. Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the Jacobson density theorem and its consequences.
- Nathan Jacobson, *Structure of Rings* (American Mathematical Society, 1956), for the density theorem in its original form.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for Schur's lemma, division rings as endomorphism rings, and semisimple modules.
- T. Y. Lam, *Lectures on Modules and Rings* (Springer, 1999), for the centralizer description of $\operatorname{End}_A(M)$.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the endomorphism rings of simple modules over finite-dimensional algebras.
- John Voight, *Quaternion Algebras* (Springer, 2021), for the quaternion and biquaternion linear algebra used in the worked cases.
