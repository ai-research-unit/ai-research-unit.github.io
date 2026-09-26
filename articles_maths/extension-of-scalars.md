
# __Extension of Scalars__

## Introduction

A ring homomorphism $\varphi:R \to S$ allows every $S$-module to be viewed as an $R$-module by restriction of scalars, and, in the other direction, every $R$-module to be converted into an $S$-module by extension of scalars, $M \mapsto S \otimes_R M$. The two constructions are adjoint, so extension is a left adjoint and is right exact, while restriction is a forgetful functor and is exact. Extension of scalars is also called base change, and it is the operation that changes the ring of coefficients: it is how a real vector space becomes complex, how a complex vector space becomes real again, and how a module over a quotient $R/I$ is seen to be $M/IM$.

Throughout, $\varphi:R \to S$ is a homomorphism of commutative rings with $1 \neq 0$, $S$ is regarded as an $R$-module via $\varphi$, and all tensor products are over $R$ unless indicated. The template is the balanced product constructed in the companion article of this category on the balanced product, and its right exactness, established in the companion article on flatness and exactness, is used throughout.

## Extension of Scalars

### Definition

**Definition.** Let $M$ be an $R$-module. The **extension of scalars** of $M$ along $\varphi$ is the $S$-module

$$
M_S \;=\; S \otimes_R M ,
$$

with $S$-action $s \cdot (s' \otimes m)=(ss') \otimes m$.

**Proposition.** The action is well defined and makes $M_S$ an $S$-module; the map $M \to M_S$, $m \mapsto 1 \otimes m$, is $R$-linear, and $M_S$ is generated over $S$ by the image of this map.

*Proof.* For fixed $s$ the map $(s',m) \mapsto ss' \otimes m$ is balanced and therefore induces an $R$-linear endomorphism of $M_S$; these endomorphisms assemble into an $S$-action because multiplication in $S$ is associative and unital. The map $m \mapsto 1 \otimes m$ is additive and $R$-linear since $r(1 \otimes m)=1 \otimes rm$; and $s \otimes m=s(1 \otimes m)$, so the image generates. $\square$

### The Adjunction with Restriction of Scalars

**Definition.** If $N$ is an $S$-module, its **restriction of scalars** to $R$ is the $R$-module $\operatorname{Res}N$ with the same underlying abelian group and $r \cdot n=\varphi(r)n$.

**Theorem.** Extension and restriction of scalars are adjoint: for every $R$-module $M$ and every $S$-module $N$ there is a natural bijection

$$
\operatorname{Hom}_S(S \otimes_R M,\,N) \;\cong\; \operatorname{Hom}_R(M,\,\operatorname{Res}N).
$$

*Proof.* Given an $S$-linear $\Phi:S \otimes_R M \to N$, the map $m \mapsto \Phi(1 \otimes m)$ is $R$-linear, since $\Phi(1 \otimes rm)=\Phi(r(1 \otimes m))=r\Phi(1 \otimes m)$. Conversely, given an $R$-linear $\psi:M \to \operatorname{Res}N$, the map $S \times M \to N$, $(s,m) \mapsto s\,\psi(m)$, is balanced: it is additive in each variable, and $(sr,m)$ and $(s,rm)$ both map to $s\varphi(r)\psi(m)=s\psi(rm)$. It therefore induces an $S$-linear $\Psi:S \otimes_R M \to N$ with $\Psi(s \otimes m)=s\psi(m)$. The two constructions are inverse, and naturality is immediate. $\square$

**Corollary.** Extension of scalars is a functor $R\text{-}\mathbf{Mod} \to S\text{-}\mathbf{Mod}$, right exact, and exact whenever $S$ is flat as an $R$-module; it preserves direct sums and is additive on homomorphisms, $\varphi_*(M \oplus M') \cong \varphi_*M \oplus \varphi_*M'$. If $S$ is free as an $R$-module, in particular if $R$ and $S$ are fields, extension of scalars is exact.

*Proof.* The right exactness is that of the tensor product. The preservation of direct sums is the isomorphism $S \otimes_R (M \oplus M') \cong (S \otimes_R M) \oplus (S \otimes_R M')$ from the companion article on the balanced product. Free modules are flat, by the companion article on flatness and exactness. $\square$

**Example.** Base change between finite fields is determined by the degrees. Let $K=\mathbb{F}_p$, let $L=\mathbb{F}_{p^n}$ and let $M=\mathbb{F}_{p^m}$ with $m$ a multiple of $n$, so that $L \subseteq M$. The minimal polynomial $f$ of a generator of $L$ over $K$ has degree $n$ and splits over $M$ into $n$ distinct linear factors, because every root of $f$ lies in $L$ and $L \subseteq M$; hence
$$
\mathbb{F}_{p^n} \otimes_{\mathbb{F}_p} \mathbb{F}_{p^m} \;\cong\; M[x]/(f) \;\cong\; M^{\,n},
$$
a product of $n$ copies of $\mathbb{F}_{p^m}$. In general, for arbitrary $m,n$,
$$
\mathbb{F}_{p^n} \otimes_{\mathbb{F}_p} \mathbb{F}_{p^m} \;\cong\; \mathbb{F}_{p^{\operatorname{lcm}(n,m)}}^{\gcd(n,m)},
$$
a product of $\gcd(n,m)$ copies of the field of degree $\operatorname{lcm}(n,m)$ over $K$: the two sides have the same dimension over $\mathbb{F}_p$ because $\gcd(n,m)\operatorname{lcm}(n,m)=nm$, and the case $\gcd(n,m)=1$ is the statement that the two fields are linearly disjoint, the product being the single field $\mathbb{F}_{p^{nm}}$. Base change here does not increase the dimension over the base field, it decomposes the tensor product into fields, and it produces a nontrivial idempotent decomposition exactly when $n$ and $m$ have a common factor greater than $1$.

## Change of Dimension

### Free Modules and Fields

**Proposition.** For every $n$ there is an $S$-module isomorphism $S \otimes_R R^n \cong S^n$, so extension of scalars along $\varphi$ carries the free $R$-module of rank $n$ to the free $S$-module of rank $n$. In particular, if $K \subseteq L$ is a field extension and $V$ is a $K$-vector space of dimension $n$, then $L \otimes_K V$ has dimension $n$ over $L$.

*Proof.* The isomorphism is $s \otimes (a_1,\dots,a_n) \mapsto (sa_1,\dots,sa_n)$, with inverse $(s_1,\dots,s_n) \mapsto \sum_i s_i \otimes e_i$. For the field case, take the images $1 \otimes e_i$ of a $K$-basis: they span, because $L \otimes_K V$ is generated over $L$ by the image of $V$ and $V=\sum_iKe_i$; and they are independent, because the $L$-linear map $L \otimes_K V \to L^n$ sending $\lambda \otimes(\sum a_ie_i)$ to $(\lambda a_i)$ is well defined and is a left inverse. $\square$

The field statement is the one that says extension of scalars does not change the dimension: complexification of an $n$-dimensional real vector space is $n$-dimensional over $\mathbb{C}$, and the dimension is *not* doubled; it is realification that doubles it, below. For a general $\varphi$ the rank can change or be lost, because $S$ need not be free, or even flat, over $R$.

### Phenomena for General Base Rings

**Proposition.** (i) For the quotient map $\mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$ one has $(\mathbb{Z}/n) \otimes_{\mathbb{Z}} M \cong M/nM$, so extension of scalars to the quotient is reduction modulo $n$.

(ii) Extension of scalars can annihilate a nonzero module: $\mathbb{Q} \otimes_{\mathbb{Z}} \mathbb{Z}/n\mathbb{Z}=0$.

(iii) Extension of scalars need not preserve rank: $\mathbb{Z}/n \otimes_{\mathbb{Z}} \mathbb{Z}^m \cong (\mathbb{Z}/n)^m$ is free of rank $m$ over $\mathbb{Z}/n$, while $(\mathbb{Z}/n) \otimes_{\mathbb{Z}} \mathbb{Z}/m \cong \mathbb{Z}/\gcd(m,n)$ is not free of rank $1$ over $\mathbb{Z}/n$ unless $\gcd(m,n)=n$, that is, unless $n \mid m$.

*Proof.* (i) The tensor product $S \otimes_R M$ for $S=R/I$ is $M/IM$: the kernel of the surjection $M \to (R/I) \otimes_R M$, $m \mapsto 1 \otimes m$, is generated by $IM$, because $I \otimes_R M \to M$ is the map $r \otimes m \mapsto rm$, with image $IM$, and the sequence $I \otimes M \to M \to (R/I) \otimes M \to 0$ is exact by right exactness. (ii) and (iii) are computations from the companion article on the balanced product. $\square$

## Base Change for Algebras

**Definition.** Let $T$ be an $R$-algebra. The **base change** of $T$ along $\varphi$ is $S \otimes_R T$, with multiplication determined by

$$
(s_1 \otimes t_1)(s_2 \otimes t_2)=s_1s_2 \otimes t_1t_2 .
$$

**Proposition.** The multiplication is well defined and makes $S \otimes_R T$ a commutative $S$-algebra with unit $1 \otimes 1$, and it is characterised by the universal property that for every $S$-algebra $U$, regarded as an $R$-algebra via $\varphi$, there is a natural bijection $\operatorname{Hom}_{S\text{-}\mathbf{Alg}}(S \otimes_R T,U) \cong \operatorname{Hom}_{R\text{-}\mathbf{Alg}}(T,U)$. In particular the square-zero extension $R[\varepsilon]/(\varepsilon^2)$ base changes to $S[\varepsilon]/(\varepsilon^2)$, and the tensor product of two algebras over a field is again an algebra over that field.

*Proof.* The displayed product is the unique $S$-bilinear map extending $R$-bilinear multiplication; the details are the standard algebra form of the universal property of $\otimes$, and the multiplication is commutative because $R$ is. $\square$

Base change of algebras is the construction that produces $S$-algebras from $R$-algebras; the algebra-side account belongs to the companion category, and it is used here only as the ring-theoretic version of the module construction.

## Realification and Complexification

### Complexification

**Definition.** Let $V$ be a real vector space. Its **complexification** is

$$
V_{\mathbb{C}} \;=\; \mathbb{C} \otimes_{\mathbb{R}} V ,
$$

viewed as a complex vector space by the action of $\mathbb{C}$ on the first factor.

**Proposition.** (i) $\dim_{\mathbb{C}}V_{\mathbb{C}}=\dim_{\mathbb{R}}V$.

(ii) The map $V \to V_{\mathbb{C}}$, $v \mapsto 1 \otimes v$, is injective and real-linear, and

$$
V_{\mathbb{C}}=V \oplus iV
$$

as real vector spaces, where $iV=\{i \otimes v\}$.

(iii) There is a conjugate-linear involution $\kappa:V_{\mathbb{C}} \to V_{\mathbb{C}}$, $\kappa(z \otimes v)=\bar z \otimes v$, whose fixed-point set is the image of $V$: $(V_{\mathbb{C}})^{\kappa}=1 \otimes V$.

*Proof.* (i) and (ii) are the field case of the dimension statement above, together with the decomposition $\mathbb{C}=\mathbb{R} \oplus i\mathbb{R}$. (iii) The map is well defined, conjugate-linear, and satisfies $\kappa^2=\operatorname{id}$; its fixed points are the tensors $z \otimes v$ with $z \in \mathbb{R}$, which are the elements of $1 \otimes V$. $\square$

**Example.** $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{R}^n \cong \mathbb{C}^n$, and $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C} \cong \mathbb{C} \times \mathbb{C}$ as $\mathbb{C}$-algebras, via $z \otimes w \mapsto (zw, z\bar w)$, the two factors corresponding to the two $\mathbb{R}$-algebra maps $\mathbb{C} \to \mathbb{C}$ applied to the second tensorand. The scalar acts on the first tensorand, so the isomorphism is $\mathbb{C}$-linear in that slot, which is what makes $(zw,z\bar w)$ the correct form: the map $(zw,\bar zw)$ is only real-linear, since it carries $\lambda(z \otimes w)$ to $(\lambda zw,\bar\lambda\bar zw)$. The second isomorphism is the simplest example in which base change splits a ring into a product.

### Realification

**Definition.** Let $W$ be a complex vector space. Its **realification** is the real vector space $\operatorname{Res}W$ obtained by restriction of scalars along $\mathbb{R} \hookrightarrow \mathbb{C}$.

**Proposition.** $\dim_{\mathbb{R}}\operatorname{Res}W=2\dim_{\mathbb{C}}W$, the multiplication by $i$ is a real-linear operator $J$ on $\operatorname{Res}W$ with $J^2=-\operatorname{id}$, and the complex vector space is recovered from the pair $(\operatorname{Res}W,J)$ by making $J$ act as $i$.

*Proof.* A complex basis $e_1,\dots,e_n$ gives a real basis $e_1,ie_1,\dots,e_n,ie_n$, so the real dimension is $2n$; the operator $J$ of multiplication by $i$ is real-linear and squares to $-1$. $\square$

**Example.** The realification of $\mathbb{C}^n$ is $\mathbb{R}^{2n}$, and complexification followed by realification returns a space of twice the real dimension: $\operatorname{Res}(V_{\mathbb{C}})$ has $\dim_{\mathbb{R}}=2\dim_{\mathbb{R}}V$. Conversely, for a complex space $W$ there is a natural isomorphism $(\operatorname{Res}W)_{\mathbb{C}} \cong W \oplus \bar W$ given by $z \otimes w \mapsto (zw,\bar zw)$, where $\bar W$ is $W$ with the conjugate complex structure; the two summands carry the two complex structures $J$ and $-J$ on the underlying real space $\operatorname{Res}W$.

### Complexification of Algebras

**Example.** Complexification applies to real algebras as well as to real spaces: for a real algebra $T$ the base change $\mathbb{C} \otimes_{\mathbb{R}} T$ is a complex algebra with multiplication $(\lambda \otimes t)(\mu \otimes t')=\lambda\mu \otimes tt'$, and the real algebra is recovered from it by restriction of scalars. The split complex numbers $\mathbb{D}=\mathbb{R}[j]/(j^2-1)$ complexify to $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{D} \cong \mathbb{C}[j]/(j^2-1) \cong \mathbb{C} \times \mathbb{C}$, the idempotents $e_\pm=\tfrac12(1 \pm j)$ of $\mathbb{D}$ becoming the two coordinate idempotents; complexification of $\mathbb{R}$ itself gives $\mathbb{C}$, and complexification of $\mathbb{C}$ splits it as $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C} \cong \mathbb{C} \times \mathbb{C}$, the example above. Whether $\mathbb{C} \otimes_{\mathbb{R}} T$ is again a field, a product of fields, or a ring with nilpotents is decided by how the defining polynomial of $T$ factors over $\mathbb{C}$. The quaternionic instance of base change is treated in *Division Algebras*.

## Behaviour of Standard Properties under Base Change

**Theorem.** Let $\varphi:R \to S$ be a ring homomorphism and $M$ an $R$-module. Then the extension of scalars $M_S=S\otimes_RM$ is (i) free if $M$ is free, (ii) projective if $M$ is projective, (iii) flat if $M$ is flat, and (iv) finitely generated if $M$ is finitely generated, finitely presented if $M$ is finitely presented.

*Proof.* (i) $S\otimes_RR^n \cong S^n$. (ii) If $M \oplus N \cong R^n$ then $M_S \oplus N_S \cong S^n$. (iii) For an $S$-module $N$ one has $N\otimes_S(S\otimes_RM) \cong N\otimes_RM$ by associativity, so exactness of $-\otimes_RM$ gives exactness of $-\otimes_SM_S$. (iv) Tensoring a finite presentation $R^p \to R^q \to M \to 0$ by $S$ gives the finite presentation $S^p \to S^q \to M_S \to 0$ of $M_S$ over $S$. $\square$

**Proposition (transitivity).** For ring homomorphisms $R \to S \to T$ and an $R$-module $M$ there is a natural isomorphism $(M_S)_T \cong M_T$; extension of scalars is compatible with composition of ring homomorphisms.

*Proof.* Both sides are $T\otimes_RM$, by the associativity of the tensor product. $\square$

**Corollary.** The extension of scalars functor is right exact, is exact exactly when $S$ is flat over $R$, and preserves arbitrary direct sums and cokernels; it preserves kernels precisely in the flat case.

*Proof.* Right exactness, preservation of direct sums and cokernels are the general properties of the tensor product, and the tensor product preserves kernels precisely when $S$ is flat, as in the companion article on flatness and exactness. $\square$

**Example.** Complexification sends real projective modules to complex projective modules and preserves finite presentation; complexification of a real module of rank $n$ has complex rank $n$, while realification of a complex module of complex rank $n$ has real rank $2n$, so the two operations are not mutually inverse.

## Summary

A ring homomorphism $\varphi:R \to S$ gives a functor $R\text{-}\mathbf{Mod} \to S\text{-}\mathbf{Mod}$, $M \mapsto M_S=S \otimes_R M$, the extension of scalars, with $S$-action $s \cdot(s' \otimes m)=(ss') \otimes m$. It is left adjoint to the restriction of scalars, $\operatorname{Hom}_S(S \otimes_R M,N) \cong \operatorname{Hom}_R(M,\operatorname{Res}N)$, hence right exact and compatible with direct sums; it is exact exactly when $S$ is flat over $R$, and in particular whenever $S$ is free over $R$, which includes the case of a field extension.

The rank behaviour is the field case first: $S \otimes_R R^n \cong S^n$, so over a field extension the dimension of a vector space is unchanged, $\dim_L(L \otimes_K V)=\dim_K V$. For a general base ring the rank can change or be lost: extension along $\mathbb{Z} \to \mathbb{Z}/n$ computes $M/nM$, it can annihilate a nonzero module as $\mathbb{Q} \otimes_{\mathbb{Z}} \mathbb{Z}/n=0$, and it converts free modules to free modules of the same rank but not in a way that respects the lattice of submodules unless $S$ is flat. Base change of algebras takes $T$ to the $S$-algebra $S \otimes_R T$ with multiplication $s_1s_2 \otimes t_1t_2$; complexification of a real space, $V_{\mathbb{C}}=\mathbb{C} \otimes_{\mathbb{R}}V$, gives a complex space of the same dimension with $V_{\mathbb{C}}=V \oplus iV$ and a conjugate-linear involution fixing $V$, while realification doubles the real dimension and is inverse to complexification in the sense that $(\operatorname{Res}W)_{\mathbb{C}} \cong W \oplus \bar W$. Complexification of a real algebra $T$ is the case $R=\mathbb{R}$, $S=\mathbb{C}$, the algebra-level instance of the construction. Base change preserves freeness, projectivity, flatness, finite generation and finite presentation, and it is transitive along a composite of ring homomorphisms; it is exact precisely when the target ring is flat over the source.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\varphi:R \to S$ | ring homomorphism of commutative rings |
| $M_S = S \otimes_R M$ | extension of scalars |
| $\operatorname{Res}N$ | restriction of scalars of an $S$-module |
| $\operatorname{Hom}_S(S \otimes_R M,N) \cong \operatorname{Hom}_R(M,\operatorname{Res}N)$ | the adjunction |
| $M/nM$ | extension along $\mathbb{Z} \to \mathbb{Z}/n$ |
| $V_{\mathbb{C}} = \mathbb{C} \otimes_{\mathbb{R}} V$ | complexification |
| $\operatorname{Res}W$ | realification of a complex vector space |
| $J$, $J^2=-\operatorname{id}$ | real operator of multiplication by $i$ |
| $\kappa$ | conjugate-linear involution of $V_{\mathbb{C}}$ |



## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for change of rings and the adjunction with restriction of scalars.
- Henri Cartan and Samuel Eilenberg, *Homological Algebra* (Princeton University Press, 1956), for base change and its exactness properties.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for extension and restriction of scalars.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for tensor products of algebras and field extensions.
- Hideyuki Matsumura, *Commutative Ring Theory* (Cambridge University Press, 1989), for flat base change.
- Joseph J. Rotman, *An Introduction to Homological Algebra* (Springer, 2nd ed. 2009), for the adjunction and its categorical content.
