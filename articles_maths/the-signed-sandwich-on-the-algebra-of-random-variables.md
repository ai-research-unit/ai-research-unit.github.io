
# __The Signed Sandwich on the Algebra of Random Variables__

## Introduction

Let $\mathcal{A}$ be the algebra of random variables, the commutative unital algebra of the bounded complex random variables on a probability space under the pointwise product, with its complex conjugation and its expectation. The probability gives the algebra a state $\varphi(x)=\mathbb E[x]$, the state gives it the **form of the category** $\langle x,y\rangle=\varphi(xy^*)=\mathbb E[x\,\bar y]$, and the form makes $\mathcal{A}$ a subspace of the Hilbert space $\mathcal{H}=L^2$ of the square-integrable variables. A **grade involution** $\alpha$ is an involutive automorphism of $\mathcal{A}$ commuting with the conjugation, and for fixed $a,b$ the **signed sandwich** is the operator
$$
S^\alpha_{a,b}(x)=a\,\alpha(x)\,b,
$$
obtained from the two-sided multiplication by inserting the grade involution between the two multiplications. This article defines that operator, computes its adjoint with respect to the form of the category, and identifies its self-adjoint, isometric and unitary members.

The two features that decide the shape of the answers are that the product is commutative and that the form is invariant under the conjugation, and they act in opposite directions. The commutativity makes the sandwich depend on $a$ and $b$ only through the product $ab$: the two-sided operator collapses onto a single left multiplication composed with $\alpha$. The invariance of the form makes the involution on the elements and the adjoint on the operators coincide for the unsigned operators, $L_a^*=L_{a^*}$, which is exactly what fails for the algebra of arithmetic functions of *The Signed Sandwich on the Algebra of Arithmetic Functions*, written. The signed adjoint is then the clean formula $S^\alpha_{a,b}\mapsto S^\alpha_{\delta(a),\delta(b)}$ with $\delta=\sigma\alpha$, the formula of the noncommutative case of *The Signed Sandwich on a Ring*, recovered here over a commutative algebra because the two structures agree.

The probabilistic content is fixed elsewhere. The random variables, their laws, the expectation and the $L^p$ spaces are *Measure-Theoretic Probability*, written, and the state used here is its expectation. The involution on the elements is *The Involution on the Algebra of Random Variables*, later in this category, where the complex conjugation and the real random variables are treated; the present article states the involution only to the extent the signed operators need it. The covariance form and its positivity are *The Covariance Function and Hermitian Positivity*, later in this category; the adjoint of the unsigned left multiplication is *The Adjoint of the Left Multiplication on the Algebra of Random Variables*, later in this category; the graded version is *The Graded Action on a Module over the Algebra of Random Variables*, later in this category; and the reflections built from the units are *Reflections as Signed Two-Sided Operators on the Algebra of Random Variables*, next in this category. The noncommutative signed sandwich is *The Signed Sandwich on a Ring*, in Part I. Nothing here reads a distance or a form as an object, and no physics is invoked.

Throughout, $(\Omega,\mathcal F,\mathbb P)$ is a probability space, $\mathcal{A}=L^\infty(\Omega,\mathcal F,\mathbb P)$ is the algebra of $\mathbb P$-classes of bounded complex random variables with the pointwise product, the conjugation $\sigma(x)=\bar x$ and the state $\varphi(x)=\mathbb E[x]$; the form is $\langle x,y\rangle=\varphi(xy^*)$ on $\mathcal{H}=L^2(\Omega,\mathbb P)$, and $\|x\|_2=\langle x,x\rangle^{1/2}$. The grade involution is $\alpha$; it commutes with $\sigma$, and $\delta=\sigma\alpha=\alpha\sigma$ is their composite. The grading is $\mathcal{A}=\mathcal{A}_{\bar0}\oplus\mathcal{A}_{\bar1}$ with $\mathcal{A}_{\bar0}=\ker(\alpha-I)$ the even part and $\mathcal{A}_{\bar1}=\ker(\alpha+I)$ the odd part.

## The Algebra of Random Variables and its Form

### The algebra, the state and the involution

**Definition.** The **algebra of random variables** is $\mathcal{A}=L^\infty(\Omega,\mathcal F,\mathbb P)$ with the pointwise product, the unit $1$, the involution
$$
\sigma(x)=\bar x,
$$
and the state $\varphi(x)=\mathbb E[x]$. The state is positive, $\varphi(x^*x)=\mathbb E[|x|^2]\ge0$, unital, $\varphi(1)=1$, and self-adjoint, $\varphi(x^*)=\overline{\varphi(x)}$. The involution is the complex conjugation, and its fixed elements, $\sigma(x)=x$, are the **real random variables**.

*Proof.* The product is commutative and associative, as the pointwise product of functions; the conjugation is an involutive anti-automorphism, $\bar{xy}=\bar x\bar y$ and $\overline{\bar x}=x$, which is an automorphism because the algebra is commutative; the state is positive and unital as the expectation, and its self-adjointness is $\mathbb E[\bar x]=\overline{\mathbb E[x]}$. The fixed elements are the variables equal to their own conjugate, which are the real-valued ones. The involution and the state are *Measure-Theoretic Probability*, and their operator theory is *The Involution on the Algebra of Random Variables*, later in this category.

### The grade involution and the grading

**Definition.** A **grade involution** is a unital involutive algebra automorphism $\alpha$ of $\mathcal{A}$ that commutes with the conjugation, $\alpha\sigma=\sigma\alpha$, and preserves the state, $\varphi\circ\alpha=\varphi$. In the standard model it is the composition with a measure-preserving involution $\varphi_0$ of $(\Omega,\mathcal F,\mathbb P)$,
$$
\alpha(x)=x\circ\varphi_0,\qquad \varphi_0^2=\mathrm{id},\qquad \varphi_0\text{ preserves }\mathbb P .
$$

**Theorem (properties of the grade involution).** For every grade involution,
$$
\alpha^2=\mathrm{id},\qquad \alpha(xy)=\alpha(x)\alpha(y),\qquad \alpha(1)=1,\qquad \alpha(x^*)=\alpha(x)^*,\qquad \alpha^*=\alpha,
$$
and $\alpha$ is unitary for the form of the category. The grading is $\mathcal{A}=\mathcal{A}_{\bar0}\oplus\mathcal{A}_{\bar1}$ with $\mathcal{A}_{\bar0}=\{x:\alpha(x)=x\}$, $\mathcal{A}_{\bar1}=\{x:\alpha(x)=-x\}$, and $\mathcal{A}_{\bar0}$ is a subalgebra while $\mathcal{A}_{\bar i}\cdot\mathcal{A}_{\bar j}\subseteq\mathcal{A}_{\overline{i+j}}$.

*Proof.* The involution and multiplicativity are those of an automorphism of order two; the unitality is the definition; the compatibility with the conjugation is the commutativity of $\alpha$ and $\sigma$; and the self-adjointness is
$$
\langle\alpha x,y\rangle=\mathbb E[(x\circ\varphi_0)\bar y]=\mathbb E[x(\bar y\circ\varphi_0)]=\langle x,\alpha y\rangle,
$$
where the middle equality is the change of variables under the measure-preserving $\varphi_0$; the unitarity is $\alpha^*\alpha=\alpha^2=\mathrm{id}$. The grading is the eigenspace decomposition of the involution $\alpha$, and the product rule is its multiplicativity: for $x\in\mathcal{A}_{\bar i}$, $y\in\mathcal{A}_{\bar j}$, $\alpha(xy)=\alpha(x)\alpha(y)=(-1)^{i}(-1)^{j}xy=(-1)^{i+j}xy$.

### The form of the category

**Definition.** The **form of the category** is
$$
\langle x,y\rangle=\varphi(xy^*)=\mathbb E[x\,\bar y]\qquad (x,y\in\mathcal{H}=L^2(\Omega,\mathbb P)),
$$
linear in the first argument, conjugate-linear in the second, and positive definite on $\mathcal{H}$.

**Theorem (invariance of the form).** The form is invariant under the conjugation of either argument,
$$
\langle x^*,y\rangle=\langle x,y^*\rangle=\overline{\langle y,x\rangle},
$$
and, for every $a\in\mathcal{A}$, the left multiplication $L_ax=ax$ satisfies
$$
L_a^*=L_{a^*} .
$$
Consequently the involution on the elements and the adjoint on the unsigned operators coincide: the multiplication representation $a\mapsto L_a$ is a $*$-representation of $\mathcal{A}$ on $\mathcal{H}$.

*Proof.* The first identity is the computation $\langle x^*,y\rangle=\mathbb E[\bar xy]=\overline{\mathbb E[x\bar y]}=\overline{\langle y,x\rangle}$. For the second,
$$
\langle L_ax,y\rangle=\mathbb E[ax\bar y]=\mathbb E[x\,\overline{a^*y}]=\langle x,L_{a^*}y\rangle,
$$
because $\overline{a^*y}=\overline{\bar a\,y}=a\bar y$; hence $L_a^*=L_{a^*}$. This is the point at which the algebra of random variables differs from the algebra of arithmetic functions under the coefficient form, where $\Theta_c\ne L_{c^*}$ and the two structures do not coincide.

## The Signed Sandwich

### Definition and the collapse

**Definition.** For $a,b\in\mathcal{A}$ the **signed sandwich** is the operator
$$
S^\alpha_{a,b}:\mathcal{A}\to\mathcal{A},\qquad S^\alpha_{a,b}(x)=a\,\alpha(x)\,b .
$$
The **signed left multiplication** is $T^\alpha_a=S^\alpha_{a,1}$ and the **signed right multiplication** is $U^\alpha_b=S^\alpha_{1,b}$.

**Theorem (the collapse).** On the commutative algebra $\mathcal{A}$,
$$
S^\alpha_{a,b}=L_{ab}\circ\alpha=\alpha\circ L_{\alpha(ab)},
$$
so the sandwich depends on $a$ and $b$ only through the product $ab$, and it factors through the left multiplication by that product. The grading is reversed,
$$
S^\alpha_{a,b}(\mathcal{A}_{\bar i})\subseteq\mathcal{A}_{\overline{\,i+|a|+|b|+1\,}}\qquad(i=0,1).
$$

*Proof.* The commutativity gives $a\alpha(x)b=(ab)\alpha(x)$, which is the first factorisation; the second is $L_{ab}\alpha=\alpha L_{\alpha(ab)}$, obtained by applying $\alpha$ to the product. The grading statement is $\alpha(\mathcal{A}_{\bar i})=\mathcal{A}_{\bar1-i}$ together with the product
rule of the grading.

**Corollary (the sandwich is not two-sided here).** Writing $c=ab$, the sandwich is $S^\alpha_c=L_c\alpha=\alpha L_{\alpha(c)}$, and the two-sided operator carries no information beyond its product. This is the same degeneracy as the arithmetic case and a stronger one: there, the convolution kept the two sides distinguishable inside the factorisation, whereas the pointwise product removes even that.

### The adjoint

**Theorem (the signed adjoint).** With respect to the form of the category, the adjoint of the signed sandwich is
$$
\bigl(S^\alpha_{a,b}\bigr)^*=S^\alpha_{\delta(a),\delta(b)}=\alpha\circ L_{(ab)^*}\qquad\text{with}\quad \delta=\sigma\alpha=\alpha\sigma .
$$
Equivalently $\bigl(S^\alpha_{a,b}\bigr)^*(y)=\alpha\bigl((ab)^*y\bigr)$.

*Proof.* The sandwich is $L_{ab}\alpha$, and the adjoint of a product is the product of the adjoints in reverse order:
$$
\bigl(L_{ab}\alpha\bigr)^*=\alpha^*L_{ab}^*=\alpha L_{(ab)^*},
$$
using $\alpha^*=\alpha$ and $L_c^*=L_{c^*}$ proved above. Since $\alpha L_c=L_{\alpha(c)}\alpha$ and $\delta(ab)=\alpha((ab)^*)$, the second expression is $L_{\delta(ab)}\alpha=S^\alpha_{\delta(a),\delta(b)}$, the last equality being the collapse $S^\alpha_{c,d}=L_{cd}\alpha$ and the multiplicativity $\delta(ab)=\delta(a)\delta(b)$ on a commutative algebra. The explicit expression is the definition of $\alpha L_{(ab)^*}$.

**Corollary (comparison with the two-sided case).** The adjoint is exactly the formula of the noncommutative signed sandwich of *The Signed Sandwich on a Ring*, $S^\alpha_{a,b}\mapsto S^\alpha_{\delta(a),\delta(b)}$, in which the composite $\delta=\sigma\alpha$ is the twisted involution of the ring. The commutativity of $\mathcal{A}$ does not spoil the formula here, because the invariance of the form has already made the adjoint of a left multiplication the left multiplication by the conjugate; the two facts, \(L_c^*=L_{c^*}\) and $\delta=\sigma\alpha$, together produce the clean adjoint.

**Proposition (the adjoint of the collapse is the collapse of the adjoint).** In terms of the product $c=ab$, the adjoint is $\bigl(S^\alpha_c\bigr)^*=\alpha L_{c^*}=S^\alpha_{\delta(c)}$.

*Proof.* This is the theorem with $c=ab$ and $\delta(ab)=\delta(c)$ on the commutative algebra.

### Self-adjointness, isometry and unitarity

**Theorem.** Write $c=ab$. Then
$$
S^\alpha_{a,b}\ \text{is self-adjoint}\iff c=\delta(c)\iff \alpha(c)=c^*,
$$
$$
S^\alpha_{a,b}\ \text{is an isometry}\iff |c|=1,\qquad S^\alpha_{a,b}\ \text{is unitary}\iff |c|=1,
$$
the two conditions coinciding because a multiplication operator on a Hilbert space is an isometry exactly when it is unitary.

*Proof.* Self-adjointness is $L_c\alpha=\alpha L_{c^*}$; writing $\alpha L_{c^*}=L_{\alpha(c^*)}\alpha=L_{\delta(c)}\alpha$, the equality is $L_c=L_{\delta(c)}$ by the collapse, hence $c=\delta(c)$, which is $\alpha(c)=c^*$. An isometry means $(L_c\alpha)^*(L_c\alpha)=\mathrm{id}$; now $(L_c\alpha)^*(L_c\alpha)=\alpha L_{c^*}L_c\alpha=\alpha L_{c^*c}\alpha=L_{\alpha(c^*c)}=L_{|c|^2}$, and this is the identity exactly when $|c|=1$. The computation with the factors in the other order is $(L_c\alpha)(L_c\alpha)^*=L_c\alpha\alpha L_{c^*}=L_{cc^*}=L_{|c|^2}$, the same condition, because $c$ commutes with $c^*$; hence $S^\alpha_c$ is an isometry exactly when it is unitary, and the condition is $|c|=1$.

**Corollary (the involutions and the unitary sandwiches).** $S^\alpha_{a,b}$ is an involution exactly when $c\,\alpha(c)=1$. In particular the unitary involutions among the signed sandwiches are the $S^\alpha_c$ with $|c|=1$ and $c\,\alpha(c)=1$.

*Proof.* $\bigl(S^\alpha_c\bigr)^2=L_c\alpha L_c\alpha=L_cL_{\alpha(c)}\alpha^2=L_{c\alpha(c)}$, which is the identity exactly when $c\alpha(c)=1$. Combined with the unitarity condition $|c|=1$ this gives the second statement.

## Worked Examples

**Example (the swap on two atoms).** Let $\Omega=\{\omega_-,\omega_+\}$ with $\mathbb P(\omega_\pm)=\frac12$ and let $\varphi_0$ interchange the two points, so that $\mathcal{A}\cong\mathbb C^2$ with $\alpha(x_-,x_+)=(x_+,x_-)$. The even part is the diagonal $\{(x,x)\}$ and the odd part is the antidiagonal; the form is $\langle x,y\rangle=\frac12(x_-\bar y_-+x_+\bar y_+)$. For $c=(c_-,c_+)$ the sandwich $S^\alpha_c=L_c\alpha$ is the map $(x_-,x_+)\mapsto(c_+x_+,c_-x_-)$; it is self-adjoint exactly when $c_-=c_+$, that is when $c$ is even, and unitary exactly when $|c_\pm|=1$. The self-adjoint unitary sandwiches are therefore the $S^\alpha_c$ with $c$ even and $|c|=1$, that is $c=(z,z)$ with $|z|=1$, a circle of operators, each the reflection $\alpha$ followed by the multiplication by the unimodular constant $z$; the two of them with $z=\pm1$ are $\pm\alpha$.

**Example (the reflection of the circle).** Let $\Omega=\mathbb R/\mathbb Z$ with the Lebesgue measure and $\varphi_0(\theta)=-\theta$, so that $\alpha(x)(\theta)=x(-\theta)$. The even functions are the symmetric ones and the odd the antisymmetric; the characters split into the cosines and the sines. For $c(\theta)=e^{2\pi i\theta}$ the sandwich $S^\alpha_c$ has $|c|=1$ and $c\,\alpha(c)=e^{2\pi i\theta}e^{-2\pi i\theta}=1$, so it is a unitary involution; its square is the identity and it belongs to the family of the corollary.

**Example (the trivial grading).** For $\alpha=\mathrm{id}$ the grading is $\mathcal{A}_{\bar0}=\mathcal{A}$, $\mathcal{A}_{\bar1}=0$, the sandwich is the unsigned $S^\alpha_{a,b}=L_{ab}$, and the adjoint is $S^\alpha_{a,b}\mapsto L_{(ab)^*}$; self-adjointness is $c=c^*$, that is $c$ real, and unitarity is $|c|=1$. This is the boundary at which the signed theory reduces to the theory of the multiplications.

## Failure of the Degenerate Cases

The signed sandwich degenerates in four configurations, all of them consequences of the commutativity and the invariance of the form. First, the sandwich does not see its two arguments separately: $S^\alpha_{a,b}$ depends only on the product $ab$, so the map $(a,b)\mapsto S^\alpha_{a,b}$ has the same image as the map $c\mapsto S^\alpha_c$ and the two-sided structure is lost. Second, the signed sandwich is never more general than a left multiplication composed with the grade involution; when $\alpha=\mathrm{id}$ it is exactly a left multiplication, and the signed theory adds nothing. Third, the correspondence between self-adjointness and the twisted involution is the equality $c=\delta(c)$, whose solution set is the $\alpha$-Hermitian elements, a proper subset of $\mathcal{A}$ that is a real subspace and not an algebra when $\delta$ is nontrivial. Fourth, the unitary signed sandwiches are parametrised by the unimodular random variables, an infinite-dimensional group, and the phrase "the unitary signed sandwiches are the scalar multiples of $\alpha$" of the arithmetic case has no counterpart here; the difference is the invariance of the form, which makes $L_c$ unitary for every unimodular $c$ rather than only for the scalars.

## Summary

Over the algebra of random variables $\mathcal{A}=L^\infty(\Omega,\mathcal F,\mathbb P)$ with the conjugation $\sigma(x)=\bar x$ and the state $\varphi(x)=\mathbb E[x]$, the form of the category is $\langle x,y\rangle=\varphi(xy^*)$, and it is invariant under the conjugation, so the left multiplication satisfies $L_a^*=L_{a^*}$ and the involution on the elements and the adjoint on the unsigned operators coincide. A grade involution $\alpha$ is a unital involutive $*$-automorphism of $\mathcal{A}$ preserving the state, in canonical form the composition with a measure-preserving involution, and it is self-adjoint and unitary for the form. The signed sandwich $S^\alpha_{a,b}(x)=a\,\alpha(x)\,b$ collapses on the commutative algebra to $S^\alpha_{a,b}=L_{ab}\alpha$, depends only on the product $c=ab$, reverses the grading, and has the adjoint $S^\alpha_{\delta(a),\delta(b)}=\alpha L_{c^*}$ with $\delta=\sigma\alpha$; it is self-adjoint exactly when $c=\delta(c)$, an isometry and unitary exactly when $|c|=1$, and an involution exactly when $c\,\alpha(c)=1$. The comparison with the arithmetic case isolates the two forces: commutativity collapses the sandwich, invariance of the form restores the clean adjoint. The involution itself is *The Involution on the Algebra of Random Variables*, later in this category, the reflections are the next article, the unsigned adjoint is *The Adjoint of the Left Multiplication on the Algebra of Random Variables*, and the graded version is *The Graded Action on a Module over the Algebra of Random Variables*, both later in this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\Omega,\mathcal F,\mathbb P)$, $\mathcal{A}=L^\infty(\Omega,\mathbb P)$ | probability space and algebra of random variables |
| $\sigma(x)=\bar x$, $x^*=\bar x$ | complex conjugation, the involution of the category |
| $\varphi(x)=\mathbb E[x]$ | the state, the expectation |
| $\mathcal{H}=L^2(\Omega,\mathbb P)$ | the Hilbert space of the form |
| $\langle x,y\rangle=\varphi(xy^*)$ | the form of the category |
| $\alpha$, $\varphi_0$ | grade involution; the measure-preserving involution with $\alpha(x)=x\circ\varphi_0$ |
| $\delta=\sigma\alpha=\alpha\sigma$, $\delta(x)=\alpha(x^*)$ | the twisted involution |
| $\mathcal{A}_{\bar0}$, $\mathcal{A}_{\bar1}$ | even and odd parts of the grading |
| $L_a$, $L_a^*=L_{a^*}$ | left multiplication and its adjoint |
| $S^\alpha_{a,b}=a\alpha(x)b=L_{ab}\alpha$ | the signed sandwich and its collapse |
| $\bigl(S^\alpha_{a,b}\bigr)^*=S^\alpha_{\delta(a),\delta(b)}$ | the signed adjoint |
| $S^\alpha_c$ | the collapsed sandwich $L_c\alpha$ |
| $c=\delta(c)$, $|c|=1$, $c\alpha(c)=1$ | self-adjoint, unitary, involutive conditions |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, Vol. I (Academic Press, 1983), for the states, the involutions and the Gelfand–Naimark form of an abelian algebra.
- Masamichi Takesaki, *Theory of Operator Algebras I* (Springer, 1979), for the states, the modular structure and the invariance of the form under the conjugation.
- Jacques Dixmier, *C*-Algebras* (North-Holland, 1977), for the positive functionals, the representations and the adjoints.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the involutions of the first and the second kind and their twisted composites.
- Nicolas Bourbaki, *Éléments de mathématique, Théories spectrales* (Hermann, then Springer), for the commutative involutive algebras and their forms.
