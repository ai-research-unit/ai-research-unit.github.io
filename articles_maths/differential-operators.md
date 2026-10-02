# __Differential Operators__

## Introduction

A differential equation is read through its operator. The expression on the left of the equation is a linear map from a space of functions to a space of functions, assembled from two ingredients only, the multiplications by the coefficients and the partial derivatives, and the equation $Lu=f$ asks for the inverse image of $f$ under that map. Two features of the map carry almost all of the theory. The first is its **order**, the number of derivatives the expression takes, together with its **symbol**, the polynomial in the frequencies that records the coefficients of the highest derivatives; the symbol is what decides whether the equation is elliptic, parabolic or hyperbolic. The second is its **formal adjoint**, the operator obtained by moving every derivative off the unknown and onto the test function, which is the integration by parts of the equation with the boundary terms discarded.

This article fixes those three objects for the differential operators of this category: the linear differential operator with variable coefficients on an open set of $\mathbb{R}^n$, its order and its symbol, the law by which symbols compose, and the transpose and the formal adjoint, together with their elementary algebra. It closes with the reading of the differential expression as an unbounded operator on $L^2$, where the domain first appears and with it the boundary condition, and it records that the domain and not the expression decides whether the operator is self-adjoint.

The treatment is flat: the domain is an open subset $\Omega$ of $\mathbb{R}^n$, and the derivatives are the partial derivatives of coordinates. The same objects on a manifold, where the symbol becomes a function on the cotangent bundle, belong to *Differential Operators on a Manifold* of *Smooth Manifolds and Differential Topology*, written in parallel. The principal symbol and the classification of a second-order equation into three types are those of *Partial Differential Equations*, and the symbol, the elliptic parametrix and the fundamental solution of an operator with constant coefficients are those of *Distributions and Fundamental Solutions*, which writes a differential operator $P$ where this article writes $L$. Nothing here imposes a boundary condition: the differential expression is the subject, and the operator it defines on a domain chosen by boundary conditions is met in *The Adjoint Boundary Condition* and *Self-Adjoint Sturm–Liouville Operators* below. The spectral theory of the self-adjoint instances is *Self-Adjoint Elliptic Operators and the Spectral Theorem*.

## Differential Operators

**Definition.** Let $\Omega \subseteq \mathbb{R}^n$ be open and let $m \in \mathbb{N}$. A **linear differential operator** of order at most $m$ on $\Omega$ is an expression

$$
L = \sum_{|\alpha|\le m} a_\alpha(x)\,\partial^\alpha ,
$$

where the sum runs over the multi-indices $\alpha = (\alpha_1,\dots,\alpha_n)$ with $|\alpha| = \sum_i\alpha_i \le m$, the **coefficients** $a_\alpha : \Omega \to \mathbb{C}$ are functions on $\Omega$, and $\partial^\alpha = \partial_1^{\alpha_1}\cdots\partial_n^{\alpha_n}$ is the partial derivative in the multi-index notation of *Distributions and Fundamental Solutions*. The operator acts on a function $u$ of class $C^m$ by

$$
(Lu)(x) = \sum_{|\alpha|\le m} a_\alpha(x)\,\partial^\alpha u(x) .
$$

The operator is of **order** $m$ if some coefficient $a_\alpha$ with $|\alpha| = m$ fails to vanish identically, and the **principal part** is then the sum of those terms, $\sum_{|\alpha|=m}a_\alpha\partial^\alpha$. Two expressions define the same operator exactly when their coefficients agree, so the operator is its coefficient family $(a_\alpha)_{|\alpha|\le m}$. The operator is **real** if every coefficient is real-valued, and **smooth** if every coefficient is of class $C^\infty$.

**Proposition (linearity and locality).** A differential operator is linear, $L(u+cv)=Lu+cLv$ for constants $c$, and it is **local**: if $u$ and $v$ agree on a neighbourhood of $x$ then $Lu$ and $Lv$ agree there. Its value at $x$ depends only on the derivatives of $u$ at $x$ up to order $m$.

*Proof.* Linearity is the linearity of the partial derivatives and of the multiplication by a function. Locality holds because $\partial^\alpha u(x)$ is computed from the values of $u$ on any neighbourhood of $x$; and the displayed formula expresses $Lu(x)$ through the finitely many numbers $\partial^\alpha u(x)$ with $|\alpha|\le m$.

**Example (the classical operators).** The following operators occur throughout the category.

| Operator | Expression | Order | Real |
|---|---|---|---|
| derivative in a direction | $\partial_i$, or $b\cdot\nabla = \sum_i b_i\partial_i$ | $1$ | yes |
| Laplacian | $\Delta = \sum_{i=1}^n\partial_i^2$ | $2$ | yes |
| Helmholtz-type | $-\Delta + c(x)$ | $2$ | yes if $c$ is real |
| Cauchy–Riemann | $\bar\partial = \tfrac12(\partial_x + i\,\partial_y)$ on $\mathbb{R}^2$ | $1$ | no |
| heat | $\partial_t - \Delta$ | $2$ | yes |
| wave | $\Box = \partial_t^2 - \Delta$ | $2$ | yes |
| Euler | $E = \sum_i x_i\partial_i$ | $1$ | yes |

The Cauchy–Riemann operator is complex, and it is the first-order operator whose square is the Laplacian in the plane, $\bar\partial\,\partial = \tfrac14\Delta$; the general construction of an operator from a frame of an algebra is *Regularity and the Cauchy–Riemann Operator*.

**Definition.** If $L_1$ and $L_2$ have orders $m_1$ and $m_2$, their **composition** $L_1L_2$ is the operator $u \mapsto L_1(L_2u)$, of order at most $m_1+m_2$, and their **sum** $L_1+L_2$ is the termwise sum, of order at most $\max(m_1,m_2)$. An operator $L$ is a **left factor** of $M$ if $M = LN$ for some operator $N$; the composition is associative and distributive over the sum, and the identity operator is the single term with $a_0=1$.

**Proposition (order of a composition).** If $M = L_1L_2$ and $a^{1}_{\alpha}$, $a^{2}_{\alpha}$ are the leading coefficients of $L_1$, $L_2$, then the leading coefficient of $M$ at order $m_1+m_2$ is the product $\sum_{|\alpha|=m_1,|\beta|=m_2,\alpha+\beta=\gamma}a^1_\alpha a^2_\beta$; in particular, if both leading parts are nowhere-vanishing in the sense of the next section, the order of $M$ is exactly $m_1+m_2$.

*Proof.* In a product of two monomials $a_\alpha\partial^\alpha\cdot b_\beta\partial^\beta$ the Leibniz rule produces terms $a_\alpha b_\beta\partial^{\alpha+\beta}$ together with lower-order terms in which at least one derivative falls on $b_\beta$; only the highest-order part $\alpha+\beta$ has order $m_1+m_2$ and its coefficient is the product of the two leading coefficients. The statement about exact order follows because the product of two functions that do not vanish anywhere does not vanish anywhere.

## The Symbol

**Definition.** The **symbol** of the operator $L = \sum_{|\alpha|\le m}a_\alpha\partial^\alpha$ is the polynomial in $\xi \in \mathbb{R}^n$,

$$
\sigma_L(x,\xi) = \sum_{|\alpha|\le m} a_\alpha(x)\,\xi^\alpha , \qquad \xi^\alpha = \xi_1^{\alpha_1}\cdots\xi_n^{\alpha_n} ,
$$

and its **principal symbol** is the homogeneous part of degree $m$ alone,

$$
\sigma_m(x,\xi) = \sum_{|\alpha| = m} a_\alpha(x)\,\xi^\alpha .
$$

The symbol is a function of $x$ and of the frequency vector $\xi$; it is the total symbol when lower-order terms are kept. The correspondence $L \leftrightarrow \sigma_L$ is one to one, because the coefficient $a_\alpha$ is recovered as the coefficient of $\xi^\alpha$, and the order of $L$ is the degree of $\sigma_L$ in $\xi$.

**Proposition (the symbol of a derivative is multiplication by $\xi$).** The symbol of the partial derivative $\partial_i$ is $\sigma_{\partial_i}(x,\xi) = \xi_i$, that of the identity is $1$, and that of the multiplication $M_a : u\mapsto a u$ is $\sigma_{M_a}(x,\xi) = a(x)$.

*Proof.* Each is read from the definition: the derivative brings the exponents of $\xi$ and the multiplication brings the coefficient.

**Theorem (the symbol of a composition).** Let $L_1$ and $L_2$ have symbols $\sigma_1$ and $\sigma_2$ and orders $m_1$ and $m_2$. Then the symbol of the composition is

$$
\sigma_{L_1L_2}(x,\xi) = \sum_{|\gamma|\le m_1} \frac{1}{\gamma!}\,\partial_\xi^\gamma\sigma_1(x,\xi)\,\partial_x^\gamma\sigma_2(x,\xi) ,
$$

the sum being finite because $\partial_\xi^\gamma\sigma_1$ vanishes for $|\gamma|>m_1$; the principal part of the right-hand side is the product $\sigma_{m_1}(x,\xi)\sigma_{m_2}(x,\xi)$ of the principal symbols.

*Proof.* It is enough to verify the identity for two monomials $a\,\partial^\alpha$ and $b\,\partial^\beta$ and to sum. By the Leibniz rule,

$$
\partial^\alpha(b\,\partial^\beta u) = \sum_{\gamma\le\alpha}\binom{\alpha}{\gamma}\partial^{\alpha-\gamma}b\,\partial^{\beta+\gamma}u ,
$$

so the symbol of the composition is $\sum_{\gamma\le\alpha}\binom{\alpha}{\gamma}a\,\partial^{\alpha-\gamma}b\,\xi^{\beta+\gamma}$. On the other side, $\partial_\xi^\gamma (\xi^\alpha) = \frac{\alpha!}{(\alpha-\gamma)!}\xi^{\alpha-\gamma}$ when $\gamma\le\alpha$ and $0$ otherwise, and $\partial_x^\gamma(\xi^\beta) = 0$ unless $\gamma=0$; hence for a general pair the right-hand side is $\sum_\gamma\frac{1}{\gamma!}\bigl(\partial_\xi^\gamma\sum_\alpha a_\alpha\xi^\alpha\bigr)\bigl(\partial_x^\gamma\sum_\beta b_\beta\xi^\beta\bigr) = \sum_{\alpha,\beta}\sum_{\gamma\le\alpha}\frac{1}{\gamma!}\frac{\alpha!}{(\alpha-\gamma)!}a_\alpha\partial^{\alpha-\gamma}b_\beta\,\xi^{\beta+\gamma}$, whose binomial factor $\frac{1}{\gamma!}\frac{\alpha!}{(\alpha-\gamma)!}$ is exactly the coefficient found above. The principal part is the term with $\gamma=0$.

**Example.** For $L_1 = \partial_x$ and $L_2 = M_a$ on $\mathbb{R}$, the composition is $\partial_x a = a\,\partial_x + a'$, whose symbol is $a(x)\xi + a'(x)$; the formula gives $\xi\cdot a + 1\cdot a'$, the same. For $L_1=L_2=\partial_x$ only the terms $\gamma=0$ and $\gamma=1$ contribute and the symbol is $\xi^2$, as it must be.

**Definition.** The operator $L$ is **elliptic** at $x$ if its principal symbol does not vanish away from the origin,

$$
\sigma_m(x,\xi)\neq0 \qquad \text{for every } \xi\in\mathbb{R}^n,\ \xi\neq0 ,
$$

and **elliptic on $\Omega$** if it is elliptic at every point of $\Omega$. The **characteristic set** of $L$ at $x$ is the zero set $\{\xi : \sigma_m(x,\xi)=0\}$ of the principal symbol, and a vector in it is a **characteristic vector**. For a real principal symbol the equation $\sigma_m(x,\xi)=0$ is the characteristic equation of *Partial Differential Equations*.

**Proposition (the two model cases).** The Laplacian $\Delta$ is elliptic, with $\sigma_2(x,\xi) = |\xi|^2$; the wave operator $\Box = \partial_t^2-\Delta$ on $\mathbb{R}^{1+n}$ is not elliptic, and its characteristic set at every point is the cone $\{\xi : \xi_t^2 = |\xi_x|^2\}$. The product of two elliptic operators is elliptic, by the product rule for the principal symbols.

*Proof.* For the Laplacian, $\sigma_2(x,\xi) = \sum_i\xi_i^2$, which vanishes only at $\xi=0$; for the wave operator, $\sigma_2(x,\xi) = \xi_t^2 - |\xi_x|^2$, whose zero set is the stated cone; the product statement is the multiplicativity of the principal symbol and the fact that a product of nonzero complex numbers is nonzero.

The symbol is defined on the frequencies at a point; the invariant reading, in which $\xi$ is a covector and the symbol lives on the cotangent bundle, is not available until the manifold is introduced, and it is *Differential Operators on a Manifold* that gives it. What the symbol decides in the flat setting — the classification of a second-order operator and the existence of a parametrix in the elliptic case — is used in *Partial Differential Equations* and *Distributions and Fundamental Solutions* respectively, and is not repeated here.

## The Transpose and the Formal Adjoint

**Definition.** Let $L = \sum_{|\alpha|\le m}a_\alpha\partial^\alpha$ have coefficients of class $C^{m}$. The **transpose** of $L$ is the operator

$$
L^{t} = \sum_{|\alpha|\le m}(-1)^{|\alpha|}\partial^\alpha\bigl(a_\alpha\,\cdot\,\bigr) ,
$$

and the **formal adjoint** of $L$ is the operator

$$
L^{\dagger} = \sum_{|\alpha|\le m}(-1)^{|\alpha|}\partial^\alpha\bigl(\bar a_\alpha\,\cdot\,\bigr) .
$$

Both are differential operators of order at most $m$, with coefficients as smooth as those of $L$. The transpose is the adjoint of $L$ for the bilinear pairing $\int_\Omega u\,v\,dx$ and the formal adjoint is the adjoint of $L$ for the Hermitian pairing $\langle u,v\rangle = \int_\Omega u\,\bar v\,dx$ of *Banach and Hilbert Spaces*, in the sense of the theorem below; the second is the transpose of the coefficient-conjugate operator, $L^{\dagger}v = \overline{L^{t}\bar v}$, and the two agree when the coefficients are real.

**Theorem (the defining identity).** Let $u$ and $v$ be of class $C_c^\infty(\Omega)$. Then

$$
\int_\Omega (Lu)\,\bar v\,dx = \int_\Omega u\,\overline{L^{\dagger}v}\,dx , \qquad \int_\Omega (Lu)\,v\,dx = \int_\Omega u\,(L^{t}v)\,dx .
$$

*Proof.* It suffices to treat a single term $a_\alpha\partial^\alpha$ and to sum. For compactly supported smooth functions the boundary terms of the integration by parts vanish, and iterating $|\alpha|$ times gives

$$
\int_\Omega a_\alpha\,\partial^\alpha u\,\bar v\,dx = (-1)^{|\alpha|}\int_\Omega u\,\partial^\alpha(\bar a_\alpha\,\bar v)\,dx = \int_\Omega u\,\overline{(-1)^{|\alpha|}\partial^\alpha(\bar a_\alpha v)}\,dx ,
$$

which is the first identity; the second is the same computation without the conjugation.

**Theorem (elementary algebra of the adjoint).** The formation of the formal adjoint is an involution, $(L^{\dagger})^{\dagger} = L$; it reverses a product, $(L_1L_2)^{\dagger} = L_2^{\dagger}L_1^{\dagger}$; it is additive, $(L_1+L_2)^{\dagger} = L_1^{\dagger}+L_2^{\dagger}$; and it commutes with the conjugation of the coefficients, $(\bar L)^{\dagger} = \overline{(L^{t})}$ where $\bar L$ has coefficients $\bar a_\alpha$. An operator with real coefficients satisfies $(L^{\dagger})v = \overline{L^{t}\bar v}$.

*Proof.* The involution and additivity are immediate from the coefficient formula. For the reversal, let $u,v \in C_c^\infty(\Omega)$; the defining identity applied twice gives

$$
\int_\Omega (L_1L_2u)\bar v = \int_\Omega (L_2u)\overline{L_1^{\dagger}v} = \int_\Omega u\,\overline{L_2^{\dagger}L_1^{\dagger}v} ,
$$

so $L_2^{\dagger}L_1^{\dagger}$ has the defining property of $(L_1L_2)^{\dagger}$, and the formal adjoint is unique by the fundamental lemma of the calculus of variations. The last assertion is the coefficient formula read with $\bar a_\alpha=a_\alpha$.

**Example (the self-adjoint expressions).** An operator equals its formal adjoint, $L = L^{\dagger}$, exactly when for every $\alpha$ one has $a_\alpha = (-1)^{|\alpha|}\sum$ of the derivatives of $a_\alpha$ contributed by the lower terms, the condition being vacuous to leading order. The model instances are the following.

| Operator | Formal adjoint | Self-adjoint |
|---|---|---|
| $\partial_i$ | $-\partial_i$ | no |
| $\Delta$ | $\Delta$ | yes |
| $-\Delta + c$ with $c$ real | $-\Delta + c$ | yes |
| $\bar\partial = \tfrac12(\partial_x + i\partial_y)$ | $-\tfrac12(\partial_x + i\partial_y)$ | no |
| $\mathrm{div}(A\nabla\cdot)$ with $A = A^{\mathsf T}$ real | itself | yes |
| $\partial_t - \Delta$ | $-\partial_t - \Delta$ | no |

The Laplacian is formally self-adjoint term by term, since each $\partial_i^2$ contributes $(-1)^2\partial_i^2$; the divergence form $\mathrm{div}(A\nabla u) = \sum_{i,j}\partial_i(a_{ij}\partial_ju)$ is formally self-adjoint exactly when the matrix $A$ is symmetric, the coefficients of the second derivatives being $a_{ij}$ and those of the first being $\sum_i\partial_ia_{ij}$. The heat operator is not formally self-adjoint, which is the operatorial form of the irreversibility recorded in *Partial Differential Equations*.

**Example (the Cauchy–Riemann operator).** On $\mathbb{R}^2$ the operator $\bar\partial = \tfrac12(\partial_x + i\partial_y)$ has formal adjoint $\bar\partial^{\dagger} = -\tfrac12(\partial_x + i\partial_y) = -\bar\partial$, since the coefficients are constant and each derivative changes sign. Its conjugate transpose is $-\partial$, where $\partial = \tfrac12(\partial_x - i\partial_y)$, and the pair $(\bar\partial,-\partial)$ is the flat instance of the adjoint pair of a first-order operator assembled from a frame, treated in *Regularity and the Cauchy–Riemann Operator*.

The formal adjoint is an operator on the same expression with the derivatives moved; it is not yet the adjoint of an operator on a Hilbert space, because no domain has been fixed. The step from the formal adjoint to an adjoint operator goes through the domain, which is the subject of the next section, and the identity between the two is the content of the Lagrange identity of *The Lagrange Identity and the Self-Adjoint System*.

## The Expression and the Operator

**Definition.** Let $L$ be a differential operator of order $m$ with coefficients of class $C^\infty$ on $\Omega$. The **maximal realisation** of $L$ on $L^2(\Omega)$ is the unbounded operator, again written $L$, with domain

$$
\mathcal{D}_{\max}(L) = \{u \in L^2(\Omega) : Lu \in L^2(\Omega)\} ,
$$

where $Lu$ is taken in the sense of distributions; the **minimal realisation** is the operator $L$ with domain the closure in the graph norm of the graph $\{(u,Lu) : u\in C_c^\infty(\Omega)\}$. Both are linear and densely defined, and the maximal realisation extends the minimal one. A **boundary condition** is a condition imposed on $u$ at $\partial\Omega$ that cuts a subspace $\mathcal{D}(L)\subseteq\mathcal{D}_{\max}(L)$ on which $L$ is closed.

**Proposition (unboundedness).** Every nonconstant-coefficient-free operator of positive order is unbounded on $L^2(\Omega)$: for $L = \partial_i$ and for every $M$ there is $u \in C_c^\infty(\Omega)$ with $\|\partial_iu\|_{L^2} > M\|u\|_{L^2}$.

*Proof.* Take a fixed bump $\varphi\in C_c^\infty$, nonnegative and not identically zero, and put $u_k(x) = \varphi(x)\,e^{ikx_i}$ for $k \in \mathbb{N}$. Then $\partial_iu_k = ik\varphi e^{ikx_i} + (\partial_i\varphi)e^{ikx_i}$, so $\|\partial_iu_k\|_{L^2} \ge |k|\|\varphi\|_{L^2} - \|\partial_i\varphi\|_{L^2}$ while $\|u_k\|_{L^2} = \|\varphi\|_{L^2}$; for $k$ large enough the quotient exceeds $M$.

**Theorem (the domain decides self-adjointness).** Let $L$ be a differential operator with smooth coefficients. The formal adjoint is the transpose of the maximal realisation in the sense that, for $v \in \mathcal{D}_{\max}(L)$ and $u \in C_c^\infty(\Omega)$,

$$
\langle Lu,v\rangle = \langle u, L^{\dagger}v\rangle ,
$$

and the minimal realisation of $L$ is contained in the adjoint of the maximal realisation of $L^{\dagger}$. The equality $\mathcal{D}(L)=\mathcal{D}(L^{\dagger})$ and $L = L^{\dagger}$ holds for some choice of boundary condition but not for the maximal realisation alone: the expression $-\Delta$ on a bounded domain is symmetric on $C_c^\infty(\Omega)$ and has distinct self-adjoint extensions differing in their boundary conditions.

*Proof.* The pairing identity is the defining identity of the formal adjoint, and it passes to $v\in\mathcal{D}_{\max}(L)$ by density of the test functions because both sides are continuous in the graph norm. The inclusion of the minimal realisation in the adjoint of the maximal one is the statement that a compactly supported test function is annihilated by every boundary term, so that the adjoint, defined by the pairing and free of boundary conditions on the test side, contains it. The failure of self-adjointness for the maximal realisation is the failure of the boundary term to vanish; the self-adjoint extensions and the boundary conditions that select them are constructed in *The Adjoint Boundary Condition*, and the case of the Sturm–Liouville expression is *Self-Adjoint Sturm–Liouville Operators*, both below.

The distinction between the expression and the operator is the one the rest of the category is built on. The three articles that follow it in this group take the expression and read from it an operator: *The Green Operator* inverts it under a boundary condition, *The Resolvent Operator* inverts it at a complex parameter, and *The Fundamental Solution Operator* inverts it on the whole space by convolution.

## Summary

A differential equation is read through its operator $L = \sum_{|\alpha|\le m}a_\alpha\partial^\alpha$ on an open set of $\mathbb{R}^n$, an expression that is linear and local and is determined by its coefficient family. Its order is the highest number of derivatives, its principal part the sum of the terms of highest order, and its symbol the polynomial $\sigma_L(x,\xi)=\sum_{|\alpha|\le m}a_\alpha(x)\xi^\alpha$ whose degree is the order and whose top part is the principal symbol. The symbol composes by the Leibniz rule, $\sigma_{L_1L_2}=\sum_\gamma\frac{1}{\gamma!}\partial^\gamma_\xi\sigma_1\,\partial^\gamma_x\sigma_2$, with the product of the principal symbols as its principal part, and the operator is elliptic when its principal symbol vanishes only at $\xi=0$; the Laplacian is elliptic with principal symbol $|\xi|^2$, and the wave operator is not, its characteristic set being the cone $\xi_t^2=|\xi|^2$.

The transpose $L^{t}=\sum(-1)^{|\alpha|}\partial^\alpha(a_\alpha\,\cdot\,)$ and the formal adjoint $L^{\dagger}=\sum(-1)^{|\alpha|}\partial^\alpha(\bar a_\alpha\,\cdot\,)$ are the operators defined by the integration by parts of $\int (Lu)v$ and $\int (Lu)\bar v$ against compactly supported test functions, and they are characterised by those identities. The formation of the formal adjoint is an involution, it reverses products and is additive, and an operator is formally self-adjoint when it equals it: the Laplacian and the real divergence form with symmetric matrix are, the first derivative and the heat operator are not. The formal adjoint is an expression and not yet an operator adjoint; the passage requires the choice of a domain, and it is the domain and not the expression that decides self-adjointness, the maximal realisation of $-\Delta$ on a bounded domain having distinct self-adjoint restrictions given by distinct boundary conditions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Omega \subseteq \mathbb{R}^n$ | Open domain of the operator |
| $\alpha$, $|\alpha|$, $\partial^\alpha$ | Multi-index, its length and the corresponding partial derivative |
| $a_\alpha$ | Coefficient of the derivative $\partial^\alpha$ |
| $L = \sum_{|\alpha|\le m}a_\alpha\partial^\alpha$ | Linear differential operator of order at most $m$ |
| $m$ | Order of $L$ |
| $\sigma_L(x,\xi)$ | Symbol of $L$, $\sum_{|\alpha|\le m}a_\alpha(x)\xi^\alpha$ |
| $\sigma_m(x,\xi)$ | Principal symbol, the terms with $|\alpha|=m$ alone |
| elliptic | $\sigma_m(x,\xi)\neq0$ for every $\xi\neq0$ |
| characteristic set | the zero set of the principal symbol at $x$ |
| $L^{t}$, $L^{\dagger}$ | Transpose and formal adjoint of $L$ |
| $\langle u,v\rangle = \int_\Omega u\bar v\,dx$ | Hermitian pairing, linear in the first argument |
| $\mathcal{D}_{\max}(L)$, $\mathcal{D}_{\min}(L)$ | Maximal and minimal domains of the realisation on $L^2$ |

## Further Reading

- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I* (Springer, 2nd ed. 1990), for the calculus of differential operators, their symbols and the composition law.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II* (Springer, 1983), for the formal adjoint, the transpose and the Lagrange identity in their general form.
- Michael E. Taylor, *Partial Differential Equations I* (Springer, 2nd ed. 2011), for the symbol, ellipticity and the construction of a parametrix.
- Gerald B. Folland, *Introduction to Partial Differential Equations* (Princeton University Press, 2nd ed. 1995), for the operator-theoretic reading of a differential expression and the role of the domain.
- Jean Dieudonné, *Éléments d'analyse* VIII (Gauthier-Villars, 1978), for the abstract theory of differential operators on an open set.
- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 2nd ed. 1976), for the realisation of a differential expression as an unbounded operator and the comparison of its domains.
