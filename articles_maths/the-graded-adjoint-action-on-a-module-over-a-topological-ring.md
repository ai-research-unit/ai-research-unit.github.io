
# __The Graded Adjoint Action on a Module over a Topological Ring__

## Introduction

A graded action of a ring on a module is an action twisted by the grading, and on a topological ring with a grade involution and an involution it is read with the adjoint as follows: the module carries a continuous parity operator $\pi$, the twisted multiplication is $r\star m = r\cdot\pi(m)$, and the adjoint of the twisted left multiplication is again a twisted left multiplication, $\bigl(\ell_r^\pi\bigr)^\dagger = \ell_{\delta(r)}^\pi$ with $\delta = \sigma\alpha$, exactly when the parity operator is self-adjoint for the form and semilinear for the action, that is $\pi(r\cdot m) = \alpha(r)\cdot\pi(m)$. The article closes the operator theory group by lifting the one-sided adjoint of the previous article from the regular module to an arbitrary topological module, proving the compatibility of the graded adjoint action with the involution, identifying the `*`-representation it defines, and reading the homogeneous case, where the parity operator is the sign change and the even part is its fixed module.

The article assumes the graded action, the twisted action, the parity operator and the semilinearity relation from *The Graded Action on a Module over a Topological Ring*; the topological module, the continuous linear operators and the strong topology from *Topological Modules and their Operators* and *Operators on a Topological Module*; the twisted multiplication $\ell_r^\pi$ from *The Graded Action on a Module over a Topological Ring* and the one-sided adjoint from *The Signed Adjoint of the Left Multiplication on a Topological Ring*; the involution, the grade involution, the semilinearity and the fixed subring from *Involutive Topological Rings and Fields*; the sesquilinear form and the adjoint from *The Involution on Bounded Operators of a Ring*; and the Hermitian form from *The Adjoint under a Hermitian Valuation* in the valued case.

Throughout, $R$ is a Hausdorff topological ring with a continuous involution $\sigma$ and a continuous grade involution $\alpha$ commuting with $\sigma$; $\delta = \sigma\alpha$; $M$ is a Hausdorff topological $R$-module with a continuous **parity operator** $\pi$, an involutive additive homeomorphism with $\pi^2 = \mathrm{id}$ and the semilinearity $\pi(r\cdot m) = \alpha(r)\cdot\pi(m)$; $B$ is a continuous sesquilinear form on $M$ with the adjoint $T^\dagger$ defined by $B(Tm,n) = B(m,T^\dagger n)$; the **graded (twisted) action** is

$$
r\star m = r\cdot\pi(m) , \qquad \ell_r^\pi(m) = r\cdot\pi(m) ;
$$

and the module is **graded**, $M = M^0\oplus M^1$, when $\pi$ is the sign change of the homogeneous parts.

## The Graded Adjoint Action

**Theorem (the parity operator and the form).** If the parity operator is self-adjoint for the form,

$$
B(\pi m, n) = B(m, \pi n) ,
$$

and the operators $L_r(m) = r\cdot m$ have adjoints $L_r^\dagger = L_{\sigma(r)}$ for the action, then the twisted multiplication has adjoint

$$
\bigl(\ell_r^\pi\bigr)^\dagger = \ell_{\delta(r)}^\pi , \qquad \delta = \sigma\alpha ,
$$

so the graded adjoint action is the graded action with the parameter replaced by its $\delta$-image, and the adjoint operation is an involution on the class of twisted left multiplications.

**Proof.** $\ell_r^\pi = L_r\circ\pi$, so $(\ell_r^\pi)^\dagger = \pi^\dagger L_r^\dagger = \pi L_{\sigma(r)}$ by the self-adjointness of $\pi$ and the module adjoint formula. Applying this to $m$ gives $\pi(\sigma(r)\cdot m)$; the semilinearity of $\pi$ gives $\pi(\sigma(r)\cdot m) = \alpha(\sigma(r))\cdot\pi(m) = \delta(r)\cdot\pi(m) = \ell_{\delta(r)}^\pi(m)$. The double adjoint is immediate from $\delta^2 = \mathrm{id}$ and $\pi^2 = \mathrm{id}$.

**Remark (the role of the two hypotheses).** Both hypotheses are used and each is indispensable: without the self-adjointness of $\pi$ the adjoint of the twist is not the twist of the adjoint, and without the semilinearity $\pi(rm) = \alpha(r)\pi(m)$ the adjoint of the twisted multiplication is not a twisted multiplication at all, but a composite of the action, the parity operator and the involution.

**Corollary (the regular module).** For $M = R$ with the regular action, $\pi = \alpha$ and $B$ the form of the category, the theorem is $\ell_r^\dagger = \ell_{\delta(r)}$ of *The Signed Adjoint of the Left Multiplication on a Topological Ring*; the graded adjoint action on the regular module is the signed adjoint action of the previous article.

**Proof.** Substitute $M = R$, $\pi = \alpha$ and $L_r = L_r$; the semilinearity is the defining property of the grade involution and the self-adjointness is $\tau\circ\alpha = \tau$.

**Corollary (the self-adjoint, unitary and involutive twisted multiplications).** The twisted left multiplication satisfies

$$
\bigl(\ell_r^\pi\bigr)^\dagger = \ell_r^\pi \iff \delta(r) = r , \qquad \bigl(\ell_r^\pi\bigr)^\dagger\ell_r^\pi = \mathrm{id} \iff \delta(r)\alpha(r)\in K , \qquad \bigl(\ell_r^\pi\bigr)^2 = \mathrm{id} \iff r\alpha(r)\in K ,
$$

with $K$ the units inducing the grade involution, when the parametrisation is injective; in particular the graded adjoint action is self-adjoint exactly on the parameters fixed by the twist.

**Proof.** The parametrisation is injective when $\pi$ is onto, and the computations are those of *The Signed Adjoint of the Left Multiplication on a Topological Ring* read on the module; the unitarity and involutivity conditions are the module-level composites $\ell_{\delta(r)}^\pi\ell_r^\pi = \ell_{\delta(r)\alpha(r)}^\pi$ and $(\ell_r^\pi)^2 = \ell_{r\alpha(r)}^\pi$.

## Compatibility with the Involution

**Theorem (the `*`-representation).** The graded adjoint action is a `*`-representation of the ring with involution in the involutive algebra of adjointable operators exactly when the parity operator is self-adjoint and the action is semilinear; the involution of the ring acts on the parameters by $\delta = \sigma\alpha$, and the representation is faithful when $\pi$ is onto and the action is faithful.

**Proof.** The map $r\mapsto\ell_r^\pi$ is additive and multiplicative up to the twist by the theorem and the twisted composition law, and the adjoint of the image is the image of the twist, which is the `*`-representation property; the faithfulness is that $\ell_r^\pi = 0$ iff $r\cdot\pi(m) = 0$ for all $m$, that is $r$ acts as zero, so the kernel is the annihilator of the action.

**Corollary (the graded commutator and the sign rule).** On a genuinely graded module the twisted multiplications of homogeneous parameters satisfy the sign rule: the adjoint action of the odd part anticommutes with the parity operator in the sense that

$$
\ell_r^\pi\circ\pi = \pi\circ\ell_{\alpha(r)}^\pi ,
$$

and the even part commutes with $\pi$; the obstruction to associativity of the twisted action is exactly the nonvanishing of the graded commutator on the odd part, as in *The Graded Action on a Module over a Topological Ring*.

**Proof.** $\pi(\ell_r^\pi(m)) = \pi(r\cdot\pi(m)) = \alpha(r)\cdot\pi(\pi(m)) = \alpha(r)\cdot m$, while $\ell_{\alpha(r)}^\pi(\pi(m)) = \alpha(r)\cdot\pi(\pi(m)) = \alpha(r)\cdot m$, so $\pi\ell_r^\pi = \ell_{\alpha(r)}^\pi\pi$; the sign rule for homogeneous $r$ is the statement that this commutation is $(-1)^{|r|}$.

## The Graded Case and the Homogeneous Operators

**Theorem (homogeneity and the fixed module).** When $M = M^0\oplus M^1$ and $\pi$ is the sign change, the parity operator is self-adjoint for the graded form, the twisted multiplication is homogeneous of the same degree as the parameter, the fixed module of $\pi$ is the even part $M^0$, a closed submodule, and the adjoint of a homogeneous twisted multiplication is homogeneous of the same degree; the twisted multiplications by the even parameters form a subalgebra and those by the odd parameters form a subspace shifting the parity.

**Proof.** The sign change is an additive involution fixing $M^0$ and negating $M^1$, hence self-adjoint for a form even on the homogeneous parts; the homogeneity is $r\star M^j\subseteq M^{i+j}$ for $r\in R^i$; the fixed module is closed as the equalizer of the continuous $\pi$ and the identity; the parity of the adjoint is the parity of the parameter because $\delta$, $\alpha$ and $\sigma$ preserve the grading, as in *Involutions of a Graded Ring*.

**Corollary (the duality and the adjoint module).** The adjoint action makes the dual $M^*$ with the transpose action a graded module over the same ring with the twisted parameters; the parity operator of $M^*$ is the transpose of $\pi$, self-adjoint for the dual form, and the twisted multiplications on $M$ and on $M^*$ are adjoint to each other.

**Proof.** The transpose action $(T^{\mathrm t}\varphi)(m) = \varphi(Tm)$ gives $\ell_r^\pi$ on $M^*$ the adjoint $\ell_{\delta(r)}^\pi$ of the operator on $M$, by the defining identity of the adjoint; the parity operator dualises and remains an involution and self-adjoint for the dual form.

## Topological Compatibility and Examples

**Theorem (continuity and closedness).** The parity operator is a continuous involutive homeomorphism, the twisted left multiplications are bounded and continuous for a continuous action, the adjoint map is continuous in the strong topology on the adjointable operators, and the module of fixed points of $\pi$ and the set of self-adjoint twisted multiplications are closed.

**Proof.** The continuity of $\pi$ and of the action gives the boundedness and continuity of $\ell_r^\pi$; the adjoint map is continuous by *The Involution on Bounded Operators of a Ring*; the fixed module is closed as an equalizer, and the self-adjoint parameters are the fixed points of the continuous map $\delta$ read through the continuous injective parametrisation.

**Example (the regular module).** $M = R$, $\pi = \alpha$; the twisted multiplication is the signed left multiplication and the graded adjoint action is $\ell_r^\dagger = \ell_{\delta(r)}$, recovering the previous article.

**Example (the exterior algebra).** $M = \Lambda(V)$ over a field with the usual grading and the parity operator the sign change on the odd part; the twisted multiplication by an odd vector anticommutes with $\pi$ and the even part commutes with it, the sign rule in its simplest form; the adjoint twisted multiplication is by the $\delta$-image.

**Example (the Hermitian module).** $M = R^n$ over a ring with involution and grade involution, with the Hermitian form and the parity operator the conjugate-transpose-compatible sign change; the graded adjoint action is the conjugate transpose of the twisted multiplication, and the unitary twisted multiplications are those with $\delta(r)\alpha(r)$ in the kernel.

**Example (the parity operator on a graded vector space).** $M = V^0\oplus V^1$ over a field, $\pi$ the sign change, $R$ the endomorphism ring or the group algebra of the grading group; the graded adjoint action is the signed action of the endomorphisms on the graded space, and its self-adjoint elements are the endomorphisms commuting with the twist.

**Example (the trivial parity operator).** For $\pi = \mathrm{id}$ the module is evenly graded, the twisted action is the ordinary action, and the graded adjoint action is the adjoint action $L_r^\dagger = L_{\sigma(r)}$ of *The Involution on Bounded Operators of a Ring*; the graded theory degenerates to the untwisted one.

## Summary

A graded action of a topological ring with an involution $\sigma$ and a grade involution $\alpha$ on a topological module with a parity operator $\pi$ admits an adjoint exactly when $\pi$ is self-adjoint for the form and semilinear for the action, $\pi(r\cdot m) = \alpha(r)\cdot\pi(m)$; the adjoint is then the graded adjoint action $\bigl(\ell_r^\pi\bigr)^\dagger = \ell_{\delta(r)}^\pi$ with $\delta = \sigma\alpha$, and the adjoint operation is an involution on the twisted left multiplications. The graded adjoint action is a `*`-representation of the ring with involution in the involutive algebra of adjointable operators, and on a genuinely graded module it obeys the sign rule $\ell_r^\pi\pi = \pi\ell_{\alpha(r)}^\pi$, with the even part commuting and the odd part anticommuting with the parity operator. In the graded case $M = M^0\oplus M^1$ the twisted multiplication is homogeneous of the degree of its parameter, the fixed module is the closed even part, and the dual module carries the transpose graded action. On the regular module the construction is the signed adjoint action of *The Signed Adjoint of the Left Multiplication on a Topological Ring*, and the whole group of operator articles is the adjoint theory of the signed operators of rings and fields.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma$, $\alpha$, $\delta = \sigma\alpha$ | Involution, grade involution, twist |
| $\pi$, $\pi^2 = \mathrm{id}$ | Parity operator of the module |
| $\pi(r\cdot m) = \alpha(r)\cdot\pi(m)$ | Semilinearity of $\pi$ |
| $B(\pi m,n) = B(m,\pi n)$ | Self-adjointness of $\pi$ |
| $r\star m = r\cdot\pi(m) = \ell_r^\pi(m)$ | The graded (twisted) action |
| $\bigl(\ell_r^\pi\bigr)^\dagger = \ell_{\delta(r)}^\pi$ | The graded adjoint action |
| $\delta(r) = r$ | Self-adjoint twisted multiplications |
| $\ell_r^\pi\pi = \pi\ell_{\alpha(r)}^\pi$ | The sign rule |
| $M = M^0\oplus M^1$, $M^\pi = M^0$ | Grading and fixed module |

## Further Reading

- Charles A. Weibel, *An Introduction to Homological Algebra* (Cambridge University Press, 1994), for graded rings and modules and the sign rule of the twisted action.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for graded modules, semilinear operators and the transpose action.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the involutions of a ring acting on a module and the symmetric operators.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the graded involutions and the unitary operators of a graded module.
- Seth Warner, *Topological Fields* (North-Holland, 1989), for the continuous linear operators of a topological module and the strong topology.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the adjoint of a module action, self-adjointness and the `*`-representation.
