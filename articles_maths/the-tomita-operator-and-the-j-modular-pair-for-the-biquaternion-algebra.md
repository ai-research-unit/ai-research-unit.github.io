# __The Tomita Operator and the J-Modular Pair for the Biquaternion Algebra__

## Introduction

For a Krein–von Neumann algebra $\mathcal{M}$ on a Krein space $K$ and a $J$-cyclic, $J$-separating vector $\xi$, the **Tomita operator** is the antilinear map $S(\Lambda\xi)=\Lambda^{\dagger}\xi$; its polar decomposition $S=\jmath\Delta^{1/2}$ produces the **$J$-modular operator** $\Delta$ and the **$J$-modular conjugation** $\jmath$, and the flow $\sigma_t(\Lambda)=\Delta^{\mathrm{i}t}\Lambda\Delta^{-\mathrm{i}t}$ is the modular group (*The Indefinite Modular Operator*, *Krein–Tomita–Takesaki Theory*). This article computes the operator for the biquaternion algebra.

The computation splits in two, and the split is the content. In the **definite reading**, where the algebra is the finite-dimensional von Neumann algebra $M_2(\mathbb{C})$ with its trace $\mathrm{Sc}$ and $\xi=e_0$, the Tomita operator is the Hermitian star itself, $S(\tilde Q)=\tilde Q^{*}$; it is antiunitary, so the modular operator is the identity, the modular conjugation is the star, and the modular flow is trivial. In the **indefinite reading** the operator is not even definable: the left regular image of the algebra is not closed under the Krein adjoint, since $(L_{\tilde Q})^{\dagger}=R_{\bar{\tilde Q}}$ leaves it (*The Biquaternion Algebra and the Krein–von Neumann Property*), and the envelope that replaces it admits no separating vector. The biquaternion algebra therefore has one modular pair, the definite one, and the indefinite theory sees nothing of it.

The general theory is *The Indefinite Modular Operator*, *Krein–Tomita–Takesaki Theory* and *The Modular Operator and Tomita-Takesaki Theory*; the definite instance of the operator is *The Adjoint of the Left Multiplication on a Hilbert Algebra* and *The Two-Sided Operators and the Modular Conjugation*; the Hilbert structure of the biquaternion algebra is *Hilbert Algebras*, *The Hermitian Form on the Biquaternion Algebra* and *Positivity and the Hermitian Cone of the Biquaternion Algebra with Hermitian Adjoint*; the failure of the indefinite representation is *The Biquaternion Algebra and the Krein–von Neumann Property*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0,e_1,e_2,e_3$, $e_k^{2}=-e_0$, central $i$, and $\tilde Q=\sum_{\mu=0}^{3}Q_\mu e_\mu$. The involution is the Hermitian star ${}^{*}$, the natural conjugation is ${}^{\natural}$, the bar is the coefficient conjugation, and $\mathrm{Sc}$ is the scalar part. The definite form is $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P^{*}\tilde Q)=\sum_\mu P_\mu^{*}Q_\mu$, and the quaternion sesquilinear form is $\langle\tilde Q,\tilde P\rangle_{\natural*}=\mathrm{Sc}(\tilde P^{\natural*}\tilde Q)=\sum_\mu\varepsilon_\mu P_\mu^{*}Q_\mu$ with $\varepsilon=(1,-1,-1,-1)$ and fundamental symmetry $J={}^{\natural}$. The left regular image is $\mathcal{M}=\{L_{\tilde Q}\}$, $L_{\tilde Q}(\tilde S)=\tilde Q\tilde S$, the right regular image is $\mathcal{M}'=\{R_{\tilde Q}\}$. The **modular conjugation** is written $\jmath$ to keep it apart from the fundamental symmetry $J={}^{\natural}$; the general articles write $J$ for the former, and the biquaternion articles write $J$ for the latter.

## The Hilbert Algebra of the Biquaternion Algebra

**Proposition (the Hilbert algebra).** With the involution ${}^{*}$, the trace $\tau=\mathrm{Sc}$ and the form $\langle\tilde P,\tilde Q\rangle=\mathrm{Sc}(\tilde P^{*}\tilde Q)$, the biquaternion algebra is a Hilbert algebra: the form is positive definite and Hermitian, and the adjoint axiom

$$
\langle\tilde Q\tilde S,\tilde T\rangle=\langle\tilde S,\tilde Q^{*}\tilde T\rangle
$$

holds for all $\tilde Q,\tilde S,\tilde T$.

**Proof.** Positive definiteness is $\langle\tilde Q,\tilde Q\rangle=\sum_\mu|Q_\mu|^{2}>0$ for $\tilde Q\neq0$, and Hermitian symmetry is immediate from the coefficient expansion. For the adjoint axiom, $\langle\tilde Q\tilde S,\tilde T\rangle=\mathrm{Sc}((\tilde Q\tilde S)^{*}\tilde T)=\mathrm{Sc}(\tilde S^{*}\tilde Q^{*}\tilde T)$, and the last expression is $\langle\tilde S,\tilde Q^{*}\tilde T\rangle$; the trace property of $\mathrm{Sc}$ is not even needed, associativity alone giving the identity.

**Proposition (the cyclic and separating unit).** Let $\xi=\iota(1)=e_0$. The orbit is $\mathcal{M}\xi=\{\tilde Q e_0\}=\mathbb{B}$, so $\xi$ is cyclic for $\mathcal{M}$, and $L_{\tilde Q}\xi=\tilde Q=0$ forces $\tilde Q=0$, so $\xi$ is separating for $\mathcal{M}$. Hence the Tomita operator of the pair $(\mathcal{M},\xi)$ is defined and densely defined.

**Proof.** $L_{\tilde Q}\xi=\tilde Q$, and the map $\tilde Q\mapsto\tilde Q$ is onto $\mathbb{B}$ and injective. Density is trivial in finite dimension, and separatingness is the injectivity just used.

## The Tomita Operator

**Theorem (the operator is the star).** The Tomita operator of the pair $(\mathcal{M},\xi)$ is

$$
S(\tilde Q\,\xi)=\tilde Q^{*}\xi ,
\qquad\text{that is}\qquad
S(\tilde Q)=\tilde Q^{*}\quad\text{on } \mathbb{B}.
$$

**Proof.** By definition $S(\Lambda\xi)=\Lambda^{*}\xi$ for $\Lambda=L_{\tilde Q}\in\mathcal{M}$, and the definite adjoint of the left multiplication is $L_{\tilde Q}^{*}=L_{\tilde Q^{*}}$ (*The Adjoint of the Left Multiplication on a Hilbert Algebra*). Hence $S(\tilde Q\xi)=L_{\tilde Q^{*}}e_0=\tilde Q^{*}$, as claimed.

**Proposition (elementary properties).** $S$ is antilinear and involutive, $S^{2}=\mathrm{id}$, and it is antiunitary for the definite form,

$$
\langle S\tilde P,S\tilde Q\rangle=\overline{\langle\tilde P,\tilde Q\rangle} ,
\qquad\text{whence}\qquad
\|S\tilde P\|=\|\tilde P\| .
$$

**Proof.** Antilinearity is that of the star. For the involution, $S^{2}(\tilde Q)=(\tilde Q^{*})^{*}=\tilde Q$. For the antiunitarity, using $(Q^{*})_\mu=\varepsilon_\mu\bar Q_\mu$ with $\varepsilon_0=1$ and $\varepsilon_k=-1$,

$$
\langle\tilde P^{*},\tilde Q^{*}\rangle=\sum_\mu (P^{*})_\mu^{*}\,(Q^{*})_\mu=\sum_\mu \varepsilon_\mu^{2}P_\mu\bar Q_\mu=\sum_\mu P_\mu\bar Q_\mu=\overline{\langle\tilde P,\tilde Q\rangle} .
$$

**Corollary (the polar decomposition).** $S=\jmath\Delta^{1/2}$ with

$$
\Delta=\mathrm{id} ,\qquad \jmath=S={}^{*} ,
$$

so the **modular operator is the identity**, the **modular conjugation is the star**, and the modular flow is trivial, $\sigma_t(\Lambda)=\Delta^{\mathrm{i}t}\Lambda\Delta^{-\mathrm{i}t}=\Lambda$ for every $t$.

**Proof.** $S$ is antiunitary, so its polar decomposition is $S=\jmath$ with $\Delta=S^{*}S=\mathrm{id}$; the modular flow is then the identity flow.

**Remark (why the modular operator is trivial).** The modular operator collapses to the identity exactly when the Tomita operator is isometric, equivalently when the vector state is tracial. Here the vector state is

$$
\omega(L_{\tilde Q})=\langle\xi,\tilde Q\rangle=\mathrm{Sc}(\tilde Q)=Q_0 ,
$$

and it is tracial, $\omega(L_{\tilde Q}L_{\tilde R})=(QR)_0=(RQ)_0=\omega(L_{\tilde R}L_{\tilde Q})$, because $\mathrm{Sc}(\tilde Q\tilde R)=\mathrm{Sc}(\tilde R\tilde Q)$; the functional $\mathrm{Sc}$ is the normalised trace of $\mathbb{B}$, $2\,\mathrm{Sc}(\tilde Q)=\mathrm{Tr}\,\Phi(\tilde Q)$ in the matrix model. So the vector state of the unit **is the trace**, and the modular flow of the pair is the identity flow. The triviality is a property of the vector and not of the algebra: $\mathcal{M}\cong M_2(\mathbb{C})$ is a factor whose trace is not the vector state of a general $\xi$, and a cyclic and separating vector other than a scalar multiple of $e_0$ carries a non-tracial vector state and hence a non-trivial modular operator.

## The Modular Conjugation and the Two Sides

**Theorem (the conjugation changes sides).** The modular conjugation exchanges the left and the right multiplications,

$$
\jmath\,L_{\tilde Q}\,\jmath=R_{\tilde Q^{*}} ,
\qquad\text{hence}\qquad
\jmath\,\mathcal{M}\,\jmath=\mathcal{M}' .
$$

**Proof.** For every $\tilde S$, $(\jmath L_{\tilde Q}\jmath)(\tilde S)=(\tilde Q\,\tilde S^{*})^{*}=\tilde S\,\tilde Q^{*}=R_{\tilde Q^{*}}(\tilde S)$; as $\tilde Q$ ranges over $\mathbb{B}$ the right multiplications range over $\mathcal{M}'$, which gives the second identity. This is the commutant theorem of Tomita in the definite case, $\jmath\mathcal{M}\jmath=\mathcal{M}'$, computed on the biquaternion algebra.

**Remark (the definite shadow of an indefinite identity).** The exchange of the sides is the same phenomenon as the indefinite identity $(L_{\tilde Q})^{\dagger}=R_{\bar{\tilde Q}}$ of *J-Self-Adjoint and J-Unitary Operators on the Biquaternion Algebra*, with the star in place of the bar: the definite modular conjugation realizes by an antiunitary operator what the indefinite adjoint realizes by a conjugate-linear adjoint. The star and the bar are the two conjugations through which the two theories exchange the sides.

## The Indefinite Obstruction

**Proposition (the operator is not definable).** On the canonical Krein space $(\mathbb{B},\langle\cdot,\cdot\rangle_{\natural*})$ the Tomita operator of the indefinite theory, $S(\Lambda\xi)=\Lambda^{\dagger}\xi$, presupposes that the algebra is closed under the indefinite adjoint. The left regular image is not: $(L_{\tilde Q})^{\dagger}=R_{\bar{\tilde Q}}\notin\mathcal{M}$ for non-central $\tilde Q$. Hence the map $\tilde Q\mapsto\tilde Q^{\dagger}$ leaves the algebra and the operator $S$ is not defined for the biquaternion algebra on its own Krein space.

**Proof.** The operator is defined on the orbit of a Krein–von Neumann algebra, and $\mathcal{M}$ is not one for the quaternion sesquilinear form by the corollary of *The Biquaternion Algebra and the Krein–von Neumann Property*; the same computation shows that $\Lambda^{\dagger}\xi$ is not an orbit value $\Lambda'\xi$ for $\Lambda=L_{\tilde Q}$ with non-central $\tilde Q$.

**Proposition (the envelope has no separating vector).** The smallest Krein–von Neumann algebra containing $\mathcal{M}$ is $\mathcal{L}(\mathbb{B})\cong M_4(\mathbb{C})$, and it admits no separating vector: for every $\xi\neq0$ there is a nonzero $T$ with $T\xi=0$. Hence the envelope carries no modular pair either.

**Proof.** Take $T$ the rank-one operator with image the line $\mathbb{C}\xi$ composed with a projection onto the orthogonal complement of $\xi$, so that $T\xi=0$ while $T\neq0$; separatingness of $\xi$ would require $T=0$. So no vector is separating for the full operator algebra, and the three data of the indefinite modular theory — algebra, $J$-cyclic and $J$-separating vector, self-dual cone — cannot be completed for the envelope.

**Remark (the twisted symmetries).** For the twisted fundamental symmetries $J'=R_c$ of *The Biquaternion Algebra and the Krein–von Neumann Property*, with $c^{*}=c$ and $c^{2}=e_0$, the image $\mathcal{M}$ *is* a $J'$-algebra and $\xi=e_0$ is $J'$-cyclic and $J'$-separating, with $S'={}^{*}$ and $\Delta'=\mathrm{id}$ exactly as in the definite case. But the modular conjugation must commute with the fundamental symmetry, $\jmath'J'=J'\jmath'$, and here $\jmath'J'(\tilde S)=c\tilde S^{*}$ while $J'\jmath'(\tilde S)=\tilde S^{*}c$, so the two agree only for central $c$. For every non-central $c$ the twisted pair is a Krein–von Neumann algebra **without** a $J'$-modular conjugation. Definiteness of the modular theory is not recovered by the twist; it is recovered only by the definite reading $J=\mathrm{id}$.

## Worked Examples

### The Modular Pair of the Algebra

The pair $(\mathcal{M},\xi)$ with $\mathcal{M}=\{L_{\tilde Q}\}$, $\xi=e_0$, has $\omega=\mathrm{Sc}$ as its vector state, the trace itself, $S(\tilde Q)=\tilde Q^{*}$, $\Delta=\mathrm{id}$, $\jmath={}^{*}$, and the trivial flow. In the matrix model $\Phi:\mathbb{B}\to M_2(\mathbb{C})$ (*Biquaternion Objects and Their Matrix Correspondences*), the star is the conjugate transpose, so $S$ acts by $\Phi(\tilde Q)\mapsto\Phi(\tilde Q)^{*}$, and the modular conjugation exchanges the left and the right matrix multiplications.

### The Forced Failure on the Krein Space

On the Krein space $(\mathbb{B},\langle\cdot,\cdot\rangle_{\natural*})$, the naive candidate $S(\tilde Q)=\tilde Q^{\dagger}\xi$ would send $\tilde Q$ to the coefficient conjugate $\bar{\tilde Q}$. That map is antilinear and involutive, but it is not the Tomita operator: it is not of the form $x^{\dagger}\xi$ with $x$ in the algebra, because the adjoint of the left multiplication, $\tilde Q^{\dagger}=R_{\bar{\tilde Q}}$, is a right multiplication. The coefficient conjugation is the involution of the quaternion sesquilinear form and the star is the involution of the definite form, and the modular theory selects the second.

## Summary

The biquaternion algebra is a **Hilbert algebra** for the trace $\mathrm{Sc}$ and the Hermitian star, the unit $\xi=e_0$ is cyclic and separating for the left regular image, and the **Tomita operator of the pair is the star itself**, $S(\tilde Q)=\tilde Q^{*}$. It is antilinear, involutive and antiunitary, so the polar decomposition is $S=\jmath\Delta^{1/2}$ with **$\Delta=\mathrm{id}$** and **$\jmath={}^{*}$**, the modular flow is trivial, and the triviality is the traciality of the vector state of the unit, which is the trace $\mathrm{Sc}$ of the algebra. The modular conjugation exchanges the two sides, $\jmath L_{\tilde Q}\jmath=R_{\tilde Q^{*}}$ and $\jmath\mathcal{M}\jmath=\mathcal{M}'$, which is the definite shadow of the indefinite identity $(L_{\tilde Q})^{\dagger}=R_{\bar{\tilde Q}}$. In the indefinite reading the operator is not definable, because the left regular image is not closed under the Krein adjoint, and the envelope that replaces it, $\mathcal{L}(\mathbb{B})\cong M_4(\mathbb{C})$, has no separating vector; the twisted fundamental symmetries give a Krein–von Neumann algebra but no commuting modular conjugation. So the modular data of the biquaternion algebra is **definite**: it lives on the Hilbert space of $J=\mathrm{id}$, where the unit gives the star as Tomita operator and the identity as modular operator, and it does not exist on the Krein space at all. The general theory is *The Indefinite Modular Operator*, *Krein–Tomita–Takesaki Theory* and *The Modular Operator and Tomita-Takesaki Theory*; the operator of the definite case is *The Adjoint of the Left Multiplication on a Hilbert Algebra*; and the obstruction is *The Biquaternion Algebra and the Krein–von Neumann Property*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{M}=\{L_{\tilde Q}\}$, $\xi=e_0$ | The pair carrying the modular data |
| $S(\tilde Q)=\tilde Q^{*}$ | The Tomita operator, the Hermitian star |
| $S=\jmath\Delta^{1/2}$ | The polar decomposition |
| $\Delta=\mathrm{id}$ | The modular operator, trivial by traciality |
| $\jmath={}^{*}$ | The modular conjugation |
| $\jmath L_{\tilde Q}\jmath=R_{\tilde Q^{*}}$ | The conjugation exchanges the sides |
| $\sigma_t=\mathrm{id}$ | The modular flow |
| $\omega(L_{\tilde Q})=\mathrm{Sc}(\tilde Q)=Q_0$ | The vector state, the trace |
| $(L_{\tilde Q})^{\dagger}=R_{\bar{\tilde Q}}$ | The indefinite adjoint, outside the algebra |
| $\mathcal{L}(\mathbb{B})\cong M_4(\mathbb{C})$ | The envelope, with no separating vector |

## Further Reading

- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics*, vol. 1 (Springer, 1987), for the Tomita operator of a von Neumann algebra and its polar decomposition.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 2 (Academic Press, 1986), for the modular operator, the modular conjugation and the commutant theorem.
- Masamichi Takesaki, *Tomita's Theory of Modular Hilbert Algebras and Its Applications*, Lecture Notes in Mathematics 128 (Springer, 1970), for the Hilbert algebra origin of the construction.
- János Bognár, *Indefinite Inner Product Spaces*, Ergebnisse der Mathematik und ihrer Grenzgebiete 78 (Springer, 1974), for the self-dual cones of a Krein space.
- Konrad Schmüdgen, *Unbounded Operator Algebras and Representation Theory* (Akademie-Verlag, 1990), for the indefinite adjoint and the closability of the Tomita operator.
- Alain Connes, *Noncommutative Geometry* (Academic Press, 1994), for the modular theory as the source of the von Neumann algebra classification.
