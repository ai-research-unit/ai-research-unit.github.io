
# __The Bergman Operator__

## Introduction

A domain $\Omega \subseteq \mathbb{C}^n$ carries a chosen form of its own: the inner product of square-integrable functions, restricted to the holomorphic ones. The **Bergman space** $A^2(\Omega)$ is the space of holomorphic functions on $\Omega$ that are square-integrable for Lebesgue measure, a closed subspace of the Hilbert space $L^2(\Omega)$, and therefore itself a Hilbert space. The **Bergman operator** is the orthogonal projection
$$
P : L^2(\Omega) \longrightarrow A^2(\Omega),
$$
the operator that assigns to a square-integrable function its best holomorphic approximation. It is the archetype of an operator that the geometry of the domain defines: it is the projection onto the holomorphic functions, it is self-adjoint and idempotent for the chosen inner product, it is an integral operator whose kernel is a reproducing kernel, and it transforms by an explicit factor under a biholomorphism. The metric that the same kernel generates, the **Bergman metric**, is the geometry the projection produces, and it is the subject of the article *Hermitian Symmetric Spaces and the Bergman Metric*, later in this category.

The article has four sections: the Bergman space and the projection; the Bergman kernel and the reproducing property; the operator properties of the projection; and the transformation law. The Hilbert space, the orthogonal projection, the completeness and the reproducing kernel are *Hilbert Spaces*, *Reproducing Kernel Hilbert Spaces* and *Bounded Operators on a Hilbert Space*; the several-complex-variable theory of holomorphic functions, the domains of holomorphy and the convergence of the power series are *Several Complex Variables* and *Analytic Functions and Power Series*; and Lebesgue measure, the $L^2$ space and the integral are *Measure and Integration*. None of that is re-derived. The Bergman metric, the automorphism group of a bounded domain and the Hermitian symmetric spaces are *Hermitian Symmetric Spaces and the Bergman Metric*; the involutions of the projection are *Involutions of the Bergman Operator*, in the `* Operator Theory` group.

Throughout, $\Omega \subseteq \mathbb{C}^n$ is a bounded domain, $dV$ is Lebesgue measure on it, $L^2(\Omega)$ is the space of measurable $f$ with $\int_\Omega |f|^2\,dV < \infty$, its inner product is $\langle f, g\rangle = \int_\Omega f\bar g\,dV$, $A^2(\Omega)$ is the **Bergman space** of holomorphic $f \in L^2(\Omega)$, $P$ is the Bergman operator, and $K : \Omega\times\Omega \to \mathbb{C}$ is the Bergman kernel.

## The Bergman Space and the Projection

**Definition.** The **Bergman space** of the bounded domain $\Omega$ is
$$
A^2(\Omega) = \bigl\{\, f : \Omega \to \mathbb{C} \ \text{holomorphic},\ \textstyle\int_\Omega |f|^2\,dV < \infty \,\bigr\} ,
$$
with the inner product inherited from $L^2(\Omega)$. The **Bergman operator** is the orthogonal projection $P$ of $L^2(\Omega)$ onto $A^2(\Omega)$.

**Proposition (the Bergman space is a Hilbert space).** $A^2(\Omega)$ is a closed subspace of $L^2(\Omega)$, hence a Hilbert space with the restricted inner product; convergence in $A^2(\Omega)$ implies locally uniform convergence, and the point evaluations $f \mapsto f(z)$ are continuous linear functionals on $A^2(\Omega)$ for every $z \in \Omega$.

**Proof.** On a compact $L \subseteq \Omega$ the mean-value inequality for a holomorphic function gives $|f(z)| \le c_L\,\|f\|_{L^2(\Omega)}$ for $z \in L$ and a constant $c_L$ that depends only on the distance from $L$ to the boundary; hence a Cauchy sequence in $A^2$ is Cauchy for locally uniform convergence, its limit is holomorphic by Weierstrass's theorem, and the limit lies in $L^2$; this proves closedness and the continuity of the evaluations at once. The mean-value inequality is *Several Complex Variables*.

**Proposition (the projection exists).** For a closed subspace of a Hilbert space the orthogonal projection exists, is unique, is linear, and is characterised by $P f \in A^2(\Omega)$ and $f - Pf \perp A^2(\Omega)$; in particular $P$ is the identity on $A^2(\Omega)$ and kills the orthogonal complement.

**Proof.** This is the projection theorem of *Hilbert Spaces* applied to the closed subspace $A^2(\Omega)$; the characterisation is the definition of the orthogonal decomposition $L^2 = A^2 \oplus (A^2)^{\perp}$.

## The Bergman Kernel and the Reproducing Property

**Definition.** Let $(\varphi_j)_{j \ge 0}$ be an orthonormal basis of $A^2(\Omega)$. The **Bergman kernel** of $\Omega$ is
$$
K(z, w) = \sum_{j \ge 0} \varphi_j(z)\,\overline{\varphi_j(w)} .
$$

**Proposition (the kernel is well defined, independent of the basis and reproducing).** The series converges absolutely and locally uniformly, the sum does not depend on the orthonormal basis, $K$ is holomorphic in $z$ and antiholomorphic in $w$, it satisfies the Hermitian symmetry $K(w, z) = \overline{K(z, w)}$, and for every $f \in A^2(\Omega)$
$$
f(z) = \langle f, K(\cdot, z)\rangle = \int_\Omega f(w)\,\overline{K(z, w)}\,dV(w) .
$$

**Proof.** For fixed $z$ the functional $f \mapsto f(z)$ is continuous by the previous section, so it is represented by a unique vector $K_z \in A^2(\Omega)$ with $f(z) = \langle f, K_z\rangle$, by Riesz's theorem of *Hilbert Spaces*; expanding $K_z = \sum_j \langle K_z,\varphi_j\rangle\varphi_j$ and using $\langle K_z,\varphi_j\rangle = \overline{\varphi_j(z)}$ gives $K_z = \sum_j \overline{\varphi_j(z)}\,\varphi_j$, and $K(z,w) = \overline{K_w(z)}$ is its evaluation. The absolute and locally uniform convergence is the convergence in $A^2$ together with the continuity of the evaluations; the independence of the basis is the uniqueness of the representing vector; the symmetry is $K(w,z) = \overline{K(z,w)}$ read from the display.

**Corollary (the kernel is the projection's kernel).** $P$ is the integral operator with kernel $K$,
$$
(Pf)(z) = \int_\Omega K(z, w)\,f(w)\,dV(w) \qquad (f \in L^2(\Omega)),
$$
and $K(\cdot, w) \in A^2(\Omega)$ for every $w$.

**Proof.** For $f \in L^2$ the function $Pf \in A^2$ is reproduced by the kernel, $(Pf)(z) = \langle Pf, K(\cdot,z)\rangle = \langle f, P K(\cdot,z)\rangle = \langle f, K(\cdot,z)\rangle$, since $K(\cdot,z) \in A^2$ is fixed by $P$ and $P$ is self-adjoint; writing the inner product as an integral gives the display.

**Example (the unit disc).** For $\Omega = \mathbb{D} \subseteq \mathbb{C}$ the monomials $\sqrt{(j+1)/\pi}\,z^j$, $j \ge 0$, are an orthonormal basis of $A^2(\mathbb{D})$, and
$$
K_{\mathbb{D}}(z, w) = \frac{1}{\pi}\sum_{j\ge0}(j+1)(z\bar w)^j = \frac{1}{\pi\,(1 - z\bar w)^2} .
$$
The kernel is positive on the diagonal, $K_{\mathbb{D}}(z,z) = \pi^{-1}(1-|z|^2)^{-2}$, and the Bergman metric it generates, $\partial\bar\partial\log K(z,z)$, is the hyperbolic metric of the disc; the metric is developed in *Hermitian Symmetric Spaces and the Bergman Metric*.

## The Operator Properties of the Projection

**Proposition.** The Bergman operator is a bounded self-adjoint idempotent,
$$
P^2 = P, \qquad P^{*} = P, \qquad \|P\| = 1, \qquad P \ge 0 ,
$$
where ${}^{*}$ is the adjoint for the $L^2$ inner product; its range is $A^2(\Omega)$, its kernel is $(A^2(\Omega))^{\perp}$, and $I - P$ is the projection onto $(A^2(\Omega))^{\perp}$.

**Proof.** An orthogonal projection in a Hilbert space satisfies $P^2 = P$ and $P^{*} = P$; a nonzero idempotent self-adjoint operator has norm one, because $\|P\|^2 = \|P^{*}P\| = \|P\|$ and $P \neq 0$; positivity is $\langle Pf,f\rangle = \langle P^2f,f\rangle = \langle Pf,Pf\rangle \ge 0$; the range and kernel are the definitions of an orthogonal projection. All of this is *Bounded Operators on a Hilbert Space*.

**Proposition (the kernel is positive definite).** Let $z_1,\dots,z_m \in \Omega$ and $c_1,\dots,c_m \in \mathbb{C}$. Then
$$
\sum_{i,j=1}^{m} c_i\,\overline{c_j}\,K(z_i, z_j) \ \ge\ 0 ,
$$
with equality only when $\sum_i c_i K(\cdot, z_i) = 0$; the Bergman kernel is thus a positive-definite kernel in the sense of *Reproducing Kernel Hilbert Spaces*, and $A^2(\Omega)$ is its reproducing kernel Hilbert space.

**Proof.** The sum is $\bigl\langle \sum_j c_j K(\cdot,z_j), \sum_i c_i K(\cdot,z_i)\bigr\rangle \ge 0$, and it vanishes exactly when the vector $\sum_i c_i K(\cdot,z_i)$ is zero. The identification of $A^2(\Omega)$ with the Hilbert space of the kernel is the Aronszajn theorem, *Reproducing Kernel Hilbert Spaces*.

**Remark (the projection and the chosen form).** Every statement of this section is measured against the inner product $\langle f,g\rangle = \int_\Omega f\bar g\,dV$, and it is this form, not only the holomorphic structure, that fixes the operator: a different measure on the same domain gives a different Bergman space, a different kernel and a different projection. The operator is therefore an object of the geometry of the domain, and the domain's automorphisms, which act on the projection, are the motions of the Bergman metric.

## The Transformation Law

**Theorem (the isometry of a biholomorphism).** Let $F : \Omega_1 \to \Omega_2$ be a biholomorphism with Jacobian determinant $\det F'$. Then the map
$$
U_F : A^2(\Omega_2) \longrightarrow A^2(\Omega_1), \qquad (U_F g)(z) = g\bigl(F(z)\bigr)\det F'(z),
$$
is an isometry onto its image, and the Bergman kernels are related by
$$
K_{\Omega_1}(z, w) = \det F'(z)\; K_{\Omega_2}\bigl(F(z), F(w)\bigr)\; \overline{\det F'(w)} .
$$

**Proof.** The change of variables $z = F^{-1}(\zeta)$ has real Jacobian $|\det F'|^2$, so $\int_{\Omega_1}|g\circ F|^2\,|\det F'|^2\,dV = \int_{\Omega_2}|g|^2\,dV$ and $U_F$ is an isometry; its inverse is $h \mapsto (h\circ F^{-1})\det(F^{-1})'$. For the kernel, the reproducing property of $K_{\Omega_1}$ must be transported by the isometry: for $h \in A^2(\Omega_1)$ one has $h(z) = \langle h, K_{\Omega_1}(\cdot,z)\rangle = \langle U_F^{-1}h, U_F^{-1}K_{\Omega_1}(\cdot,z)\rangle$, and computing $U_F^{-1}K_{\Omega_1}(\cdot,z)$ from the isometry and the reproducing property of $K_{\Omega_2}$ gives the displayed factor. This is the transformation law of the Bergman kernel.

**Corollary (invariance of the automorphism group's action).** A biholomorphism $F : \Omega \to \Omega$ of the domain maps the projection by conjugation, $U_F P U_F^{-1} = P$, and acts on the Bergman kernel by the factor above; in particular the Bergman metric is invariant under the holomorphic automorphisms of $\Omega$.

**Proof.** The conjugation statement is that $U_F$ preserves the subspace $A^2(\Omega)$ and hence the projection onto it; the metric statement is that $\partial\bar\partial\log K(z,z)$ transforms by the modulus of the holomorphic factor, which is a holomorphic reparametrisation of the Kähler potential. The automorphism group and the metric are *Hermitian Symmetric Spaces and the Bergman Metric*.

**Example (unit disc invariance check).** For $F(z) = e^{i\theta}z$ one has $\det F' = e^{i\theta}$ and $K_{\mathbb{D}}(F(z),F(w)) = K_{\mathbb{D}}(z,w)$, so the transformation law reads $K_{\mathbb{D}}(z,w) = e^{i\theta}K_{\mathbb{D}}(z,w)e^{-i\theta}$, an identity; for the disc automorphism $F(z) = \tfrac{z-a}{1-\bar a z}$ the same computation reproduces $K_{\mathbb{D}}$ and shows the invariance of the hyperbolic metric.

## Summary

A bounded domain $\Omega \subseteq \mathbb{C}^n$ carries the Bergman space $A^2(\Omega)$ of holomorphic square-integrable functions, a closed subspace of $L^2(\Omega)$ and hence a Hilbert space, and the Bergman operator $P$ is the orthogonal projection of $L^2(\Omega)$ onto it. The projection is represented by the Bergman kernel $K(z,w) = \sum_j \varphi_j(z)\overline{\varphi_j(w)}$, holomorphic in $z$, antiholomorphic in $w$, Hermitian and positive definite, and reproducing every $f \in A^2$ by the integral against $K$; it satisfies $P^2 = P$, $P^{*} = P$, $\|P\| = 1$ and $P \ge 0$ for the chosen $L^2$ form. A biholomorphism $F : \Omega_1 \to \Omega_2$ acts by the isometry $g \mapsto (g\circ F)\det F'$, and the kernels transform by $K_{\Omega_1}(z,w) = \det F'(z)\,K_{\Omega_2}(F(z),F(w))\,\overline{\det F'(w)}$, so the holomorphic automorphisms of the domain preserve the projection up to conjugation and the Bergman metric up to holomorphic reparametrisation. The metric, the automorphism group and the Hermitian symmetric spaces are *Hermitian Symmetric Spaces and the Bergman Metric*; the involutions of the projection are *Involutions of the Bergman Operator*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Omega \subseteq \mathbb{C}^n$ | a bounded domain; $dV$ Lebesgue measure |
| $L^2(\Omega)$ | square-integrable functions, $\langle f,g\rangle = \int_\Omega f\bar g\,dV$ |
| $A^2(\Omega)$ | the Bergman space, the holomorphic functions in $L^2(\Omega)$ |
| $P$ | the Bergman operator, the orthogonal projection onto $A^2(\Omega)$ |
| $K(z,w)$ | the Bergman kernel, $\sum_j \varphi_j(z)\overline{\varphi_j(w)}$ |
| $\varphi_j$ | an orthonormal basis of $A^2(\Omega)$ |
| $U_F$ | the isometry $g \mapsto (g\circ F)\det F'$ of a biholomorphism |
| $\det F'$ | the Jacobian determinant of a biholomorphism |

## Further Reading

- Stefan Bergman, *The Kernel Function and Conformal Mapping* (American Mathematical Society, second edition, 1970), for the kernel function and its transformation law.
- Steven G. Krantz, *Function Theory of Several Complex Variables* (American Mathematical Society, second edition, 2001), for the Bergman space, the kernel and the projection on a domain.
- Elias M. Stein and Rami Shakarchi, *Complex Analysis* (Princeton University Press, 2003), for the mean-value inequality and the elementary behaviour of the Bergman space of the disc.
- Nachman Aronszajn, "Theory of reproducing kernels", *Transactions of the American Mathematical Society* **68** (1950), 337–404, for the reproducing kernel and its positive definiteness.
