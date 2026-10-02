
# __The Involution on the Algebra of Random Variables__

## Introduction

The algebra of random variables carries a single involution, the complex conjugation of the random variable,
$$
x^*=\bar x ,
$$
and the involution is the structure that turns the algebra into a probability theory: it selects the **real random variables** as its fixed elements, it defines the positive elements as the squares of the real ones, and it makes the expectation a **state**, positive and faithful. This article is the `*` theory of the algebra of random variables. It defines the involution, identifies the real random variables, records the decomposition of an element into a real and an imaginary part, the modulus and the positive cone, describes the algebra as a commutative von Neumann algebra with its Gelfand description and its lattice-ordered self-adjoint part, and derives the spectral theory of a real random variable, its spectral measure and its distribution.

The conventions are those fixed for the category in *The Signed Sandwich on the Algebra of Random Variables*, earlier in this category: $\mathcal{A}=L^\infty(\Omega,\mathcal F,\mathbb P)$ with the pointwise product, the conjugation $x^*=\bar x$, the state $\varphi(x)=\mathbb E[x]$ and the form of the category $\langle x,y\rangle=\varphi(xy^*)$. The non-commutative generalization, where the algebra is not assumed commutative, is *Non-Commutative Probability and the Involutive Algebra of Random Variables*, earlier in this category, and the present article is its commutative case. The state, the positivity, the form and the realness here are the ones used throughout the category; the covariance of the form is *The Covariance Function and Hermitian Positivity*, later in this category, and the conjugate symmetry of the Fourier transform of the law is *The Characteristic Function and Conjugate Symmetry*, later in this category. The involution on the algebra of arithmetic functions, which has the same formula on the values and a different product, is *The Involution on the Algebra of Arithmetic Functions*, written, and the conjugations of the number systems are *Conventions in Mathematics*, written. The operator-algebraic background, the Gelfand duality, the von Neumann algebras, the positive functionals and the spectral theorem are *Operator Algebras*, written. No physics is invoked.

Throughout, $(\Omega,\mathcal F,\mathbb P)$ is a probability space, $\mathcal{A}=L^\infty(\Omega,\mathcal F,\mathbb P)$ is the algebra of $\mathbb P$-classes of bounded complex random variables with
the pointwise product, the unit $1$ and the conjugation $x^*=\bar x$, the state is $\varphi(x)=\mathbb E[x]$, the form is $\langle x,y\rangle=\varphi(xy^*)$ on $\mathcal{H}=L^2(\Omega,\mathbb P)$, and the norm of $\mathcal{A}$ is the essential supremum $\|x\|_\infty$. The self-adjoint elements are written $\mathcal{A}_{sa}$ and the positive ones $\mathcal{A}_+$, and the real part and the imaginary part of $x$ are written $\Re x$ and $\Im x$.

## The Involution

### Definition and first properties

**Definition.** The **involution** of the algebra of random variables is the complex conjugation
$$
\mathcal{A}\to\mathcal{A},\qquad x\mapsto x^*=\bar x .
$$

**Theorem.** The conjugation is an involutive, isometric, conjugate-linear anti-automorphism of $\mathcal{A}$:
$$
(x^*)^*=x,\qquad (x+y)^*=x^*+y^*,\qquad (\lambda x)^*=\bar\lambda\,x^*,\qquad (xy)^*=y^*x^*=x^*y^* ,
$$
it commutes with the product because the algebra is commutative, it satisfies $\|x^*\|_\infty=\|x\|_\infty$, and it is isometric for the form, $\langle x^*,y^*\rangle=\overline{\langle y,x\rangle}$.

*Proof.* Each identity is the corresponding property of the conjugation of complex numbers, applied pointwise; the compatibility with the product is $\overline{xy}=\bar x\bar y$ in the commutative algebra, and the isometry is $|\bar x|=|x|$. The last identity is the anti-linearity of the form.

### The real and the imaginary parts

**Definition.** An element $x$ is **self-adjoint** (or **real**) if $x^*=x$. The **real part** and the **imaginary part** are
$$
\Re x=\tfrac12(x+x^*),\qquad \Im x=\tfrac{1}{2i}(x-x^*).
$$

**Theorem (the decomposition).** Every $x\in\mathcal{A}$ has the unique decomposition
$$
x=\Re x+i\,\Im x,\qquad \Re x,\ \Im x\in\mathcal{A}_{sa},
$$
and $x$ is self-adjoint exactly when $\Im x=0$; the self-adjoint elements are exactly the real-valued random variables, $\mathcal{A}_{sa}=L^\infty(\Omega,\mathcal F,\mathbb P;\mathbb{R})$, and they form a real linear subspace of $\mathcal{A}$ with $\mathcal{A}=\mathcal{A}_{sa}\oplus i\mathcal{A}_{sa}$.

*Proof.* The conjugate of $\Re x$ is $\frac12(\bar x+x)=\Re x$, so the real part is self-adjoint, and the same for the imaginary part; the sum reconstructs $x$; the uniqueness is the directness of the sum, proved by taking the conjugate of $a+ib=c+id$ with $a,b,c,d$ self-adjoint, which gives $b=d$. An element of $L^\infty$ is fixed by the conjugation exactly when it is real-valued.

**Theorem (the realness criterion).** An element $x$ is self-adjoint if and only if $\|x-x^*\|_2=0$, that is if and only if $\varphi\bigl((x-x^*)^2\bigr)=0$.

*Proof.* The form is positive definite, $\langle z,z\rangle=\mathbb E|z|^2=0$ implying $z=0$, because a nonzero square-integrable function has a positive integral of its square; hence $x-x^*=0$ is equivalent to the vanishing of its norm, and $x-x^*=0$ is the self-adjointness.

### The positive elements and the modulus

**Definition.** An element is **positive**, written $x\ge0$, if $x=y^*y$ for some $y\in\mathcal{A}$; the **modulus** of $x$ is $|x|=(x^*x)^{1/2}$, the square root taken in $\mathcal{A}$.

**Theorem (the positive cone).** $\mathcal{A}_+=\{x^*x:x\in\mathcal{A}\}=\{y^2:y\in\mathcal{A}_{sa},\ y\ge0\}$ is a convex cone, closed under addition, and $x\ge0$ exactly when $x$ is real and $x(\omega)\ge0$ for $\mathbb P$-almost every $\omega$. The cone is proper, $\mathcal{A}_+\cap(-\mathcal{A}_+)=\{0\}$, and it defines a partial order on $\mathcal{A}_{sa}$.

*Proof.* The identity $x^*x=|x|^2$ is the product of the conjugate and the element, and it is a nonnegative function; conversely a real nonnegative $y$ is the square of its real nonnegative square root, so the two descriptions of $\mathcal{A}_+$ coincide. The closure under addition is the pointwise inequality, and the properness is the faithfulness of the pointwise order.

**Theorem (the polar decomposition).** Every $x$ factors as
$$
x=u\,|x|,\qquad u\in\mathcal{A},\qquad |u|=1\ \text{on }\{|x|>0\},\qquad u=\mathrm{sgn}\,x ,
$$
and $u$ is unitary in $\mathcal{A}$, $u^*u=uu^*=1$, exactly when $x$ is invertible; in general $u$ is unitary on the closure of the support of $x$. The modulus is described by $|x|^2=x^*x$.

*Proof.* The sign $u$ is the function equal to $x/|x|$ where $x\ne0$ and to $1$ else; then $u|x|=x$, and $|u|=1$ wherever $|x|>0$. The unitarity off the zeros of $x$ is the identity $u^*u=|u|^2=1$ there, and the global unitarity is the invertibility of $x$.

## The Algebra, the State and the Form

### The state and the GNS form

**Theorem (the state).** The expectation $\varphi(x)=\mathbb E[x]$ is a state:
$$
\varphi(1)=1,\qquad \varphi(x^*x)=\mathbb E[|x|^2]\ge0,\qquad \varphi(x^*)=\overline{\varphi(x)},
$$
and it is **faithful**: $\varphi(x^*x)=0$ implies $x=0$. The associated form $\langle x,y\rangle=\varphi(xy^*)$ is a genuine inner product on $\mathcal{H}=L^2(\Omega,\mathbb P)$, it is invariant under the involution, and the left multiplication satisfies $L_a^*=L_{a^*}$.

*Proof.* The positivity and the unitality are the properties of the expectation; the faithfulness is the vanishing of $\mathbb E|z|^2$ implying $z=0$; the invariance of the form and the adjoint identity are those of *The Signed Sandwich on the Algebra of Random Variables*, earlier in this category, and they hold because the state is tracial in the commutative algebra. The positivity and the faithfulness are exactly the hypothesis the non-commutative theory of *Non-Commutative Probability and the Involutive Algebra of Random Variables*, earlier in this category, must impose.

### The lattice-ordered self-adjoint part

**Theorem.** The self-adjoint part $\mathcal{A}_{sa}$ is a lattice: for real $x,y$ the pointwise maximum and minimum
$$
(x\vee y)(\omega)=\max\{x(\omega),y(\omega)\},\qquad (x\wedge y)(\omega)=\min\{x(\omega),y(\omega)\}
$$
belong to $\mathcal{A}_{sa}$, and
$$
x\vee y=\tfrac12(x+y+|x-y|),\qquad x\wedge y=\tfrac12(x+y-|x-y|).
$$
The algebra $\mathcal{A}$ is a commutative von Neumann algebra, hence a commutative $C^*$-algebra, and its self-adjoint part is the lattice-ordered real vector space of the bounded real random variables with the order generated by the cone $\mathcal{A}_+$.

*Proof.* The pointwise maximum and minimum of two bounded measurable functions are bounded and measurable; the displayed identities are the usual formulas with the modulus, and $|x-y|$ is in $\mathcal{A}_{sa}$. The von Neumann algebra structure is *Operator Algebras*.

### The Gelfand description

**Theorem (Gelfand).** As a commutative $C^*$-algebra $\mathcal{A}=C(\Omega_{\mathcal{A}})$ for the compact Hausdorff space $\Omega_{\mathcal{A}}$ of the characters, and the involution becomes the complex conjugation of the functions on $\Omega_{\mathcal{A}}$; the probability measure $\mathbb P$ corresponds to the state $\varphi$ by integration, $\varphi(x)=\int_{\Omega_{\mathcal{A}}}\hat x\,d\nu$, and $\nu$ is a Baire probability measure on $\Omega_{\mathcal{A}}$.

*Proof.* The Gelfand duality represents a commutative $C^*$-algebra as the algebra of continuous functions on its character space, and the self-adjoint elements correspond to the real-valued functions; the state is a positive functional, hence a measure by the Riesz representation. The correspondence is the probabilistic form of the Gelfand–Naimark theorem.

## The Spectral Theory of a Real Random Variable

### The spectral measure

**Theorem (the spectral theorem).** Let $x\in\mathcal{A}_{sa}$. There is a unique **spectral measure** $E_x$, a projection-valued measure on the Borel sets of the spectrum $\operatorname{spec}(x)\subseteq\mathbb{R}$, with
$$
x=\int_{\mathbb{R}}t\,dE_x(t),\qquad f(x)=\int_{\mathbb{R}}f(t)\,dE_x(t)
$$
for every bounded Borel $f$ on the spectrum, and the functional calculus $f\mapsto f(x)$ is a unital $*$-homomorphism of the bounded Borel functions onto the closed algebra generated by $x$.

*Proof.* Since $\mathcal{A}$ is commutative, the closed unital algebra generated by the single self-adjoint $x$ is a commutative $C^*$-algebra isomorphic to $C(\operatorname{spec}(x))$, the isomorphism sending $x$ to the coordinate function $t\mapsto t$; the spectral measure is the corresponding projection-valued measure, and the functional calculus is the isomorphism. The general statement is *Operator Algebras*; in the present model it is the multiplication by $x(\omega)$ together with the distribution of $x$.

### The distribution

**Theorem (the distribution of a real random variable).** Let $x\in\mathcal{A}_{sa}$ and let $\mu_x$ be the law of the random variable $x$, $\mu_x(A)=\mathbb P(x\in A)$. Then
$$
\varphi(f(x))=\mathbb E[f(x)]=\int_{\mathbb{R}}f\,d\mu_x
$$
for every bounded Borel $f$, the moments are $\varphi(x^n)=\int t^n\,d\mu_x$, and $\mu_x$ is the scalar measure $\langle E_x(\cdot)\mathbf 1,\mathbf 1\rangle$ of the spectral measure.

*Proof.* The first identity is the change of variables in the integral defining the expectation, and the second is its specialisation to $f(t)=t^n$; the last is the identification of the scalar spectral measure with the law of $x$, since $\varphi(E_x(A))=\mathbb P(x\in A)$.

## Comparison with the Other Involutions

**Theorem (comparison).** The involution on the algebra of random variables, $x\mapsto\bar x$, is the **pointwise** complex conjugation, in this respect the same formula as the coefficient involution on the algebra of arithmetic functions of *The Involution on the Algebra of Arithmetic Functions*, written; the difference between the two theories is not in the involution but in the product, the pointwise product here and the Dirichlet convolution there. The involution here is also the one used by the signed operators of *The Signed Sandwich on the Algebra of Random Variables*, earlier in this category, whose grade involution $\alpha$ is a second involutive automorphism commuting with it, and their composite $\delta=\sigma\alpha$ is the twisted involution of that theory.

*Proof.* The identity of the two involutions on the values is the definition; the difference of the products is the difference of the algebras; the commutation of the conjugation with the grade involution and the definition of $\delta$ are recorded in the earlier article.

## Worked Examples

**Example (the two-atom algebra).** Let $\Omega=\{\omega_-,\omega_+\}$ with $\mathbb P(\omega_\pm)=\frac12$. Then $\mathcal{A}\cong\mathbb{C}^2$ with $\bar x=(x_-^*,x_+^*)$, $\mathcal{A}_{sa}\cong\mathbb{R}^2$ with the pointwise order, $\varphi(x)=\frac12(x_-+x_+)$, and the form is the Euclidean form of $\mathbb{C}^2$ up to the factor $\frac12$. The spectral measure of a real $x=(x_-,x_+)$ is the sum of the two point masses at the values $x_\pm$ with weights $\frac12$.

**Example (the circle).** Let $\Omega=\mathbb R/\mathbb Z$ with the Lebesgue measure. The function $x(\theta)=\cos(2\pi\theta)$ is self-adjoint, its distribution is the arcsine law, $\frac{1}{\pi\sqrt{1-t^2}}$ on $[-1,1]$, its spectral measure is the push-forward of the Lebesgue measure under the cosine, and the functional calculus sends a bounded Borel $f$ to the function $f(\cos(2\pi\theta))$.

**Example (the modulus and the sign).** For $x(\omega)$ vanishing on a set of positive probability the polar decomposition $x=u|x|$ has $u=\mathrm{sgn}\,x$ unitary only off the zero set; the failure of the unitarity is the failure of the invertibility. The modulus provides the lattice operations, $x\vee y=\frac12(x+y+|x-y|)$, and the positivity of the cone is the pointwise positivity of the function.

**Example (the state of the arithmetic case is not tracial).** In the algebra of arithmetic functions the coefficient involution $\sigma(f)(n)=\overline{f(n)}$ is the same conjugation, but the augmentation $\varphi(f)=f(1)$ is a state whose form is not invariant under the translations, and the positivity of the state has a different content; the comparison isolates the role of the product and shows that the involution alone does not give the probability.

## Failure of the Degenerate Cases

The involution degenerates in four configurations. First, the involution is the identity on the real part but the algebra $\mathcal{A}$ is genuinely complex only when there are complex-valued random variables; on a trivial probability space the algebra is $\mathbb{C}$, the involution is the conjugation of the scalars, and the `*` theory is one-dimensional. Second, the faithfulness of the state is special: for a general positive functional the form is only semi-definite and the involution does not separate the elements; the commutative algebra with the expectation is faithful, and the non-commutative theory must impose the faithfulness explicitly. Third, the self-adjoint part is a lattice here because the algebra is commutative and the order is pointwise; this is the lattice-ordered structure available in the commutative case and it fails for the non-commutative random variables, where the maximum of two self-adjoint elements need not exist. Fourth, the involution and the grade involution of the signed theory commute and are distinct; treating them as one structure is the error the corpus forbids, and the twisted composite $\delta=\sigma\alpha$ is the object that mixes them.

## Summary

The involution of the algebra of random variables $\mathcal{A}=L^\infty(\Omega,\mathcal F,\mathbb P)$ is the complex conjugation $x^*=\bar x$, an involutive, isometric, conjugate-linear anti-automorphism that is an automorphism because the algebra is commutative. Its fixed elements are the **real random variables**, $\mathcal{A}_{sa}=L^\infty(\Omega,\mathbb P;\mathbb{R})$, every element decomposes uniquely as $x=\Re x+i\,\Im x$ with self-adjoint parts, the realness is equivalent to the vanishing of $\|x-x^*\|_2$, and the positive elements $x=y^*y$ form a proper convex cone with the modulus $|x|=(x^*x)^{1/2}$ and the polar decomposition $x=u|x|$. The expectation is a faithful state, the form $\langle x,y\rangle=\varphi(xy^*)$ is a genuine inner product, and the involution is invariant under it; the self-adjoint part is a lattice with $x\vee y=\frac12(x+y+|x-y|)$, the algebra is a commutative von Neumann algebra, and its Gelfand description is the algebra of continuous functions on the character space with the conjugation. The spectral theorem gives every real $x$ a spectral measure and the functional calculus, and the law of $x$ is the scalar spectral measure with the moments $\varphi(x^n)$. The non-commutative generalization is *Non-Commutative Probability and the Involutive Algebra of Random Variables*, the covariance is *The Covariance Function and Hermitian Positivity*, and the conjugate symmetry of the Fourier transform is *The Characteristic Function and Conjugate Symmetry*, both later in this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $x^*=\bar x$ | the involution, complex conjugation |
| $\mathcal{A}_{sa}$ | the self-adjoint (real) random variables |
| $\Re x=\frac12(x+x^*)$, $\Im x=\frac{1}{2i}(x-x^*)$ | real and imaginary parts |
| $\varphi(x)=\mathbb E[x]$ | the state, faithful |
| $\langle x,y\rangle=\varphi(xy^*)$ | the form of the category |
| $|x|=(x^*x)^{1/2}$, $x=u|x|$ | modulus and polar decomposition |
| $\mathcal{A}_+=\{x^*x\}$ | the positive cone |
| $x\vee y=\frac12(x+y+|x-y|)$ | the lattice operations |
| $E_x$, $x=\int t\,dE_x(t)$ | the spectral measure of a real $x$ |
| $\mu_x(A)=\mathbb P(x\in A)$ | the law of $x$ |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, Vol. I (Academic Press, 1983), for the involutions, the states, the positivity and the spectral theorem.
- Jacques Dixmier, *C*-Algebras* (North-Holland, 1977), for the Gelfand duality, the commutative $C^*$-algebras and the functional calculus.
- Masamichi Takesaki, *Theory of Operator Algebras I* (Springer, 1979), for the von Neumann algebras, the faithful states and the modular structure.
- Patrick Billingsley, *Probability and Measure* (Wiley, 3rd edition, 1995), for the random variables, the distributions and the expectation as a positive functional.
- William Arveson, *An Invitation to C*-Algebras* (Springer, 1976), for the self-adjoint operators, the spectral measures and the order structure.
