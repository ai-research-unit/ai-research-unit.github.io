
# __Modules over an Algebra__

## Introduction

A module over an algebra is the object obtained when the scalar structure of a module and the multiplicative structure of a ring are allowed to act together. The general theory of modules over a ring is the subject of *Modules*; the general theory of algebras is the subject of *Algebras: A General Introduction*. This article fixes the object at their intersection, and it is the first entry of the category *Linear spaces over Algebras*, so the conventions fixed here — the base ring, the algebra, the side on which modules are written, the notation for the regular module and for the homomorphism groups — are held throughout the category.

Throughout, $R$ is a commutative ring with identity $1 \neq 0$, and $A$ is an **associative unital $R$-algebra**: an $R$-module equipped with an $R$-bilinear associative product and a two-sided unit $1_A$. As in *Modules*, the default base is the commutative ring rather than the field, and every place where a result needs a field, a division ring, characteristic zero, or invertibility of $2$ is flagged. Left modules are the default; a right module is written with the ring as a subscript on the right, as in $M_A$. The unital assumption is essential and is not repeated: $A$ has a unit, module actions are unital, and algebra homomorphisms preserve the unit.

The passage from a ring to an algebra is not a change of axioms — every ring is a $\mathbb{Z}$-algebra — but a change of what may be asserted. An algebra carries a second action, of its base ring, on top of its ring structure, and the extra flexibility of the base ring is what makes the theory of this category different from the theory of category 04. Two facts recur. The first is that a module over an algebra is a module over the algebra's base ring as well, so the module is an $R$-module with additional structure; the second is that the algebra need not be commutative, so left and right modules genuinely differ and the naive tensor product of two modules need not exist. Both are developed below, and the tensor product appropriate to the noncommutative case is the balanced product .

## Algebras and Their Modules

### The definition of an algebra

Recall from *Algebras: A General Introduction* that an $R$-algebra is an $R$-module $A$ with a product $A \times A \to A$, $(a,b) \mapsto ab$, that is $R$-bilinear:

$$
a(b+c)=ab+ac, \qquad (a+b)c=ac+bc, \qquad r(ab)=(ra)b=a(rb),
$$

for all $a,b,c \in A$ and $r \in R$. The algebra is **associative** if $(ab)c=a(bc)$ for all $a,b,c$, and **unital** if there is $1_A \in A$ with $1_A a = a 1_A = a$ for all $a$. The unit is unique when it exists. Multiplication by the base ring is recovered from the unit, $ra = (r 1_A)a$, so the $R$-module structure is determined by the ring structure together with the structural map $R \to Z(A)$, $r \mapsto r1_A$, which lands in the center. Thus a unital $R$-algebra is the same thing as a ring $A$ together with a unital ring homomorphism $R \to Z(A)$.

The center of $A$ is

$$
Z(A)=\{z \in A : za=az \text{ for all } a \in A\}.
$$

It is a commutative subalgebra containing the image of $R$, and it is the largest commutative part of $A$. When $R$ happens to be a field, a **central** algebra is one for which $Z(A)=R1_A$.

### Left, right and bimodules

A **left $A$-module** is an abelian group $(M,+)$ together with a map

$$
A \times M \to M, \qquad (a,m) \mapsto am,
$$

such that for all $a,b \in A$ and $m,n \in M$,

$$
a(m+n)=am+an, \qquad (a+b)m=am+bm, \qquad (ab)m=a(bm), \qquad 1_A m = m.
$$

These are the axioms (M1)–(M4) of *Modules* §1, with the general ring now carrying an $R$-algebra structure. A **right $A$-module** is defined with the action written on the right, $M \times A \to M$, $(m,a)\mapsto ma$, subject to

$$
(m+n)a=ma+na, \qquad m(a+b)=ma+mb, \qquad m(ab)=(ma)b, \qquad m1_A=m.
$$

An **$(A,B)$-bimodule** ${}_A M_B$ is an abelian group that is a left $A$-module and a right $B$-module with the two actions commuting:

$$
a(mb)=(am)b \qquad (a \in A,\ b \in B,\ m \in M).
$$

Every left $A$-module is a right $A^{\mathrm{op}}$-module and conversely, where $A^{\mathrm{op}}$ is the **opposite algebra**, the $R$-module $A$ with the reversed product $a \cdot_{\mathrm{op}} b = ba$. Thus the theory of right modules is the theory of left modules over the opposite algebra, and it suffices to develop one side. The left regular module ${}_A A$ is an $(A,A)$-bimodule, with left action by multiplication and right action also by multiplication, the two commuting by associativity.

### The action as a homomorphism

Giving a left $A$-module structure on $M$ is the same as giving a unital ring homomorphism

$$
\rho : A \to \operatorname{End}_{\mathbb{Z}}(M), \qquad \rho(a)(m)=am,
$$

where $\operatorname{End}_{\mathbb{Z}}(M)$ is the endomorphism ring of the abelian group $M$. The axiom $(ab)m=a(bm)$ says $\rho(ab)=\rho(a)\rho(b)$ and $1_Am=m$ says $\rho(1_A)=\mathrm{id}$. Because $\rho$ is a ring homomorphism and $M$ is an $R$-module through the structural map, the image of $R$ acts by $R$-scalars; equivalently $\rho$ is a homomorphism of $R$-algebras when $\operatorname{End}_{\mathbb{Z}}(M)$ is regarded as an $R$-algebra through the structural map of $M$. This is the precise sense in which a module is a **representation** of the algebra: the algebra is realized by endomorphisms of an abelian group. The kernel of $\rho$ is a two-sided ideal, and $M$ is **faithful** if $\rho$ is injective.

For a right $A$-module the same statement holds with $\operatorname{End}_{\mathbb{Z}}(M)^{\mathrm{op}}$, or equivalently with an anti-homomorphism $A \to \operatorname{End}_{\mathbb{Z}}(M)$.

## Elementary Identities

The following hold in every left $A$-module, by the argument of *Modules* §2:

$$
0_A m = 0, \qquad a 0 = 0, \qquad (-a)m = a(-m) = -(am), \qquad (-a)(-m)=am,
$$

$$
a(m-n)=am-an, \qquad (a-b)m=am-bm,
$$

and the elements $0 \in M$ and $-m$ are unique. The same identities hold on the right, with the obvious changes of order.

The base ring acts through the unit: for $r \in R$, $r m = (r 1_A)m$. Consequently every left $A$-module is an $R$-module, and every $A$-linear map is $R$-linear. This is the single most important consequence of the algebra structure, and it is what makes the category comparable with the categories of the surrounding chapters: a module over the $\mathbb{R}$-algebra $\mathbb{H}$ is an $\mathbb{R}$-vector space carrying additional structure, and a module over the $\mathbb{C}$-algebra $\mathbb{B}$ is a $\mathbb{C}$-vector space carrying additional structure.

## Examples

**(a) Modules over a field.** If $A=F$ is a field, then an $F$-module is exactly an $F$-vector space. Here the algebra structure adds nothing, and the theory collapses to linear algebra.

**(b) Modules over a commutative ring.** If $A=R$ is commutative, a left $R$-module is an $R$-module in the sense of *Modules*, and left and right modules coincide by $mr=rm$. This is the setting of category 04.

**(c) The regular module.** The algebra $A$ acts on itself by left multiplication, $\rho(a)(b)=ab$; the resulting left module is the **left regular module** ${}_A A$. Its submodules are exactly the left ideals of $A$. Likewise, $A$ acts on itself by right multiplication, giving the right regular module $A_A$, whose submodules are the right ideals, and the two-sided ideals are the submodules of the bimodule ${}_A A_A$. This example is the reason the theory of one-sided ideals is the theory of submodules of the regular module.

**(d) Free modules.** The direct sum $A^n = A \oplus \cdots \oplus A$ of $n$ copies of ${}_A A$ is the free left $A$-module of rank $n$, with standard basis $e_1,\dots,e_n$. Every free module is a direct sum of copies of the regular module; this is the algebra-level form of the statement of *Modules* §9.

**(e) Matrix algebras.** Let $A=M_n(F)$ and let $S=F^n$ be the space of column vectors, acted on by matrix multiplication. Then $S$ is a left $M_n(F)$-module, the **defining module** of the matrix algebra, and it is simple. The left regular module is $M_n(F)$, which as a left module is

$$
M_n(F) \cong S \oplus \cdots \oplus S \qquad (n \text{ summands}),
$$

the summands being the spaces of matrices supported in a single column. Thus the regular module of $M_n(F)$ is $n$ copies of $S$, and $S$ is not free when $n \geq 2$: a free $M_n(F)$-module is $A^k=S^{\oplus nk}$, so the number of copies of $S$ in a free module is a multiple of $n$, whereas $S=S^{\oplus 1}$ is a single copy and $n \nmid 1$ for $n \geq 2$ — this is taken up in §Free, Projective and the Rigidity of the Algebra.

**(f) Group algebras.** For a group $G$ and a commutative ring $R$, the group algebra $R[G]$ is the free $R$-module on the elements of $G$ with the product extending the group multiplication bilinearly; it is a unital associative $R$-algebra, generally noncommutative when $G$ is nonabelian. An $R[G]$-module is exactly a representation of $G$ on an $R$-module, that is, a group homomorphism $G \to \operatorname{Aut}_R(M)$. The theory is developed from the module side , and the group algebra is the bridge between group theory and the module theory of this category.

**(g) Division algebras.** A unital associative algebra $D$ over a field $F$ is a **division algebra** if every nonzero element is invertible. Then $D$ is a division ring, and by *Modules* §19 every $D$-module is free, so the module theory of $D$ is linear algebra with scalars in a division ring. The quaternions $\mathbb{H}$ are the classical real example, and their modules are not covered here.

**(h) Algebras with zero divisors.** The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the complexification of $\mathbb{H}$, is a unital associative $\mathbb{C}$-algebra isomorphic to $M_2(\mathbb{C})$. It is not a division algebra; it has zero divisors, and as example (e) shows, not every $\mathbb{B}$-module is free. The simple module is the defining module of the picture algebra, treated .

**(i) Polynomial algebras.** For a field $F$ and an indeterminate $x$, the polynomial algebra $F[x]$ is commutative, and an $F[x]$-module structure on a vector space $V$ is exactly an $F$-linear operator $T:V\to V$, with $x \cdot v=T(v)$. The finitely generated modules over the principal ideal domain $F[x]$ are classified by the structure theorem of *Modules* §15, and the classification is the rational and Jordan normal forms.

## Submodules and Quotients

A subset $N \subseteq M$ of a left $A$-module is a **submodule** if it is an additive subgroup and is closed under the action: $n-n' \in N$ and $an \in N$ for all $a \in A$ and $n,n' \in N$. Equivalently, $N$ is a subgroup stable under every operator $\rho(a)$; when $A$ is a field this is exactly a subspace. The trivial submodules are $0$ and $M$; a nonzero module whose only submodules are these is **simple**. The zero module is not called simple.

The intersection of any family of submodules is a submodule, and the **sum** $\sum_i N_i$ of submodules, consisting of all finite sums of elements of the $N_i$, is the smallest submodule containing every $N_i$. For a subset $S \subseteq M$, the submodule **generated** by $S$ is the set of finite $A$-linear combinations $\sum_i a_i s_i$; the module is **cyclic** if $M=Am$ for some $m$, and **finitely generated** if $M=Am_1+\cdots+Am_k$. Since $A$ is an $R$-algebra, every submodule is an $R$-submodule, but the converse fails: an $R$-submodule need not be $A$-stable.

For a submodule $N \subseteq M$, the cosets $M/N=\{m+N : m \in M\}$ form a left $A$-module under

$$
(m+N)+(m'+N)=(m+m')+N, \qquad a(m+N)=am+N,
$$

the action being well defined because $N$ is closed under scalars. The **natural projection** $\pi: M \to M/N$, $\pi(m)=m+N$, is $A$-linear and surjective with kernel $N$. This is the quotient module of *Modules* §5.

The **correspondence theorem** holds in the algebra setting exactly as in the ring setting: for a submodule $N \subseteq M$, the submodules of $M/N$ correspond bijectively, by $L \mapsto L/N$, to the submodules of $M$ containing $N$, and the correspondence preserves inclusions, sums and intersections. In particular the submodules of the regular module ${}_A A$ are the left ideals of $A$, and those of $A/N$ for a left ideal $N$ correspond to the left ideals lying between $N$ and $A$.

## Homomorphisms

A map $f: M \to N$ of left $A$-modules is **$A$-linear** if

$$
f(m+m')=f(m)+f(m'), \qquad f(am)=a f(m)
$$

for all $a \in A$ and $m,m' \in M$. Since $A$ is an $R$-algebra, every $A$-linear map is $R$-linear, but the converse fails, and the gap between the two notions is not covered here. The **kernel** $\ker f$ and **image** $\operatorname{im} f$ are submodules of $M$ and $N$; $f$ is injective if and only if $\ker f=0$; the **cokernel** is $N/\operatorname{im} f$; and $f$ is an **isomorphism** if it is bijective, in which case the inverse is automatically $A$-linear and we write $M \cong N$.

The set $\operatorname{Hom}_A(M,N)$ of $A$-linear maps is an abelian group under pointwise addition, with zero the zero map. It carries no natural left $A$-module structure when $A$ is noncommutative: the attempt $(af)(m)=a f(m)$ fails to be $A$-linear, since $(af)(bm)=a f(bm)=ab f(m)$ while $b(af)(m)=ba f(m)$, and these differ unless $a$ and $b$ commute. What is available is a module structure over the center. If $z \in Z(A)$ then $(zf)(m)=f(zm)$ defines the same map as $(zf)(m)=z f(m)$, and this makes $\operatorname{Hom}_A(M,N)$ a module over $Z(A)$, hence in particular an $R$-module. More generally, if ${}_B M_A$ is a $(B,A)$-bimodule then $\operatorname{Hom}_A(M,N)$ is a left $B$-module by $(bf)(m)=f(bm)$, the bimodule axiom providing the $A$-linearity of $bf$.

The **endomorphism ring** $\operatorname{End}_A(M)=\operatorname{Hom}_A(M,M)$ is a unital associative ring under composition, its unit the identity, and it is an $R$-algebra through $R \to Z(\operatorname{End}_A(M))$. Its group of units is the **automorphism group** $\operatorname{Aut}_A(M)$. Both are studied .

### The isomorphism theorems

For left $A$-modules the three isomorphism theorems hold by the same coset arguments as for groups and rings:

**(a)** $M/\ker f \cong \operatorname{im} f$ for every $f \in \operatorname{Hom}_A(M,N)$.

**(b)** $(N+P)/P \cong N/(N \cap P)$ for submodules $N,P \subseteq M$.

**(c)** $(M/N)/(P/N) \cong M/P$ for submodules $N \subseteq P \subseteq M$, the quotient $P/N$ being a submodule of $M/N$ identified through the correspondence theorem.

The proofs pass to cosets as in *Modules* §7. The first isomorphism theorem has the following useful form.

**Proposition.** Let $M$ be a left $A$-module and $f \in \operatorname{Hom}_A(A,M)$, where $A$ is the left regular module. Then $f$ is determined by $m=f(1_A)$, and $f \mapsto f(1_A)$ is an isomorphism of abelian groups

$$
\operatorname{Hom}_A(A,M) \cong M.
$$

*Proof.* For $b \in A$, $A$-linearity gives $f(b)=f(b1_A)=bf(1_A)=bm$, so $f$ is determined by $m=f(1_A)$. Conversely, for any $m \in M$ the map $f(b)=bm$ is $A$-linear: $f(b b')=b b' m=b (b'm)=b f(b')$. The two constructions are inverse, and both are additive in $f$ and in $m$. $\square$

## The Regular Module and Its Endomorphisms

The endomorphism ring of the regular module has a description dual to the preceding proposition and is used repeatedly.

**Theorem.** Multiplication on the right gives a ring isomorphism

$$
A^{\mathrm{op}} \xrightarrow{\ \sim\ } \operatorname{End}_A({}_A A), \qquad a \longmapsto (b \mapsto b a).
$$

*Proof.* For $a \in A$, the map $R_a(b)=ba$ is $A$-linear because $R_a(c b)=(c b)a=c(ba)=c R_a(b)$. It is additive, and $R_a \circ R_{a'}=R_{a'a}$, so $a \mapsto R_a$ is a ring homomorphism $A^{\mathrm{op}}\to\operatorname{End}_A(A)$. It is injective, since $R_a(1_A)=a$; and it is surjective, since for any $f \in \operatorname{End}_A(A)$ and $b \in A$ one has $f(b)=f(b 1_A)=b f(1_A)=R_{f(1_A)}(b)$. $\square$

Taking units gives $\operatorname{Aut}_A({}_A A) \cong (A^{\mathrm{op}})^{\times} \cong A^{\times}$, the group of units of $A$, under the same map; the inverse of $R_a$ is $R_{a^{-1}}$. Thus the automorphisms of the left regular module are exactly the right multiplications by units, a fact that is invisible over a commutative base ring and is the first sign of the asymmetry of the noncommutative case.

## Annihilators, Cyclic Modules and Simple Modules

For $m \in M$, the **annihilator** is the set

$$
\operatorname{Ann}_A(m)=\{a \in A : am=0\}.
$$

It is a left ideal of $A$: it is an additive subgroup, and if $am=0$ then $(ba)m=b(am)=0$. The **annihilator of the module** is

$$
\operatorname{Ann}_A(M)=\{a \in A : am=0 \text{ for all } m \in M\}=\bigcap_{m \in M}\operatorname{Ann}_A(m),
$$

which is a two-sided ideal, since $a$ annihilates $M$ precisely when $\rho(a)=0$ for the action homomorphism $\rho$ of §The action as a homomorphism. Thus $\operatorname{Ann}_A(M)=\ker \rho$ and $M$ is faithful exactly when $\operatorname{Ann}_A(M)=0$. The quotients $A/\operatorname{Ann}_A(m)$ and $A/\operatorname{Ann}_A(M)$ are respectively a cyclic left module and an $R$-algebra.

**Proposition.** For every $m \in M$, the map $A \to M$, $a \mapsto am$, induces an isomorphism of left $A$-modules

$$
A/\operatorname{Ann}_A(m) \cong Am.
$$

*Proof.* The map is $A$-linear by associativity and has image $Am$ and kernel $\operatorname{Ann}_A(m)$; apply the first isomorphism theorem. $\square$

Consequently the cyclic left $A$-modules are exactly the quotients $A/L$ by left ideals $L$, the correspondence being $L \mapsto A/L$ and $M \mapsto \operatorname{Ann}_A(m)$ for a chosen generator $m$. Passing to $A/L$ from $L$ recovers $L$, and the submodules of $A/L$ correspond to the left ideals between $L$ and $A$.

**Schur's lemma.** Let $S$ and $T$ be simple left $A$-modules and let $f \in \operatorname{Hom}_A(S,T)$. Then $\ker f$ and $\operatorname{im} f$ are submodules of $S$ and $T$, so by simplicity each is $0$ or the whole module. If $f \neq 0$ then $\ker f \neq S$ and $\operatorname{im} f \neq 0$, hence $\ker f=0$ and $\operatorname{im} f=T$, so $f$ is an isomorphism. Therefore

$$
\operatorname{Hom}_A(S,T)=0 \text{ if } S \not\cong T, \qquad \operatorname{End}_A(S) \text{ is a division ring.}
$$

In particular $\operatorname{Aut}_A(S)=\operatorname{End}_A(S)^{\times}$ is the multiplicative group of that division ring. The lemma is developed and applied in .

A nonzero module is simple if and only if it is isomorphic to $A/\mathfrak{m}$ for a **maximal left ideal** $\mathfrak{m}$: simplicity of $S$ corresponds under the proposition to the absence of left ideals strictly between $\operatorname{Ann}_A(m)$ and $A$ for a nonzero $m$. If $A$ is commutative, the maximal left ideals are the maximal ideals, and this recovers the familiar description of simple modules over a commutative ring.

## Free, Projective and the Rigidity of the Algebra

A **free** left $A$-module is a direct sum of copies of ${}_A A$, equivalently a module with a basis in the sense of *Modules* §9: a set $B$ such that every element has a unique expression as a finite $A$-linear combination of elements of $B$. That a basis element has trivial annihilator is immediate. Every module is a quotient of a free module: choosing a generator set $\{m_i\}$ of $M$ and mapping the free module on the same index set to $M$ by $e_i \mapsto m_i$ gives a surjection, so $M \cong F/K$ for free $F$ and submodule $K$.

A left $A$-module $P$ is **projective** if every diagram of $A$-linear maps with $q$ surjective can be completed, equivalently if every short exact sequence $0 \to L \to N \to P \to 0$ splits, equivalently if $P$ is a direct summand of a free module. Free modules are projective. Over a division ring every module is free, hence projective; over a general algebra this fails, and the failure is where the algebra-specific phenomena begin. The basic examples are these.

- Over $A=M_n(F)$ with $n \geq 2$, the simple module $S=F^n$ is a direct summand of the regular module, so it is projective; but it is not free, since a free $M_n(F)$-module is $A^k=S^{\oplus nk}$, so the number of copies of $S$ in a free module is a multiple of $n$, whereas $S$ itself is a single copy. So $S$ is projective and not free.
- Over the biquaternion algebra $\mathbb{B} \cong M_2(\mathbb{C})$, the same description holds with $n=2$ and $F=\mathbb{C}$: the defining module $S=\mathbb{C}^2$ is projective but not free, and a finitely generated $\mathbb{B}$-module is free precisely when its complex dimension is divisible by $4$.
- Over a division algebra, and in particular over $\mathbb{H}$, every module is free, so projectivity is automatic.

The contrast between $\mathbb{H}$ and $\mathbb{B}$ is the theme of: the first is a division algebra, the second a matrix algebra, and freeness of modules distinguishes them. Over a division ring the rank of a free module is well defined, by the invariant basis number property of *Modules* §19; over a general algebra the rank of a free module exists whenever $A$ has invariant basis number, which holds when $A$ is commutative by *Modules* §10 and when $A$ has a maximal two-sided ideal $\mathfrak{m}$ with $A/\mathfrak{m}$ left artinian — then $A/\mathfrak{m}$ is a matrix ring over a division ring and has invariant basis number, and tensoring $A^{(I)}\cong A^{(J)}$ with $A/\mathfrak{m}$ over $A$ gives $(A/\mathfrak{m})^{(I)}\cong(A/\mathfrak{m})^{(J)}$, hence $|I|=|J|$ — in particular when $A$ is a finite-dimensional algebra over a field.

## Direct Sums, Products and Idempotents

For a family $\{M_i\}$ of left $A$-modules, the **direct product** $\prod_i M_i$ and the **direct sum** $\bigoplus_i M_i$ are defined componentwise exactly as in *Modules* §8; for finite index sets they coincide, and we write $M_1 \oplus \cdots \oplus M_n$. The sum is the coproduct and the product the product in the category of left $A$-modules.

For submodules $N_1,\dots,N_k \subseteq M$, the internal direct sum $M=N_1\oplus\cdots\oplus N_k$ means that every $m$ has a unique expression $m=n_1+\cdots+n_k$ with $n_i \in N_i$; equivalently $M=N_1+\cdots+N_k$ and $N_i \cap \sum_{j \neq i} N_j=0$ for each $i$. A submodule $N$ is a **direct summand** if $M=N\oplus N'$ for some $N'$.

**Proposition.** A submodule $N \subseteq M$ is a direct summand if and only if $N=\operatorname{im} e$ for an idempotent $e \in \operatorname{End}_A(M)$.

*Proof.* If $M=N \oplus N'$, let $e$ be the projection onto $N$ along $N'$; it is $A$-linear, idempotent, and has image $N$. Conversely, if $e^2=e$, then $\operatorname{im} e=\{m : e(m)=m\}$ and $\ker e$ are submodules, and for every $m$ one has $m=e(m)+(m-e(m))$ with $e(m) \in \operatorname{im} e$ and $m-e(m) \in \ker e$; hence $M=\operatorname{im} e \oplus \ker e$. $\square$

Applying the proposition to the regular module, an idempotent $e \in A$ gives the decomposition ${}_A A = Ae \oplus A(1_A-e)$, so the left ideal $Ae$ is a projective left $A$-module. Idempotents in the algebra thus manufacture projective modules, and in a matrix algebra they manufacture all direct summands.

## Nakayama's Lemma over Noncommutative Rings

The Jacobson radical of $A$ is the intersection of its maximal left ideals; equivalently, the intersection of its maximal right ideals, and it is a two-sided ideal $J(A)$. It is treated . The following form of Nakayama's lemma holds for modules over a noncommutative ring and is the noncommutative counterpart of *Modules* §11.

**Theorem (Nakayama).** Let $I \subseteq J(A)$ be a two-sided ideal contained in the Jacobson radical, let $M$ be a finitely generated left $A$-module, and let $N \subseteq M$ be a submodule. If $M=N+IM$ then $M=N$. In particular, if $IM=M$ then $M=0$.

*Proof.* Passing to $M/N$, it suffices to show that if $M$ is finitely generated and $IM=M$ then $M=0$. Let $m_1,\dots,m_k$ generate $M$ with $k$ minimal. Since $IM=M$, we have $m_k=\sum_i a_i m_i$ with $a_i \in I$. Then

$$
(1_A-a_k)m_k=\sum_{i<k}a_i m_i.
$$

The element $1_A-a_k$ is invertible because $a_k \in J(A)$: if $1-a$ is not left-invertible then $A(1-a)$ is a proper left ideal, so it lies in a maximal left ideal, which contains $J(A)$ and hence $a$, giving $1=(1-a)+a$ in that ideal, a contradiction. Thus there is $u$ with $u(1_A-a_k)=1_A$, and $1_A-u=-ua_k \in J(A)$ since $J(A)$ is a two-sided ideal, so the same argument applied to $1_A-(1_A-u)$ shows that $u$ is left-invertible as well; then $u(1_A-a_k)=1_A$ and $vu=1_A$ force $1_A-a_k=v\bigl(u(1_A-a_k)\bigr)=v$, so $1_A-a_k$ has the two-sided inverse $u$. Multiplying by this inverse expresses $m_k$ in terms of $m_1,\dots,m_{k-1}$, contradicting minimality unless $k=0$. $\square$

The commutativity of the base ring plays no role, and it is the two-sidedness of $I$ and the containment $I \subseteq J(A)$ that replace it.

## The Category of Modules

The left $A$-modules and the $A$-linear maps form a category $\operatorname{Mod}(A)$, also written ${}_A\operatorname{Mod}$. It is an abelian category: $\operatorname{Hom}_A(M,N)$ is an abelian group, composition is bilinear, finite products and coproducts exist and coincide, every map has a kernel and a cokernel, and every map factors as a coimage-isomorphism-image. It has enough projectives, because every module is a quotient of a free module, and enough injectives, because every module embeds in an injective one by the standard construction of the injective envelope. The category is $R$-linear, in that the hom-sets are $R$-modules and composition is $R$-bilinear.

Two algebras $A$ and $B$ are **Morita equivalent** when their module categories are equivalent, $\operatorname{Mod}(A)\simeq\operatorname{Mod}(B)$; this is developed . The equivalence need not come from an isomorphism of algebras; the matrix algebras $M_n(A)$ are all Morita equivalent to $A$, which is why the module theory of the biquaternion algebra is the module theory of $\mathbb{C}$, and why the defining module of $\mathbb{B}$ carries all the module-theoretic information of the algebra.

## Summary

Fix a commutative ring $R$ and a unital associative $R$-algebra $A$. A left $A$-module is an abelian group with an action of $A$ satisfying the four axioms, equivalently a unital ring homomorphism $A \to \operatorname{End}_{\mathbb{Z}}(M)$; a left module is automatically an $R$-module because $R$ acts through the unit. Left, right and bimodules are distinguished when $A$ is noncommutative, and passing to $A^{\mathrm{op}}$ converts one side into the other. Submodules, quotient modules and $A$-linear maps are defined by the same clauses as for a commutative ring, and the three isomorphism theorems hold; the submodules of the regular module ${}_A A$ are the left ideals, so cyclic modules are the quotients $A/L$, and simple modules are the quotients $A/\mathfrak{m}$ by maximal left ideals.

The endomorphism ring $\operatorname{End}_A(M)$ is an $R$-algebra but not in general an $A$-module, only a module over the center; the regular module has $\operatorname{End}_A({}_A A)\cong A^{\mathrm{op}}$ and $\operatorname{Aut}_A({}_A A)\cong A^{\times}$ by right multiplication. Schur's lemma makes $\operatorname{End}_A(S)$ a division ring for a simple $S$. Free modules are direct sums of ${}_A A$, projective modules are their direct summands, and the idempotents of $A$ produce projective modules $Ae$; over a division algebra every module is free, while over the matrix algebra $M_n(F)$ the simple module $S=F^n$ is projective and not free. Nakayama's lemma holds over noncommutative rings for ideals inside the Jacobson radical. The modules form an abelian $R$-linear category $\operatorname{Mod}(A)$, and the guiding equivalence relation on algebras is Morita equivalence, under which $A$ and $M_n(A)$ have the same module theory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | commutative ring with identity $1 \neq 0$ |
| $F$, $K$ | fields |
| $A$ | unital associative $R$-algebra, generally noncommutative |
| $A^{\mathrm{op}}$ | opposite algebra, product $a \cdot_{\mathrm{op}} b = ba$ |
| $A^{\times}$ | group of units of $A$ |
| $Z(A)$ | center of $A$ |
| $1_A$ | unit of $A$ |
| $M$, $N$, $P$ | left $A$-modules |
| $M_A$ | right $A$-module |
| ${}_A M_B$ | $(A,B)$-bimodule |
| ${}_A A$, $A_A$ | left and right regular modules |
| $Ae$ | projective left module from an idempotent $e$ |
| $\operatorname{Hom}_A(M,N)$ | abelian group of $A$-linear maps |
| $\operatorname{End}_A(M)$ | endomorphism ring of $M$ |
| $\operatorname{Aut}_A(M)$ | automorphism group of $M$ |
| $\operatorname{Ann}_A(m)$, $\operatorname{Ann}_A(M)$ | annihilator of an element, of the module |
| $\mathfrak{m}$ | maximal left ideal |
| $S$ | simple (irreducible) module |
| $J(A)$ | Jacobson radical of $A$ |
| $\operatorname{Mod}(A)$ | category of left $A$-modules |
| $M \cong N$ | isomorphism of modules |





## Further Reading

- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 2nd ed. 1992), for modules over a general ring, the regular module, the isomorphism theorems, and Morita equivalence.
- Nicolas Bourbaki, *Algebra I* (Springer, 1989), for the algebra-level treatment of modules, tensor products and change of rings.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for free and projective modules and the division-ring case.
- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004), for the elementary theory of modules and the structure theorem over a principal ideal domain.
- Thomas W. Hungerford, *Algebra* (Springer, 1974), for the algebraic background and Nakayama's lemma.
- Nathan Jacobson, *Basic Algebra II* (Dover, 2nd ed. 2009), for the structure theory of rings and their modules.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the Jacobson radical, semisimple rings and the density theorem.
- T. Y. Lam, *Lectures on Modules and Rings* (Springer, 1999), for projective and injective modules over noncommutative rings.
- Joseph J. Rotman, *An Introduction to Homological Algebra* (Springer, 2nd ed. 2009), for the abelian category of modules.
