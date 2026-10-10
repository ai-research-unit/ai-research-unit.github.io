# __The Biquaternion Quadratic Map and Its Julia Sets__

## Introduction

In the complex plane the quadratic family is one map, $\zeta\mapsto\zeta^2+C$, and one filled Julia set for each parameter. In the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ the same formula denotes several maps at once, because the square of an element can be read with the general plain bilinear product, with one of the three other products the space carries, or with the left, the right and the matrix product, and the maps so obtained are not equivalent. This article fixes the reading, defines the family and its filled Julia set, and separates what survives the passage from the field to the algebra from what does not.

The algebra, its conjugations and its six distinguished subspaces are *Introduction to the General Plain Algebra of Biquaternions* and *Introduction to the Six Subspaces*; its zero divisors and its idempotents are *Biquaternion Zero Divisors* and *Biquaternion Idempotents and Projections*; the norm and the Euclidean norm are *Biquaternion Norm and Invertibility*; the matrix model is *Introduction to the 2×2 Matrix Representation of Biquaternions* and *Biquaternion 2×2 Matrix Element Representation $M_2(\mathbb{C})$*. These are used here and none is restated. The classical theory in $\mathbb{C}$ is *The Julia Sets of a Complex Polynomial*, *The Mandelbrot Set and the Quadratic Family* and *The Fatou Components and the Classification of the Dynamics*, and the comparison with it is made section by section.

This article owns the several readings of the square and the choice of the map, the definition of the biquaternion quadratic family, the filled Julia set and the Julia set, their complete invariance, the equivariance of the family under the conjugations, the critical set, and the reduction of the central-parameter family to a pair of complex quadratic families in the matrix model. It does not treat the escape radius (*The Escape Radius and the Green's Function for the Biquaternions*), the parameter locus (*The Biquaternion Mandelbrot Set and the Connectedness Locus*), the slices (*The Slices of the Biquaternion Julia Sets*), the zero divisors as a dynamical phenomenon (*The Zero Divisors and the Singular Julia Sets*), the Jacobian and the Fatou theory (*The Biquaternion Holomorphic Dynamics and the Jacobian*), or the dimension (*The Hausdorff Dimension of the Biquaternion Julia Sets*). No physical vocabulary is used.

**Standing convention.** Throughout, $\tilde Q=\sum_\mu Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$ is a biquaternion, $\tilde C$ is the parameter, and $\tilde Q^2$ is the square in the general plain bilinear product, so that the family is

$$
F_{\tilde C}(\tilde Q)=\tilde Q^2+\tilde C ,
$$

the sum being that of the underlying complex vector space. The parameter is fixed and the article writes $F$ for $F_{\tilde C}$ where no confusion results.

## The Several Readings of the Square

The formula $\tilde Q\mapsto\tilde Q^2$ is unambiguous once a product is chosen and the square is read as the diagonal of the corresponding bilinear map. Both clauses matter.

**The general plain bilinear square.** The general plain bilinear product $\tilde P\tilde Q$ is the only one of the four general products of the space that is the multiplication of an associative unital $\mathbb{C}$-algebra (*Introduction to the General Plain Algebra of Biquaternions*). Its diagonal $\tilde Q\tilde Q$ is the square this article uses. In the four complex coordinates it is a polynomial map with no conjugated coordinate, hence holomorphic; this is what makes the matrix model above all a model of *complex* dynamics.

**The diagonal of a left or a right multiplication.** For a fixed element $\tilde A$ the two maps

$$
\tilde R\mapsto \tilde A\tilde R+\tilde C \quad (\text{left}), \qquad \tilde R\mapsto \tilde R\tilde A+\tilde C \quad (\text{right})
$$

are affine: for $\tilde A$ a unit they are conjugate to a linear map, their orbits are exponentials, and their Julia set is empty. They return the quadratic family only on the diagonal $\tilde R=\tilde Q=\tilde A$. **The left and the right products give the square only on the diagonal; off the diagonal they give two affine families with no fractal content.** The matrix product agrees with the general plain bilinear square on the nose, because $\Phi$ is an algebra isomorphism (*Introduction to the 2×2 Matrix Representation of Biquaternions*).

**The conjugate squares.** Replacing one factor by a conjugate gives a map of a different kind. With the natural conjugate, $\tilde Q\tilde Q^{\natural}=N(\tilde Q)e_0$ is central and scalar, so the "natural quadratic family" is $\tilde Q\mapsto N(\tilde Q)e_0+\tilde C$, a scalar-valued map whose orbit is governed by the complex numbers $N(F^n(\tilde Q))$ alone. With the Hermitian conjugate, $\tilde Q\tilde Q^{*}$ is the Hermitian biquaternion whose scalar part is the square of the Euclidean norm, and the "Hermitian quadratic family" is a real-analytic, non-holomorphic map with values in the Hermitian subspace $\mathbb{M}_+$. These are different theories; neither is the theory of this article.

| reading of the square | the map | kind | the theory |
|---|---|---|---|
| general plain bilinear $\tilde Q\tilde Q$ | $\tilde Q\mapsto\tilde Q^2+\tilde C$ | holomorphic, quadratic | this article |
| natural $\tilde Q\tilde Q^{\natural}$ | $\tilde Q\mapsto N(\tilde Q)e_0+\tilde C$ | scalar-valued, uses the bar | *Biquaternion Square Roots of a General Element* |
| Hermitian $\tilde Q\tilde Q^{*}$ | $\tilde Q\mapsto\tilde Q\tilde Q^{*}+\tilde C$ | real-analytic, not holomorphic | *Biquaternion Norm and Invertibility* |
| left or right $\tilde A\tilde R$, $\tilde R\tilde A$ | affine in $\tilde R$ | no fractal | — |
| matrix $\Phi^{-1}\bigl(\Phi(\tilde Q)^2\bigr)$ | $\tilde Q\mapsto\tilde Q^2+\tilde C$ | the same map | *The Matrix Representation and the Biquaternion Dynamics* |

**Remark (why the choice is a choice).** The general plain bilinear product is the canonical multiplication of $\mathbb{B}$ once $\mathbb{B}$ is presented as a $\mathbb{C}$-algebra with the quaternion relations, so the first line of the table is the canonical reading. What is *not* canonical is the size. The algebra carries a complex-valued multiplicative norm $N$, its modulus $r=\sqrt{|N|}$, and the Euclidean norm $\|\cdot\|_E$, and no one of the three is singled out by the algebra. **The map is canonical; the norm used to define boundedness is a choice of metric, and the escape radius depends on it.** Boundedness itself does not, by the next section.

## The Quadratic Family

**Definition.** The **biquaternion quadratic family** is the family of self-maps of $\mathbb{B}$

$$
F_{\tilde C}:\mathbb{B}\to\mathbb{B}, \qquad F_{\tilde C}(\tilde Q)=\tilde Q^2+\tilde C ,
$$

one map for each parameter $\tilde C\in\mathbb{B}$. The **orbit** of a point $\tilde Q$ is the sequence $\tilde Q_0=\tilde Q$, $\tilde Q_{n+1}=F_{\tilde C}(\tilde Q_n)$.

**Proposition (the orbit is a polynomial in the initial point).** For every $n$ there is a polynomial $p_n$ of degree $2^n$ with

$$
p_0(\tilde Q)=\tilde Q, \qquad p_{n+1}(\tilde Q)=p_n(\tilde Q)^2+\tilde C, \qquad \tilde Q_n=p_n(\tilde Q).
$$

If $\tilde C$ is central, $\tilde C=Ce_0$ with $C\in\mathbb{C}$, every $p_n$ has coefficients in the centre and $\tilde Q_n$ is a polynomial in $\tilde Q$ alone.

**Proof.** Induction on $n$: $\tilde Q_{n+1}=p_n(\tilde Q)^2+\tilde C=p_{n+1}(\tilde Q)$ by the recursion. If $\tilde C$ is central the recursion stays in the polynomial ring over the centre, and the evaluation is taken in the commutative subalgebra $\mathbb{C}[\tilde Q]$ generated by one element.

The last clause is why the central parameter is the computable one: $\mathbb{C}[\tilde Q]$ has complex dimension at most two, and a polynomial in one element is a polynomial in its two coordinates there (*Introduction to the General Plain Algebra of Biquaternions*, §*The Subalgebra Generated by One Element*).

## The Filled Julia Set and the Julia Set

**Definition.** The **filled Julia set** of $F_{\tilde C}$ is the set of points whose orbit is bounded,

$$
\mathcal K_{\tilde C}=\{\tilde Q\in\mathbb{B} : (F_{\tilde C}^{n}(\tilde Q))_{n\ge0} \text{ is bounded}\},
$$

and the **Julia set** is its boundary, $J_{\tilde C}=\partial\mathcal K_{\tilde C}$.

**Remark (boundedness does not depend on the norm).** In the finite-dimensional real vector space $\mathbb{B}\cong\mathbb{R}^8$ all norms are equivalent, so a sequence is bounded for one norm exactly when it is bounded for every norm. **The filled Julia set is a set-theoretic object of the algebra and not of a chosen metric.** This is the sharpest contrast with the escape radius, which is a metric statement and does depend on the norm (*The Escape Radius and the Green's Function for the Biquaternions*).

**Proposition (complete invariance).** $F_{\tilde C}(\mathcal K_{\tilde C})\subset\mathcal K_{\tilde C}$ and $F_{\tilde C}^{-1}(\mathcal K_{\tilde C})=\mathcal K_{\tilde C}$; the same holds with $J_{\tilde C}$ in place of $\mathcal K_{\tilde C}$. Both sets are closed.

**Proof.** If $\tilde Q\in\mathcal K$ then the orbit of $F(\tilde Q)$ is the orbit of $\tilde Q$ with its first term deleted, hence bounded, so $F(\tilde Q)\in\mathcal K$ and $F(\mathcal K)\subset\mathcal K$. Conversely if $F(\tilde Q)\in\mathcal K$ then the orbit of $\tilde Q$ is the bounded orbit of $F(\tilde Q)$ preceded by the single point $\tilde Q$, hence bounded, so $\tilde Q\in\mathcal K$; thus $F^{-1}(\mathcal K)=\mathcal K$. For the Julia set: if $\tilde Q\in J=\partial\mathcal K$ and $V$ is a neighbourhood of $F(\tilde Q)$, then $F^{-1}(V)$ is a neighbourhood of $\tilde Q$, so it meets $\mathcal K$ — giving $V\cap\mathcal K\neq\emptyset$ because $F(\mathcal K)\subset\mathcal K$ — and it meets the complement of $\mathcal K$ — giving a point whose image lies in $V$ and, since $F^{-1}(\mathcal K)=\mathcal K$, outside $\mathcal K$. Hence $F(J)\subset J$. Conversely if $F(\tilde Q)\in J$ then $\tilde Q\in F^{-1}(\mathcal K)=\mathcal K$; if $\tilde Q$ were interior to $\mathcal K$ then $F(\tilde Q)$ would be interior, because a non-constant holomorphic map is open, contradicting $F(\tilde Q)\in\partial\mathcal K$; hence $\tilde Q\in J$ and $F^{-1}(J)\subset J$; the inclusion $J\subset F^{-1}(J)$ is the previous one. Closedness of $\mathcal K$ is that of a sublevel set of a continuous function, and of $J$ that of a boundary.

No properness of $F$ was used, and none holds: the equation $\tilde Q^2=\tilde W$ has the whole cone of square-zero elements as its fibre over $\tilde W=0$.

## The Conjugations and the Equivariance

**Theorem (equivariance).** Let $g$ be one of the three conjugations ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}$ — the non-identity elements of the group of involutions — and let $g$ act coefficientwise on the parameter. Then

$$
g\circ F_{\tilde C}=F_{g(\tilde C)}\circ g .
$$

Consequently $g(\mathcal K_{\tilde C})=\mathcal K_{g(\tilde C)}$ and $g(J_{\tilde C})=J_{g(\tilde C)}$.

**Proof.** Each of the three maps is an anti-automorphism of the ring, so $g(\tilde Q^2)=(g\tilde Q)^2$; and each is real-linear or conjugate-linear, hence preserves boundedness of a sequence. Applying $g$ to $F_{\tilde C}(\tilde Q)=\tilde Q^2+\tilde C$ gives $(g\tilde Q)^2+g\tilde C=F_{g(\tilde C)}(g\tilde Q)$.

**Remark (the reversal is excluded by a sign).** The fourth conjugation, the reversal $\flat$, satisfies $(\tilde P\tilde Q)^{\flat}=-\tilde Q^{\flat}\tilde P^{\flat}$, so $(\tilde Q^2)^{\flat}=-(\tilde Q^{\flat})^2$ and $\flat\circ F_{\tilde C}=F^{-}_{\flat(\tilde C)}\circ\flat$, where $F^{-}_{\tilde C'}(\tilde Q)=-\tilde Q^2+\tilde C'$ is the odd quadratic family. **The reversal carries the even family to the odd family and is not a symmetry of the even fractal** (*The Three Conjugations and the Symmetric Biquaternion Fractals*).

**Corollary (the symmetry group of the fractal).** Let $G_{\tilde C}=\{g\in\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\} : g(\tilde C)=\tilde C\}$. Then $\mathcal K_{\tilde C}$ and $J_{\tilde C}$ are invariant under every element of $G_{\tilde C}$, and $G_{\tilde C}$ is one of the five subgroups

1. the Klein four-group $G$, when $\tilde C=Ce_0$ with $C$ real;
2. $\{\mathrm{id},{}^{\natural}\}$, when $\tilde C$ is central with $C$ non-real;
3. $\{\mathrm{id},\bar{\cdot}\}$, when $\tilde C$ lies in the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ but is not central;
4. $\{\mathrm{id},{}^{*}\}$, when $\tilde C$ lies in the Hermitian sector $\mathbb{M}_+$ but is not central;
5. the trivial group $\{\mathrm{id}\}$, otherwise.

**Proof.** The group of involutions $G=\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\}$ is *The Group of Involutions*; the fixed set of ${}^{\natural}$ is the centre, of $\bar{\cdot}$ the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, and of ${}^{*}$ the Hermitian sector $\mathbb{M}_+$, so the stabiliser of $\tilde C$ is the stabiliser of the intersection of the fixed spaces that contain it. The invariance of the sets is the theorem applied elementwise. The five cases and the names of the corresponding symmetric fractals are the subject of *The Three Conjugations and the Symmetric Biquaternion Fractals*.

## The Critical Set

**Definition.** The **critical set** of $F_{\tilde C}$ is the set of points where the complex derivative $dF_{\tilde C}$ fails to be invertible.

**Proposition (the critical set).** For every parameter, the derivative of $F_{\tilde C}$ at $\tilde Q$ is the sum of the left and the right multiplication,

$$
dF_{\tilde C}|_{\tilde Q}(\tilde P)=\tilde Q\tilde P+\tilde P\tilde Q ,
$$

and its determinant is, up to a fixed non-zero factor depending only on the identification of $\mathbb{B}$ with $\mathbb{C}^4$,

$$
\det dF_{\tilde C}|_{\tilde Q} \;=\; 4\,N(\tilde Q)\,(2Q_0)^2 .
$$

Hence the critical set is the union of the zero-divisor cone $\{N(\tilde Q)=0\}$ and the vector subspace $\{Q_0=0\}=\mathrm{Vect}(\mathbb{B})$.

**Proof.** The family is $\tilde Q^2$ plus a constant, so its derivative is that of the general plain bilinear square, which is $\tilde P\mapsto\tilde Q\tilde P+\tilde P\tilde Q$ by the product rule. Transport along the algebra isomorphism $\Phi$ to $M_2(\mathbb{C})$: in the coordinates $(M_{11},M_{12},M_{21},M_{22})$ the linear map $V\mapsto MV+VM$ has matrix $I\otimes M+M^{\mathsf{T}}\otimes I$, whose determinant is $\det(M)\operatorname{tr}(M)^2\cdot 4$; substituting $\det\Phi(\tilde Q)=N(\tilde Q)$ and $\operatorname{tr}\Phi(\tilde Q)=2Q_0$ gives the formula. The determinant is a polynomial in $\tilde Q$ that is not identically zero, so its zero set is a hypersurface of the complex four-space; by the product formula that zero set is the union of the quadric $N(\tilde Q)=0$ and the hyperplane $Q_0=0$, which is the statement. 

Counting the coordinates, the critical set is the zero set of that one non-zero polynomial, hence a hypersurface of the complex four-space, with the two components named. The zero-divisor cone is the quadric $N(\tilde Q)=0$ and the vector subspace is the hyperplane $Q_0=0$.

**Remark.** The critical set is larger than the zero-divisor cone: it also contains the whole vector subspace $\mathrm{Vect}(\mathbb{B})$ of pure biquaternions, where the derivative degenerates because $Q_0=0$ makes the two eigenvalues of $\Phi(\tilde Q)$ opposite. **The derivative is singular exactly on the union of the zero divisors and the pure vectors, a hypersurface with two components.** The singular set governs the Fatou theory (*The Biquaternion Holomorphic Dynamics and the Jacobian*).

## The Central Parameter and the Eigenvalue Reduction

**Theorem (central parameter, eigenvalue reduction).** Let $\tilde C=Ce_0$ with $C\in\mathbb{C}$, let $q_n$ be the iterates of the complex quadratic map $\zeta\mapsto\zeta^2+C$ starting from $\zeta_0=\zeta$, and let $p_n$ be as above. For every $\tilde Q$,

$$
\Phi(F_{\tilde C}^{n}(\tilde Q))=p_n\bigl(\Phi(\tilde Q)\bigr)=q_n\text{ applied to the spectrum},
$$

in the sense that the spectrum of $\Phi(F_{\tilde C}^{n}(\tilde Q))$ is $\{q_n(\lambda_1),q_n(\lambda_2)\}$ for the spectrum $\{\lambda_1,\lambda_2\}$ of $\Phi(\tilde Q)$. If $\Phi(\tilde Q)$ is diagonalisable, then $\tilde Q\in\mathcal K_{\tilde C}$ if and only if both eigenvalues lie in the filled Julia set $K_C$ of $\zeta\mapsto\zeta^2+C$. If $\Phi(\tilde Q)$ has a repeated eigenvalue $\lambda$ and is not scalar, the extra condition is that the derivative sequence $(q_n'(\lambda))$ be bounded as well.

**Proof.** For a polynomial $p$ and a matrix $M$, the eigenvalues of $p(M)$ are the values of $p$ on the eigenvalues of $M$; this is the statement that the spectrum is transported by polynomial functional calculus, and it holds for every polynomial without any hypothesis on $M$. Boundedness: if $M=SJS^{-1}$ with $J$ the Jordan form, then $p_n(M)=Sp_n(J)S^{-1}$, and $p_n(J)$ is diagonal with entries $p_n(\lambda_j)$ when the eigenvalues are distinct, bounded exactly when each $(p_n(\lambda_j))$ is bounded, and is a Jordan block $\left(\begin{smallmatrix}p_n(\lambda)&p_n'(\lambda)\\0&p_n(\lambda)\end{smallmatrix}\right)$ for a repeated non-scalar eigenvalue, bounded exactly when both $(p_n(\lambda))$ and $(p_n'(\lambda))$ are. Norm equivalence finishes the boundedness claim.

**Corollary ($\tilde C=0$).** For the map $F_0(\tilde Q)=\tilde Q^2$ the iterated polynomial is $p_n(x)=x^{2^n}$, so the spectrum of $\Phi(F_0^n(\tilde Q))$ is $\{\lambda_1^{2^n},\lambda_2^{2^n}\}$ and

$$
\mathcal K_0=\{\tilde Q : \rho(\Phi(\tilde Q))<1\}\cup\{\tilde Q : \rho(\Phi(\tilde Q))=1 \text{ and } \Phi(\tilde Q) \text{ diagonalisable}\} .
$$

In particular every square-zero element has $\rho(\Phi(\tilde Q))=0$ and so lies in $\mathcal K_0$, however large its Euclidean norm is.

**Proof.** $q_n(\zeta)=\zeta^{2^n}$ and $q_n'(\zeta)=2^n\zeta^{2^n-1}$. For $|\lambda|<1$ the orbit tends to $0$; for $|\lambda|>1$ it escapes; for $|\lambda|=1$ the orbit stays on the unit circle and is bounded, while $|q_n'(\lambda)|=2^n$ is unbounded, so a non-scalar Jordan block at $|\lambda|=1$ makes the iterate unbounded and a diagonalisable one does not. A square-zero element is a non-zero nilpotent $2\times2$ matrix, of spectrum $\{0,0\}$ and not a Jordan block at a non-zero eigenvalue, so its iterate is $0$ from the first step and lies in $\mathcal K_0$.

**Example (the square-zero element).** The element $\tilde Q=e_1+ie_2$ is a pure vector with $(\mathbf Q,\mathbf Q)=1+i^2=0$, hence $\tilde Q^2=0$; its orbit under $F_0$ is $\tilde Q,0,0,\dots$, so it lies in $\mathcal K_0$ at distance $\sqrt2$ from the origin. It is the smallest witness that the filled Julia set is not confined to a bounded ball and that no escape radius can be stated in the Euclidean norm: an element of norm arbitrarily large and square-zero maps to $0$ in one step.

## Summary

The biquaternion quadratic family is $F_{\tilde C}(\tilde Q)=\tilde Q^2+\tilde C$ in the general plain bilinear product, the only one of the four general products that makes the space an associative unital $\mathbb{C}$-algebra; the other readings of the square give a scalar map for the natural conjugate, a real-analytic map for the Hermitian conjugate, and two affine families for the left and right multiplications, the last coinciding with the quadratic family only on the diagonal. The filled Julia set $\mathcal K_{\tilde C}$ is the set of bounded orbits and the Julia set is its boundary; both are closed and completely invariant, and boundedness is independent of the norm because the algebra is finite-dimensional. The family is equivariant under the three conjugations of the group of involutions, $g\circ F_{\tilde C}=F_{g(\tilde C)}\circ g$, the reversal being excluded because it carries the even family to the odd one; so the fractal carries the stabiliser of the parameter, which is the whole group for a real central parameter, the subgroup $\{\mathrm{id},{}^{\natural}\}$ for a non-real central parameter, $\{\mathrm{id},\bar{\cdot}\}$ for a non-central real quaternion, $\{\mathrm{id},{}^{*}\}$ for a non-central Hermitian element, and the trivial group otherwise. The derivative is $\tilde P\mapsto\tilde Q\tilde P+\tilde P\tilde Q$ and its determinant is proportional to $N(\tilde Q)Q_0^2$, so the critical set is the union of the zero-divisor cone and the vector subspace of pure vectors. For a central parameter the whole dynamics reduces, through the matrix model, to the complex quadratic map acting on the two eigenvalues; the reduction is exact for a diagonalisable matrix and acquires a derivative condition on a non-scalar Jordan block, and for the parameter zero it gives $\mathcal K_0$ as the set of matrices with spectral radius below one together with the diagonalisable matrices of spectral radius one.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra, $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $\tilde Q=\sum_\mu Q_\mu e_\mu$ | a biquaternion, $\mu=0,1,2,3$ |
| $Q_0$ | the scalar part |
| $N(\tilde Q)=\sum_\mu Q_\mu^2$ | the biquaternion norm, multiplicative, complex |
| $r(\tilde Q)=\sqrt{|N(\tilde Q)|}$ | the unique real multiplicative semi-norm |
| $\|\tilde Q\|_E$ | the Euclidean norm $\sqrt{\sum_\mu|Q_\mu|^2}$ |
| $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ | the matrix realization |
| ${}^{\natural},\bar{\cdot},{}^{*},\flat$ | quaternion, complex, Hermitian and anti-Hermitian conjugation |
| $F_{\tilde C}(\tilde Q)=\tilde Q^2+\tilde C$ | the biquaternion quadratic family |
| $p_n$ | the polynomial with $\tilde Q_n=p_n(\tilde Q)$, $p_{n+1}=p_n^2+\tilde C$ |
| $\mathcal K_{\tilde C}$ | the filled Julia set, the locus of bounded orbits |
| $J_{\tilde C}=\partial\mathcal K_{\tilde C}$ | the Julia set |
| $q_n$, $K_C$ | the complex iterates $\zeta\mapsto\zeta^2+C$ and the complex filled Julia set |
| $G=\{\mathrm{id},{}^{\natural},\bar{\cdot},{}^{*}\}$ | the group of involutions |

## Further Reading

- *Introduction to the General Plain Algebra of Biquaternions* (`articles_maths/introduction-to-the-general-plain-algebra-of-biquaternions.md`), for the algebra, its one associative unital product and the plane generated by one element.
- *Introduction to the 2×2 Matrix Representation of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-representation-of-biquaternions.md`), for the isomorphism $\Phi$, the trace and the determinant.
- *The Group of Involutions* (`articles_maths/the-group-of-involutions.md`), for the four conjugations, their fixed spaces and the orbits that give the symmetry groups.
- *The Julia Sets of a Complex Polynomial* (`articles_maths/the-julia-sets-of-a-complex-polynomial.md`), *The Mandelbrot Set and the Quadratic Family* (`articles_maths/the-mandelbrot-set-and-the-quadratic-family.md`) and *The Fatou Components and the Classification of the Dynamics* (`articles_maths/the-fatou-components-and-the-classification-of-the-dynamics.md`), for the one-variable theory the family generalises.
- *The Escape Radius and the Green's Function for the Biquaternions* (`articles_maths/the-escape-radius-and-the-greens-function-for-the-biquaternions.md`), for the metric statement the filled Julia set dispenses with.
