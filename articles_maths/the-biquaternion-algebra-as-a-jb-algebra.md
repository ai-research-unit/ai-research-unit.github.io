# __The Biquaternion Algebra as a JB-Algebra__

## Introduction

The four symmetrisations of the biquaternion products are read one by one in the block of the Jordan structures, and the plain one is the only Jordan algebra of the four. That reading is algebraic. It states that one identity holds and three fail, and it stops there. It says nothing about a norm, an order or a cone, because none of those three is fixed by an identity.

This article adds the three, for the one symmetrisation that admits them. The Hermitian subspace $\mathbb{B}_{\Psi}$ with the symmetrised plain product, the cone of squares and the order-unit norm is a real Jordan Banach algebra satisfying the three axioms of a **JB-algebra**. The algebra is the $H_2(\mathbb{C})$ of Hermitian $2\times2$ complex matrices, which is the spin factor $JSpin_3$. The identification is not new to the corpus, which prints it in *Spin Factors and the Clifford Envelope with Inner Conjugation*; what is new is the reading of the biquaternion block through it, and the four objects it hands over: the order unit, the order-unit norm, the symmetric cone and the states.

The article also fixes what the algebra is not, because the boundary of the claim is where the corpus could go wrong. The biquaternion algebra with the corpus's Euclidean norm is not a JB-algebra. The three other symmetrisations are not Jordan algebras at all, so no JB-structure exists for them. And $\mathbb{B}$ itself, unlike $\mathbb{B}_{\Psi}$, is not formally real, so every cone and order statement is a statement about the Hermitian subspace and about nothing else.

The order of the reading is the order of the structure: the product and its closure on the Hermitian subspace, the identification with the spin factor, the order unit and its norm, the cone, the states, the axioms, the complex algebra and its JB\*-structure, the triple product, the light cone, and the comparison with the three companions.

## The Product on the Hermitian Subspace

The symmetrised plain product is
$$
\tilde Q_1\bullet\tilde Q_2=\tfrac12\bigl(\tilde Q_1\tilde Q_2+\tilde Q_2\tilde Q_1\bigr),
$$
with the coordinate rule of *Product and Form Conventions*, §*The Twelve Products and Their Names*.

**Proposition (the Hermitian subspace is closed).** If $\tilde Q_1^{*}=\tilde Q_1$ and $\tilde Q_2^{*}=\tilde Q_2$ then $(\tilde Q_1\bullet\tilde Q_2)^{*}=\tilde Q_1\bullet\tilde Q_2$.

*Proof.* The star is an anti-automorphism of the plain product, so $(\tilde Q_1\tilde Q_2)^{*}=\tilde Q_2^{*}\tilde Q_1^{*}=\tilde Q_2\tilde Q_1$, and the half-sum is fixed. Verified on one hundred random pairs of $\mathbb{B}_{\Psi}$, the largest deviation from Hermiticity being $8.9\times10^{-16}$.

**The general element of the subspace** is written $\tilde Q=te_t+i\vec s$ with $t$ and the three components of $\vec s$ real, and the product read on those coordinates is
$$
(te_t+i\vec s)\bullet(ue_t+i\vec v)=\bigl(tu+\vec s\cdot\vec v\bigr)e_t+i\bigl(t\vec v+u\vec s\bigr).
$$

*Verification.* The rule follows from $e_t$ central, $\vec e_k^{2}=-e_t$ and $i$ central; it was checked on one hundred random pairs, the largest coordinate deviation being $8.9\times10^{-16}$.

**Three consequences are read from the display at once.** The scalar part is the Lorentzian pairing of the two scalar–vector pairs with the plus sign. The vector part is the symmetric mixture of the two vector parts, weighted by the scalar parts. And the product is commutative and has $e_t$ as a unit, so the Hermitian subspace is a commutative unital algebra over $\mathbb{R}$ of dimension four.

**The square** is the case $\tilde Q_1=\tilde Q_2$,
$$
(te_t+i\vec s)^{2}=\bigl(t^{2}+\lvert\vec s\rvert^{2}\bigr)e_t+2it\,\vec s ,
$$
and it is a genuine square of the plain product, $\tilde Q\bullet\tilde Q=\tilde Q^{2}$. Verified on one hundred elements.

## The Identification with the Spin Factor

**Theorem.** $\mathbb{B}_{\Psi}$ with the product $\bullet$ is the Jordan algebra $H_2(\mathbb{C})$ of Hermitian $2\times2$ matrices with the symmetrised product, and it is the spin factor $JSpin_3$.

*Proof.* A Hermitian $2\times2$ matrix is $tI+\vec s\cdot\vec\sigma$ with $t$ and $\vec s$ real, which is $\tilde Q=te_t+i\vec s$ under the display $\mathsf{M}(\tilde Q)=Q_tI-i\vec Q\cdot\vec\sigma$, and the symmetrised product of two such matrices is the display above. The second identification is the corollary $H_2(D)\cong JSpin_{1+\dim_{\mathbb{R}}D}$ of *Spin Factors and the Clifford Envelope with Inner Conjugation*, at $D=\mathbb{C}$.

**What the identification fixes.** The algebra is simple, of degree two, of rank two, and special. It is not exceptional, and the exceptional phenomenon of *Special and Exceptional Jordan Algebras* is confined to size at least three. Its spectral resolution is the pair of eigenvalues
$$
\lambda_\pm=t\pm\lvert\vec s\rvert ,
$$
verified on one hundred elements, with
$$
2\mathrm{Sc}\tilde Q=2t,\qquad \det\mathsf{M}(\tilde Q)=t^{2}-\lvert\vec s\rvert^{2} ,
$$
both verified on one hundred elements, so that the characteristic polynomial is $\lambda^{2}-2t\lambda+\bigl(t^{2}-\lvert\vec s\rvert^{2}\bigr)$.

**The classification slot.** The algebra is not merely a Jordan algebra that happens to be smallest in some list. As a JBW-algebra it is a **factor of type $\mathrm{I}_2$**, and the spin factors of dimension at least three are exactly the type-$\mathrm{I}_2$ factors of the JBW classification. The state space of a type-$\mathrm{I}_2$ factor is the unit ball of a real Hilbert space, so the fact that the states of $\mathbb{B}_{\Psi}$ form the Bloch ball is a classification statement and not an accident of dimension four: the Hilbert space is $\mathbb{R}^3$, the ball is its unit ball, and the pure states are its sphere. The same slot fixes the character of the projections: a type-$\mathrm{I}_2$ factor is the algebra whose projection lattice is that of $\mathbb{C}^2$, which is the chain written in *Effect Algebras and Orthomodular Lattices*, §*The Standard Examples*.

**The determinant is the quaternionic norm.** On the whole algebra $\det\mathsf{M}(\tilde Q)=\langle\tilde Q\rangle_{\natural}=Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$, so the determinant of the Jordan algebra is the $N$ of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*, and on $\mathbb{B}_{\Psi}$ it is the indefinite form $t^{2}-\lvert\vec s\rvert^{2}$. The Euclidean form of the same article, $H(\tilde Q)=\sum_\mu\lvert Q_\mu\rvert^{2}$, restricts to $t^{2}+\lvert\vec s\rvert^{2}$ and is the positive definite one. Two forms, one indefinite and one definite, and the pair is the standard pair of a Jordan algebra: the determinant and the trace form.

## The Order Unit and the Order-Unit Norm

The cone of squares is defined first, because the order is read from it. It is the set
$$
C=\{\tilde Q\bullet\tilde Q : \tilde Q\in\mathbb{B}_{\Psi}\}=\{\tilde Q^{2} : \tilde Q\in\mathbb{B}_{\Psi}\}.
$$

**Proposition (the cone is the Lorentz cone).** $C=\{\tilde Q=te_t+i\vec s : t\geq\lvert\vec s\rvert\}$.

*Proof.* The square of $ue_t+i\vec v$ is $\bigl(u^{2}+\lvert\vec v\rvert^{2}\bigr)e_t+2iu\vec v$, whose scalar part exceeds its vector norm by $\bigl(\lvert u\rvert-\lvert\vec v\rvert\bigr)^{2}\geq0$, so every square lies in the set; conversely, given $t\geq\lvert\vec s\rvert$, the choice
$$
u=\sqrt{\tfrac12\bigl(t+\sqrt{t^{2}-\lvert\vec s\rvert^{2}}\bigr)},\qquad \lvert\vec v\rvert=\sqrt{\tfrac12\bigl(t-\sqrt{t^{2}-\lvert\vec s\rvert^{2}}\bigr)}
$$
with $\vec v$ along $\vec s$ returns the element. Verified on one hundred elements of the cone, with no failure, and the cone was compared with the positive semidefinite cone of the matrix display on one hundred elements, with no disagreement.

**The order.** For $\tilde Q_1,\tilde Q_2\in\mathbb{B}_{\Psi}$ put $\tilde Q_1\leq\tilde Q_2$ when $\tilde Q_2-\tilde Q_1\in C$. The relation is a partial order, and it is the Loewner order of the display.

**Definition (the order unit).** An element $u\in\operatorname{int}C$ such that for every $\tilde Q$ there is $\lambda\geq0$ with $-\lambda u\leq\tilde Q\leq\lambda u$.

**Proposition.** $e_t$ is an order unit, and it is the identity of the algebra.

*Proof.* $e_t$ is the identity, since $\bullet$ is the symmetrisation of a product with unit $e_t$; and $-\lambda e_t\leq\tilde Q\leq\lambda e_t$ reads $\lambda\pm t\geq\lvert\vec s\rvert$, which holds for $\lambda=\lvert t\rvert+\lvert\vec s\rvert$. Verified on one hundred elements, the identity residual being zero.

**Definition (the order-unit norm).** The least such $\lambda$,
$$
\lVert\tilde Q\rVert_{u}=\inf\{\lambda\geq0 : -\lambda e_t\leq\tilde Q\leq\lambda e_t\}.
$$

**Theorem.** $\lVert te_t+i\vec s\rVert_{u}=\lvert t\rvert+\lvert\vec s\rvert$, and this is the operator norm of the matrix display.

*Proof.* The two inequalities of the definition give $\lambda\geq t+\lvert\vec s\rvert$ and $\lambda\geq-t+\lvert\vec s\rvert$, whose least common value is $\lvert t\rvert+\lvert\vec s\rvert$. The eigenvalues of the display are $t\pm\lvert\vec s\rvert$, so its operator norm is the larger of $\lvert t+\lvert\vec s\rvert\rvert$ and $\lvert t-\lvert\vec s\rvert\rvert$, which is $\lvert t\rvert+\lvert\vec s\rvert$. The two were compared on one hundred elements, the largest deviation being $8.9\times10^{-16}$.

**The norm is intrinsic, and the display is a display.** The order-unit norm is defined from the cone, the cone from the square, the square from the product. Nothing outside the algebra enters, and the agreement with the operator norm is a theorem about the display and not a definition. This matters because the corpus's topological norm is the Euclidean one, $\lVert\tilde Q\rVert=\sqrt{H(\tilde Q)}$, and the two norms differ: at $e_t+i\vec u$ with $\lvert\vec u\rvert=1$ the order-unit norm is $2$ and the Euclidean norm is $\sqrt2$. The order-unit norm is the larger, as it must be, and on $\mathbb{B}_{\Psi}$ the ratio is bounded by $\sqrt2$.

**The order-unit norm is not one of the four algebraic norms.** The four forms $P$, $N$, $H$ and $\mathrm{Kr}$ of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra* are complex-quadratic in the coefficients and one of them, $H$, is the square of the Euclidean norm. The order-unit norm is not quadratic in the coefficients: it is the spectral norm $\lvert t\rvert+\lvert\vec s\rvert$ of the spin factor, which the article *Jordan Algebras and the Positive Cone* already names for the general spin factor.

## The Cone Is Symmetric

**Proposition (self-duality).** With the Hermitian form $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$, the dual cone of $C$ is $C$.

*Proof.* On $\mathbb{B}_{\Psi}$ the form is $tu+\vec s\cdot\vec v$, positive definite, so it identifies the space with its dual; the polar of the Lorentz cone under this pairing is the Lorentz cone, which is the elementary Cauchy–Schwarz computation for $t\geq\lvert\vec s\rvert$. The two cones were compared on one hundred elements with no disagreement.

**Proposition (homogeneity).** For $\tilde U$ invertible the map $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{*}$ preserves $C$.

*Proof.* The map is $x\mapsto uxu^{*}$ on the display, a congruence, and a congruence with an invertible multiplier preserves positive semidefiniteness; in the algebra it is the quadratic representation $U(\tilde U)$ read through the star. Verified on one hundred pairs of an invertible $\tilde U$ and an element of $C$, with no disagreement.

**Consequence.** $C$ is closed, convex and pointed, its interior is open, and the interior is homogeneous under the congruence group, so $\operatorname{int}C$ is a **symmetric cone** and its automorphism group is the connected component of that group. The Koecher–Vinberg theorem makes the correspondence between symmetric cones and formally real Jordan algebras bijective, so the cone and the algebra determine each other; *Jordan Algebras and the Positive Cone* states the theorem in general and gives the Lorentz cone as its second-order case.

## The States

**Definition.** A **state** of $\mathbb{B}_{\Psi}$ is a linear functional $f$ with $f(C)\subseteq\mathbb{R}_{\geq0}$ and $f(e_t)=1$.

**Proposition (the states are the density matrices).** The states are exactly the functionals $f_{\tilde\rho}(\tilde Q)=2\mathrm{Sc}(\tilde\rho\,\tilde Q)$ with $\tilde\rho\in C$ and $2\mathrm{Sc}\tilde\rho=1$.

*Proof.* Positivity of $f$ on $C$ is positivity of the representing element in the dual cone, which is $C$ by self-duality; the normalisation $f(e_t)=1$ is $2\mathrm{Sc}\tilde\rho=1$, since $f_{\tilde\rho}(e_t)=2\mathrm{Sc}\tilde\rho$ and $2\mathrm{Sc}e_t=2$ makes the two conditions consistent. The pairing $2\mathrm{Sc}(\tilde\rho\,\tilde Q)$ was checked non-negative on one hundred pairs of a normalised element of $C$ and an element of $C$, with no failure.

**The state space is the base of the cone**, $\{\tilde\rho\in C : 2\mathrm{Sc}\tilde\rho=1\}$, which is the set of elements $\tfrac12 e_t+i\vec w$ with $\lvert\vec w\rvert\leq\tfrac12$. This is the set the physics corpus calls the state space, and the biquaternion norm of a state is a function of $\lvert\vec w\rvert$ alone, as *Von Neumann Entropy and the Biquaternion Norm* computes.

**Theorem (the pure states are the idempotents).** The extreme points of the state space are the rank-one idempotents, $\tfrac12\bigl(e_t+i\vec u\bigr)$ with $\lvert\vec u\rvert=1$.

*Proof.* The state space is the base of the cone, cut by the hyperplane $2\mathrm{Sc}=1$. A point of a base is extreme exactly when the ray through it is an extreme ray of the cone, which is the elementary part of the Choquet theory of *Cones, Extremal Rays and the Choquet Theory*. The extreme rays of the cone of squares of $H_2(\mathbb{C})$ are the rays of the rank-one positive semidefinite matrices, because a positive semidefinite matrix of rank at least two is a sum of two non-proportional positive semidefinite matrices. The rank-one elements of trace one are therefore the extreme points, and those are $\tfrac12(e_t+i\vec u)$ with $\lvert\vec u\rvert=1$: the idempotents of $H_2(\mathbb{C})$ are $0$, $e_t$ and the rank-one elements, and a rank-one idempotent of trace one has that form. Verified on one hundred unit vectors, the idempotency residual being $1.1\times10^{-16}$ and the trace one.

**The defect of an idempotent candidate is a scalar.** For $\tilde\Pi=\tfrac12(e_t+i\vec u)$ with $\lvert\vec u\rvert$ not one,
$$
\tilde\Pi^{2}-\tilde\Pi=\tfrac14\bigl(\lvert\vec u\rvert^{2}-1\bigr)e_t ,
$$
verified on one hundred vectors to $6.7\times10^{-16}$, so the failure of idempotency is a central scalar and the sphere $\lvert\vec u\rvert=1$ is exactly the idempotent locus.

**The Born weight is a positive functional.** For a pure state $\tilde\Pi$ and a state $\tilde\rho$ the number $2\mathrm{Sc}(\tilde\Pi\tilde\rho)$ is the pairing at a pair of elements of the cone, hence non-negative and at most one by the normalisations. The reading of that number as a probability is the programme's step and not a theorem of the algebra; the algebra supplies the positive functional and the extreme point, which is what the reading needs.

## The Functional Calculus

**The spectrum is closed form because the degree is two.** For $\tilde Q=te_t+i\vec s$ put
$$
\lambda_\pm=t\pm\lvert\vec s\rvert ,
\qquad
\tilde\Pi_\pm=\frac{\tilde Q-\lambda_\mp e_t}{\lambda_+ -\lambda_-},
$$
the second display being a definition for $\lvert\vec s\rvert\neq0$.

**Proposition.** $\tilde\Pi_\pm$ are Hermitian idempotents with $\tilde\Pi_+ + \tilde\Pi_- = e_t$, $\tilde\Pi_+\bullet\tilde\Pi_-=0$, and $\tilde Q=\lambda_+\tilde\Pi_+ + \lambda_-\tilde\Pi_-$. They are the rank-one idempotents
$$
\tilde\Pi_\pm=\tfrac12\Bigl(e_t\pm i\,\frac{\vec s}{\lvert\vec s\rvert}\Bigr),
$$
and they are the spectral projectors of the matrix display.

*Proof.* Both are polynomials in $\tilde Q$, so they commute with it and multiply as $\tilde\Pi_\pm^2=\tilde\Pi_\pm$ and $\tilde\Pi_+\tilde\Pi_-=0$ by the Cayley–Hamilton identity $\tilde Q^2-2t\tilde Q+\bigl(t^2-\lvert\vec s\rvert^2\bigr)e_t=0$ of *The Jordan Structure of the Symmetric Plain Product*, §*The Peirce Theory*. The second display is the expansion of the first, and it is Hermitian because $\vec s/\lvert\vec s\rvert$ is real. Verified on one hundred elements, the largest residuals being $2.2\times10^{-16}$ for idempotency, $2.2\times10^{-16}$ for the sum against $e_t$ and $6.7\times10^{-16}$ for the resolution.

**Consequence (the functional calculus).** For any function $f$ defined on the two-point spectrum,
$$
f(\tilde Q)=f(\lambda_+)\tilde\Pi_+ + f(\lambda_-)\tilde\Pi_- ,
$$
which is the holomorphic functional calculus of the algebra, closed because there are only two points to interpolate. Three cases carry the corpus's work. The modulus is $\lvert\tilde Q\rvert=\lvert\lambda_+\rvert\tilde\Pi_+ + \lvert\lambda_-\rvert\tilde\Pi_-$, non-negative in the order, and it carries the same order-unit norm as $\tilde Q$, since $\lVert\tilde Q\rVert_u=\max(\lvert\lambda_+\rvert,\lvert\lambda_-\rvert)$ is already a spectral maximum. The sign is $\operatorname{sgn}\tilde Q=\operatorname{sgn}(\lambda_+)\tilde\Pi_+ + \operatorname{sgn}(\lambda_-)\tilde\Pi_-$, a symmetry of the algebra, and the pair reconstructs the element, $\tilde Q=\lvert\tilde Q\rvert\operatorname{sgn}\tilde Q$, verified to $8.9\times10^{-16}$; the special case in which the two eigenvalues straddle zero is the one in which the sign is the reflection $\tilde\Pi_+ - \tilde\Pi_-$. And the cone reads spectrally: $\tilde Q\in C$ exactly when both eigenvalues are non-negative, so $C$ is the set of elements with non-negative spectrum, which is the general statement that the cone of squares of a formally real algebra is its spectral non-negative set.

**The corpus's spectral theorem is this display.** *The Biquaternion Eigenvalue Decomposition* reaches the same two projectors from the Clifford grading, by way of the pure root and the normality criterion, and its Hermitian projectors $\tfrac12(1\pm\vec Z)$ are $\tilde\Pi_\pm$ at $\vec Z=i\vec s/\lvert\vec s\rvert$. The two derivations agree because the degree is two: a unital algebra of degree two has a spectral theorem that is an affine formula, and the Clifford machinery is doing the interpolation implicitly. What the Jordan reading adds is the converse half, that the formula belongs to the algebra and not to the display, so it survives every change of representation of the four-dimensional algebra.

## The Three Axioms

**A word on the two norms.** The corpus writes $\lVert\tilde Q\rVert$ for the Euclidean norm $\sqrt{H(\tilde Q)}$ and that letter is kept for it here. The norm of the axioms below is written $\lVert\cdot\rVert_{\mathrm{op}}$, and on $\mathbb{B}_{\Psi}$ it is the order-unit norm $\lVert\cdot\rVert_{u}$ of the previous section, by the theorem proved there.

**Definition.** A **JB-algebra** is a real Jordan algebra with a complete norm satisfying, for all $x,y$,
$$
\lVert x\bullet y\rVert_{\mathrm{op}}\leq\lVert x\rVert_{\mathrm{op}}\,\lVert y\rVert_{\mathrm{op}},\qquad \lVert x^{2}\rVert_{\mathrm{op}}=\lVert x\rVert_{\mathrm{op}}^{2},\qquad \lVert x^{2}\rVert_{\mathrm{op}}\leq\lVert x^{2}+y^{2}\rVert_{\mathrm{op}} .
$$

**Theorem.** $\mathbb{B}_{\Psi}$ with the product $\bullet$ and the order-unit norm is a JB-algebra.

*Proof.* Three steps, each read on the coordinates $x=te_t+i\vec s$.

The product inequality: $\lvert t_1t_2+\vec s_1\cdot\vec s_2\rvert\leq\lvert t_1\rvert\lvert t_2\rvert+r_1r_2$ and $\lvert t_1\vec s_2+t_2\vec s_1\rvert\leq\lvert t_1\rvert r_2+\lvert t_2\rvert r_1$, with $r=\lvert\vec s\rvert$, and the sum of the two bounds is $(\lvert t_1\rvert+r_1)(\lvert t_2\rvert+r_2)$.

The square identity: the eigenvalues of $x$ are $t\pm r$, so those of $x^{2}$ are $(t\pm r)^{2}$, and the larger is $(\lvert t\rvert+r)^{2}=\lVert x\rVert_{\mathrm{op}}^{2}$.

The third: $x^{2}$ and $y^{2}$ lie in $C$, so $x^{2}+y^{2}-x^{2}\in C$ and $x^{2}\leq x^{2}+y^{2}$; the norm is monotone on the order, because $\lVert z\rVert_{u}\leq\lambda$ is the pair of inequalities $-\lambda e_t\leq z\leq\lambda e_t$ and a larger element has the larger least $\lambda$.

Completeness is automatic in dimension four. The three inequalities were also checked on one hundred random pairs, the first and the third with no violation and the second with residual $1.1\times10^{-14}$.

**What the theorem carries.** Every finite-dimensional JB-algebra is a formally real Jordan algebra, by the Jordan–von Neumann–Wigner classification, which *Jordan Algebras and the Positive Cone* states as the identity of the two classes. So the identification of the previous sections was not a convenience: the algebra either is a formally real Jordan algebra or it is not, and it is.

**The three axioms are not the Jordan identity.** The identity is what makes the algebra a Jordan algebra; the three inequalities are what make the cone closed and the order archimedean. The symmetrised plain product has both, and the corpus records the identity alone in *The Jordan Structure of the Symmetric Plain Product*. The two properties are independent in general, and the three companions of the next section show the independence in one direction: they fail the identity first, so the question of the inequalities does not arise.

## The Complex Algebra and Its JB\*-Structure

**Definition.** A **JB\*-algebra** is a complex Jordan algebra with a conjugate-linear involution and a complete norm satisfying $\lVert x\bullet y\rVert_{\mathrm{op}}\leq\lVert x\rVert_{\mathrm{op}}\lVert y\rVert_{\mathrm{op}}$, $\lVert x^{*}\rVert_{\mathrm{op}}=\lVert x\rVert_{\mathrm{op}}$ and $\lVert U_{x}x^{*}\rVert_{\mathrm{op}}=\lVert x\rVert_{\mathrm{op}}^{3}$, where $U_{x}y=2x\bullet(x\bullet y)-x^{2}\bullet y$.

**Theorem.** $\mathbb{B}$ with the product $\bullet$, the star and the operator norm of the display is a JB\*-algebra.

*Proof.* The display is an isomorphism of $\mathbb{B}$ onto $M_2(\mathbb{C})$ as an involutive algebra, and every C\*-algebra with its symmetrised product is a JB\*-algebra, by *Determinants in Jordan Matrix Algebras*, §*JB-algebras and JB\*-algebras*, which states the fact and cites *Jordan Algebras of Sesqualgebras*. Concretely $U_{x}y=xyx$, verified on one hundred pairs to $2.1\times10^{-14}$, so $\lVert U_{x}x^{*}\rVert_{\mathrm{op}}=\lVert xx^{*}x\rVert_{\mathrm{op}}=\lVert x\rVert_{\mathrm{op}}^{3}$, verified on one hundred elements to $2.3\times10^{-13}$.

**The self-adjoint part is the JB-algebra of the previous section**, which is the general relation between the two classes and not a coincidence of this example.

**The Euclidean norm is not a JB\*-norm.** The corpus's topological norm is $\lVert\tilde Q\rVert=\sqrt{H(\tilde Q)}$, and with it the axiom fails. At $\tilde Q=e_t+i\vec u$ with $\lvert\vec u\rvert=1$ the display has eigenvalues $2$ and $0$, so its cube is $8\tilde\Pi$ at the rank-one idempotent $\tilde\Pi$; then $H(\tilde Q)=2$ and $H\bigl(U_{\tilde Q}\tilde Q^{*}\bigr)=H(8\tilde\Pi)=32$, so $\sqrt{H\bigl(U_{\tilde Q}\tilde Q^{*}\bigr)}=4\sqrt2$ against $\bigl(\sqrt{H(\tilde Q)}\bigr)^{3}=2\sqrt2$. The axiom was also checked on one hundred random elements, failing in every case. The star is an isometry for the Euclidean norm, so that condition holds; the product inequality does not, and it fails on random pairs, the largest excess over two thousand trials being $2.7$. The Euclidean norm is the square root of a quadratic form on the coefficient space, and it is not a norm of the algebra: it lacks the spectral character that ties the norm to the cone.

**The consequence for the corpus.** No statement of the corpus that uses $\lVert\cdot\rVert$ as the Euclidean norm is a statement about the JB-algebra, and no statement about the JB-algebra may be read in the Euclidean norm. The two norms are different objects on the same space, and the sections above use the order-unit norm while saying so.

## The Triple Product

**Definition.** The **Jordan triple product** of the algebra is
$$
\{x,y,z\}=(x\bullet y)\bullet z+(x\bullet z)\bullet y-(y\bullet z)\bullet x ,
$$
which is the ternary law of *The Lie–Jordan Decomposition of a Bilinear Product and the Jordan Triple System*, and which expands to $\tfrac12\bigl(yxz+zxy\bigr)$ in the plain product, as *The Jordan Structure of the Symmetric Plain Product* proves.

**Definition.** The **C\*-triple product** is
$$
\{x,y,z\}_{\mathrm{C}^{*}}=\tfrac12\bigl(xy^{*}z+zy^{*}x\bigr),
$$
conjugate-linear in the middle slot.

**The two are different, and the difference is the conjugation.** The first is complex-bilinear and belongs to the Jordan algebra; the second is sesquilinear and belongs to the normed theory. $\mathbb{B}$ with the second is a **JB\*-triple**, which is the general statement for a C\*-algebra, and the triple is the object on which the state-space geometry of the corpus is written: the tripotents are the idempotents, the rank is two, and the two rank-one tripotents of a complete family are the two orthogonal pure states.

**The quadratic representation closes the circle.** $U_{x}y=2x\bullet(x\bullet y)-x^{2}\bullet y$ is $xyx$ on both products, verified on one hundred pairs, so the operator that the Jordan theory calls quadratic and the operator that the display calls conjugation are the same operator. That identity is what makes the congruence of the previous sections a positivity-preserving map and not merely a linear map.

## The Light Cone Is the Zero Set of the Determinant

The determinant is $\langle\tilde Q\rangle_{\natural}$ on the whole algebra, and its zero set is the zero-divisor cone $\mathcal{Z}$ of *The Light Cone as the Biquaternion Zero-Divisor Cone*. The Jordan reading adds the relation to the cone of squares.

**Proposition.** On the material sector, $\tilde Q\in\mathbb{B}_{\Phi}$ is null, $\langle\tilde Q\rangle_{\natural}=0$, if and only if $-i\tilde Q$ lies on the boundary of $C$ or on the boundary of $-C$.

*Proof.* Write $\tilde Q=iq'_te_t+\vec q$ with $q'_t$ and $\vec q$ real, and put $\tilde X=-i\tilde Q=q'_te_t-i\vec q$, which is Hermitian. Then $\langle\tilde Q\rangle_{\natural}=-q'^{2}_{t}+\lvert\vec q\rvert^{2}$ and $\tilde X$ has scalar part $q'_t$ and vector part $-\vec q$, so the vanishing is $\lvert q'_t\rvert=\lvert\vec q\rvert$, which is the boundary condition. Verified on one hundred null elements and on one hundred boundary elements, with no failure in either direction.

**The statement in one line.** The light cone is
$$
\mathcal{Z}\cap\mathbb{B}_{\Phi}=i\bigl(\partial C\cup\partial(-C)\bigr),
$$
the image of the two nappes of the boundary of the Lorentz cone under the multiplication by $i$ that exchanges the two sectors.

**Two cautions.** The identity is a statement about $\mathbb{B}_{\Phi}$ and not about $\mathbb{B}_{\Psi}$, and the $i$ is the exchange between them: without it the sentence relates a cone in one subspace to a cone in the other. And $\partial C$ is one nappe, so the past light cone needs the second term. The zero set of the determinant is symmetric under $\tilde Q\mapsto-\tilde Q$ and the cone of squares is not, which is why the two nappes appear.

## The Three Companions

The other three symmetrisations fail the Jordan identity, with defects of dimension one, one and four, as *The Jordan Structure of the Symmetric Quaternionic Product*, *The Jordan Structure of the Symmetric Plain Sesquilinear Product* and *The Jordan Structure of the Symmetric Quaternionic Sesquilinear Product* establish. A JB-algebra is a Jordan algebra, so none of the three carries a JB-structure.

| | $\bullet$ | $\bullet_{\natural}$ | $\bullet_{*}$ | $\bullet_{\natural*}$ |
|---|---|---|---|---|
| Jordan identity | yes | no | no | no |
| defect of the identity | $0$ | $1$ | $1$ | $4$ |
| image | $\mathbb{B}$ | $\mathbb{R}e_t$ | $\mathbb{R}e_t$ | $\mathbb{B}$ |
| unit | $e_t$ | none | none | none |
| cone of squares in $\mathbb{B}_{\Psi}$ | $t\geq\lvert\vec s\rvert$ | $\mathbb{R}e_t$ | $\mathbb{R}_{\geq0}e_t$ | $\mathbb{R}e_t$ |
| JB-algebra | yes | no | no | no |

**The two columns with a central image are forms and not algebras.** $\bullet_{\natural}$ and $\bullet_{*}$ take values in a one-dimensional space, so they are scalar-valued products, and a scalar-valued product cannot be a Jordan algebra of the space: the square of an element is a scalar and the Jordan identity is not even formulable on the image. The corpus records the same fact as the collapse of the cone of squares to a ray.

**The fourth column is not central and is still not a Jordan algebra.** $\bullet_{\natural*}$ has the whole algebra as image and no unit, and its defect of dimension four is the largest of the four. It is the column that shows the identity to be a genuine condition and not a consequence of having a large image.

## What the Identification Buys

**The classification, without a new check.** A finite-dimensional JB-algebra is a formally real Jordan algebra, and the classification of those is a theorem. The biquaternion block occupies one entry of it, of dimension four and degree two, and nothing else of that dimension and degree exists. The consequence is that a question about the cone, the order or the states of $\mathbb{B}_{\Psi}$ is a question about $H_2(\mathbb{C})$, and the answer is in the literature.

**The order.** The three objects of the order — the cone, the order unit, the order-unit norm — are one object read three ways, and the corpus already uses two of the three without naming them, in the effect interval and the trace-one slice of the physics corpus.

**The rigidity of the causal maps.** The result of *Causality and the Light Cone as an Information Barrier in Biquaternionic Form*, that a causal bijection of Minkowski space is a Lorentz map composed with a translation and a positive dilation, is the automorphism theorem for a symmetric cone. The cone's structure group is the congruence group of the previous section, and the theorem that a cone-preserving bijection is in that group is the Koecher–Vinberg statement. The physics article proves the result directly; the Jordan reading supplies the reason it holds and the classification of the maps.

**The states and the Born weight.** A state is a positive functional normalised at the order unit, and a pure state is an extreme point. Both sentences are theorems here and definitions in the physics corpus, and the identification of the two vocabularies is the content of the two sections above.

**The step of the quadratic map.** *The Quadratic Map and the Singular Sets* observes that the differential of the square is an anticommutator and that no one-parameter group has it as a time-one map. The Jordan identity gives the positive statement beside the negative one: $[L(\tilde Q),L(\tilde Q^{2})]=0$, so the linearisations of all iterates at a fixed element commute and are simultaneously diagonalisable. The step has no generator, and it has a family of commuting operators, which is what stands in place of a generator.

## What the Identification Does Not Buy

**No formal reality for $\mathbb{B}$.** The algebra $\mathbb{B}$ contains nilpotents, so a sum of squares can vanish with nonzero terms, and no cone of squares of the whole algebra is pointed. Only $\mathbb{B}_{\Psi}$ is formally real. Every statement of this article about a cone is a statement about the Hermitian subspace.

**No dynamics.** A JB-algebra is an order and a norm. It supplies no time, no generator and no evolution, and nothing above reads one.

**No fifth form.** The order-unit norm is a norm and not a form; it is not a bilinear pairing and it has no polarisation. The count of four forms stands.

**No claim about the other symmetrisations.** The three companions are excluded by their defects, and the exclusion is the whole of what this article says about them.

## Summary

The Hermitian subspace $\mathbb{B}_{\Psi}$ with the symmetrised plain product is the Jordan algebra $H_2(\mathbb{C})$, equivalently the spin factor $JSpin_3$: simple, of degree two, special, of dimension four. Its product is $(te_t+i\vec s)\bullet(ue_t+i\vec v)=(tu+\vec s\cdot\vec v)e_t+i(t\vec v+u\vec s)$, its square is $(t^{2}+\lvert\vec s\rvert^{2})e_t+2it\vec s$, its spectrum is $t\pm\lvert\vec s\rvert$, and its determinant is the quaternionic norm $N$.

The order unit is $e_t$, the cone of squares is the Lorentz cone $t\geq\lvert\vec s\rvert$, and the order-unit norm is $\lvert t\rvert+\lvert\vec s\rvert$, which is the operator norm of the matrix display and is not the corpus's Euclidean norm $\sqrt H$. The cone is self-dual for the trace form and homogeneous under the congruence $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{*}$, hence symmetric.

The three JB-algebra axioms hold, so $\mathbb{B}_{\Psi}$ is a JB-algebra, and $\mathbb{B}$ with the star and the operator norm is a JB\*-algebra. The Euclidean norm is not a JB\*-norm, and the axiom fails at $e_t+i\vec u$ with $\lvert\vec u\rvert=1$. The states are the density matrices, the pure states are the rank-one idempotents $\tfrac12(e_t+i\vec u)$ on the sphere, and the defect of a candidate idempotent is the central scalar $\tfrac14(\lvert\vec u\rvert^{2}-1)e_t$.

The light cone is the zero set of the determinant on the material sector, and it is the image under multiplication by $i$ of the two nappes of the boundary of the cone of squares. The three other symmetrisations are not Jordan algebras, so they carry no JB-structure, and the count of JB-algebras among the four symmetrisations is the count of Lie algebras among the four antisymmetrisations: one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}_{\Psi}$ | the Hermitian subspace, $te_t+i\vec s$ with $t,\vec s$ real |
| $\mathbb{B}_{\Phi}$ | the anti-Hermitian subspace, the material sector, $iq'_te_t+\vec q$ |
| $\tilde Q_1\bullet\tilde Q_2$ | the symmetric plain product, the Jordan product |
| $C$ | the cone of squares, the Lorentz cone $t\geq\lvert\vec s\rvert$ |
| $\lVert\cdot\rVert_{u}$ | the order-unit norm of the order unit $e_t$, equal to $\lvert t\rvert+\lvert\vec s\rvert$ |
| $\lVert\cdot\rVert_{\mathrm{op}}$ | the operator norm of the matrix display, equal on $\mathbb{B}_{\Psi}$ to the order-unit norm |
| $\sqrt{H}$ | the corpus's Euclidean norm, not a JB-norm |
| $N=\langle\cdot\rangle_{\natural}$ | the determinant of the Jordan algebra |
| $\langle\cdot,\cdot\rangle_{*}$ | the Hermitian form on $\mathbb{B}_{\Psi}$, half the Hermitian pairing |
| $U_{\tilde Q}$ | the quadratic representation, $U_{\tilde Q}\tilde P=\tilde Q\tilde P\tilde Q$ |
| $\{x,y,z\}$ | the Jordan triple product, complex-bilinear |
| $\{x,y,z\}_{\mathrm{C}^{*}}$ | the C\*-triple product, conjugate-linear in the middle slot |
| $\tilde\Pi=\tfrac12(e_t+i\vec u)$ | a rank-one idempotent, a pure state at $\lvert\vec u\rvert=1$ |
| $H_2(\mathbb{C})\cong JSpin_3$ | the two names of the algebra |

## Further Reading

- [The Jordan Structure of the Symmetric Plain Product](the-jordan-structure-of-the-symmetric-plain-product.html), for the identity, the Peirce theory and the quadratic representation of the algebra read algebraically.
- [Jordan Algebras and the Positive Cone](jordan-algebras-and-the-positive-cone.html), for the cone, the order unit, the order-unit norm and the JB-algebras in general.
- [JB\*-Algebras and the Gelfand–Naimark Theorem](jb-star-algebras-and-the-gelfand-naimark-theorem.html), for the complex class and the representation theorem.
- [Spin Factors and the Clifford Envelope with Inner Conjugation](spin-factors-and-the-clifford-envelope-with-inner-conjugation.html), for $H_2(D)\cong JSpin_{1+\dim_{\mathbb{R}}D}$ and the envelope $M_2(\mathbb{C})=\mathbb{B}$.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the four forms, which are not the order-unit norm.
- [The Hermitian Jordan Algebra](the-hermitian-jordan-algebra.html), for the symmetrisation of a sesqualgebra, which is the general construction behind the closure of $\mathbb{B}_{\Psi}$.
- [The Light Cone as the Biquaternion Zero-Divisor Cone](../articles_physics/the-light-cone-as-the-biquaternion-zero-divisor-cone.html), for the identification of the null set with the zero divisors, which the determinant reproduces.
- [States, Observables and the Born Weight](../articles_physics/states-observables-and-the-born-weight.html), for the state space, the effect interval and the Born pairing read physically.
