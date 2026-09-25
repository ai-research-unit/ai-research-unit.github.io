
# __Direct Sums, Free Modules and Rank__

## Introduction

The companion article *Modules* introduced modules over a ring, submodules, quotients, homomorphisms and the isomorphism theorems. This article develops the first layer of structure theory that the rest of the category uses: the two ways of assembling a family of modules into a larger one, the modules that are assembled from copies of the ground ring, and the invariant that measures how many copies are needed.

Throughout, $R$ is a commutative ring with identity $1 \neq 0$ and every module is a left $R$-module, unless it is stated otherwise. This is the corpus's default base: a result that needs a field, an integral domain, or the invertibility of $2$ says so at the point of use. Where a construction makes sense over a possibly noncommutative ring, the side on which $R$ acts is named explicitly.

The finite direct sum and the finite direct product of modules are the same object, and the modules built from it are the free modules, whose invariant is the rank. Over a field the rank is the dimension and everything is free; over a general commutative ring neither statement survives, and the reasons are recorded below. The two facts that carry the most weight later are the universal property of a free module, which converts a choice on a basis into a homomorphism, and the invariant basis number property, which makes rank well defined and so makes the words "free of rank $n$" meaningful.

## Direct Sums and Direct Products

### The External Direct Sum and Product

Let $\{M_i\}_{i \in I}$ be a family of $R$-modules indexed by a set $I$.

**Definition.** The **direct product** $\prod_{i \in I} M_i$ is the set of all families $(m_i)_{i \in I}$ with $m_i \in M_i$, with componentwise addition and scalar multiplication:

$$
(m_i)+(m_i')=(m_i+m_i'), \qquad r\,(m_i)=(r m_i).
$$

The **direct sum** $\bigoplus_{i \in I} M_i$ is the submodule of $\prod_{i \in I} M_i$ consisting of the families with $m_i=0$ for all but finitely many $i$.

Thus $\bigoplus_i M_i \subseteq \prod_i M_i$, and the inclusion is an equality exactly when $I$ is finite. For a finite index set $I=\{1,\dots,n\}$ both objects are written $M_1 \oplus \cdots \oplus M_n$ and are equal. The zero module is the direct sum over the empty index set, and it is the zero object: it is simultaneously initial and terminal.

Each summand carries the canonical injections and projections

$$
\iota_j : M_j \hookrightarrow \bigoplus_i M_i, \qquad \pi_j : \prod_i M_i \twoheadrightarrow M_j,
$$

where $\iota_j(m)$ has $m$ in slot $j$ and $0$ elsewhere, and $\pi_j$ reads slot $j$. On the direct sum the projections are defined by restriction, and

$$
\pi_j \circ \iota_k = \begin{cases} \operatorname{id}_{M_j}, & j=k, \\ 0, & j \neq k. \end{cases}
$$

### The Universal Properties

The product and the sum are the categorical product and coproduct, and it is these properties, not the formulas, that are used.

**Proposition (product).** For every module $N$ and every family of homomorphisms $f_i : N \to M_i$ there is a unique $f : N \to \prod_i M_i$ with $\pi_i \circ f=f_i$ for all $i$.

**Proposition (sum).** For every module $N$ and every family of homomorphisms $g_i : M_i \to N$ there is a unique $g : \bigoplus_i M_i \to N$ with $g \circ \iota_i=g_i$ for all $i$.

*Proof.* For the product take $f(n)=(f_i(n))$. For the sum take $g((m_i))=\sum_i g_i(m_i)$, a finite sum because $(m_i)$ is finitely supported; uniqueness follows on the summands. $\square$

Neither universal property restricts the family of maps, and the finiteness in the second statement lies in the *elements* of $\bigoplus_i M_i$, not in the maps out of it. The asymmetry between the two constructions appears when $I$ is infinite, and it is an asymmetry between the elements: $\bigoplus_i M_i$ is the submodule of $\prod_i M_i$ consisting of the finitely supported families, the inclusion is injective and not surjective, and the direct sum is therefore a coproduct but not a product, while the product is a product but not a coproduct. When $I$ is finite the two objects coincide, and the two universal properties make $\bigoplus_i M_i$ both a product and a coproduct; such an object is a **biproduct**. In the finite case the injections and projections satisfy the relations $\pi_j\iota_j=\operatorname{id}$, $\pi_j\iota_k=0$ for $j\neq k$, $\sum_j \iota_j\pi_j=\operatorname{id}$, and every element of the biproduct is recovered from them by $m=\iota_1\pi_1(m)+\iota_2\pi_2(m)$.

### Internal Direct Sums

The external constructions are matched by an internal description, which is how direct sum decompositions are recognised in practice.

**Definition.** Let $N_1,\dots,N_k$ be submodules of $M$. Then $M$ is their **internal direct sum**, written $M=N_1\oplus\cdots\oplus N_k$, if every $m \in M$ has a unique expression $m=n_1+\cdots+n_k$ with $n_i \in N_i$.

**Proposition.** $M=N_1\oplus\cdots\oplus N_k$ if and only if $M=N_1+\cdots+N_k$ and

$$
N_i \cap \Bigl(\sum_{j \neq i} N_j\Bigr)=0 \qquad \text{for every } i.
$$

*Proof.* Uniqueness fails exactly when two expressions differ, and their difference is a nonzero element of one $N_i$ lying in the sum of the others, with signs absorbed. $\square$

For two submodules the condition reduces to $M=N_1+N_2$ and $N_1\cap N_2=0$. The external sum and the internal sum are identified by sending $(n_i)$ to $\sum_i \iota_i(n_i)$, so no distinction is needed once the summands are submodules of a common module.

### Direct Summands and Idempotents

**Definition.** A submodule $N \subseteq M$ is a **direct summand** of $M$ if $M=N\oplus N'$ for some submodule $N'$, called a **complement** of $N$.

Over a field every subspace is a direct summ, because a basis of a subspace extends to a basis of the whole space; over a general ring this fails, and the failure is not covered here.

The module-theoretic content of a direct summand is an idempotent endomorphism.

**Proposition.** $N$ is a direct summand of $M$ if and only if $N=e(M)$ for an idempotent $e \in \operatorname{End}_R(M)$, that is $e^2=e$.

*Proof.* If $M=N\oplus N'$, let $e$ be the projection onto $N$ along $N'$; it is $R$-linear, $e(M)=N$ and $e^2=e$. Conversely, given $e^2=e$, put $N=e(M)$; then $\operatorname{id}-e$ is idempotent with image $\ker e$, and every $m=e(m)+(\operatorname{id}-e)(m)$ with $e(m) \in N$ and $m-e(m) \in \ker e$, so $M=N+\ker e$. If $m \in N \cap \ker e$ then $m=e(m')$ and $0=e(m)=e^2(m')=e(m')=m$, so the sum is direct. $\square$

The complement of $N=e(M)$ is $\ker e$, and the correspondence is with the set of idempotents of $\operatorname{End}_R(M)$. Idempotents are thus the algebraic encoding of projections; they reappear for projective modules and, over a commutative ring, in the decomposition of $R$ itself as a product of rings. When the idempotent is taken in the ring rather than in its endomorphism ring, $e\in R$, the same computation gives $M=eM\oplus(1-e)M$ together with $R=Re\oplus R(1-e)$, the **Peirce decomposition** of the module and of the ring with respect to $e$.

## Free Modules

### Definition and Bases

A subset $S \subseteq M$ is **linearly independent** if every finite relation $\sum_i r_i s_i=0$ with distinct $s_i \in S$ forces all $r_i=0$; it **generates** $M$ if every element is a finite $R$-linear combination of its elements; and it is a **basis** if it is linearly independent and generating. Equivalently, $B$ is a basis if every $m \in M$ has a unique expression

$$
m=\sum_{b \in B} r_b\, b
$$

with $r_b \in R$ and all but finitely many $r_b$ zero. The uniqueness of the coefficients is the whole point: it is the statement that the coefficients are *coordinates*, and it is exactly what a general generating set fails to provide.

**Definition.** An $R$-module is **free** if it has a basis. The zero module is free on the empty basis.

**Examples.** The module $R^n$ of $n$-tuples is free with the **standard basis** $e_1,\dots,e_n$, where $e_j$ has $1$ in slot $j$ and $0$ elsewhere. The polynomial ring $R[x]$ is free on $\{1,x,x^2,\dots\}$. Over $\mathbb{Z}$ the module $\mathbb{Z}$ is free of rank $1$; the module $\mathbb{Z}/n\mathbb{Z}$ for $n \ge 2$ is *not* free, because a nonzero free $\mathbb{Z}$-module is infinite and contains no element of finite additive order. Over the split complex numbers $\mathbb{D}$, the free modules of finite rank are the modules $\mathbb{D}^n$.

### The Universal Property

**Theorem (universal property of a free module).** Let $B$ be a basis of the free module $L$ and let $M$ be any $R$-module. Every function $\varphi : B \to M$ extends uniquely to an $R$-linear map $f : L \to M$ with $f|_B=\varphi$.

*Proof.* Existence: define $f\bigl(\sum_b r_b b\bigr)=\sum_b r_b \varphi(b)$, a finite sum and well defined because the coordinates $r_b$ are unique. Linearity is immediate. Uniqueness: any two extensions agree on a basis, and a basis generates. $\square$

The universal property is the working form of freeness and is equivalent to it: if $L$ has a generating set $B$ with this extension property, applying it with $\varphi$ the inclusion $B \hookrightarrow L$ gives a splitting of the canonical map from the free module on $B$, so $B$ is a basis. It is also the reason that a linear map may be specified on a basis and nowhere else.

### Free Modules as Direct Sums

**Proposition.** $L$ is free with basis $B$ if and only if $L \cong \bigoplus_{b \in B} R$, the direct sum of one copy of the regular module for each basis element.

*Proof.* If $B$ is a basis, the map $\bigoplus_{b \in B} R \to L$, $(r_b) \mapsto \sum_b r_b b$, is well defined because only finitely many $r_b$ are nonzero, and it is bijective by uniqueness of coordinates. Conversely a direct sum of copies of $R$ has as basis the images of the units $1$ in the summands. $\square$

So free modules are exactly the direct sums of copies of $R$, and the rank, when it is defined, is the number of summands. Write

$$
R^{(I)}=\bigoplus_{i \in I} R
$$

for the free module on a basis indexed by $I$; in particular $R^{(n)}=R^n$ and $R^{(\varnothing)}=0$.

### Every Module is a Quotient of a Free Module

**Theorem.** Every $R$-module $M$ is a quotient of a free module.

*Proof.* Let $B$ be a generating set of $M$, for instance $B=M$ itself. The universal property extends the inclusion $B \hookrightarrow M$ to a surjection $R^{(B)} \to M$, whose kernel is a submodule $K$. The first isomorphism theorem gives $M \cong R^{(B)}/K$. $\square$

A surjection $L \twoheadrightarrow M$ with $L$ free is a **presentation** of $M$, and $K=\ker(L \to M)$ is the **relation module**. This is the input to the structure theory and to the theory of exact sequences developed: a module is controlled by the way it is a quotient of a free module. Over a field every relation module is again free and can be made trivial by a change of basis of $L$, which is Gaussian elimination; over $\mathbb{Z}$ the relation module is free but the quotient need not be.

## Rank and the Invariant Basis Number Property

### The Problem

For a free module with basis $B$, one wants to call $|B|$ its **rank**. This presupposes that any two bases have the same cardinality. For a finitely generated free module over a commutative ring this is true, but it is a theorem and not a tautology, and there are rings where it fails.

**Definition.** A ring $R$ has **invariant basis number** (IBN) if $R^m \cong R^n$ as $R$-modules with $m,n$ finite implies $m=n$. If $R$ has IBN, the **rank** of a free module is the cardinality of any basis, written $\operatorname{rk}_R L$, and $L$ is free of rank $n$ exactly when $L \cong R^n$.

### Rank over Commutative Rings

**Theorem.** Every commutative ring with $1 \neq 0$ has invariant basis number.

*Proof.* Suppose $R^m \cong R^n$, and let $\mathfrak{m}$ be a maximal ideal, which exists by Zorn's lemma. The field $k=R/\mathfrak{m}$ is an $R$-module via $r\cdot \bar{s}=\overline{rs}$, and $k \otimes_R R^j \cong k^j$ for every $j$ because $k \otimes_R R \cong k$ and tensor products distribute over finite direct sums. Applying the functor $k \otimes_R -$ to the isomorphism $R^m \cong R^n$ gives an isomorphism $k^m \cong k^n$ of $k$-vector spaces, so $m=n$ by the field case. $\square$

The proof uses only that $-\otimes_R k$ is a functor, not that it is exact; this is why it applies without flatness hypotheses. Two consequences are worth naming. First, rank is additive over direct sums: if $L$ and $L'$ are free then so is $L \oplus L'$, with basis the disjoint union, and

$$
\operatorname{rk}_R (L \oplus L')=\operatorname{rk}_R L + \operatorname{rk}_R L'.
$$

Second, a free module has a well-defined rank but a submodule of a free module need not be free, so "rank of a submodule" is not available in general.

### Rank over Division Rings and the Failure of IBN

Over a division ring the classical argument works: a maximal linearly independent subset of a module is a basis, since a relation with nonzero coefficient on an outside element can be solved by invertibility. Hence every module over a division ring is free and any two bases of a finitely generated module have the same cardinality. In particular every module over a division ring $D$ obeys the vector-space theory, as recorded in *Modules*; the quaternion algebra is treated in *Division Algebras*.

Invariant basis number is not a formality. Let $k$ be a field and let $V$ be a $k$-vector space of countably infinite dimension, and put $R=\operatorname{End}_k(V)$, a noncommutative ring. Decompose $V=V_0 \oplus V_1$ into two subspaces each of countable dimension, so that $V_0 \cong V_1 \cong V$; then $R \cong \operatorname{Hom}_k(V_0 \oplus V_1,V)$ as left $R$-modules, and

$$
R \cong \operatorname{Hom}_k(V_0,V) \oplus \operatorname{Hom}_k(V_1,V) \cong R \oplus R,
$$

so $R \cong R^2$ and, iterating, $R^m \cong R^n$ for all $m,n \ge 1$. This ring has no invariant basis number, and "rank" is meaningless for it. The commutative case is therefore a genuine hypothesis in the theorem above.

### Rank and Generation

Rank is the smallest number of generators of a *free* module, but it is not the smallest number of generators of an arbitrary module, and the two differ in an essential way. If $M$ is generated by $n$ elements there is a surjection $R^n \twoheadrightarrow M$, so $M$ is a quotient of a free module of rank $n$; the kernel of that surjection measures the difference. A module generated by $n$ elements can also be generated by more, and it can be isomorphic to a quotient of $R^n$ in many ways.

**Proposition.** If $M$ is a quotient of $R^n$ and $N$ is a quotient of $R^m$ then $M \oplus N$ is a quotient of $R^{n+m}$; and a submodule of a finitely generated module over a Noetherian ring is finitely generated.

*Proof.* Compose the two surjections with the injections into the direct sum. For the second statement, the submodule is a quotient of a submodule of $R^n$; over a Noetherian ring every submodule of $R^n$ is finitely generated, by induction on $n$ and the definition of Noetherian. $\square$

## Finitely Generated Modules

### Finite Generation

**Definition.** An $R$-module $M$ is **finitely generated** if $M=Rm_1+\cdots+Rm_k$ for finitely many elements $m_1,\dots,m_k$.

**Proposition.** $M$ is finitely generated if and only if there is a surjection $R^k \twoheadrightarrow M$ for some $k \ge 0$.

*Proof.* Given generators, send the standard basis to them and extend by the universal property of $R^k$; given a surjection, the images of the standard basis generate. $\square$

Over a field the finitely generated modules are the finite-dimensional vector spaces, and all of them are free; over $\mathbb{Z}$ they are the finitely generated abelian groups, and $\mathbb{Z}/n\mathbb{Z}$ is finitely generated but not free. Finite generation is preserved by quotients, by finite direct sums, and by extension of scalars, and it is *not* preserved by passing to submodules without a Noetherian hypothesis. This is one of the few places where a commutative ring behaves visibly worse than a field.

### Nakayama's Lemma

Finitely generated modules are controlled by their quotients modulo the Jacobson radical.

**Lemma (Nakayama).** Let $I \subseteq J(R)$ be an ideal contained in the Jacobson radical and let $M$ be a finitely generated $R$-module with $IM=M$. Then $M=0$. More generally, if $N \subseteq M$ is a submodule with $M=N+IM$ then $M=N$.

*Proof.* Suppose $M \neq 0$ and let $m_1,\dots,m_k$ be a minimal generating set. From $M=IM$ we get $m_k=\sum_i a_i m_i$ with $a_i \in I$; rearranging,

$$
(1-a_k)m_k=\sum_{i<k} a_i m_i.
$$

Since $a_k \in J(R)$, the element $1-a_k$ is a unit, so $m_k$ lies in the span of $m_1,\dots,m_{k-1}$, contradicting minimality. The second statement applies the first to $M/N$. $\square$

For a local ring $(R,\mathfrak{m})$ one takes $I=\mathfrak{m}$, and Nakayama then says that a finitely generated module over a local ring has a minimal generating set of exactly $\dim_{k}(M/\mathfrak{m}M)$ elements, where $k=R/\mathfrak{m}$; this number is the **minimal number of generators**. Nakayama is used in the structure theory and in the theory of projective modules.

### Noetherian Rings

**Definition.** A commutative ring $R$ is **Noetherian** if its ideals satisfy the ascending chain condition, equivalently if every ideal is finitely generated.

**Theorem.** The following are equivalent for a commutative ring $R$: (i) $R$ is Noetherian; (ii) every submodule of a finitely generated $R$-module is finitely generated; (iii) every submodule of $R^n$ is finitely generated for every $n$.

*Proof.* (ii) $\Rightarrow$ (iii) is immediate with $M=R^n$; (iii) $\Rightarrow$ (i) is the case $n=1$; (i) $\Rightarrow$ (ii) is proved by induction on the number of generators, using that an extension of two finitely generated modules is finitely generated and that $R$ Noetherian makes every ideal, hence every submodule of $R$, finitely generated. $\square$

Principal ideal domains are Noetherian, and so is every finitely generated algebra over a field; both facts are used later. What Noetherianity buys here is exactly the statement that a relation module is finitely generated, which is what makes a finite presentation available and what makes the structure theorem for finitely generated modules over a PID provable. In a non-Noetherian ring a finitely generated module can have submodules that are not finitely generated, and the structure theory has no analogue.

## Rank in the Standard Cases

### Over a Field

If $R=F$ is a field then every module is free, every submodule of a free module is free, and the rank of a free module is its **dimension**, written $\dim_F V$. Two finite-dimensional vector spaces are isomorphic exactly when their dimensions agree, because a bijection between bases extends to an isomorphism , conversely, an isomorphism carries a basis to a basis. This is the whole of the classification of finitely generated $F$-modules, and it is the case against which every other case is measured. The companion articledevelops it; the point recorded here is that it holds because every element of $F^{\times}$ is a unit, so a nonzero coefficient in a relation can always be divided out.

### Over the Integers

For $R=\mathbb{Z}$ the free modules are the groups $\mathbb{Z}^n$, of rank $n$, and the finitely generated modules are the finitely generated abelian groups. Rank is the number of free summands in the structure theorem for finitely generated modules over a principal ideal domain, and it is not the order of the group: the groups $\mathbb{Z}$ and $\mathbb{Z}\oplus \mathbb{Z}/2\mathbb{Z}$ have ranks $1$ and $1$ but are not isomorphic, the free rank being only one of the two invariants. The other invariant is the torsion, and it is invisible to rank.

### Over a Principal Ideal Domain

Over a principal ideal domain, every submodule of a free module is free. This is the theorem that makes a presentation $0 \to K \to R^n \to M \to 0$ computable: $K$ has a basis, so it is described by a matrix, and the structure of $M$ is read off from that matrix. Over a general commutative ring the corresponding statement is false, and the standard counterexample is the ideal $(x,y) \subseteq R=k[x,y]$, which is a submodule of the free module $R$ of rank $1$ and is not free: it is not principal, so it is not free of rank $1$, and it is not free of rank $n \ge 2$ either, since tensoring with the fraction field $k(x,y)$ turns it into $k(x,y)$ itself, of dimension $1$, while a free module of rank $n$ would give dimension $n$.

### Over the Split Complex Numbers

The split complex numbers $\mathbb{D}=\mathbb{R}[j]/(j^2-1)$ are not a domain, and their module theory is governed by the idempotents $e_\pm=\tfrac{1}{2}(1 \pm j)$, which satisfy $e_+^2=e_+$, $e_-^2=e_-$, $e_+e_-=0$ and $e_++e_-=1$. The ring isomorphism

$$
\mathbb{D} \cong \mathbb{R} \times \mathbb{R}, \qquad a+bj \longmapsto (a+b,\ a-b),
$$

sends $e_+$ to $(1,0)$ and $e_-$ to $(0,1)$. Every $\mathbb{D}$-module therefore splits as $M \cong M_+ \oplus M_-$ with $M_\pm$ real vector spaces, and

$$
\mathbb{D}^{(I)} \cong \mathbb{R}^{(I)} \oplus \mathbb{R}^{(I)}
$$

as an $\mathbb{R}$-module. So a free $\mathbb{D}$-module of rank $n$ is a pair of real vector spaces each of dimension $n$, and a $\mathbb{D}$-module is free of rank $n$ exactly when both idempotent components are real vector spaces of dimension $n$. Rank over $\mathbb{D}$ is thus a pair of ordinary dimensions constrained to be equal. This is the first place in the category where a single rank is replaced by several invariants because the ring has zero divisors.

### Over a Polynomial Ring

For $R=K[x]$ over a field $K$, the free modules are $K[x]^{(I)}$; the module $K[x]^n$ is free of rank $n$, and a matrix over $K[x]$ represents a homomorphism $K[x]^m \to K[x]^n$ with respect to the standard bases. The polynomial ring is a principal ideal domain, so submodules of free modules are free and the rank of a submodule of $K[x]^n$ is at most $n$; both facts are used in the module-theoretic treatment of a linear operator.

### Rank and the Fraction Field

Over an integral domain $R$ with fraction field $K=\operatorname{Frac}(R)$, tensoring with $K$ is a way to extract a numerical invariant from a module that need not be free. The **rational rank** of an $R$-module $M$ is

$$
\operatorname{rk}^{K} M=\dim_K (M \otimes_R K).
$$

Since $K$ is a flat $R$-module, a free module of rank $n$ has rational rank $n$, and a torsion module has rational rank $0$. For a finitely generated module over a principal ideal domain the rational rank equals the free rank, and the difference between the module and its rational rank is exactly its torsion. Over a general domain the rational rank can be finite while the module is not free, so it is an invariant of limited resolution; its virtue is that it is always defined.

## Free Resolutions

The presentation of a module by a free module can be iterated, and the resulting chain is the basic object of homological algebra.

**Definition.** A **free resolution** of an $R$-module $M$ is an exact sequence

$$
\cdots \xrightarrow{d_3} L_2 \xrightarrow{d_2} L_1 \xrightarrow{d_1} L_0 \xrightarrow{\epsilon} M \to 0
$$

in which every $L_i$ is a free $R$-module. It is **finite** if $L_i=0$ for all $i$ beyond some $N$. The **projective dimension** of $M$ is the least length of a finite projective resolution, or $\infty$ if none exists.

Every module has a free resolution: choose a surjection $\epsilon:L_0 \to M$, then a surjection $L_1 \to \ker \epsilon$, then a surjection $L_2 \to \ker d_1$, and continue. If $M$ is finitely generated over a Noetherian ring, the construction can be performed with finitely generated free modules at every stage, because each kernel is then finitely generated. A module of projective dimension $0$ is a projective module, which is the next topic after rank; over a field every module has projective dimension $0$, and over a principal ideal domain every module has projective dimension at most $1$. The proof that the resolution does not depend on the choices made, in the sense that the derived functors computed from it do not, lies outside this article.

## Summary

A family of modules is assembled by the direct product, whose elements are arbitrary families, and the direct sum, whose elements are finitely supported families; for finite index sets the two coincide and form a biproduct. Internally, $M$ is the direct sum of submodules when every element has a unique expression as a sum of one element from each, which for two summands is the condition $N_1+N_2=M$ and $N_1\cap N_2=0$. Direct summands are exactly the images of idempotent endomorphisms.

A free module is one with a basis, equivalently a direct sum of copies of the regular module $R$; its universal property says that a map on a basis extends uniquely and is the practical test for freeness. Every module is a quotient of a free module, and the kernel of such a quotient is its relation module, which controls the module. Rank is well defined over every commutative ring with $1 \neq 0$ by the invariant basis number property, proved by reducing modulo a maximal ideal and using the field case; it fails over some noncommutative rings, for instance $\operatorname{End}_k(V)$ for $V$ of infinite dimension.

Finitely generated modules are the quotients of some $R^k$. Nakayama's lemma controls them modulo the Jacobson radical, and over a Noetherian ring their submodules are again finitely generated. A free resolution iterates the presentation of a module by free modules and supplies the input to the homological theory developed.

| Notion | Over a field $F$ | Over a commutative ring $R$ |
|---|---|---|
| Every module free | yes | no |
| Rank well defined | yes (dimension) | yes (IBN) |
| Submodule of a f.g. module is f.g. | yes | only if $R$ is Noetherian |
| Basis of a submodule of a free module | exists | need not exist |
| Direct summands | all subspaces | the images of idempotents |
| Classification of f.g. modules | by dimension | only when $R$ is a PID |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | commutative ring with identity $1 \neq 0$ unless stated otherwise |
| $F$, $K$ | a field |
| $M$, $N$, $L$ | modules, left unless stated |
| $\mathbb{Z}/n\mathbb{Z}$ | integers modulo $n$ |
| $\prod_i M_i$ | direct product of a family of modules |
| $\bigoplus_i M_i$ | direct sum, the finitely supported submodule of the product |
| $R^{(I)}$, $R^{(n)}=R^n$ | free module, direct sum of copies of $R$ indexed by $I$ |
| $\iota_j$, $\pi_j$ | canonical injection and projection of a direct sum or product |
| $N_1 \oplus \cdots \oplus N_k$ | internal direct sum of submodules |
| $\operatorname{rk}_R L$ | rank of a free module |
| $e \in \operatorname{End}_R(M)$, $e^2=e$ | idempotent endomorphism; $e(M)$ is a direct summand |
| $J(R)$ | Jacobson radical of $R$ |
| $IM$ | submodule generated by products $am$, $a \in I$, $m \in M$ |
| $L_1 \to L_0 \to M \to 0$ | free resolution of a module |







## Further Reading

- M. F. Atiyah and I. G. Macdonald, *Introduction to Commutative Algebra* (Addison-Wesley, 1969), for Nakayama's lemma, Noetherian rings and the local theory.
- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for the universal properties of sums and products and the module conventions.
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003), for free modules and invariant basis number.
- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004), for the elementary theory with examples.
- Thomas W. Hungerford, *Algebra* (Springer, 1974), for free modules, rank and direct sums.
- T. Y. Lam, *Lectures on Modules and Rings* (Springer, 1999), for the failure of invariant basis number and the examples.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for free modules and resolutions.
- Joseph J. Rotman, *An Introduction to Homological Algebra* (Springer, 2nd ed. 2009), for free resolutions and projective dimension.
