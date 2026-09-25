# __Modules__

## Introduction

A **module over a ring** $R$ is an abelian group on which $R$ acts by scalars, satisfying the axioms of a vector space with scalars drawn from a ring rather than a field. When $R$ is a field this is exactly a vector space, so modules generalize vector spaces to arbitrary rings. Modules over a commutative ring were introduced in *Rings: A General Introduction* (§14–§15); this article develops the theory systematically, from submodules, quotients, and homomorphisms, through free modules, exact sequences, and tensor products, to the structure theorem over a principal ideal domain and the projective, injective, and division-ring cases.

Throughout, $R$ is an associative ring with identity $1 \neq 0$ and modules are left modules. When $R$ is commutative, left and right modules agree via $mr = rm$ and we speak of $R$-modules, matching *Rings*; commutativity is flagged whenever used. The companion articles *Vector Spaces: A General Introduction* and *Algebras: A General Introduction* work over commutative rings; the extra generality here is needed for tensor products, projective modules, and the division-ring case. We assume familiarity with rings, ideals, and vector spaces.

---

# Part I: Foundations

## 1. Definition of a Module

A **left $R$-module** is an abelian group $(M,+)$ with a scalar multiplication $R \times M \to M$, $(r,m) \mapsto rm$, such that for all $r,s \in R$ and $m,n \in M$:

$$
r(m+n)=rm+rn, \qquad (r+s)m=rm+sm, \qquad (rs)m=r(sm), \qquad 1m=m.
$$

These are axioms (M1)–(M4) of *Rings* §14, now for a possibly noncommutative $R$. A **right $R$-module** uses $M \times R \to M$, $(m,r) \mapsto mr$, with $(m+n)r=mr+nr$, $m(r+s)=mr+ms$, $m(rs)=(mr)s$, $m1=m$. Over a commutative ring a left module becomes a right module by $mr := rm$, so the two notions coincide. The **zero module** $\{0\}$ has one element.

## 2. Elementary Properties

For a left $R$-module $M$: $0m=0$; $r0=0$; $(-r)m=r(-m)=-(rm)$; $(-r)(-m)=rm$; $r(m-n)=rm-rn$; $(r-s)m=rm-sm$; and the elements $0$ and $-m$ are unique.

The scalar action is equivalent to a unital ring homomorphism

$$
\rho : R \to \operatorname{End}_{\mathbb{Z}}(M), \qquad \rho(r)(m)=rm,
$$

where $\operatorname{End}_{\mathbb{Z}}(M)$ is the endomorphism ring of the abelian group $M$. Axiom (M3) gives $\rho(rs)=\rho(r)\circ\rho(s)$ and (M4) gives $\rho(1)=\operatorname{id}$; conversely, every such homomorphism makes $M$ a left $R$-module. So a module is exactly a representation of $R$ by endomorphisms of an abelian group.

## 3. Examples

The first example is the ring itself. It is the one that reduces the theory of ideals to the theory of modules, and it is used throughout.

**Definition.** Let $R$ be a ring with identity $1$. The **left regular module** ${}_R R$ is the abelian group $(R,+)$ with the scalar multiplication

$$
R \times R \to R, \qquad (r,m) \mapsto rm,
$$

the multiplication of $R$. The **right regular module** $R_R$ is $(R,+)$ with $(m,r) \mapsto mr$, and the left and right actions together make $R$ a **bimodule** ${}_R R_R$, the two commuting by associativity. The side on which the scalars are written is recorded by the side of the subscript.

The carrier of ${}_R R$ is the additive group $(R,+)$, which is only an abelian group and carries no multiplication; the multiplication of $R$ is not discarded but retained, and it is the action. Axioms (M1)–(M4) of §1 are then the ring axioms verbatim: the two distributive laws, associativity, and the law $1m=m$. The element $1$ alone is a basis, so ${}_R R$ is the free module of rank one, and the direct sums of its copies are the free modules (§9).

**Theorem.** For $L \subseteq R$: $L$ is a submodule of ${}_R R$ if and only if $L$ is a left ideal of $R$; $L$ is a submodule of $R_R$ if and only if it is a right ideal; and $L$ is a submodule of ${}_R R_R$ if and only if it is a two-sided ideal.

*Proof.* By §4 a submodule of ${}_R R$ is an additive subgroup $L$ with $rl \in L$ for every $r \in R$, $l \in L$; by *Rings* §6 an additive subgroup $L$ is a left ideal under exactly the same condition. The scalar action of ${}_R R$ is by definition the multiplication of $R$, so the two conditions are the same formula and not merely equivalent ones. The right-handed and the two-sided statement are the same argument with the multiplication read on the right, or on both sides. $\square$

The bijection is the identity map on subsets of $R$, so it is an isomorphism of the lattice of submodules of ${}_R R$ onto the lattice of left ideals of $R$: it preserves inclusion, intersection and sum. The one-sided ideal theory of $R$ is therefore the submodule theory of its regular module, and the language of ideals in *Rings* is the language of this example.

**(a)** If $R=F$ is a field, $F$-modules are vector spaces.

**(b)** $\mathbb{Z}$-modules are exactly abelian groups, with the unique action $n \cdot a = a+\cdots+a$. Hence finitely generated abelian groups are the finitely generated $\mathbb{Z}$-modules, and §15 recovers their classification.

**(c)** By the theorem above, the submodules of ${}_R R$ are the left ideals of $R$, that is, the ideals when $R$ is commutative, so ideals are modules (*Rings* §6). For an ideal $I$ of commutative $R$, both $I$ and $R/I$ are $R$-modules.

**(d)** $R^n$ is the free $R$-module of rank $n$, and $M_n(R)$ is free of rank $n^2$. For noncommutative $R$, the column space is a left module and the row space a right module.

**(e)** $R[x]$ is free on $\{1,x,x^2,\dots\}$, as is every $R[x]/(f)$. Over a field $K$, a $K[x]$-module structure on a vector space $V$ is exactly a $K$-linear operator $T:V\to V$ with $x \cdot v=T(v)$, and the $K[x]$-submodules are the $T$-invariant subspaces (§16).

**(f)** For a group $G$ and commutative ring $R$, the group ring $R[G]$ is an $R$-algebra, and $R[G]$-modules are exactly the $R$-linear representations of $G$.

**(g)** A division ring $D$ has no zero divisors, so $D$-modules are $D$-vector spaces (§19); a field is the commutative case. Rings with zero divisors, such as the split-complex numbers $\mathbb{D}$, are not division rings, and their module theory follows their ideal structure. The quaternion algebra is treated in *Division Algebras*.

## 4. Submodules

A subset $N \subseteq M$ is a **submodule** if it is an additive subgroup and closed under scalars: $n-n' \in N$ and $rn \in N$ for $r \in R$ and $n,n' \in N$. It is then itself an $R$-module; the trivial submodules are $0$ and $M$.

The intersection of any family of submodules is a submodule, and the **sum** $\sum_i N_i$, consisting of all finite sums $\sum_i n_i$ with $n_i \in N_i$, is the smallest submodule containing every $N_i$. For $S \subseteq M$, the submodule **generated by $S$** is the set of finite $R$-linear combinations of elements of $S$; $M$ is **cyclic** if $M=Rm$.

The **annihilator** $\operatorname{Ann}(m)=\{r : rm=0\}$ is a left ideal, and $R/\operatorname{Ann}(m) \cong Rm$ via $r \mapsto rm$. The annihilator $\operatorname{Ann}(M)=\{r : rm=0 \text{ for all } m\}$ is a two-sided ideal. A nonzero module is **simple** if its only submodules are $0$ and $M$; then $M \cong R/\mathfrak{m}$ for a maximal left ideal $\mathfrak{m}$.

## 5. Quotient Modules

For a submodule $N \subseteq M$, the cosets $M/N=\{m+N\}$ form a left $R$-module under

$$
(m+N)+(m'+N)=(m+m')+N, \qquad r(m+N)=rm+N,
$$

which is well defined because $N$ is closed under scalars. The **natural projection** $\pi:M \to M/N$, $\pi(m)=m+N$, is surjective with kernel $N$.

## 6. Module Homomorphisms

A map $f:M \to N$ of left $R$-modules is **$R$-linear** (a **homomorphism**) if $f(m+m')=f(m)+f(m')$ and $f(rm)=rf(m)$; it is an **isomorphism** if bijective, written $M \cong N$. Its **kernel** $\ker f=\{m : f(m)=0\}$ and **image** $\operatorname{im} f=\{f(m)\}$ are submodules of $M$ and $N$, $f$ is injective if and only if $\ker f=0$, and its **cokernel** is $N/\operatorname{im} f$. The set $\operatorname{Hom}_R(M,N)$ is an abelian group, and $\operatorname{End}_R(M)=\operatorname{Hom}_R(M,M)$ is a ring under composition with unit group $\operatorname{Aut}_R(M)$.

When $R$ is commutative, $\operatorname{Hom}_R(M,N)$ is an $R$-module via $(rf)(m)=rf(m)=f(rm)$. For noncommutative $R$ there is in general no natural $R$-module structure, only the abelian group (and a module structure over the center); this is one reason the series works over commutative rings.

## 7. The Isomorphism Theorems

For left $R$-modules: **(a)** $M/\ker f \cong \operatorname{im} f$; **(b)** $(A+B)/B \cong A/(A \cap B)$ for submodules $A,B \subseteq M$; **(c)** $M/B \cong (M/A)/(B/A)$ for submodules $A \subseteq B \subseteq M$; **(d)** (correspondence) the submodules of $M/N$ correspond bijectively, preserving inclusions, sums, and intersections, to the submodules of $M$ containing $N$, via $L \mapsto L/N$. The proofs pass to cosets exactly as for groups and rings.

---

# Part II: Constructions

## 8. Direct Sums and Products

For a family $\{M_i\}_{i \in I}$ of left $R$-modules, the **direct product** $\prod_i M_i$ consists of families $(m_i)$ with componentwise operations, and the **direct sum** is the submodule

$$
\bigoplus_i M_i=\Bigl\{(m_i) \in \textstyle\prod_i M_i : m_i=0 \text{ for all but finitely many } i\Bigr\}.
$$

Thus $\bigoplus_i M_i \subseteq \prod_i M_i$, with equality for finite $I$, where we write $M_1 \oplus \cdots \oplus M_n$. The product is the categorical product and the sum the coproduct.

For submodules $N_1,\dots,N_k \subseteq M$, we write $M=N_1 \oplus \cdots \oplus N_k$ ($M$ is their **internal direct sum**) if every $m$ has a unique expression $m=n_1+\cdots+n_k$ with $n_i \in N_i$; equivalently, $M=N_1+\cdots+N_k$ and $N_i \cap \bigl(\sum_{j \neq i} N_j\bigr)=0$ for each $i$. A submodule $N$ is a **direct summand** if $M=N \oplus N'$ for some $N'$; this holds if and only if $N=e(M)$ for an **idempotent** $e \in \operatorname{End}_R(M)$, namely the projection onto $N$ along a complement.

## 9. Free Modules and Bases

A **linear combination** of $S \subseteq M$ is a finite sum $\sum r_i s_i$; $S$ **generates** $M$ if every element is one, and is **linearly independent** if $r_1s_1+\cdots+r_ks_k=0$ for distinct $s_i \in S$ forces all $r_i=0$. A **basis** is a linearly independent generating set, equivalently a set $B$ such that every $m$ has a unique finite expansion $m=\sum_{b \in B} r_b b$. A module is **free** if it has a basis; the zero module is free on the empty basis. This is the definition of *Rings* §15.

$R^n$ is free with the **standard basis** $e_1,\dots,e_n$, and $R[x]$ is free on $\{1,x,x^2,\dots\}$. Over $\mathbb{Z}$, the module $\mathbb{Z}$ is free of rank $1$, but $\mathbb{Z}/n\mathbb{Z}$ is not free for $n \geq 2$: a nonzero free $\mathbb{Z}$-module is infinite, while the empty-basis free module is zero.

**Universal property.** A function from a basis $B$ of a free module $F$ to any module $M$ extends uniquely to a homomorphism $F \to M$. Hence $F \cong \bigoplus_{i \in I} R$ for a basis of cardinality $I$, so free modules are exactly the direct sums of copies of the regular module ${}_R R$ of §3.

**Every module is a quotient of a free module:** mapping a free basis labelled by the elements of $M$ to those elements gives a surjection $F \to M$, so $M \cong F/\ker \varphi$. Over an integral domain, free modules are torsion-free (§14).

## 10. Rank and the Invariant Basis Number Property

The **rank** of a free module is the cardinality of a basis; well-definedness requires that all bases have the same cardinality. A ring has **invariant basis number** (IBN) if $R^m \cong R^n$ with $m,n$ finite implies $m=n$.

**Theorem.** Every commutative ring with $1 \neq 0$ has IBN. *Proof sketch.* Take a maximal ideal $\mathfrak{m}$ (Zorn's lemma); then $R/\mathfrak{m}$ is a field, and from $R^m \cong R^n$, tensoring with $R/\mathfrak{m}$ gives an isomorphism $(R/\mathfrak{m})^m \cong (R/\mathfrak{m})^n$ of vector spaces, so $m=n$. $\square$

Division rings also have IBN (§19), so free modules over every ring in this series have a well-defined rank, and a finitely generated free module of rank $n$ is $R^n$; this is the rank used in *Algebras: A General Introduction*. Some rings do fail IBN, so the theorem is a genuine statement, not a formality.

## 11. Finitely Generated Modules

$M$ is **finitely generated** if $M=Rm_1+\cdots+Rm_k$ for finitely many elements, equivalently if there is a surjection $R^k \to M$. Over a field these are the finite-dimensional vector spaces, all free; over $\mathbb{Z}$ they are the finitely generated abelian groups. Finite generation does not imply freeness: $\mathbb{Z}/n\mathbb{Z}$ is finitely generated and not free for $n \geq 2$.

A commutative ring $R$ is **Noetherian** if every ideal is finitely generated, equivalently if its ideals satisfy the ascending chain condition. Then $R$ is Noetherian if and only if every submodule of every finitely generated $R$-module is finitely generated. Principal ideal domains are Noetherian, which is the finiteness input for §15.

**Nakayama's lemma.** If $I \subseteq J(R)$ lies in the Jacobson radical and $M$ is finitely generated with $IM=M$, then $M=0$; equivalently, if $M=N+IM$ for a submodule $N$, then $M=N$. For a local ring one takes $I$ to be its maximal ideal.

## 12. Exact Sequences

A sequence $\cdots \to M_{i+1} \xrightarrow{f_{i+1}} M_i \xrightarrow{f_i} M_{i-1} \to \cdots$ is **exact at $M_i$** if $\operatorname{im} f_{i+1}=\ker f_i$, and **exact** if it is exact everywhere. Thus $0 \to A \xrightarrow{f} B$ is exact if and only if $f$ is injective, and $B \xrightarrow{g} C \to 0$ is exact if and only if $g$ is surjective. A **short exact sequence** $0 \to A \xrightarrow{i} B \xrightarrow{q} C \to 0$ has $i$ injective, $\operatorname{im} i=\ker q$, and $q$ surjective, and then $B/A \cong C$; the basic example is $0 \to N \to M \to M/N \to 0$.

**Splitting lemma.** For $0 \to A \xrightarrow{i} B \xrightarrow{q} C \to 0$, the following are equivalent: (i) there is a **section** $s:C \to B$ with $qs=\operatorname{id}_C$; (ii) there is a **retraction** $r:B \to A$ with $ri=\operatorname{id}_A$; (iii) $B \cong A \oplus C$ compatibly with $i$ and $q$. The sequence then **splits**. Every short exact sequence of vector spaces splits, because every subspace has a complement, but $0 \to \mathbb{Z} \xrightarrow{\cdot 2} \mathbb{Z} \to \mathbb{Z}/2\mathbb{Z} \to 0$ does not, since a splitting would give an element of order $2$ in $\mathbb{Z}$.

**Functors.** The functor $\operatorname{Hom}_R(M,-)$ is **left exact** and $-\otimes_R M$ is **right exact**: in general $\operatorname{Hom}_R(M,-)$ need not preserve surjections, and $-\otimes_R M$ need not preserve injections.

## 13. Tensor Products of Modules

Let $R$ be commutative. A map $b:M \times N \to P$ is **bilinear** if it is linear in each variable: $b(m+m',n)=b(m,n)+b(m',n)$, $b(m,n+n')=b(m,n)+b(m,n')$, and $b(rm,n)=b(m,rn)=r\,b(m,n)$. The **tensor product** $M \otimes_R N$ is generated by symbols $m \otimes n$ subject to

$$
(m+m')\otimes n=m\otimes n+m'\otimes n, \quad m\otimes(n+n')=m\otimes n+m\otimes n', \quad (rm)\otimes n=m\otimes(rn)=r(m\otimes n),
$$

that is, it is the quotient of the free module on $M \times N$ by these relations. Its **universal property** is that every bilinear $b$ factors uniquely as $\tilde{b} \circ \otimes$ for an $R$-linear map $\tilde{b}:M \otimes_R N \to P$ with $\tilde{b}(m \otimes n)=b(m,n)$. Elements are finite sums $\sum_i m_i \otimes n_i$, and not every element is an elementary tensor.

**Properties.** $R \otimes_R M \cong M$; $M \otimes_R N \cong N \otimes_R M$; $(M \otimes_R N)\otimes_R P \cong M \otimes_R (N \otimes_R P)$; $\bigl(\bigoplus_i M_i\bigr)\otimes_R N \cong \bigoplus_i (M_i \otimes_R N)$, and $M \otimes_R 0=0$; the tensor product of finitely generated modules is finitely generated. There is a natural **tensor–hom adjunction** $\operatorname{Hom}_R(M \otimes_R N,P) \cong \operatorname{Hom}_R\bigl(M,\operatorname{Hom}_R(N,P)\bigr)$.

**Base change.** For a ring homomorphism $R \to S$, the tensor product $S \otimes_R M$ is an $S$-module: **extension of scalars**, of which complexification in *Algebras: A General Introduction* is the algebra-level case.

**Flatness.** A module $M$ is **flat** if $-\otimes_R M$ preserves injections. Free modules and projective modules (§17) are flat. Over $\mathbb{Z}$, the module $\mathbb{Z}$ is flat but $\mathbb{Z}/n\mathbb{Z}$ for $n \geq 2$ is not: tensoring $0 \to \mathbb{Z} \xrightarrow{\cdot n} \mathbb{Z}$ with $\mathbb{Z}/n\mathbb{Z}$ gives the zero map, which is not injective.

---

# Part III: Structure Theory over a Principal Ideal Domain

## 14. Torsion and Annihilators

Let $R$ be an integral domain. An element $m \in M$ is a **torsion element** if $rm=0$ for some $0 \neq r \in R$; the **torsion submodule** $M_{\mathrm{tor}}=\{m : rm=0 \text{ for some } r \neq 0\}$ is a submodule, since $rm=sn=0$ with $r,s \neq 0$ gives $rs(m+n)=0$. The module $M$ is **torsion-free** if $M_{\mathrm{tor}}=0$ and **torsion** if $M=M_{\mathrm{tor}}$; the quotient $M/M_{\mathrm{tor}}$ is torsion-free.

Over a principal ideal domain, $\operatorname{Ann}(m)=(a)$ for some $a \in R$ and $Rm \cong R/(a)$. For a prime $p$, the **$p$-primary component** $M_p=\{m : p^n m=0 \text{ for some } n \geq 1\}$ is a submodule, and a finitely generated torsion module is the direct sum of its finitely many nonzero primary components, $M=\bigoplus_p M_p$.

## 15. The Structure Theorem for Finitely Generated Modules over a PID

**Structure theorem.** Let $R$ be a principal ideal domain and let $M$ be a finitely generated $R$-module. Then

$$
M \cong R^r \oplus R/(d_1) \oplus \cdots \oplus R/(d_k)
$$

for some $r \geq 0$ and nonzero non-units $d_1 \mid d_2 \mid \cdots \mid d_k$ in $R$. The **free rank** $r$ and the **invariant factors** $d_i$ (up to multiplication by units) are uniquely determined by $M$. Thus $M$ is the direct sum of a free module and a torsion module, and the torsion part is a finite direct sum of cyclic torsion modules.

Applying the Chinese remainder theorem to the prime-power factors of the $d_i$ gives the **elementary divisor form** $M \cong R^r \oplus \bigoplus_i R/(p_i^{e_i})$ with $p_i$ prime and $e_i \geq 1$; the prime powers are unique up to units and reordering. The invariant factors are recovered by grouping, for each prime, the exponents in nondecreasing order.

*Proof sketch.* Choose a surjection $R^n \to M$ with kernel $K$, so $M \cong R^n/K$; over a PID, $K$ is free, say of rank $m \leq n$. In suitable bases the inclusion $K \hookrightarrow R^n$ has **Smith normal form** $\operatorname{diag}(d_1,\dots,d_m,0,\dots,0)$ with $d_1 \mid \cdots \mid d_m$, so $K$ is generated by $d_1e_1,\dots,d_me_m$ and $M \cong R/(d_1)\oplus\cdots\oplus R/(d_m)\oplus R^{n-m}$. Uniqueness follows by tensoring with the fraction field (which gives $r$) and localizing at each prime (which gives the exponents). $\square$

**Corollaries.** Over a principal ideal domain: a finitely generated module is free if and only if it is torsion-free; every finitely generated torsion-free module is free; every submodule of a finitely generated free module is free; and every finitely generated module is Noetherian, in the sense that all its submodules are finitely generated. This is the module-level form of the ideal structure of a PID noted in *Rings* §19.

## 16. Applications

**(a) Finitely generated abelian groups.** For $R=\mathbb{Z}$, every finitely generated abelian group is $\mathbb{Z}^r \oplus \mathbb{Z}/(d_1)\oplus\cdots\oplus\mathbb{Z}/(d_k)$ with $d_1 \mid \cdots \mid d_k$ and $d_i \geq 2$, and a finite abelian group is $\mathbb{Z}/(p_1^{e_1})\oplus\cdots\oplus\mathbb{Z}/(p_s^{e_s})$, the usual classification into cyclic groups of prime-power order.

**(b) Rational canonical form.** If $V$ is finite-dimensional over a field $K$ and $T:V \to V$ is linear, then $x \cdot v=T(v)$ makes $V$ a finitely generated torsion $K[x]$-module, so $V \cong K[x]/(f_1)\oplus\cdots\oplus K[x]/(f_k)$ with $f_1 \mid \cdots \mid f_k$. The $f_i$ are the invariant factors of $T$; taken monic, the largest is the minimal polynomial and their product is the characteristic polynomial, and the resulting block matrix of companion matrices is the **rational canonical form**, valid over any field.

**(c) Jordan normal form.** If the characteristic polynomial of $T$ splits into linear factors over $K$ (for instance, if $K$ is algebraically closed), the elementary divisor form is $V \cong \bigoplus_{\lambda}\bigoplus_j K[x]/\bigl((x-\lambda)^{e_{\lambda,j}}\bigr)$, each summand corresponding to a Jordan block; assembling the blocks gives the **Jordan normal form**.

---

# Part IV: Projective and Injective Modules

## 17. Projective Modules

A left $R$-module $P$ is **projective** if for every surjection $q:B \to C$ and every homomorphism $f:P \to C$ there is $g:P \to B$ with $qg=f$. Equivalently: every short exact sequence $0 \to A \to B \to P \to 0$ splits; or $P$ is a direct summand of a free module; or $\operatorname{Hom}_R(P,-)$ is exact. Free modules are projective, and projective modules are flat. So projectivity is freeness up to a complementary summand.

Over a principal ideal domain every projective module is free: a projective is a direct summand of a free module, hence a submodule of a free module, and submodules of free modules over a PID are free (§15). Over a local ring every finitely generated projective module is free. Over a general commutative ring projectives need not be free: in $R=\mathbb{Z}/6\mathbb{Z}$ the idempotent $e=3$ gives $R=Re \oplus R(1-e) \cong \mathbb{Z}/2\mathbb{Z}\oplus\mathbb{Z}/3\mathbb{Z}$, so $Re \cong \mathbb{Z}/2\mathbb{Z}$ is projective but not free, since a nonzero free $R$-module has at least $6$ elements while $Re$ has $2$. More generally, an idempotent $e \in R$ makes the left ideal $Re$ a projective module.

**Dual basis lemma.** Over a commutative ring, $P$ is finitely generated projective if and only if there are $p_1,\dots,p_n \in P$ and $f_1,\dots,f_n \in \operatorname{Hom}_R(P,R)$ with $x=\sum_i f_i(x)p_i$ for all $x \in P$.

## 18. Injective Modules

Dually, a left $R$-module $I$ is **injective** if for every injection $i:A \to B$ and every homomorphism $f:A \to I$ there is $g:B \to I$ with $gi=f$. Equivalently, every short exact sequence $0 \to I \to B \to C \to 0$ splits, or $\operatorname{Hom}_R(-,I)$ is exact. **Baer's criterion** reduces the test to left ideals: $I$ is injective if and only if every homomorphism $J \to I$ from a left ideal $J \subseteq R$ extends to a homomorphism $R \to I$.

A module over an integral domain is **divisible** if the equation $rm'=m$ is solvable for every $m$ and every $0 \neq r$. Over a principal ideal domain, $I$ is injective if and only if it is divisible. Hence over $\mathbb{Z}$ the injective modules are the divisible abelian groups: $\mathbb{Q}$ and $\mathbb{Q}/\mathbb{Z}$ are injective, while $\mathbb{Z}$ is not. Every module embeds into an injective module, its **injective envelope**, dual to every module being a quotient of a free module.

## 19. Modules over a Division Ring

Let $D$ be a division ring. Since every nonzero element is invertible, the analogy with linear algebra is exact.

**Theorem.** Every left $D$-module is free. *Proof sketch.* Extend a linearly independent set $\{m\}$ with $m \neq 0$ to a maximal linearly independent set $B$, using Zorn's lemma. If some element $x$ lay outside the span of $B$, then $B \cup \{x\}$ would be linearly independent, since a relation with nonzero coefficient on $x$ can be solved for $x$ by invertibility; this contradicts maximality. Hence $B$ is a basis. $\square$

Consequently every $D$-module has a basis, any two bases have the same cardinality (the **dimension**), every submodule is a direct summand, every short exact sequence splits, and every module is projective, injective, and flat. The step that fails over general rings is the solvability of $ax=b$ for $a \neq 0$: over $\mathbb{Z}$ the linearly independent set $\{2\}$ is maximal but does not span.

A field is a division ring (*Rings* §13), so $F$-modules are vector spaces and enjoy the theory above; the theorem applies to every division ring, commutative or not. Rings with zero divisors, such as the split-complex numbers, are not division rings, so these results do not apply to them. The quaternion algebra is treated in *Division Algebras*.

---

# Part V: Summary

## Summary

A module over $R$ is an abelian group with a scalar action of $R$, generalizing a vector space; over a commutative ring left and right modules coincide, matching *Rings* §14. Submodules, quotients, homomorphisms, and the isomorphism theorems behave as for groups and rings. Direct products and sums coincide for finite families, and direct summands are exactly the images of idempotent endomorphisms. Free modules have bases and are direct sums of copies of $R$; rank is well defined over commutative rings and division rings by IBN, and every module is a quotient of a free module. Exactness packages injectivity and surjectivity, the splitting lemma characterizes split sequences, $\operatorname{Hom}$ is left exact, and $\otimes$ is right exact. Tensor products are characterized by bilinearity, distribute over direct sums, implement base change, and define flatness. Over a PID, finitely generated modules decompose uniquely into a free part and cyclic torsion pieces, classifying finitely generated abelian groups and yielding the rational canonical and Jordan forms. Projectives are the direct summands of free modules, and for them surjections split; injectives are their dual, and over a PID they are exactly the divisible modules. Over a division ring every module is free, and module theory becomes linear algebra.

| Property | Over a field $F$ | Over a commutative ring $R$ |
|---|---|---|
| Every module is free | yes | no |
| Rank well defined | yes | yes |
| Submodule of a finitely generated module is finitely generated | yes | only if $R$ is Noetherian |
| Every short exact sequence splits | yes | no |
| Every module is projective and injective | yes | no |
| Every module is flat | yes | no |
| Finitely generated modules are classified | by dimension | only over a PID |

---

## Further Reading

- Michael Artin, *Algebra* (Prentice Hall, 1991).
- M. F. Atiyah and I. G. Macdonald, *Introduction to Commutative Algebra* (Addison-Wesley, 1969).
- Paul M. Cohn, *Basic Algebra: Groups, Rings and Fields* (Springer, 2003).
- David S. Dummit and Richard M. Foote, *Abstract Algebra* (Wiley, 3rd ed. 2004).
- Thomas W. Hungerford, *Algebra* (Springer, 1974).
- Nathan Jacobson, *Basic Algebra I* and *II* (Dover, 2nd ed. 2009).
- T. Y. Lam, *Lectures on Modules and Rings* (Springer, 1999).
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002).
- Joseph J. Rotman, *An Introduction to Homological Algebra* (Springer, 2nd ed. 2009).
- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994).
