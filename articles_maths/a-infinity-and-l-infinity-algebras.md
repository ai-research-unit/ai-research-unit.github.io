
# __A-Infinity and L-Infinity Algebras__

## Introduction

An **$A_\infty$-algebra** is a graded module with a differential, a multiplication and a sequence of higher operations, subject to identities that make the multiplication associative up to an explicit homotopy, the homotopy itself coherent up to a further homotopy, and so on. An **$L_\infty$-algebra** is the same notion with the multiplication replaced by a bracket and the symmetry of the operations reversed: the operations are graded antisymmetric, and the identities make the Jacobi identity hold up to homotopy, coherently. The two notions are the homotopy-coherent weakenings of the associative and the Lie algebra, and they are the structures in which deformation theory is naturally expressed: the Maurer–Cartan elements of an $L_\infty$-algebra are its deformations, and the obstruction calculus of *Deformation Quantization* is their theory.

The article is the eleventh of the category. It follows *Differential Graded Algebras* and *Differential Graded Categories*, whose strict structures it weakens, and it precedeswhose defining condition is a condition on a differential graded category whose higher operations are generally nonzero. Its three structural results are the **Stasheff identities** for the operations and their reformulation as the statement that an $A_\infty$-algebra is a square-zero coderivation of the tensor coalgebra, the **homotopy transfer theorem** of Kadeishvili, which produces an $A_\infty$-structure on the homology of a differential graded algebra and thereby exhibits the homology as a minimal model, and the **Maurer–Cartan theory** of $L_\infty$-algebras, with the gauge equivalence of solutions and its role in deformation theory.

The article is algebraic. The bar and cobar constructions, the coalgebra language and the higher operations are those of *Differential Graded Algebras* and of the operadic theory above it in the menu; the deformation-theoretic applications are those of *Deformation Quantization*, and the topological and model-categorical refinements — the little disks operad, the $\infty$-categorical and stable-homotopy versions — belong to Part II and are deferred. No distance, no norm, no manifold and no topology is used.

Throughout, $k$ is a commutative ring with identity, later a field of characteristic $0$ where signs involve factorials; all graded modules are $\mathbb{Z}$-graded over $k$; $V[1]$ denotes the shifted module with $V[1]_n = V_{n+1}$; the **desuspension sign** convention is that an element $v\in V$ regarded in $V[1]$ has degree $\lvert v\rvert - 1$; and all operations are $k$-linear.

## $A_\infty$-Algebras

### The Stasheff identities

**Definition.** An **$A_\infty$-algebra** is a graded $k$-module $A$ together with $k$-linear maps

$$
m_n : A^{\otimes n}\to A, \qquad n\geq1, \qquad \deg m_n = 2-n,
$$

satisfying, for every $n\geq1$, the **Stasheff identity**

$$
\sum_{r+s+t=n}(-1)^{r+st}\,m_{r+1+t}\bigl(\mathrm{id}^{\otimes r}\otimes m_s\otimes\mathrm{id}^{\otimes t}\bigr) = 0 ,
$$

where the identity is applied to $A^{\otimes n}$ in the evident way, with the Koszul sign rule of *Differential Graded Algebras* accounting for the permutation of the homogeneous arguments; the sign displayed is the unadorned positional sign, and the grading-dependent signs of the general form are obtained by moving the arguments past the operation. An $A_\infty$-algebra is **minimal** if $m_1 = 0$ and **strict** if $m_n = 0$ for all $n\geq3$.

**Proposition (the low identities).** The Stasheff identities for $n = 1,2,3$ read respectively

$$
m_1m_1 = 0 ,
$$

$$
m_1m_2 = m_2(m_1\otimes\mathrm{id}) + m_2(\mathrm{id}\otimes m_1) ,
$$

$$
m_2(m_2\otimes\mathrm{id}) - m_2(\mathrm{id}\otimes m_2) = -m_1m_3 - m_3(m_1\otimes\mathrm{id}\otimes\mathrm{id}) - m_3(\mathrm{id}\otimes m_1\otimes\mathrm{id}) - m_3(\mathrm{id}\otimes\mathrm{id}\otimes m_1) .
$$

Thus $m_1$ is a differential, $m_2$ is a chain map for that differential, and the **associativity defect** $m_2(m_2\otimes\mathrm{id}) - m_2(\mathrm{id}\otimes m_2)$ is the image under $m_1$ of the higher operation $m_3$ together with the terms in which $m_3$ is applied to arguments one of which is an $m_1$-image. In particular:

1. the defect is a boundary, so multiplication is associative up to a homotopy given by $m_3$;
2. if $m_1 = 0$ then the defect vanishes identically and $m_2$ is strictly associative;
3. the operations $m_n$ for $n\geq3$ are the higher homotopies, and the identity for $n = 4$ says that $m_3$ is a derivation of $m_2$ up to a homotopy $m_4$.

*Proof.* The identity for $n=1$ has the single term $r=s-1=t=0$, giving $m_1m_1 = 0$; for $n=2$ the terms are $(r,s,t) = (0,2,0),(1,1,0),(0,1,1)$, which are $m_1m_2$, $-m_2(m_1\otimes\mathrm{id})$ and $-m_2(\mathrm{id}\otimes m_1)$, with the positional signs $(-1)^{r+st}$ evaluated as $(-1)^{0+0}=1$, $(-1)^{1+0}=-1$, $(-1)^{0+1}=-1$. The case $n=3$ similarly has the six terms of the display, the two with $s=2$ giving the associativity defect and the four with $s=1$ or $s=3$ giving the $m_1$ and $m_3$ terms. $\square$

**Remark.** A **differential graded algebra** is exactly an $A_\infty$-algebra with $m_n = 0$ for $n\geq3$; conversely, an $A_\infty$-algebra with $m_1 = 0$ and $m_n = 0$ for $n\geq3$ is a graded associative algebra. The interest of the notion lies in the intermediate cases, where the multiplication is associative only up to the coherent homotopies $m_3,m_4,\dots$, and in the guarantee — the homotopy transfer theorem below — that these cases arise unavoidably, since the homology of a differential graded algebra carries such a structure whether or not it is strict.

### The coderivation description

**Definition.** Let $\bar T(A[1]) = \bigoplus_{n\geq1}(A[1])^{\otimes n}$ be the **reduced tensor coalgebra** on the shift of $A$, with the deconcatenation coproduct of *Differential Graded Algebras*. A **coderivation** of $\bar T(A[1])$ of degree $1$ is a map $b$ satisfying $\Delta b = (b\otimes\mathrm{id} + \mathrm{id}\otimes b)\Delta$; it is determined by its components $b_n : (A[1])^{\otimes n}\to A[1]$, and the condition $b^2 = 0$ is a system of identities on the components.

**Theorem (standard).** An $A_\infty$-algebra structure on a graded $k$-module $A$ is equivalent to a square-zero coderivation $b$ of degree $1$ on the reduced tensor coalgebra $\bar T(A[1])$. Under the equivalence, the operations $m_n$ of degree $2-n$ on $A$ correspond to the components $b_n$ of degree $1$ on $A[1]$, the shift accounting for the degree shift $2-n \mapsto 1$, and the identity $b^2 = 0$ is the Stasheff identity.

*Proof (outline).* A coderivation is determined by its restriction to the generators, and the components $b_n$ are the obstructions to strictness; the correspondence $b_n = m_n$ after the shift makes $\deg b_n = \deg m_n - (\text{shift}) = 1$. The identity $b^2 = 0$ decomposes according to the number of inputs into the sum $\sum_{r+s+t=n}(-1)^{r+st}b_{r+1+t}(1^r\otimes b_s\otimes1^t) = 0$, which is the Stasheff identity. $\square$

The theorem is the reason the higher operations are unavoidable and the reason they are coherent: the single equation $b^2 = 0$ on a coalgebra contains all the Stasheff identities at once, and the coalgebra language is the natural home of the theory. It also gives the compact definition of a **morphism**: a morphism of $A_\infty$-algebras is a morphism of the underlying coalgebras commuting with the coderivations.

**Definition.** A **morphism of $A_\infty$-algebras** $f : A\to B$ is a family of maps $f_n : A^{\otimes n}\to B$ of degree $1-n$ for $n\geq1$ satisfying

$$
\sum_{r+s+t=n}(-1)^{r+st}f_{r+1+t}\bigl(\mathrm{id}^{\otimes r}\otimes m_s\otimes\mathrm{id}^{\otimes t}\bigr) = \sum_{i_1+\cdots+i_j=n} m_j\bigl(f_{i_1}\otimes\cdots\otimes f_{i_j}\bigr) ,
$$

equivalently, a morphism of the tensor coalgebras commuting with the coderivations. The morphism is a **quasi-isomorphism** if $f_1$ is a quasi-isomorphism of complexes. The composition is given by the sum over all partitions, and the identity morphism has $f_1 = \mathrm{id}$ and $f_n = 0$ for $n\geq2$.

### The homotopy transfer theorem

**Theorem (Kadeishvili, standard).** Let $A$ be a differential graded algebra and let $H = H^\bullet(A)$ be its homology, with the induced product. Suppose that there is a homotopy retraction of complexes

$$
(H,0)\ \xrightarrow{\ i\ }\ (A,d)\ \xrightarrow{\ p\ }\ (H,0), \qquad pi = \mathrm{id}_H, \qquad \mathrm{id}_A - ip = d h + h d ,
$$

that is, $i$ is a quasi-isomorphism of complexes whose image consists of $d$-cycles. Then $H$ carries an $A_\infty$-algebra structure with $m_1 = 0$, $m_2$ the product induced by the product of $A$, and

$$
m_n = \sum_{\text{plane trees with }n\text{ leaves}} \pm p\,b_h\,b_h\cdots b_h\,i^{\otimes n}
$$

where $b_h(\alpha_1,\dots,\alpha_r) = (-1)^{\lvert\alpha_1\rvert+\cdots+\lvert\alpha_{r-1}\rvert}h(\alpha_1\cdots\alpha_{r-1})\alpha_r$ is the "circle operation" built from the homotopy $h$ and the product of $A$; further, there is an $A_\infty$-quasi-isomorphism $H\to A$ extending $i$. The resulting minimal $A_\infty$-algebra is the **minimal model** of $A$.

*Proof (outline).* The formulas are the standard tree formulas of the transfer theorem. The operations $m_n$ are defined by summing over the trees with $n$ leaves obtained by iterated insertions of $h$; the Stasheff identities are verified by summing over the ways of splitting a tree, and the two sides of the identity correspond to the two orders in which an edge can be cut, so that the terms cancel in pairs except for the required ones. The $A_\infty$-morphism $H\to A$ is given by the same tree sum with $i$ at the leaves. $\square$

**Corollary.** Every differential graded algebra is quasi-isomorphic, as an $A_\infty$-algebra, to its minimal model $H^\bullet(A)$, so the $A_\infty$-structure on the homology is a complete invariant of the $A_\infty$-homotopy type of the algebra up to quasi-isomorphism. In particular, two differential graded algebras that are quasi-isomorphic have quasi-isomorphic minimal models, and the minimal model is unique up to a non-canonical $A_\infty$-quasi-isomorphism.

**Example (a minimal $A_\infty$-structure with $m_3\neq0$).** Let $A$ be a differential graded algebra over a field whose homology is $H = H^0\oplus H^1\oplus H^2$ with basis $1$ in degree $0$, $u,v$ in degree $1$ and $w$ in degree $2$, and suppose that the induced product satisfies $m_2(u,v) = w$ with all other products of positive-degree elements vanishing. Then $m_2$ is associative, the defect in the identity for $n=3$ is zero, and the minimal model has $m_3 = 0$ unless the differential graded algebra has a nontrivial Massey product. To obtain $m_3\neq0$ one takes the differential graded algebra computing a nontrivial **Massey product** $\langle\alpha,\beta,\gamma\rangle$; then the transferred structure has $m_3(\alpha,\beta,\gamma) = \pm\langle\alpha,\beta,\gamma\rangle$, a nonzero element of the homology, so the minimal model is not a graded algebra and the original differential graded algebra is **not formal** in the sense of *Differential Graded Algebras*. The transfer theorem is therefore the mechanism by which failure of formality is detected by a higher operation.

## $A_\infty$-Modules and $A_\infty$-Categories

**Definition.** Let $A$ be an $A_\infty$-algebra. A (left) **$A_\infty$-module** over $A$ is a graded $k$-module $M$ together with maps

$$
m_n^M : A^{\otimes(n-1)}\otimes_k M \to M, \qquad n\geq1, \qquad \deg m_n^M = 2-n ,
$$

satisfying the **module identities**: for every $n\geq1$,

$$
\sum_{r+s+t=n}(-1)^{r+st}m^M_{r+1+t}\bigl(\mathrm{id}^{\otimes r}\otimes m_s\otimes\mathrm{id}^{\otimes t}\bigr) = \sum_{r+s=n}(-1)^{r}m^M_{r+1}\bigl(\mathrm{id}^{\otimes r}\otimes m^M_s\bigr),
$$

in which the operations $m_s$ of $A$ act on the $A$-factors and the operations $m^M_s$ act on the $A$-factors and the single module variable, the two sides being read on $A^{\otimes(n-1)}\otimes_kM$. A morphism of $A_\infty$-modules is a family $f_n : A^{\otimes(n-1)}\otimes_kM\to N$ of degree $1-n$ subject to the corresponding identity; the homotopy category of $A_\infty$-modules over $A$ has the $A_\infty$-modules as objects and the homotopy classes of morphisms as morphisms.

**Proposition.** Let $A$ be an $A_\infty$-algebra. Then an $A_\infty$-module over $A$ is the same thing as a square-zero coderivation of the coalgebra $\bar T(A[1])\otimes_kM[1]$ extending the coderivation $b$ that defines $A$ and vanishing on $M[1]$; consequently a strict module over a differential graded algebra $A$ is an $A_\infty$-module with $m_n^M = 0$ for $n\geq3$, and every $A_\infty$-module over $A$ is quasi-isomorphic to a strict module, namely to its transferred structure.

*Proof.* The first statement is the argument of the coderivation theorem applied to the module coalgebra: a coderivation extending $b$ is determined by its components on the $M$-part, and the components are exactly the operations $m^M_n$. The second statement is the homotopy transfer theorem applied to the module, with the homotopy retraction of $M$ in place of that of $A$; the construction is the same tree sum, with the leaves on the $M$-side not carrying the $i$-maps. $\square$

**Definition.** An **$A_\infty$-category** is a class of objects with graded Hom complexes and composition maps

$$
m_n : \operatorname{Hom}(x_{n-1},x_n)\otimes_k\cdots\otimes_k\operatorname{Hom}(x_0,x_1)\to\operatorname{Hom}(x_0,x_n), \qquad n\geq1,\ \deg m_n = 2-n,
$$

satisfying the Stasheff identities of the first section, read with the composable Hom complexes in place of the tensor powers of a single module. A differential graded category is exactly an $A_\infty$-category with $m_n = 0$ for $n\geq3$, so the notion of *Differential Graded Categories* is the strict case; the homotopy transfer theorem holds in the many-object setting and produces a minimal $A_\infty$-structure on the cohomology of the Hom complexes, which is the mechanism by which the higher operations arise. The $A_\infty$-categories are the algebraic objects whose homotopy theory — the localisation at quasi-equivalences and the resulting $\infty$-categorical structure — belongs to Part II, together with the stable-homotopy and model-categorical formulations.

## $L_\infty$-Algebras

### Definitions and low identities

**Definition.** An **$L_\infty$-algebra** is a graded $k$-module $V$ together with $k$-linear maps

$$
\ell_n : V^{\otimes n}\to V, \qquad n\geq1, \qquad \deg\ell_n = 2-n,
$$

that are **graded antisymmetric** in the sense that

$$
\ell_n(v_{\sigma(1)},\dots,v_{\sigma(n)}) = \chi(\sigma)\,\ell_n(v_1,\dots,v_n)
$$

for the Koszul sign $\chi(\sigma) = (-1)^{\lvert v_{\sigma}\rvert}$ of the permutation, and satisfy the **higher Jacobi identities**

$$
\sum_{i+j=n+1}\ \sum_{\sigma}(-1)^{\epsilon(\sigma)}\,\ell_j\bigl(\ell_i(v_{\sigma(1)},\dots,v_{\sigma(i)}),v_{\sigma(i+1)},\dots,v_{\sigma(n)}\bigr) = 0 ,
$$

where $\sigma$ runs over the permutations that move the first $i$ arguments past the remaining $n-i$ arguments, and $\epsilon(\sigma)$ is the Koszul sign of the resulting permutation of the homogeneous arguments, computed with their degrees. An $L_\infty$-algebra is **minimal** if $\ell_1 = 0$, and **strict** if $\ell_n = 0$ for $n\geq3$.

**Proposition (the low identities).** The identities for $n = 1,2,3$ read

$$
\ell_1\ell_1 = 0, \qquad \ell_1\ell_2 = \ell_2(\ell_1\otimes\mathrm{id}) + \ell_2(\mathrm{id}\otimes\ell_1),
$$

$$
\sum_{\mathrm{cyc}}\ell_2\bigl(\ell_2\otimes\mathrm{id}\bigr) = -\,\ell_1\ell_3 - \sum_{\mathrm{cyc}}\ell_3\bigl(\ell_1\otimes\mathrm{id}\otimes\mathrm{id}\bigr) ,
$$

where $\sum_{\mathrm{cyc}}$ denotes the sum over the three cyclic permutations of the three arguments. Thus $\ell_1$ is a differential for which the bracket $\ell_2$ is a chain map, and the **Jacobi defect**, the cyclic sum on the left, is a boundary: it equals the image of $\ell_3$ under $\ell_1$ together with the terms in which one argument of $\ell_3$ is replaced by its $\ell_1$-image. In particular:

1. if $V$ is concentrated in degree $0$ and $\ell_n = 0$ for $n\geq3$, then $V$ is a Lie algebra;
2. if $\ell_1 = 0$ the Jacobi identity holds strictly, and $\ell_3$ and the higher operations measure the deviation of the structure from being a strict graded Lie algebra;
3. a **differential graded Lie algebra** is exactly an $L_\infty$-algebra with $\ell_n = 0$ for $n\geq3$.

*Proof.* The identity for $n=1$ has $i=j=1$ and gives $\ell_1\ell_1=0$; for $n=2$ the terms with $i=1$ give $\ell_2(\ell_1\otimes\mathrm{id}) + \ell_2(\mathrm{id}\otimes\ell_1)$ and the term with $i=2$ gives $\ell_1\ell_2$; for $n=3$ the terms with $j=2,i=2$ give the three cyclic combinations, whose sum is the Jacobi defect, and the remaining terms involve $\ell_1$ and $\ell_3$. $\square$

**Theorem (the coderivation description).** An $L_\infty$-algebra structure on a graded $k$-module $V$ is equivalent to a square-zero coderivation of degree $1$ on the **symmetric coalgebra** $S(V[1]) = \bigoplus_{n\geq0}S^n(V[1])$, where the symmetric coalgebra carries the cocommutative deconcatenation coproduct. Under the equivalence the operation $\ell_n$ of degree $2-n$ corresponds to the component of the coderivation on $S^n(V[1])$, and the graded antisymmetry of $\ell_n$ is the commutativity of the symmetric coalgebra.

The theorem is the exact analogue of the $A_\infty$-statement with the tensor coalgebra replaced by the symmetric one; replacing the symmetric coalgebra by the tensor coalgebra is the passing from the Lie to the associative setting, and this is the formal content of the parallelism between the two halves of the article.

### The Maurer–Cartan equation and gauge equivalence

**Definition.** Let $V$ be an $L_\infty$-algebra. A **Maurer–Cartan element** is an element $x\in V_1$ satisfying

$$
\sum_{n\geq1}\frac{1}{n!}\,\ell_n(x,\dots,x) = 0 .
$$

Each term has degree $(2-n) + n\cdot1 = 2$, so the equation is a condition in $V_2$ and the sum is finite whenever $V$ is bounded above. In the case of a differential graded Lie algebra it reduces to

$$
\ell_1(x) + \tfrac12\ell_2(x,x) = 0 ,
$$

the classical Maurer–Cartan equation. Two Maurer–Cartan elements $x,x'$ are **gauge equivalent** if they are connected by the action of the group generated by the exponentials of the derivations $\sum_{n\geq1}\frac{1}{n!}\ell_{n+1}(x,\dots,x,-)$, whose $n=1$ term has degree $0$ and whose higher terms are the nilpotent corrections that the higher operations contribute; the set of gauge equivalence classes is the **Maurer–Cartan moduli space** $\mathcal{MC}(V)/\sim$.

**Proposition.** The Maurer–Cartan equation is invariant under the action of the gauge group; gauge equivalence is an equivalence relation; and the gauge group is the exponential of the $L_\infty$-algebra $V$ in the sense of the Baker–Campbell–Hausdorff series, which is finite and well defined over a field of characteristic $0$ for nilpotent inputs.

*Proof.* The invariance is the statement that the derivation $\partial_x = \sum\frac{1}{n!}\ell_{n+1}(x,\dots,x,-)$ satisfies $\partial_x(MC(x)) = 0$ when $x$ is Maurer–Cartan; this is the $n=1$ case of the higher Jacobi identity applied to $x,\dots,x$ and one further argument. The equivalence relation is the standard one of a group action, and the finiteness of the Baker–Campbell–Hausdorff series for nilpotent inputs is the classical statement. $\square$

**Theorem (deformation theory, standard).** Let $A$ be an algebra and let $V = \operatorname{Hom}_k(C_\bullet,A)$ be the differential graded Lie algebra of cochains on a resolution $C_\bullet$ of $A$, with the Gerstenhaber bracket of *Deformation Quantization*. Then the Maurer–Cartan elements of $V$ are exactly the deformed multiplications on $A$, the gauge equivalence of Maurer–Cartan elements is exactly the equivalence of deformations, and the moduli space $\mathcal{MC}(V)/\sim$ is the space of formal deformations of $A$ up to equivalence. In the same way the twisting morphisms of *Differential Graded Algebras*, satisfying $d\tau + \tau\star\tau = 0$, are the Maurer–Cartan elements of the convolution $L_\infty$-algebra $\operatorname{Hom}_k(C,A)$.

This is the precise sense in which deformation theory is the theory of Maurer–Cartan elements, and it is the reason the $L_\infty$-language is the natural one for the classification theorems of *Deformation Quantization* and for the deformation theory, where the second cohomology group classifies the infinitesimal deformations of a Lie algebra and the third contains the obstruction.

## Summary

An **$A_\infty$-algebra** is a graded $k$-module $A$ with operations $m_n : A^{\otimes n}\to A$ of degree $2-n$ satisfying the **Stasheff identities** $\sum_{r+s+t=n}(-1)^{r+st}m_{r+1+t}(\mathrm{id}^{\otimes r}\otimes m_s\otimes\mathrm{id}^{\otimes t}) = 0$. The low cases say that $m_1$ is a differential, $m_2$ is a chain map, and the associativity defect of $m_2$ is the $m_1$-boundary of $m_3$ together with further $m_3$-terms, so that multiplication is associative up to the homotopy $m_3$; if $m_1 = 0$ the defect vanishes and $m_2$ is strictly associative. A differential graded algebra is the case $m_n = 0$ for $n\geq3$. Equivalently, an $A_\infty$-algebra is a square-zero coderivation of degree $1$ on the reduced tensor coalgebra $\bar T(A[1])$; morphisms are given by families $f_n$ of degree $1-n$ satisfying the composition identity, and a quasi-isomorphism has $f_1$ a quasi-isomorphism. The **homotopy transfer theorem** of Kadeishvili attaches to any homotopy retraction $(H,0)\to(A,d)\to(H,0)$ an $A_\infty$-structure on $H$ with $m_1 = 0$, $m_2$ the induced product and the higher $m_n$ given by sums over trees with insertions of the homotopy, together with an $A_\infty$-quasi-isomorphism $H\to A$; the result is the **minimal model** of $A$, and it is non-strict exactly when the differential graded algebra is not formal, the obstruction being detected by Massey products.

An **$L_\infty$-algebra** is a graded $k$-module $V$ with graded antisymmetric operations $\ell_n$ of degree $2-n$ satisfying the higher Jacobi identities; $\ell_1$ is a differential, the Jacobi defect of $\ell_2$ is a boundary, a Lie algebra is the case concentrated in degree $0$ with $\ell_n = 0$ for $n\geq3$, and a differential graded Lie algebra is the case $\ell_n = 0$ for $n\geq3$ in general. Equivalently, an $L_\infty$-algebra is a square-zero coderivation of degree $1$ on the symmetric coalgebra $S(V[1])$. A **Maurer–Cartan element** is $x\in V_1$ with $\sum_n\frac{1}{n!}\ell_n(x,\dots,x) = 0$, which for a differential graded Lie algebra is $dx + \tfrac12[x,x] = 0$; the gauge group generated by the exponentials of $\sum\frac{1}{n!}\ell_{n+1}(x,\dots,x,-)$ acts on the Maurer–Cartan elements, and the quotient is the **Maurer–Cartan moduli space**. The Maurer–Cartan elements of the deformation complex of an algebra are its formal deformations and the gauge classes are their equivalence classes, which is the deformation theory of *Deformation Quantization* ; the twisting morphisms of *Differential Graded Algebras* are the Maurer–Cartan elements of a convolution $L_\infty$-algebra. The $\infty$-categorical and stable-homotopy refinements belong to Part II.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $k$, $A$, $V$ | ground ring or field, $A_\infty$-algebra, $L_\infty$-algebra |
| $m_n$ | $A_\infty$-operations of degree $2-n$ |
| $\ell_n$ | $L_\infty$-operations, graded antisymmetric, degree $2-n$ |
| $m_1, m_2, m_3$ | differential, multiplication, associativity homotopy |
| $\ell_1, \ell_2, \ell_3$ | differential, bracket, Jacobi homotopy |
| $V[1]$ | shift, $V[1]_n = V_{n+1}$ |
| $\bar T(A[1])$ | reduced tensor coalgebra; $A_\infty$-structure = coderivation $b$, $b^2=0$ |
| $S(V[1])$ | symmetric coalgebra; $L_\infty$-structure = coderivation $\ell$, $\ell^2=0$ |
| $f_n$ | components of an $A_\infty$-morphism, degree $1-n$ |
| $\sum_n\frac{1}{n!}\ell_n(x,\dots,x) = 0$ | Maurer–Cartan equation |
| $\mathcal{MC}(V)/\sim$ | Maurer–Cartan moduli space, gauge equivalence |
| $\langle\alpha,\beta,\gamma\rangle$ | Massey product |
| $b_h$ | circle operation with the homotopy $h$ in the transfer theorem |



## Further Reading

- James D. Stasheff, "Homotopy associativity of $H$-spaces I, II", *Transactions of the American Mathematical Society* **108** (1963), 275–312, for the original definition and the higher associativity identities.
- Tornike Kadeishvili, "On the theory of homology of fiber spaces", *Russian Mathematical Surveys* **35** (1980), 231–238, for the homotopy transfer theorem and the minimal model.
- Tom Lada and James Stasheff, "Introduction to sh Lie algebras for physicists", *International Journal of Theoretical Physics* **32** (1993), 1087–1103, for the $L_\infty$-identities and the Maurer–Cartan equation.
- Maxim Kontsevich and Yan Soibelman, "Homological mirror symmetry and torus fibrations", in *Symplectic Geometry and Mirror Symmetry* (World Scientific, 2001), 203–263, for the deformation theory controlled by $L_\infty$-algebras and the Maurer–Cartan formalism.
- Bernhard Keller, "Introduction to $A_\infty$-algebras and modules", *Homology, Homotopy and Applications* **3** (2001), 1–35, for the coderivation description, modules and functor categories.
- Kenji Lefèvre-Hasegawa, *Sur les $A_\infty$-catégories* (Thèse de doctorat, Université Paris 7, 2003), for the $A_\infty$-category formalism and the transfer theorem in the many-object setting.
- Martin Markl, "Transferring $A_\infty$ (and $L_\infty$) structures", *Journal of Noncommutative Geometry* **10** (2016), 1087–1136, for the explicit tree formulas of the transfer theorem.
