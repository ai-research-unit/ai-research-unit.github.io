
# __The Sheaf of Differential Operators__

## Introduction

The multiplication operators and the vector fields of *Operators on a Variety* generate, under composition, a larger sheaf of operators on the structure sheaf: the **differential operators**, whose order is the number of commutators with functions that it takes to kill them. The sheaf $\mathcal{D}_X$ so obtained is a sheaf of non-commutative, filtered $k$-algebras, it contains the functions as the operators of order zero and the vector fields as the operators of order at most one, and its associated graded sheaf is the symmetric algebra of the tangent sheaf, which is the sheaf of **symbols**. A module over $\mathcal{D}_X$ is an $\mathcal{O}_X$-module on which the derivations act compatibly with the multiplication — the algebraic form of a connection — and the symbol controls the module through its characteristic variety. This article fixes the sheaf, its filtration, its algebra structure, its symbol, and the $\mathcal{D}$-module structure, and it is the sixth and last article of the `- Operator Theory` group.

The differential operators here are **algebraic**: they are defined by iterated commutators with functions and by the resulting filtration, as Grothendieck defined them, and not by limits of difference quotients. A derivation is the algebraic derivation of Part I's *Derivations of a Ring* and the partial operators $\partial_i$ are the derivations of the polynomial ring, so nothing analytic is used. The differential operators of analysis — the Cauchy–Riemann operator of *Regularity and the Cauchy–Riemann Operator* and the differential operators of Part III — are different objects defined by the smooth structure, and this article neither constructs nor uses them. The connection and curvature of the written *Fibre Bundles, Connections and Curvature* are the geometric form of the same data, quoted here only in the comparison of a locally free $\mathcal{D}$-module with a bundle carrying a connection.

Throughout $X$ is a variety over a field $k$; the statements are local on $X$ and are proved on an affine chart, where $\mathcal{O}_X(X) = A$ is a finitely generated $k$-algebra and $\mathcal{T}_X$ is the tangent sheaf of *Operators on a Variety*. The **Weyl algebra** $A_n(k) = k[x_1,\ldots,x_n]\langle\partial_1,\ldots,\partial_n\rangle$ with $[\partial_i,x_j] = \delta_{ij}$ is the model case $X = \mathbb{A}^n_k$.

## Differential Operators on the Structure Sheaf

**Definition.** A $k$-linear endomorphism $D$ of $\mathcal{O}_X$ is a **differential operator of order at most $n$** if, for all functions $f_0,f_1,\ldots,f_n$,
$$
[f_n,[f_{n-1},[\cdots[f_0,D]\cdots]]] = 0 ,
$$
where $[f,D] = m_fD - Dm_f$ is the commutator with the multiplication $m_f$. Write $\mathcal{D}_X^n$ for the sheaf of these operators and
$$
\mathcal{D}_X = \bigcup_{n\geq0}\mathcal{D}_X^n
$$
for the **sheaf of differential operators**.

**Theorem (the filtration).** The $\mathcal{D}_X^n$ are sheaves of $k$-vector spaces, they are $\mathcal{O}_X$-submodules of $\mathcal{E}nd_k(\mathcal{O}_X)$, and
$$
\mathcal{D}_X^0\subseteq\mathcal{D}_X^1\subseteq\mathcal{D}_X^2\subseteq\cdots, \qquad
\mathcal{D}_X^m\circ\mathcal{D}_X^n\subseteq\mathcal{D}_X^{m+n} .
$$
Consequently $\mathcal{D}_X$ is a sheaf of filtered $k$-algebras under composition, and $\mathcal{D}_X^0$ is its subalgebra of operators linear over the structure sheaf.

*Proof.* The defining condition is linear in $D$, so $\mathcal{D}_X^n$ is a $k$-vector space. It is an $\mathcal{O}_X$-module because the functions commute among themselves, so that $[f,gD] = g[f,D]$, and multiplication by a function does not raise the order. The containment is the observation that a vanishing $(n+1)$-fold commutator also has vanishing $n$-fold commutator in the sense required. For the composition, use the identity $[fg,D] = f[g,D] + [f,D]g$ to write the $n$-fold commutator of a product as a sum of products of commutators whose orders add; a composition of an operator of order $m$ and one of order $n$ is then of order at most $m+n$.

**Theorem (order zero is the layer of *Operators on a Variety*).** The operators of order at most zero are exactly the multiplications: $\mathcal{D}_X^0 = \mathcal{E}nd_{\mathcal{O}_X}(\mathcal{O}_X) = \mathcal{O}_X$.

*Proof.* The condition $[f,D]=0$ for all $f$ is exactly $\mathcal{O}_X$-linearity, and $\mathcal{O}_X$-linear endomorphisms of $\mathcal{O}_X$ are the multiplications by the theorem of *Operators on a Variety*.

**Theorem (order one is the multiplications and the vector fields).** There is a short exact sequence of $\mathcal{O}_X$-modules
$$
0\longrightarrow\mathcal{O}_X\longrightarrow\mathcal{D}_X^1\xrightarrow{\ \sigma_1\ }\mathcal{T}_X\longrightarrow0 ,
$$
which splits, so that $\mathcal{D}_X^1\cong\mathcal{O}_X\oplus\mathcal{T}_X$. The map $\sigma_1$ sends $D$ to the derivation $f\mapsto[D,f]$.

*Proof.* For $D\in\mathcal{D}_X^1$ the assignment $\delta_D(f) = [D,f]$ takes values in $\mathcal{D}_X^0 = \mathcal{O}_X$ and is a derivation: it is $k$-linear, and
$$
\delta_D(fg) = [D,fg] = f[D,g] + [D,f]g = f\,\delta_D(g) + \delta_D(f)\,g ,
$$
by the identity above. Its kernel is $\mathcal{D}_X^0$. The derivation $\delta$ is itself an operator of order at most one, and $\sigma_1(\delta) = \delta$ since $[\delta,f] = \delta(f)$ by the Leibniz rule, so the map $f\mapsto f\cdot1$ together with $\delta\mapsto\delta$ splits the sequence.

**Theorem (generation and relations).** The algebra $\mathcal{D}_X$ is generated as a sheaf of $k$-algebras by $\mathcal{O}_X$ and $\mathcal{T}_X$, subject to the relations
$$
D\,f - f\,D = D(f) \quad (D\in\mathcal{T}_X,\ f\in\mathcal{O}_X), \qquad
D\,E - E\,D = [D,E] \quad (D,E\in\mathcal{T}_X),
$$
where $[D,E]$ is the Lie bracket of derivations of *Operators on a Variety*.

*Proof.* Every operator of order at most $n$ is a sum of products of at most $n$ derivations with functions: by induction on $n$, subtracting from $D$ a product of $\sigma_1(D)$ with a monomial in the derivations lowers the order, using the filtration theorem. The two relations are the definitions of the commutator with a function and of the bracket of two derivations.

**Example (the Weyl algebra).** On $X = \mathbb{A}^n_k$ the structure sheaf is $k[x_1,\ldots,x_n]$ and the vector fields are the free module on $\partial_1,\ldots,\partial_n$, so
$$
\mathcal{D}_{\mathbb{A}^n} = A_n(k) = k[x_1,\ldots,x_n]\langle\partial_1,\ldots,\partial_n\rangle, \qquad [\partial_i,x_j] = \delta_{ij},\quad [\partial_i,\partial_j] = 0, \quad [x_i,x_j]=0 .
$$
Each element has a unique normal form $\sum_{\alpha,\beta}c_{\alpha\beta}\,x^{\alpha}\partial^{\beta}$ with $c_{\alpha\beta}\in k$ and $\alpha,\beta\in\mathbb{N}^n$, finite; this is the Poincaré–Birkhoff–Witt form for the Weyl algebra, and it exhibits $\mathcal{D}_{\mathbb{A}^n}$ as an infinite-dimensional $k$-algebra filtered by $|\beta|\leq n$. On the affine line $A_1(k) = k[x]\langle\partial\rangle$ is generated by $x$ and $\partial$ with $[\partial,x]=1$.

## The Symbol and the Graded Algebra

**Definition.** The **associated graded sheaf** of $\mathcal{D}_X$ is
$$
\operatorname{gr}\mathcal{D}_X = \bigoplus_{n\geq0}\mathcal{D}_X^n\big/\mathcal{D}_X^{n-1},
$$
with the multiplication induced by the composition. For $D\in\mathcal{D}_X^n$ the class of $D$ in $\operatorname{gr}_n\mathcal{D}_X = \mathcal{D}_X^n/\mathcal{D}_X^{n-1}$ is its **symbol**, written $\sigma(D)$ or $\sigma_n(D)$ when the order is to be named.

**Theorem (the symbol algebra is the symmetric algebra of the tangent sheaf).** The symbol map induces an isomorphism of graded $\mathcal{O}_X$-algebras
$$
\operatorname{gr}\mathcal{D}_X\ \cong\ \operatorname{Sym}_{\mathcal{O}_X}\mathcal{T}_X ,
$$
so the symbol algebra is commutative, generated by the symbols of the derivations, and $\operatorname{gr}_n\mathcal{D}_X = \operatorname{Sym}^n\mathcal{T}_X$.

*Proof.* The relations of the generation theorem have symbols $D f - f D\mapsto$ class of $Df - fD$, which lies in $\mathcal{D}_X^0$, hence vanishes in degree one, so the symbols of $\mathcal{O}_X$ and $\mathcal{T}_X$ commute; the Lie bracket $[D,E]$ lies in $\mathcal{D}_X^1$ and therefore vanishes in degree two. Hence $\operatorname{gr}\mathcal{D}_X$ is generated by $\mathcal{O}_X$ in degree zero and $\mathcal{T}_X$ in degree one as a commutative graded algebra, and there are no further relations, which is the Poincaré–Birkhoff–Witt theorem for a filtered algebra whose associated graded is generated in degree at most one. The degree-$n$ piece is the $n$-th symmetric power.

**Definition.** For $D\in\mathcal{D}_X^n$ the symbol $\sigma_n(D)\in\operatorname{Sym}^n\mathcal{T}_X$ is the **principal symbol**; an operator of order exactly $n$ has nonzero principal symbol, and the principal symbol of a product is the product of the principal symbols. The **symbol of a product** is therefore multiplicative, and the top-degree part of a composition is the product of the top-degree parts.

**Theorem (the symbol Poisson bracket).** The commutator of operators induces a bracket
$$
\{\sigma_m(D),\sigma_n(E)\} = \sigma_{m+n-1}([D,E])
$$
on $\operatorname{gr}\mathcal{D}_X$, under which $\operatorname{gr}\mathcal{D}_X$ is a graded $\mathcal{O}_X$-algebra with a bracket of degree $-1$ satisfying the Leibniz rule in each variable. On the symbols of two derivations it is the Lie bracket, $\{\sigma_1(D_1),\sigma_1(D_2)\} = \sigma_1([D_1,D_2])$, and on a function and a derivation it is the action, $\{f,\sigma_1(D)\} = D(f)$.

*Proof.* The commutator of an operator of order $m$ and one of order $n$ has order at most $m+n-1$, because the top-degree symbols commute by the previous theorem; the induced bracket is well defined on the graded pieces, bilinear and alternating, and satisfies the Leibniz rule by the derivation identity of the filtration theorem. The two displayed evaluations are the definitions of the commutator with a function and of the bracket of derivations.

## Modules over the Sheaf of Differential Operators

**Definition.** A **left $\mathcal{D}_X$-module** is a sheaf $\mathcal{M}$ of left modules over the sheaf of algebras $\mathcal{D}_X$; equivalently, it is a quasi-coherent $\mathcal{O}_X$-module with a $k$-linear map
$$
\nabla : \mathcal{T}_X\times\mathcal{M}\longrightarrow\mathcal{M}, \qquad (D,m)\longmapsto\nabla_D(m),
$$
satisfying
$$
\nabla_{fD}(m) = f\,\nabla_D(m), \qquad \nabla_D(fm) = D(f)\,m + f\,\nabla_D(m), \qquad \nabla_{[D,E]}(m) = \nabla_D\nabla_E(m) - \nabla_E\nabla_D(m)
$$
for all functions $f$, derivations $D,E$ and sections $m$. A **right** $\mathcal{D}_X$-module is defined by reversing the side of the action, and passing from a left module $\mathcal{M}$ to the right module $\mathcal{H}om_{\mathcal{O}_X}(\mathcal{M},\mathcal{O}_X)$ uses the inverse-transpose rule for the action of an operator.

**Proposition (a locally free $\mathcal{D}$-module is a bundle with a connection).** If $\mathcal{M}$ is a locally free $\mathcal{O}_X$-module of finite rank carrying a $\mathcal{D}_X$-module structure, then $\nabla$ is a connection on $\mathcal{M}$ in the sense of the written *Fibre Bundles, Connections and Curvature*, and the integrability condition is exactly the third displayed identity. Conversely every integrable connection on a locally free sheaf endows it with the structure of a $\mathcal{D}_X$-module.

*Proof.* The first two identities are the definition of a connection: $\nabla$ is $\mathcal{O}_X$-linear in the derivation slot and satisfies the Leibniz rule in the section slot. The third is the vanishing of the curvature, so an integrable connection and a locally free $\mathcal{D}$-module are the same datum; on a smooth variety over a field of characteristic zero the identification is an equivalence of categories.

**Definition (the characteristic variety).** Let $\mathcal{M}$ be a coherent $\mathcal{D}_X$-module. The **symbol ideal** of $\mathcal{M}$ is the ideal sheaf of $\operatorname{gr}\mathcal{D}_X$ generated by the symbols of the operators that annihilate a finite generating set of $\mathcal{M}$, and the **characteristic variety** of $\mathcal{M}$ is the zero locus of that ideal, read inside the spectrum of the symmetric algebra $\operatorname{Sym}_{\mathcal{O}_X}\mathcal{T}_X$, which is the algebraic model of the cotangent bundle of $X$.

*Proof.* The symbol ideal is well defined because a change of generators changes the ideal by multiplication by a unit of $\operatorname{gr}\mathcal{D}_X$, so its zero locus depends only on $\mathcal{M}$; the characteristic variety is that zero locus, and it is a closed subvariety of the spectrum of the symmetric algebra.

**Theorem (the Bernstein inequality).** Let $X$ be smooth over a field of characteristic zero and let $\mathcal{M}\neq0$ be a finitely generated $\mathcal{D}_X$-module. Then the characteristic variety of $\mathcal{M}$ has dimension at least $\dim X$, and a module for which the dimension is exactly $\dim X$ is **holonomic**.

*Proof.* The proof is the estimate of the cohomological dimension of the de Rham complex of $\mathcal{M}$: the symbol ideal has enough structure that its zero locus cannot be too small once $\mathcal{M}$ is nonzero and finitely generated, and the bound is the algebraic form of the statement that a nonzero system of linear partial differential operators has a solution space of dimension at least the number of variables. The details are not reproduced here; the inequality is the central dimension theorem of the theory of $\mathcal{D}$-modules.

**Example (the structure sheaf as a $\mathcal{D}$-module).** The structure sheaf $\mathcal{O}_X$ is a left $\mathcal{D}_X$-module with $\nabla_D(f) = D(f)$: the first two identities are the definition of a derivation and the third is the identity $[D,E](f) = D(E(f))-E(D(f))$. Its annihilator is the left ideal generated by the vector fields, its symbol ideal is generated by $\mathcal{T}_X$ inside $\operatorname{Sym}\mathcal{T}_X$, and its characteristic variety is the zero section of the spectrum of the symmetric algebra, of dimension $\dim X$; the sheaf is the basic example of a holonomic module, and the de Rham complex of $\mathcal{O}_X$ is the algebraic de Rham complex of *Sheaves in Algebraic Geometry*.

**Example (the polynomial ring and the Weyl algebra).** On $X=\mathbb{A}^n$ a $\mathcal{D}$-module is a left module over the Weyl algebra $A_n(k)$. The polynomial ring $k[x_1,\ldots,x_n]$ is a module with $\partial_i$ acting by the partial derivation, the localisation $k[x_1,\ldots,x_n]_f$ is a module for every $f$, and not every such localisation is finitely generated over $A_n(k)$; the finite generation of a $\mathcal{D}$-module is a stronger condition than the finite generation of the $\mathcal{O}$-module.

## The Symbol in Characteristic $p$

**Remark (what changes in characteristic $p$).** Over a field of characteristic zero the algebra of differential operators is generated by the functions and the derivations, and the symbol algebra $\operatorname{gr}\mathcal{D}_X\cong\operatorname{Sym}_{\mathcal{O}_X}\mathcal{T}_X$ captures it completely. In characteristic $p$ the same pattern holds for the operators defined by the commutator condition, but the algebra is larger than the one generated by the vector fields: it contains the operators of order at most $p$ that are not products of at most $p$ derivations with functions, the **divided-power operators**, whose existence is the reason the divided powers $\partial^{[n]} = \partial^n/n!$ are not defined for $n\geq p$ in terms of the base field. The centre of $\mathcal{D}_X$ becomes large — it contains the $p$-th powers $f^p$ of the functions, and the operators built from the $p$-th powers of the derivations on the **Frobenius twist** of *The Frobenius Operator* lie in the centre as well — and $\mathcal{D}_X$ becomes a finite module over that centre in the smooth case. This is the arithmetic phenomenon that makes the theory of $\mathcal{D}$-modules in characteristic $p$ a theory of the Frobenius, and it is recorded here only in its shape: the precise statement needs the Frobenius twist and the Azumaya structure of $\mathcal{D}_X$ over it, which are developed from the operator of *The Frobenius Operator* and are not part of this article.

## Summary

The differential operators on a variety $X$ are the $k$-linear endomorphisms of the structure sheaf killed by enough commutators with functions: $\mathcal{D}_X = \bigcup_n\mathcal{D}_X^n$ with $\mathcal{D}_X^n$ cut out by the vanishing of the $(n+1)$-fold commutator. The sheaf $\mathcal{D}_X$ is a sheaf of filtered $k$-algebras, its degree-zero part is the layer $\mathcal{O}_X$ of the multiplication operators, its degree-one part is $\mathcal{O}_X\oplus\mathcal{T}_X$ with the symbol the derivation $f\mapsto[D,f]$, and it is generated by the functions and the vector fields with the relations $[D,f]=D(f)$ and $[D,E]=[D,E]$. The associated graded sheaf is the symmetric algebra of the tangent sheaf, $\operatorname{gr}\mathcal{D}_X\cong\operatorname{Sym}_{\mathcal{O}_X}\mathcal{T}_X$, the symbol of an operator is its class in the graded algebra, the symbol of a composition is the product of the symbols, and the commutator induces on the graded algebra a bracket of degree $-1$ that restricts to the Lie bracket of the derivations. A module over $\mathcal{D}_X$ is an $\mathcal{O}_X$-module with a compatible action of the derivations, that is, a connection when the module is locally free; the symbol ideal and the characteristic variety are the invariants it carries, with the Bernstein inequality as the dimension bound. In characteristic $p$ the centre of $\mathcal{D}_X$ becomes large and the Frobenius is the operator that governs it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{D}_X^n$ | differential operators of order at most $n$ |
| $\mathcal{D}_X=\bigcup_n\mathcal{D}_X^n$ | sheaf of differential operators; filtered $k$-algebra |
| $[f,D]=m_fD-Dm_f$ | commutator with a multiplication |
| $\mathcal{D}_X^0=\mathcal{O}_X$ | order zero: the multiplication operators |
| $\mathcal{D}_X^1=\mathcal{O}_X\oplus\mathcal{T}_X$ | order one: multiplications and vector fields |
| $\sigma_1(D)(f)=[D,f]$ | the symbol of an operator of order one |
| $\operatorname{gr}\mathcal{D}_X=\bigoplus_n\mathcal{D}_X^n/\mathcal{D}_X^{n-1}$ | associated graded sheaf |
| $\operatorname{gr}\mathcal{D}_X\cong\operatorname{Sym}_{\mathcal{O}_X}\mathcal{T}_X$ | the symbol algebra is the symmetric algebra of the tangent sheaf |
| $\{-,-\}$ | bracket of degree $-1$ on the symbol algebra |
| $A_n(k)=k[x_1,\ldots,x_n]\langle\partial_1,\ldots,\partial_n\rangle$ | Weyl algebra; $\mathcal{D}_{\mathbb{A}^n}$ |
| $\nabla_D$, $\nabla_D(fm)=D(f)m+f\nabla_D(m)$ | $\mathcal{D}$-module structure; connection when $\mathcal{M}$ is locally free |
| symbol ideal, characteristic variety | ideal of symbols of annihilators; its zero locus |
| divided powers $\partial^{[n]}$, centre of $\mathcal{D}_X$ in characteristic $p$ | the extra central operators; the Frobenius twist |

## Further Reading

- Alexandre Grothendieck, *Éléments de géométrie algébrique IV, §16* (Publications Mathématiques de l'IHÉS 32, 1967), for the definition of a differential operator by iterated commutators and the order filtration.
- Jean-Pierre Serre, *Faisceaux algébriques cohérents* (Annals of Mathematics 61, 1955), for the modules over the sheaf of differential operators on a variety.
- Alexander Beilinson and Joseph Bernstein, *A proof of Jantzen conjectures* (Advances in Soviet Mathematics 16, 1993), for the characteristic variety, the Bernstein inequality and the theory of holonomic modules.
- Masaki Kashiwara, *D-modules and Microlocal Calculus* (American Mathematical Society, 2003), for the microlocal theory of the characteristic variety and the symbol.
- Armand Borel, Pierre-Paul Grivel, Bernard Kaup, Albrecht Haefliger, Bernhard Malgrange and Frédéric Ehlers, *Algebraic D-Modules* (Academic Press, 1987), for the systematic algebraic treatment of $\mathcal{D}$-modules on a smooth variety.
