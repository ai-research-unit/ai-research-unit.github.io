
# __Simple and Semisimple Modules__

## Introduction

A module is simple when it has no proper nonzero submodule, and semisimple when it is a direct sum of simples. These are the two smallest and the two best-behaved classes of modules over an algebra, and the theory built on them — Schur's lemma, the Jacobson radical, the density theorem and the Wedderburn–Artin structure theorem — is the backbone of the representation theory developed in . The object of this article is the classification of modules by their simple constituents, and the classification of the algebras over which that classification is as simple as possible.

The conventions are those fixed in *Modules over an Algebra*: $R$ is a commutative ring with identity, $A$ is a unital associative $R$-algebra, modules are left modules, $S$ denotes a simple module, $D=\operatorname{End}_A(S)$ its endomorphism division ring, and $J(A)$ is the Jacobson radical. The base is the commutative ring; several results below require the base field and are flagged where they do. Schur's lemma and the density theorem are established in *Automorphisms of Modules over an Algebra* and are used here without reproof.

The plan is as follows. The simple modules are classified first: they are the quotients $A/\mathfrak{m}$ by maximal left ideals, and their endomorphism rings are division rings. The semisimple modules are then characterised by four equivalent conditions, and their endomorphism rings are computed as products of matrix rings over division rings. The algebras whose modules are all semisimple are identified by the Wedderburn–Artin theorem, and the obstruction to semisimplicity is isolated in the Jacobson radical. The last section fixes the composition series and the length, which measure how far a general module is from being semisimple.

## Simple Modules

### Definition and first properties

A nonzero left $A$-module $S$ is **simple** if its only submodules are $0$ and $S$. The zero module is excluded by the definition. A submodule of a simple module is therefore either zero or the whole module, and every nonzero element of $S$ generates $S$, since $Am$ is a nonzero submodule.

**Proposition.** A nonzero left $A$-module $S$ is simple if and only if $S \cong A/\mathfrak{m}$ for a maximal left ideal $\mathfrak{m} \subseteq A$.

*Proof.* If $S$ is simple, choose $0 \neq m \in S$ and consider the $A$-linear surjection $A \to S$, $a \mapsto am$, which exists because $Am=S$. Its kernel is a left ideal $\mathfrak{m}$ with $A/\mathfrak{m}\cong S$, and $\mathfrak{m}$ is maximal: the submodules of $A/\mathfrak{m}$ correspond to the left ideals between $\mathfrak{m}$ and $A$, and simplicity of $A/\mathfrak{m}$ says there are none. Conversely, if $\mathfrak{m}$ is maximal, the submodules of $A/\mathfrak{m}$ correspond to the left ideals containing $\mathfrak{m}$, of which there are only $\mathfrak{m}$ and $A$; hence $A/\mathfrak{m}$ is simple. $\square$

Thus the simple left $A$-modules are exactly the quotients of the regular module by its maximal left ideals. When $A$ is commutative, the maximal left ideals are the maximal (two-sided) ideals, so the simple $A$-modules are the quotients $A/\mathfrak{M}$ by maximal ideals; when $A$ is a field, the only simple module is the field itself. When $A$ is noncommutative, distinct maximal left ideals can give isomorphic simple modules, and the classification up to isomorphism requires the radicals of §The Jacobson Radical.

### Schur's lemma

The endomorphism ring of a simple module is as small as a ring can be.

**Theorem (Schur).** Let $S$ and $T$ be simple left $A$-modules. Then every $A$-linear map $f: S \to T$ is zero or an isomorphism, and

$$
\operatorname{End}_A(S)=D \text{ is a division ring}, \qquad \operatorname{Aut}_A(S)=D^{\times}.
$$

The lemma is proved in *Automorphisms of Modules over an Algebra*; it is recalled here because it governs the whole theory of semisimple modules. The division ring $D$ may be strictly larger than the base field, and its size is a genuine invariant of $S$: for $A=M_n(F)$ the simple module has $D=F$, while for a division algebra $D$ over $F$ the regular module is simple with endomorphism ring $D^{\mathrm{op}}$, so a noncommutative division algebra is itself the division ring attached to a simple module. Over an algebraically closed field every finite-dimensional simple module over a finite-dimensional algebra has $D=F$, which is why the representation theory of such algebras has no further arithmetic content.

### Examples

**(a)** Over a field $F$, the simple modules are the one-dimensional vector spaces; every vector space of dimension $\geq 2$ has proper subspaces.

**(b)** Over $A=M_n(F)$, there is exactly one simple module up to isomorphism, the defining module $S=F^n$ of column vectors. Every nonzero vector is a cyclic generator, and $\operatorname{End}_A(S)\cong F$ by the computation of *Automorphisms of Modules over an Algebra*.

**(c)** Over the biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$, again there is exactly one simple module up to isomorphism, the defining module $S=\mathbb{C}^2$, with $\operatorname{End}_{\mathbb{B}}(S)\cong\mathbb{C}$.

**(d)** Over a division ring $D$, the regular module ${}_D D$ is simple: a nonzero left ideal of $D$ contains an invertible element and is therefore all of $D$. So a division ring has exactly one simple module, its regular module, with endomorphism ring $D^{\mathrm{op}}$.

**(e)** Over the polynomial algebra $F[x]$, the simple modules are the quotients $F[x]/(p)$ for irreducible $p$, one for each maximal ideal $(p)$; the zero ideal is prime but not maximal, so the field of fractions $F(x)=F[x]_{(0)}$ is an $F[x]$-module that is not simple. Over an algebraically closed field the irreducible polynomials are the linear ones, so the finite-dimensional simple modules are the one-dimensional modules $F[x]/(x-\lambda)$, $\lambda \in F$.

**(f)** Over a commutative ring $R$, the simple modules are the quotients $R/\mathfrak{M}$ by maximal ideals; when $R$ is a field these are copies of the field.

## Semisimple Modules

### Definition and equivalent conditions

A left $A$-module $M$ is **semisimple**, or **completely reducible**, if it is a direct sum of simple submodules. The sum of all simple submodules of $M$ is the **socle** $\operatorname{soc}(M)$, and $M$ is semisimple precisely when $M=\operatorname{soc}(M)$. The equivalence of the following characterisations is standard and is proved in the sources cited; the first two are the ones used in practice.

**Theorem.** For a left $A$-module $M$ the following are equivalent.

1. $M$ is a sum of simple submodules.
2. $M$ is a direct sum of simple submodules.
3. Every submodule $N \subseteq M$ is a direct summand of $M$.
4. Every submodule $N \subseteq M$ has a complement, i.e. $M=N \oplus N'$ for some submodule $N'$.

*Proof sketch.* The implication (2)$\Rightarrow$(1) and (4)$\Leftrightarrow$(3) are immediate. For (1)$\Rightarrow$(3), let $N$ be a submodule and use Zorn's lemma on the set of submodules disjoint from $N$ to obtain a maximal such $L$; if $N+L \neq M$, a simple summand of $M$ not contained in $N+L$ can be adjoined to $L$, contradicting maximality, so $M=N\oplus L$. For (3)$\Rightarrow$(2), write $M=\operatorname{soc}(M)\oplus N'$ using (3), and suppose $N'\neq0$; fix $0\neq x\in N'$ and let $L$ be maximal among the submodules of $N'$ not containing $x$, which exists by Zorn's lemma. By (3), $L$ is a direct summand, say $N'=L\oplus K$, and writing $x=l+y$ with $l\in L$ one has $0\neq y\in K$. Every nonzero submodule $Q\subseteq K$ contains $y$, since otherwise $L\oplus Q$ would be a strictly larger submodule of $N'$ not containing $x$. Hence $Ay$ is contained in every nonzero submodule of $K$, and since by (3) the submodule $Ay$ has a complement in $K$, that complement must be $0$; so $K=Ay$, and $K$ is simple because every nonzero submodule of it contains $y$. Then $K\subseteq\operatorname{soc}(M)$, contradicting $N'\cap\operatorname{soc}(M)=0$. $\square$

A submodule and a quotient of a semisimple module are semisimple, and a direct sum of semisimple modules is semisimple. In particular, every direct summand of a semisimple module is semisimple, and $M$ is semisimple exactly when every element of $M$ lies in a direct sum of simple submodules.

### Isotypic decomposition

Two simple modules $S$ and $T$ are **isomorphic** or not, and by Schur's lemma there are no nonzero maps between non-isomorphic simples. Grouping the simple summands of a semisimple module by isomorphism class gives the **isotypic decomposition**.

**Theorem.** Let $M$ be a semisimple left $A$-module with simple constituents $S_1,\dots,S_r$ pairwise non-isomorphic. Then

$$
M \cong \bigoplus_{i=1}^{r} M_i, \qquad M_i \cong S_i^{\oplus n_i},
$$

where $n_i$ is a cardinal, and the **isotypic components** $M_i$ are the sums of all submodules isomorphic to $S_i$. The decomposition is unique: the submodules isomorphic to $S_i$ are exactly those of $M_i$, and $M_i$ is the image of the projection of $M$ onto the $i$-th block in any such decomposition.

The endomorphism ring of a semisimple module factors accordingly. For a single simple module $S$ with $D=\operatorname{End}_A(S)$ and a direct sum $S^{\oplus n}$,

$$
\operatorname{End}_A(S^{\oplus n}) \cong M_n(D),
$$

the matrices with entries in the division ring, by the same computation as for $M_n(F)$ in *Automorphisms of Modules over an Algebra*. Passing to a general semisimple module with isotypic decomposition as above,

$$
\operatorname{End}_A(M) \cong \prod_{i=1}^{r} M_{n_i}\bigl(\operatorname{End}_A(S_i)\bigr),
$$

a product of matrix rings over division rings. In particular the endomorphism ring of a semisimple module of finite length is semisimple, by the criterion of the next section, and its center is the product of the centers of the division rings $\operatorname{End}_A(S_i)$.

For the rest of the article $D_i$ denotes the division ring of the $i$-th factor of a Wedderburn decomposition, so that $D_i\cong\operatorname{End}_A(S_i)^{\mathrm{op}}$: for a division ring $D_0$ the defining module of $M_n(D_0)$ has endomorphism ring $D_0^{\mathrm{op}}$, the $A$-linear endomorphisms of $D_0^n$ being the right multiplications by scalars. The two division rings agree whenever $D_i\cong D_i^{\mathrm{op}}$, which is the case for every division ring occurring in this corpus.

## Semisimple Algebras and Wedderburn–Artin

### Semisimple algebras

The algebra $A$ is **semisimple** if the left regular module ${}_A A$ is semisimple. By the theorem above this is equivalent to every left ideal of $A$ being a direct summand of ${}_A A$, and by the proposition on direct summands of *Modules over an Algebra* this is equivalent to every left ideal being generated by an idempotent. A semisimple algebra is automatically left artinian, and also left noetherian: ${}_A A$ is generated by $1_A$, hence is a finite direct sum of simple modules, and a finite direct sum of simple modules is artinian and noetherian because each simple module is.

**Proposition.** If $A$ is semisimple, every left $A$-module is semisimple.

*Proof.* Every module is a quotient of a free module, hence of a direct sum of copies of ${}_A A$; quotients of semisimple modules are semisimple. $\square$

Thus over a semisimple algebra the module theory is completely determined by the set of simple modules and their endomorphism division rings.

### The structure theorem

**Theorem (Wedderburn–Artin).** Let $A$ be a unital ring. Then $A$ is semisimple if and only if

$$
A \cong \prod_{i=1}^{r} M_{n_i}(D_i)
$$

for division rings $D_1,\dots,D_r$ and positive integers $n_1,\dots,n_r$. The number $r$, the integers $n_i$ and the division rings $D_i$ are determined by $A$ up to permutation of the factors.

*Proof sketch.* Write ${}_A A=\bigoplus_i S_i^{\oplus n_i}$ with $S_i$ pairwise non-isomorphic simple. By the endomorphism computation of §Isotypic decomposition, $\operatorname{End}_A({}_A A)\cong\prod_i M_{n_i}(\operatorname{End}_A(S_i))$. But $\operatorname{End}_A({}_A A)\cong A^{\mathrm{op}}$ by the theorem on the regular module of *Modules over an Algebra*, so $A^{\mathrm{op}}\cong\prod_i M_{n_i}(\operatorname{End}_A(S_i))$ and, taking opposites, $A\cong\prod_i M_{n_i}(\operatorname{End}_A(S_i)^{\mathrm{op}})$. This is a product of matrix rings over the division rings $\operatorname{End}_A(S_i)^{\mathrm{op}}$, which is the stated form with $D_i=\operatorname{End}_A(S_i)^{\mathrm{op}}$. The uniqueness of the factors is the Jordan–Hölder theorem applied to the regular module together with the division-ring form of Schur's lemma. $\square$

Several consequences are immediate.

- The simple left $A$-modules are, up to isomorphism, exactly one $S_i$ for each factor $M_{n_i}(D_i)$: the defining module $D_i^{n_i}$ of column vectors, with $\operatorname{End}_A(S_i)\cong D_i^{\mathrm{op}}$.
- The center of $A$ is $\prod_i Z(D_i)$, so $A$ is central simple over its center exactly when $r=1$, and central simple over the base field $F$ exactly when $r=1$ and $Z(D_1)=F$.
- A ring is a **division ring** exactly when it is semisimple with $r=n_1=1$, so that $A=D_1$.
- A ring is a **matrix ring over a division ring** exactly when it is semisimple and simple in the sense of having no nontrivial two-sided ideals; this is the simple Artinian case.

### The density form

Combining the Wedderburn–Artin theorem with the density theorem of *Automorphisms of Modules over an Algebra* gives a description of any finite-dimensional algebra in terms of its simple modules. If $A$ is finite-dimensional over a field and $S_1,\dots,S_r$ are its simple modules with $D_i=\operatorname{End}_A(S_i)^{\mathrm{op}}$, then

$$
A/J(A) \cong \prod_{i=1}^{r} M_{n_i}(D_i), \qquad n_i=\dim_{D_i} S_i,
$$

and $A/J(A)$ acts faithfully and densely on the direct sum $S_1^{\oplus n_1}\oplus\cdots\oplus S_r^{\oplus n_r}$, the kernel of the action of $A$ itself being $J(A)=\bigcap_i\operatorname{Ann}_A(S_i)$. This is the structure theorem in the form used by representation theory: the simple modules, their endomorphism division rings and their multiplicities determine the algebra up to its radical.

## The Jacobson Radical

### Definition

The **Jacobson radical** $J(A)$ of $A$ is the intersection of all maximal left ideals of $A$. Equivalently it is the intersection of all maximal right ideals, and it is a two-sided ideal. The equivalence is proved with the following characterisations, all standard.

**Theorem.** For $a \in A$ the following are equivalent.

1. $a \in J(A)$, i.e. $a$ lies in every maximal left ideal.
2. $a$ annihilates every simple left $A$-module.
3. $1-xa$ is left-invertible for every $x \in A$.
4. $1-ax$ is right-invertible for every $x \in A$.
5. $1-xay$ is invertible for all $x,y \in A$.

*Proof sketch.* The equivalence of (1) and (2) follows from the description of simple modules as $A/\mathfrak{m}$: $a$ annihilates $A/\mathfrak{m}$ precisely when $a \in \mathfrak{m}$ for every maximal left ideal. For (2)$\Rightarrow$(3), if $1-xa$ had no left inverse then $A(1-xa)$ lies in a maximal left ideal, which contains $a$ and $xa$, whence $1 \in$ that ideal, a contradiction; the converse and the right-handed statements are symmetric. $\square$

The radical is thus the obstruction to semisimplicity, and it is a two-sided ideal precisely because of the symmetric form (5).

### The quotient by the radical

**Theorem (Jacobson).** $J(A/J(A))=0$ for every ring $A$. If in addition $A$ is left artinian, then $A/J(A)$ is semisimple, and $J(A)$ is nilpotent and is the largest nilpotent left ideal.

*Proof sketch.* The maximal left ideals of $A/J(A)$ are the images of the maximal left ideals of $A$, so their intersection is zero, giving $J(A/J(A))=0$; this alone does not make $A/J(A)$ semisimple, as $A=F[x]$ shows. When $A$ is left artinian its radical is nilpotent, by the standard induction on the length of the regular module. For semisimplicity, take a nonzero left ideal of the artinian ring $A/J(A)$; it contains a minimal left ideal $I$. Since a left ideal with $I^2=0$ lies in the Jacobson radical, and $J(A/J(A))=0$, one has $I^2\neq0$; choosing $a\in I$ with $Ia\neq0$ gives $Ia=I$, hence $e\in I$ with $ea=a$, and the left ideal $\{y\in I : ya=0\}$ is proper (it does not contain $e$) hence zero, so $e^2-e\in I$ and $(e^2-e)a=0$ force $e^2=e$ and $I=Ae$. An idempotent makes $Ae$ a direct summand of ${}_AA$, so $I$ is a simple direct summand, and a maximal family of such summands has sum all of $A/J(A)$ by the usual Zorn argument. $\square$

So every artinian algebra is an extension of a semisimple algebra by a nilpotent radical, and the module theory of $A$ is the module theory of $A/J(A)$ together with the deformations introduced by $J(A)$. The precise statement is that $A$ and $A/J(A)$ have the same simple modules: every simple $A$-module is annihilated by $J(A)$ by characterization (2), hence is a simple $A/J(A)$-module, and conversely by inflation.

**Nakayama's lemma.** For a two-sided ideal $I \subseteq J(A)$ and a finitely generated left $A$-module $M$, if $M=N+IM$ then $M=N$; in particular $IM=M$ forces $M=0$. This is proved in *Modules over an Algebra*. It is the standard tool for lifting generation from $M/IM$ and is used.

### Semisimplicity criteria

Combining the results above:

$$
A \text{ semisimple} \iff A \text{ left artinian and } J(A)=0 \iff \text{every left } A\text{-module is semisimple},
$$

and over a semisimple algebra every short exact sequence of modules splits, every module is projective and injective, and the global homological dimension is zero. The first equivalence combines Jacobson's theorem of §The quotient by the radical with the left artinianity of a semisimple algebra; the second is the proposition of §Semisimple algebras in one direction and the case of the regular module in the other.

## The Socle and Essential Submodules

The radical measures how far a module is from semisimple by removing the top; the socle measures the same thing by keeping the bottom.

### Definition and first properties

The **socle** of a left $A$-module $M$ is the sum of all its simple submodules,

$$
\operatorname{soc}(M)=\sum_{S\subseteq M \text{ simple}} S,
$$

with the convention that the sum over an empty family is $0$.

**Proposition.** $\operatorname{soc}(M)$ is the largest semisimple submodule of $M$; it is the direct sum of the simple submodules of $M$, and $M$ is semisimple if and only if $\operatorname{soc}(M)=M$.

*Proof.* A sum of simple modules is semisimple, since by the theorem of §Semisimple Modules it is a direct sum of a subfamily of them; a submodule of a semisimple module is semisimple, so every semisimple submodule of $M$ is contained in the sum of its simple submodules, which is $\operatorname{soc}(M)$; this proves maximality. Writing $\operatorname{soc}(M)$ as the sum of the simple submodules indexed by isomorphism class and applying the isotypic decomposition of §Semisimple Modules gives the direct-sum statement. The final equivalence is immediate from maximality, since a semisimple $M$ is spanned by its simple submodules. $\square$

### Essential submodules

A submodule $N\subseteq M$ is **essential** if $N\cap N'\neq0$ for every nonzero submodule $N'\subseteq M$.

**Theorem.** $\operatorname{soc}(M)$ is contained in every essential submodule, and if $M$ has finite length then $\operatorname{soc}(M)$ is itself essential, so that $\operatorname{soc}(M)$ is the intersection of the essential submodules of $M$.

*Proof.* If $N$ is essential and $S\subseteq M$ is simple, then $S\cap N$ is a nonzero submodule of $S$, hence equal to $S$, so $S\subseteq N$; summing over the simple submodules gives $\operatorname{soc}(M)\subseteq N$. Suppose now that $M$ has finite length and let $0\neq N'\subseteq M$. Then $N'$ has finite length and is nonzero, so it contains a minimal nonzero submodule, which is simple; hence $N'\cap\operatorname{soc}(M)\neq0$, and $\operatorname{soc}(M)$ is essential. Since $\operatorname{soc}(M)$ is then one of the essential submodules and is contained in all of them, the intersection is $\operatorname{soc}(M)$. $\square$

### The socle of the regular module

Applied to the left regular module, the socle

$$
\operatorname{soc}({}_AA)=\sum_{L\subseteq A \text{ minimal left ideal}} L
$$

is a two-sided ideal: it is a left ideal by construction, and for $a\in A$ the image $\operatorname{soc}({}_AA)\cdot a$ of a semisimple module is semisimple, hence contained in the socle, which gives right stability. For a finite-dimensional algebra the socle is the annihilator of the radical,

$$
\operatorname{soc}({}_AA)=\{a\in A : J(A)\,a=0\},
$$

because $J(A)$ annihilates every simple module, and conversely a module annihilated by $J(A)$ is a module over the semisimple algebra $A/J(A)$ and hence semisimple. The two ideals bound the regular module at its two ends: $\operatorname{soc}({}_AA)$ is its largest semisimple submodule, generated by the minimal left ideals, and $A/J(A)$ is its largest semisimple quotient, the radical being the intersection of the maximal left ideals.

### Examples

**(a) Semisimple rings.** If $A$ is semisimple then $\operatorname{soc}({}_AA)=A$, and more generally $\operatorname{soc}(M)=M$ for every $M$.

**(b) Domains.** If $A$ is a commutative domain that is not a field, then $A$ has no minimal left ideal, so $\operatorname{soc}({}_AA)=0$. Indeed, for a nonzero non-unit $a\in A$ the inclusion $Aa^2\subseteq Aa$ is strict: equality would give $a=a^2b$ for some $b$, hence $a(1-ab)=0$, and since $A$ is a domain and $a\neq0$ one has $ab=1$, making $a$ a unit and $Aa=A$. A commutative domain that is not a field contains a nonzero non-unit, and a nonzero left ideal all of whose nonzero elements are units is the whole ring; so every nonzero left ideal contains a strictly smaller nonzero left ideal and has no minimal member. The examples are $\mathbb{Z}$ and $F[x]$.

**(c) Cyclic groups.** For the abelian group $\mathbb{Z}/n\mathbb{Z}$ as a $\mathbb{Z}$-module with $n=p_1^{a_1}\cdots p_r^{a_r}$, the simple submodules are spanned by the elements of order $p_i$, one for each $i$, so $\operatorname{soc}(\mathbb{Z}/n\mathbb{Z})\cong\bigoplus_i\mathbb{Z}/p_i\mathbb{Z}$. For $n=p^a$ this is the unique simple submodule, spanned by the elements of order $p$.

**(d) The biquaternion algebra.** $\mathbb{B}\cong M_2(\mathbb{C})$ is semisimple, so $\operatorname{soc}({}_\mathbb{B}\mathbb{B})=\mathbb{B}$; for the defining module $S$ the socle is $S$ itself, and the socle of $S^{\oplus k}$ is $S^{\oplus k}$, in agreement with the classification.

## Composition Series and Length

A **composition series** of a left $A$-module $M$ is a finite strictly increasing chain of submodules

$$
0=M_0 \subset M_1 \subset \cdots \subset M_\ell=M
$$

with each successive quotient $M_i/M_{i-1}$ simple. The quotients are the **composition factors**, and $\ell$ is the **length** of the series. The Jordan–Hölder theorem, standard and proved by induction on length, states that any two composition series of $M$ have the same length and the same multiset of composition factors up to isomorphism. When a composition series exists, the common length is written $\ell_A(M)$ or $\operatorname{length}_A(M)$, and the multiplicity of a simple module $S$ among the factors is written $[M:S]$.

A module has finite length if and only if it is both noetherian and artinian, i.e. it satisfies the ascending and descending chain conditions on submodules. Over a finite-dimensional algebra every finitely generated module has finite length, since it is a finite-dimensional vector space. A semisimple module has finite length exactly when its isotypic decomposition $M\cong\bigoplus_i S_i^{\oplus n_i}$ is finite, and then $\ell_A(M)=\sum_i n_i$, the total number of simple summands; in particular, if $M\cong S^{\oplus n}$ is a multiple of a single simple module over a finite-dimensional algebra $A$ over a field $F$, then $\ell_A(M)=n=\dim_F M/\dim_F S$.

**Proposition.** If $0 \to L \to M \to N \to 0$ is a short exact sequence of modules of finite length, then $\ell_A(M)=\ell_A(L)+\ell_A(N)$, and for each simple $S$, $[M:S]=[L:S]+[N:S]$.

*Proof.* Concatenate a composition series of $L$ with the preimage of a composition series of $N$. $\square$

The length is therefore additive on short exact sequences, and it measures the deviation of $M$ from semisimplicity: $M$ is semisimple exactly when it is the direct sum of its simple submodules, equivalently when every short exact sequence $0\to L\to M\to N\to 0$ splits.

## Examples

**(a) Fields and division rings.** A field $F$ is semisimple: its regular module is one-dimensional, hence simple, and Wedderburn–Artin reads $F=M_1(F)$. A division ring $D$ is semisimple for the same reason, with $J(D)=0$ since the only maximal left ideal is $0$. Both are simple artinian rings.

**(b) Matrix algebras.** $M_n(F)$ is semisimple for every field $F$ and every $n \geq 1$, with $J(M_n(F))=0$. Its unique simple module is $S=F^n$, and the regular module is $S^{\oplus n}$; the Wedderburn–Artin decomposition is the single factor $M_n(F)$. The biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is the case $n=2$, $F=\mathbb{C}$.

**(c) Commutative semisimple rings.** For a commutative ring $R$, semisimplicity is equivalent to $R$ being a finite product of fields. Indeed a product of fields is semisimple, and conversely the Wedderburn–Artin factors of a commutative semisimple ring are commutative division rings, hence fields.

**(d) The polynomial algebra.** $F[x]$ is a principal ideal domain, so it is not artinian: the descending chain $(x) \supset (x^2) \supset (x^3) \supset \cdots$ does not stabilize. Its Jacobson radical is zero, but it is not semisimple, which shows that the artinian hypothesis in the criterion of §Semisimplicity criteria cannot be dropped. Its modules are classified by the structure theorem of *Modules* §15.

**(e) Local algebras.** The quotient $F[x]/(x^n)$ is a local ring with maximal ideal $(x)/(x^n)$ and radical $J=(x)/(x^n) \neq 0$; its unique simple module is $F$, on which $x$ acts as $0$. It is not semisimple for $n \geq 2$, and its regular module has length $n$ with repeated composition factor $F$.

**(f) Group algebras.** For a finite group $G$ and a field $F$, the group algebra $F[G]$ is semisimple if and only if $\operatorname{char} F$ does not divide $|G|$; this is Maschke's theorem, the module-theoretic form of complete reducibility. When $\operatorname{char} F=p$ divides $|G|$, the radical is nonzero and the theory becomes modular; the simple $F[G]$-modules are then the simple modules of $F[G]/J(F[G])$. The decomposition of $F[G]$ into matrix algebras in the semisimple case is the content .

**(g) Algebras with radical.** For a finite-dimensional algebra over a field the radical is nilpotent, so $A$ is semisimple exactly when $J(A)=0$. Over the $\mathbb{R}$-algebra $\mathbb{H}$ the radical vanishes because $\mathbb{H}$ is a division ring; over $\mathbb{B}$ it vanishes because $\mathbb{B}$ is a matrix algebra. Both are semisimple, and their module theory is as described.

## Summary

A nonzero module is simple when it has no proper nonzero submodule; the simple left $A$-modules are the quotients $A/\mathfrak{m}$ by maximal left ideals, up to isomorphism. Schur's lemma makes the endomorphism ring of a simple module a division ring $D$ and its automorphism group $D^{\times}$. A module is semisimple when it is a sum of simples, equivalently a direct sum of simples, equivalently when every submodule is a direct summand; the isotypic decomposition groups the simple summands by isomorphism class, and the endomorphism ring of a semisimple module is a product $\prod_i M_{n_i}(\operatorname{End}_A(S_i))$ of matrix rings over the endomorphism division rings of its simple constituents. An algebra is semisimple when its regular module is, equivalently when every module is; the Wedderburn–Artin theorem then writes $A\cong\prod_i M_{n_i}(D_i)$, the factors being determined up to permutation, and the simple modules are the defining modules $D_i^{n_i}$.

The obstruction to semisimplicity is the Jacobson radical $J(A)$, the intersection of the maximal left ideals, characterized as the set of elements annihilating every simple module and as the set of $a$ for which every $1-xay$ is invertible. It is a two-sided ideal and $J(A/J(A))=0$ always, but $A/J(A)$ is semisimple only in the artinian case, where $J(A)$ is also the largest nilpotent ideal. Hence $A$ is semisimple precisely when it is left artinian with zero radical, and over a finite-dimensional algebra this is simply $J(A)=0$. Composition series and their length make the deviation explicit and are additive on short exact sequences. The examples — fields and division rings, matrix algebras, products of fields, polynomial algebras, local algebras, group algebras and the biquaternion algebra — show the range of the theory; over a field of characteristic not dividing the order of a finite group, the group algebra is semisimple, which is the precise algebraic content of Maschke's theorem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | commutative ring with identity, the base ring |
| $A$ | unital associative $R$-algebra |
| $F$ | a field |
| $S$, $T$ | simple left $A$-modules |
| $A/\mathfrak{m}$ | simple module from a maximal left ideal $\mathfrak{m}$ |
| $D=\operatorname{End}_A(S)$ | division ring of a simple module |
| $D_i=\operatorname{End}_A(S_i)^{\mathrm{op}}$ | division ring of the $i$-th Wedderburn factor, $M_{n_i}(D_i)$ |
| $\operatorname{End}_A(M)$ | endomorphism ring of $M$ |
| $\operatorname{Aut}_A(M)$ | automorphism group of $M$ |
| $\operatorname{soc}(M)$ | socle, the sum of the simple submodules |
| essential submodule | $N\subseteq M$ with $N\cap N'\neq0$ for all nonzero $N'\subseteq M$ |
| $S^{\oplus n}$ | direct sum of $n$ copies of $S$ |
| $M_i \cong S_i^{\oplus n_i}$ | isotypic component of a semisimple module |
| $\prod_i M_{n_i}(D_i)$ | Wedderburn–Artin decomposition of a semisimple ring |
| $J(A)$ | Jacobson radical of $A$ |
| $\ell_A(M)$, $\operatorname{length}_A(M)$ | length of a module of finite length |
| $[M:S]$ | multiplicity of the simple module $S$ among the composition factors |
| $F[G]$ | group algebra of a finite group $G$ over $F$ |
| $\mathbb{H}$, $\mathbb{B}$ | quaternions and biquaternions |
| $\operatorname{char} F$ | characteristic of the field $F$ |



## Further Reading

- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, 2nd ed. 1992), for semisimple modules, the socle, and the Wedderburn–Artin theorem with the Jordan–Hölder theory.
- Nicolas Bourbaki, *Algebra VIII* (Springer, 2012), for the structure of semisimple algebras and the Jacobson radical.
- Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Wiley, 1962), for semisimple algebras in the representation-theoretic setting.
- I. N. Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the density theorem and its use in the structure theory.
- Nathan Jacobson, *Basic Algebra II* (Dover, 2nd ed. 2009), for the radical, semisimplicity and the density theorem.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the Jacobson radical, the Wedderburn–Artin theorem and Maschke's theorem.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the radical of a finite-dimensional algebra and its nilpotence.
- Jean-Pierre Serre, *Linear Representations of Finite Groups* (Springer, 1977), for complete reducibility and the character-theoretic consequences of semisimplicity.
