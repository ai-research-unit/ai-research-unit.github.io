
# __Integral Representations__

## Introduction

Let $G$ be a finite group, let $R$ be an integral domain and let $L$ be an $R[G]$-module which is finitely generated and projective as an $R$-module — an $R[G]$-**lattice**. The study of the lattices is the integral representation theory of $G$: it sits between the ordinary theory of a finite group over a field, treated, and the modular theory of *Modular Representation Theory*, in which the base is a field of characteristic dividing the order; the passage from the field to the ring records the arithmetic of the group action, and the integral theory is strictly finer than the rational one, because a module over $\mathbb{Q}[G]$ may split into pieces while an integral lattice with the same rational form does not, and two lattices with the same rational form need not be isomorphic.

The article is the twenty-sixth and last of the corpus's category *Linear Spaces over Linear Algebras*, and it follows *Blocks and Defect Groups*; the integral lattice is what underlies a decomposition number there and what makes precise the reduction of an ordinary representation, and the article closes the category by treating the base ring as a genuine ring rather than a field. It develops the lattices and their rational forms, the failure of the rational decomposition over the ring with the two-*dimension example for the cyclic group of order two computed in full and verified, the Krull–Schmidt situation over a discrete valuation ring and over $\mathbb{Z}$, the finiteness of the number of lattices of a given rank by the theorem of **Jordan–Zassenhaus**, the reduction of a lattice to a positive characteristic and its relation to the decomposition matrix, and the classification results: the correspondence of **Latimer–MacDuffee** between the lattices of a cyclic group and the ideal classes of the cyclotomic ring, with the class group as the obstruction to the uniqueness.

Two boundaries are explicit. The structure theory of the underlying $\mathbb{Z}$-modules — the finite generation, the structure theorem for the finitely generated abelian groups, and the theory of the modules over a principal ideal domain — is not developed here: it is the subject of *Modules over a PID* and *Finitely Generated Abelian Groups*, which supply the classification of the underlying abelian groups used throughout, and the present article adds the action of $G$ to that structure. The analytic side — the $p$-adic completions of the rings of integers, the zeta functions of the lattices and the analytic class number formula that measures the obstruction — belongs to Part III, and its use is deferred.

Throughout, $G$ is a finite group, $R$ is an integral domain with fraction field $K$ (most often $R = \mathbb{Z}$, $K = \mathbb{Q}$), $\mathcal{O}$ is a discrete valuation ring with residue field $k$ of characteristic $p$ and maximal ideal $(\pi)$, an $R[G]$-**lattice** is a finitely generated projective $R[G]$-module, $K\otimes_RL$ is its **rational form**, $L^{(p)} = \mathbb{Z}_{(p)}\otimes_{\mathbb{Z}}L$ is a localisation, $\bar L = L\otimes_{\mathcal{O}}k$ is the reduction of an $\mathcal{O}$-lattice, $\zeta_n$ is a primitive $n$-th root of unity, $\mathbb{Z}[\zeta_n]$ is the cyclotomic ring, and $\mathrm{Cl}$ denotes a class group.

## Lattices and their Rational Forms

**Definition.** Let $R$ be an integral domain and $G$ a finite group. An $R[G]$-**lattice** is a left $R[G]$-module $L$ which is finitely generated and projective as an $R$-module; when $R$ is a principal ideal domain this is the same as a finitely generated torsion-free $R[G]$-module, by the structure theorem of *Modules over a PID*. A **sublattice** of a lattice is a submodule which is again a lattice, the **rank** of $L$ is the rank of the free $K$-module $K\otimes_RL$, and the functor $L\mapsto K\otimes_RL$ is the **rationalisation**, a functor from the $R[G]$-lattices to the finite-dimensional $K[G]$-modules.

**Proposition.** Let $R$ be a principal ideal domain and let $L$, $M$ be $R[G]$-lattices. Then:

1. the $R[G]$-lattices form an additive category with the direct sums, the kernels and the cokernels which are again lattices;
2. $\operatorname{Hom}_{R[G]}(L,M)$ is a finitely generated torsion-free $R$-module, which is free when $R$ is a principal ideal domain, and $\operatorname{End}_{R[G]}(L)$ is an $R$-order in the semisimple algebra $K\otimes_R\operatorname{End}_{R[G]}(L)$;
3. the rationalisation is a functor which is exact on the lattices and full, but not surjective on the isomorphism classes: two non-isomorphic lattices can have isomorphic rational forms;
4. the endomorphism ring $\operatorname{End}_{R[G]}(L)$ is an $R$-order in the semisimple $K$-algebra $\operatorname{End}_{K[G]}(K\otimes_RL)$, and the lattices of a fixed rational form are studied through the orders so obtained.

*Proof.* The first two statements are the standard properties of the finitely generated torsion-free modules over a principal ideal domain, for which the structure theorem of *Modules over a PID* gives $\operatorname{Hom}_{R[G]}(L,M)$ torsion-free and finitely generated, hence free; the functoriality and the exactness of the rationalisation follow from the flatness of the localisation $R\subseteq K$, and the failure of injectivity on the isomorphism classes is exhibited in the next section. The last statement is the standard description of a lattice as the data of the algebra of the endomorphisms together with a maximal $R$-order; the details are in the references. $\square$

**Definition.** Let $L$ be an $R[G]$-lattice and let $p$ be a prime. The **localisation** of $L$ at $p$ is the $\mathbb{Z}_{(p)}[G]$-lattice $L^{(p)} = \mathbb{Z}_{(p)}\otimes_{\mathbb{Z}}L$, where $\mathbb{Z}_{(p)}$ is the ring of the rational numbers with denominator prime to $p$; the **genus** of $L$ is the set of the isomorphism classes of the lattices $M$ with $M^{(p)}\cong L^{(p)}$ for every prime $p$ and $K\otimes M\cong K\otimes L$; the genus is the set of the lattices which are locally isomorphic to $L$, and the number of the classes in a genus is the **class number** of the lattice, the obstruction to the uniqueness of a lattice with a given set of localisations.

**Theorem (Jordan–Zassenhaus, standard).** Let $R$ be the ring of the integers of a number field, let $G$ be a finite group and let $n$ be a positive integer. Then there are only finitely many isomorphism classes of $R[G]$-lattices of rank $n$; more generally, for an $R$-order $\Lambda$ in a semisimple $K$-algebra there are finitely many isomorphism classes of $\Lambda$-lattices of each rank, and the class number of each genus is finite.

*Proof (outline).* One realises the lattices of rank $n$ as the $R$-lattices in the fixed $K[G]$-module $K^n$ which are stable under the order, and these are the maximal elements of a set of lattices that is bounded by a fixed lattice up to the finite index; the finiteness of the number of the sublattices of bounded index of a fixed lattice gives the result. The proof is the standard one and is recorded in the references. $\square$

**Remark (Krull–Schmidt).** Over a discrete valuation ring the $R[G]$-lattices have finite length and the Krull–Schmidt theorem holds, so that the decompositions into indecomposables are unique; over $\mathbb{Z}$ the theorem can fail, and the classical examples, due to Swan, exhibit a $\mathbb{Z}[G]$-lattice with two inequivalent decompositions into indecomposable lattices, the failure being measured by the class group of the order. This is the sense in which the integral theory over $\mathbb{Z}$ is genuinely more complicated than the modular theory of *Modular Representation Theory*, where the base is a field and the decomposition is always unique.

## Two Rank-Two Lattices for the Cyclic Group of Order Two

**Example.** Let $G = C_2 = \{1,t\}$ and $R = \mathbb{Z}$, so that $\mathbb{Z}[G] = \mathbb{Z}[t]/(t^2-1)$. Consider the two lattices

$$
L_1 = \mathbb{Z}[C_2], \qquad L_2 = \mathbb{Z}\oplus\mathbb{Z}^- ,
$$

where $\mathbb{Z}^-$ is the rank-one lattice on which $t$ acts by $-1$. Both have rank two and both have the same rational form: rationalising, $\mathbb{Q}\otimes_{\mathbb{Z}}\mathbb{Z}[C_2] = \mathbb{Q}[C_2]\cong\mathbb{Q}\oplus\mathbb{Q}^-$ with the idempotents $\frac12(1\pm t)$, and $\mathbb{Q}\otimes_{\mathbb{Z}}L_2 = \mathbb{Q}\oplus\mathbb{Q}^-$ as well, so the two lattices are indistinguishable to the rational representation theory of $G$. They are not isomorphic:

1. $L_2$ decomposes as the direct sum of the two rank-one lattices $\mathbb{Z}$ and $\mathbb{Z}^-$; the lattice $L_1$ is indecomposable, because a decomposition of $\mathbb{Z}[C_2]$ would give an idempotent of $\mathbb{Z}[C_2]$, and the integral idempotents are the elements $a+bt$ with $(a+bt)^2 = a+bt$, that is $2ab = b$ and $a^2+b^2 = a$, whose only solutions in the integers are $(a,b) = (0,0)$ and $(1,0)$, since $b(2a-1) = 0$ and $2a-1$ is odd forces $b = 0$, after which $a^2 = a$, giving the trivial idempotents $0$ and $1$;
2. the two lattices are distinguished by the invariants $L/(t-1)L$ and $L/(t+1)L$, which are the $\mathbb{Z}$-modules with the covariant structure: for $L_1 = \mathbb{Z}[C_2]$ one has $\mathbb{Z}[C_2]/(t-1)\cong\mathbb{Z}$ and $\mathbb{Z}[C_2]/(t+1)\cong\mathbb{Z}$; for $L_2$ one has $L_2/(t-1)L_2\cong\mathbb{Z}\oplus\mathbb{Z}/2$ and $L_2/(t+1)L_2\cong\mathbb{Z}/2\oplus\mathbb{Z}$; the invariant factors are the trivial ones $(1)$ in the first case and $(2)$ in the second, so the two lattices are not isomorphic, an isomorphism being necessarily compatible with the action and inducing isomorphisms of these quotients.

The computations were carried out with the exact Smith normal forms of the integer matrices $t-1$ and $t+1$ on each lattice: for $L_1$ in the basis $\{1,t\}$ the matrix of $t$ is $\begin{pmatrix}0&1\\1&0\end{pmatrix}$, whose $t-1$ and $t+1$ have the invariant factors $(1)$ after the removal of the free part; for $L_2$ the matrix of $t$ is $\operatorname{diag}(1,-1)$, whose $t-1$ and $t+1$ have the invariant factor $2$; and the integral idempotents of $\mathbb{Z}[C_2]$ were enumerated by solving $a^2+b^2 = a$, $2ab = b$ in the integers. The conclusion is the phenomenon that distinguishes the integral representation theory from the rational one: the rational module $\mathbb{Q}[C_2]$ is the direct sum of two one-dimensional modules, but the lattice $\mathbb{Z}[C_2]$ is indecomposable, since the splitting projectors involve the division by $\lvert G\rvert$.

**Remark.** The example is the lowest case of the general theory: the rational type of a lattice does not determine it, and the obstruction is the arithmetic of the order $\operatorname{End}_{\mathbb{Z}[G]}(L)$. For a lattice of rank $n$ with rational form $V$ the lattices of that rational form are the maximal $\mathbb{Z}$-orders inside the semisimple algebra $\operatorname{End}_{\mathbb{Q}[G]}(V)$, and the classification is by the genus together with the class group; the modular theory, by contrast, is the localisation at a prime and therefore sees only the local structure, which is the reason it is simpler.

## The Reduction to a Positive Characteristic

**Definition.** Let $\mathcal{O}$ be a discrete valuation ring of characteristic zero with residue field $k$ of characteristic $p$ and let $L$ be an $\mathcal{O}[G]$-lattice. The **reduction** of $L$ is the $k[G]$-module $\bar L = L\otimes_{\mathcal{O}}k$, of the same composition length data as the $k[G]$-modules of *Modular Representation Theory*; the character of the ordinary module $K\otimes_{\mathcal{O}}L$ and the Brauer character of $\bar L$ agree on the $p$-regular elements of $G$, and the **decomposition numbers** $d_{\chi j}$ of the modular theory are the multiplicities of the simple modules $S_j$ in the reductions of the lattices affording the ordinary irreducible characters.

**Proposition.** Let $L$ be an $\mathcal{O}[G]$-lattice and let $\chi$ be the ordinary character of its rational form. Then:

1. the reduction $\bar L$ is a $k[G]$-module of finite length and its composition factors are the simple modules $S_j$ of $k[G]$;
2. the Brauer character of $\bar L$ is the restriction of $\chi$ to the $p$-regular elements, so that $\chi(g) = \sum_jd_j\varphi_j(g)$ with $d_j$ the multiplicities of the composition factors;
3. the reduction depends on the choice of the lattice with the given rational form: two lattices with isomorphic rational forms can have non-isomorphic reductions, and the multiplicities of the composition factors can differ; what is independent of the choice is the Brauer character, which equals the restriction of the ordinary character to the $p$-regular elements;
4. the decomposition matrix of *Modular Representation Theory* is the matrix of the multiplicities of the reductions of a set of lattices affording the ordinary irreducible characters, and the Cartan matrix is $D^{\mathsf{T}}D$.

*Proof.* The reduction is the base change along $\mathcal{O}\to k$, and the trace of an element of finite order prime to $p$ on the reduction equals its trace on the rational form because the eigenvalues are the roots of unity of order prime to $p$ lifted to characteristic zero, giving the second statement; the third is the same phenomenon as in the example of the previous section, the localisation and the reduction being the two faces of the change of the base ring. The last statement is the definition of the decomposition matrix together with the theorem of the previous articles. $\square$

**Remark (the three levels).** The three theories — the ordinary over a field of characteristic zero, the modular over a field of characteristic $p$, and the integral over a discrete valuation ring or over $\mathbb{Z}$ — are related as the base changes $\mathbb{Z}\to\mathbb{Q}$ and $\mathcal{O}\to k$; the integral lattices are the common refinement, and the whole of the block theory of *Blocks and Defect Groups* is a theory of the lattices: the block idempotents lift from $k[G]$ to $\mathcal{O}[G]$, the defect groups are the vertices of the indecomposable modules of the block in the sense of Green, and the Brauer correspondence compares the lattices of $G$ with those of the normaliser of the defect group.

## Classification Results

**Theorem (Latimer–MacDuffee, standard).** Let $f\in\mathbb{Z}[x]$ be monic and irreducible over $\mathbb{Q}$ of degree $n$, let $\alpha$ be a root of $f$ and let $\mathbb{Z}[\alpha]$ be the order generated by $\alpha$. Then the similarity classes of the integral $n\times n$ matrices with the characteristic polynomial $f$ are in bijection with the ideal classes of the order $\mathbb{Z}[\alpha]$; equivalently, the isomorphism classes of the $\mathbb{Z}[x]$-lattices of rank $n$ on which $x$ acts with the characteristic polynomial $f$ are the ideal classes of $\mathbb{Z}[\alpha]$, the lattice attached to an ideal being the ideal regarded as a $\mathbb{Z}[x]$-module through the multiplication by $\alpha$.

*Proof (outline).* An integral matrix with the characteristic polynomial $f$ makes the underlying $\mathbb{Z}^n$ into a $\mathbb{Z}[\alpha]$-module which is torsion-free of rank $n$, hence isomorphic to an ideal of the order; the similarity of the matrices is the isomorphism of the modules, and the converse attaches to an ideal its multiplication matrix. The theorem is that of Latimer and MacDuffee, and the proof is recorded in the references. $\square$

**Corollary (the cyclotomic case).** Let $n\geq1$ and let $f = \Phi_n$ be the $n$-th cyclotomic polynomial, so that $\mathbb{Z}[\alpha] = \mathbb{Z}[\zeta_n]$. Then the isomorphism classes of the $\mathbb{Z}[C_n]$-lattices of rank $\varphi(n)$ affording the cyclotomic rational representation are in bijection with the ideal classes of the cyclotomic ring $\mathbb{Z}[\zeta_n]$; there is exactly one such lattice, the ring $\mathbb{Z}[\zeta_n]$ itself with the action of $\zeta_n$, if and only if the class group of $\mathbb{Z}[\zeta_n]$ is trivial, and the number of the classes is the class number of the cyclotomic field.

**Example.** For $n = 2$ the cyclotomic polynomial is $\Phi_2 = x+1$, the cyclotomic ring is $\mathbb{Z}[\zeta_2] = \mathbb{Z}$ of class number one, and the single cyclotomic lattice of rank one is the lattice $\mathbb{Z}^-$ of the previous section, on which $t$ acts by $-1$. For $n = 3$ the ring $\mathbb{Z}[\zeta_3]$ has class number one as well, and the cyclotomic lattice of rank two is unique; the first case in which the correspondence is non-trivial is $n = 23$, where the class group of $\mathbb{Q}(\zeta_{23})$ has order three, so that there are three cyclotomic lattices of rank $\varphi(23) = 22$ up to isomorphism, and the integral representations distinguish them while the rational representation does not. The rank-two lattices with the regular rational form, which are not of the cyclotomic type for $n = 2$, are a separate question, and they were discussed in the previous section: there are exactly two of them, and the cyclotomic lattices are the ones of rank one.

**Theorem (the integral theory of the cyclic groups, standard).** Let $G$ be a finite group all of whose Sylow subgroups are cyclic. Then the indecomposable $\mathbb{Z}[G]$-lattices are controlled by the cyclotomic rings attached to the cyclic subgroups of $G$: the building blocks are the lattices induced from the lattices of the cyclic subgroups, the classification of the latter being the ideal class classification above, and the class group of the order $\mathbb{Z}[G]$ is a quotient of the direct sum of the class groups of the cyclotomic rings of the cyclic subgroups. In particular the projective $\mathbb{Z}[G]$-lattices are free exactly when these class groups contribute nothing.

*Proof (outline).* The local structure is determined by the modular theory of the previous article, the cyclic Sylow condition making the blocks uniserial, and the global classification is reduced to the theory of the maximal orders and the ideals of the cyclotomic rings; the precise statement is due to Swan and is recorded in the references. $\square$

**Definition.** The **Grothendieck group** $G_0(R[G])$ of the $R[G]$-lattices is the free abelian group on the isomorphism classes of the lattices modulo the relations $[L\oplus M] = [L]+[M]$; the rationalisation and the reduction induce maps

$$
G_0(\mathbb{Z}[G])\longrightarrow G_0(\mathbb{Q}[G]), \qquad G_0(\mathcal{O}[G])\longrightarrow G_0(k[G]),
$$

the first carrying a lattice to its rational form and the second to its reduction, and the second has the decomposition matrix as its matrix with respect to the bases of the ordinary and the modular modules; consequently the integral theory carries the information of both the ordinary and the modular theory, and the change of rings of *Change of Rings* is the algebraic operation behind these maps.

**Remark (the arithmetic of the lattices).** The integral representation theory is the meeting point of the representation theory of the finite groups with the arithmetic of the orders: the classification of the lattices of a given rational type is the classification of the maximal orders in a semisimple algebra, the obstruction to the uniqueness is the class group, the local classification is the modular theory, and the finiteness is the theorem of Jordan–Zassenhaus. The analytic invariants of the orders — the zeta functions of the lattices and their functional equations, the class number formula and the analytic class group — require the completions and the limits of Part III, and their use here is deferred; the algebraic statements of the present article are the ones that belong to the algebra of the group rings.

## Summary

Let $G$ be a finite group and $R$ an integral domain with fraction field $K$. An $R[G]$-**lattice** is a finitely generated projective $R[G]$-module; over a principal ideal domain it is the same as a finitely generated torsion-free $R[G]$-module, whose underlying $R$-module is classified by the structure theorem of *Modules over a PID* and *Finitely Generated Abelian Groups*, and the rationalisation $L\mapsto K\otimes_RL$ is an exact full functor which is far from injective on the isomorphism classes. The example of the cyclic group $C_2$ is computed and verified: the lattices $\mathbb{Z}[C_2]$ and $\mathbb{Z}\oplus\mathbb{Z}^-$ have the same rational form and are not isomorphic, because $\mathbb{Z}[C_2]$ is indecomposable — the only integral idempotents of $\mathbb{Z}[C_2]$ are $0$ and $1$ — while $\mathbb{Z}\oplus\mathbb{Z}^-$ splits; the two are distinguished by the invariant factors of $L/(t-1)L$ and $L/(t+1)L$, computed by the Smith normal form as $(1)$ and $(2)$ respectively. Over a discrete valuation ring the lattices have finite length and the **Krull–Schmidt** theorem holds, while over $\mathbb{Z}$ the unique decomposition can fail, the classical examples being due to Swan; the number of lattices of a fixed rank is finite by the theorem of **Jordan–Zassenhaus**, and the **genus** with its class number measures the local-to-global failure. The **reduction** $\bar L = L\otimes_{\mathcal{O}}k$ of an $\mathcal{O}$-lattice is the $k[G]$-module whose Brauer character is the restriction of the ordinary character of $L$ to the $p$-regular elements, and the **decomposition matrix** of *Modular Representation Theory* is the matrix of the multiplicities of these reductions, with $C = D^{\mathsf{T}}D$; the blocks and defect groups of *Blocks and Defect Groups* are the theory of these lattices over a valuation ring. The classification of the lattices of the cyclic groups is the correspondence of **Latimer–MacDuffee** with the ideal classes of the cyclotomic ring $\mathbb{Z}[\zeta_n]$, so that the class group of the cyclotomic field is the obstruction to the uniqueness of a lattice with a given rational form. The analytic invariants of the orders and the $p$-adic refinements belong to Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$, $K$, $G$ | integral domain, its fraction field, finite group |
| $R[G]$-lattice | finitely generated projective $R[G]$-module |
| $K\otimes_RL$ | rational form of a lattice |
| $L^{(p)} = \mathbb{Z}_{(p)}\otimes L$ | localisation at a prime |
| genus, class number | lattices locally isomorphic to $L$, number of classes |
| $L_1 = \mathbb{Z}[C_2]$, $L_2 = \mathbb{Z}\oplus\mathbb{Z}^-$, $\mathbb{Z}^-$ | the two rank-two lattices and the sign lattice |
| $L/(t-1)L$, $L/(t+1)L$ | invariants of a $\mathbb{Z}[C_2]$-lattice, Smith normal form |
| $\mathcal{O}$, $k$, $\bar L = L\otimes_{\mathcal{O}}k$ | valuation ring, residue field, reduction of a lattice |
| $d_{\chi j}$, $D$, $C = D^{\mathsf{T}}D$ | decomposition numbers, decomposition and Cartan matrices |
| $\mathbb{Z}[\zeta_n]$, ideal class | cyclotomic ring, Latimer–MacDuffee classification |
| $G_0(R[G])$ | Grothendieck group of the lattices |





## Further Reading

- Ralph H. Latimer and Cyrus C. MacDuffee, "A correspondence between classes of ideals and classes of matrices", *Annals of Mathematics* **34** (1933), 313–316, for the correspondence for the cyclic groups.
- Robert G. Swan, "Projective modules over group rings and maximal orders", *Annals of Mathematics* **76** (1962), 55–61, and "K-theory and G-theory", *Algebraic K-theory I* (Springer Lecture Notes in Mathematics 341, 1973), for the failure of the unique decomposition and the class groups of the integral group rings.
- Irving Reiner, *Maximal Orders* (Academic Press, 1975), for the theory of the orders, the lattices, the genus and the Jordan–Zassenhaus theorem.
- Charles W. Curtis and Irving Reiner, *Representation Theory of Finite Groups and Associative Algebras* (Interscience, 1962), and *Methods of Representation Theory II* (Wiley, 1987), for the integral representation theory, the Jordan–Zassenhaus theorem and the reduction modulo a prime.
- Wilhelm Plesken, *Group Rings of Finite Groups over the Integers* (Springer Lecture Notes in Mathematics 1026, 1983), for the classification of the integral representations of the finite groups.
- Serge Lang, *Algebraic Number Theory* (Springer, 1994), for the ideal classes, the class number and the arithmetic of the cyclotomic fields used in the classification.
- Carl Ludwig Siegel, "Über die analytische Theorie der quadratischen Formen", *Annals of Mathematics* **36** (1935), 527–606, for the analytic class number theory and the local-to-global methods.
