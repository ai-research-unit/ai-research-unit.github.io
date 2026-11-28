# __The Mode Expansion: Peter–Weyl, the Fourier Transform and the Character Expansion__

## Introduction

Every band of the series asks the same question of its field equation, and asks it in one of two languages. The equation is linear in the field, its symbol is a polynomial in the wave number, and the solutions are wanted in the basis in which that symbol is diagonal. In the bands whose carrier has a phase the basis is plane waves and the language is the Fourier transform. In the bands whose group is simple the plane waves do not exist and the basis is a set of characters, and the language is the character expansion. The two are filed in separate slots, derived from separate premises, and never compared.

They are one operation. The operation is expansion in the characters of the group the field is a function on, and its general form is the Peter–Weyl theorem. The Fourier transform is that theorem in the case where every irreducible representation is one-dimensional. The character expansion is that theorem in the case where the function depends on the group element only through its conjugacy class. Neither is a special case of the other; both are special cases of the theorem, and the theorem is what this article states.

**Two groups act on every field, and only one of them can be non-abelian.** The argument of the field is a point of spacetime, and translations act on it. The value of the field lies in a carrier, and the carrier's group acts on it. A mode is labelled by one character of each. The translation group is abelian in every band of the series, whatever the gauge group is, so a momentum label always survives. The carrier's group varies — trivial at the free layer, $\mathrm{U}(1)$ at electromagnetism, $\mathrm{SU}(2)\times\mathrm{U}(1)$ at the electroweak force, $\mathrm{SU}(3)$ at the strong force, $\mathrm{SU}(4)$ at the primordial — and with it varies the second label, which is an integer, a pair of integers, or a triple.

**What is standard, and what the algebra supplies.** Peter–Weyl, the orthogonality relations, the Plancherel theorem, the structure of the unitary dual, and the classification of the irreducible representations of the classical groups are mathematics, and are imported here from the articles named at the end. Nothing in this article proves them. The algebra supplies two things they do not. The first is the identification of the symbol with the algebra's own quadratic form: under the transform the gradient becomes multiplication by $2\pi i\tilde\Upsilon_{\Phi}$, so the dispersion relation of a carrier is the level set of the norm and the zero set of the symbol is the light cone. The second is the split of the label into its two factors, the momentum the translation supplies and the weight the carrier supplies, which is what makes the phrase *a mode of this carrier* mean one thing across the series.

**What this does not do.** It does not derive a mass, a coupling, or the representation a physical field sits in. The expansion is defined for every representation of every group in the series, and which representation is occupied is an input the expansion cannot supply. It also does not quantise: the modes are a classical basis, and the promotion of that basis to a Fock space is the separate postulate of the section above.

## The Two Groups of a Field

Let the field be $F_{\mathrm{fn}}:\mathbb{R}^4\to\mathbb{B}$, and let $G$ be the group of the carrier. The translations act on the argument, $F_{\mathrm{fn}}(x)\mapsto F_{\mathrm{fn}}(x+a)$, and $G$ acts on the value, $F_{\mathrm{fn}}(x)\mapsto g\cdot F_{\mathrm{fn}}(x)$. The two actions commute, and the field is a function on the product $\mathbb{R}^4\times G$ in the sense that a mode is a function of both variables.

The reason the product matters is one theorem about duals: for compact groups $K_1,K_2$,

$$
\operatorname{Irr}(K_1\times K_2)=\operatorname{Irr}(K_1)\times\operatorname{Irr}(K_2),\qquad d_{\pi_1\boxtimes\pi_2}=d_{\pi_1}d_{\pi_2},\qquad \chi_{\pi_1\boxtimes\pi_2}=\chi_{\pi_1}\chi_{\pi_2},
$$

so an irreducible of the product is a pair and its character is a product. The pair is the mode's label. This is why a mode of the electroweak carrier is labelled by $(j,n)$ and not by a single number: the carrier's group is a product, its dual is a product, and the label inherits the product structure.

**The free layer is the case where the second factor is trivial.** At the free layer the carrier's group is $\mathrm{SU}(1)=\{e\}$, which has one irreducible, of dimension one, with trivial character. Its dual is a single point, the label it contributes carries no information, and a mode is labelled by its momentum alone. The band's expansion is therefore the pure translation transform, which is what the free-layer articles use and why they need no group theory at all.

**A $\mathrm{U}(1)$ factor contributes an integer.** The dual of $\mathrm{U}(1)$ is $\mathbb Z$, the character $n$ is $\chi_n(\theta)=e^{2\pi i n\theta}$, and the label is the winding number. This is the case in which the two groups are of the same kind: a $\mathrm{U}(1)$ factor of the carrier behaves exactly as the translation group does, its characters are exponentials, and its labels add under multiplication.

The distinction that the rest of the article turns on is between this case and the case in which the carrier's group is simple. There the dual is not a group, the characters are not exponentials, and the label does not add.

## The General Theorem

**Theorem (Peter–Weyl).** Let $K$ be a compact Hausdorff group and let $\operatorname{Irr}(K)$ be the set of equivalence classes of its irreducible continuous unitary representations, each finite-dimensional with dimension $d_\pi$. Then:

**(a)** the matrix coefficients $k\mapsto\langle\pi(k)u,v\rangle$ span a subspace dense in $C(K)$ and in $L^p(K)$ for every $1\le p<\infty$;

**(b)** for orthonormal bases $(e_i)$ of $\mathcal{H}_\pi$ and $(f_l)$ of $\mathcal{H}_\sigma$,

$$
\int_K\pi_{ij}(k)\,\overline{\sigma_{lm}(k)}\,dk=\frac{1}{d_\pi}\,\delta_{\pi\sigma}\,\delta_{il}\,\delta_{jm},
$$

so that $\sqrt{d_\pi}\,\pi_{ij}$ is an orthonormal basis of $L^2(K)$ and

$$
L^2(K)\cong\bigoplus_{\pi\in\operatorname{Irr}(K)}\bigl(\mathcal{H}_\pi\otimes\mathcal{H}_\pi^{*}\bigr),
$$

each irreducible occurring with multiplicity $d_\pi$;

**(c)** every continuous unitary representation of $K$ is a direct sum of finite-dimensional irreducibles;

**(d)** the characters $\chi_\pi(k)=\operatorname{Tr}\pi(k)$ form an orthonormal basis of the subspace $L^2(K)^K$ of class functions.

The transform is the coefficient map of (b),

$$
(\mathcal F f)(\pi)=\int_K f(k)\,\pi(k)\,dk\in\operatorname{End}(\mathcal{H}_\pi),
$$

and it is a unitary equivalence of $L^2(K)$ with the direct sum of the matrix algebras, which is the compact case of Plancherel. Its algebra property is that convolution becomes operator multiplication,

$$
\widehat{f*g}(\pi)=(\mathcal F f)(\pi)\,(\mathcal F g)(\pi),
$$

proved by the substitution $x=yz$ and the invariance of Haar measure.

**Three features of this statement govern everything below.** The output is an operator, not a number. The index is a set, not a group. And the diagonalisation is of the convolution algebra, not of a differential operator — the differential operator enters only after the translation factor is separated, which is the subject of the next section.

## The Abelian Degeneration: the Fourier Transform

Suppose $K$ is abelian. Then every irreducible unitary representation is one-dimensional, so $d_\pi=1$, the operator $(\mathcal F f)(\pi)$ is a scalar, and the index set $\operatorname{Irr}(K)=K^{\vee}$ acquires a group structure: the tensor product of two one-dimensional representations is one-dimensional and irreducible, the product of characters is a character, and the label adds. The scalar is the character, the transform is $\hat f(\chi)=\int_K f\,\overline{\chi}\,dk$, and Peter–Weyl reads: the characters are an orthonormal basis of $L^2(K)$.

**Fourier analysis is exactly this case, and there is nothing else to it.** For $K=\mathbb{R}^n$ the characters are $x\mapsto e^{2\pi i\langle\nu,x\rangle}$; for $K=S^1$ they are $e^{2\pi in\theta}$; for a finite abelian group they are the $|K|$ homomorphisms into the roots of unity, and (b) is the discrete Fourier transform with the Wedderburn decomposition of the group algebra. The four standard cases are one theorem.

**The biquaternion transform is the case $K=\mathbb{R}^4$.** The corpus's kernel is built from an element whose square is the unit and a complex scalar beside it,

$$
W(t,\omega)=\exp(-2\pi i\,\tilde{Z}\,\omega t),\qquad \tilde{Z}^{2}=e_t ,
$$

and it is the character pairing of the additive group with the wave-number element, with the direction of the pairing supplied by a root of one. The root is not decoration: the halving map sends it to the idempotent pair $\tilde\Pi_{\mathrm{id},\pm}=\tfrac12(e_t\pm\tilde{Z})$, the kernel factors as

$$
W(t,\omega)=e^{-2\pi i\omega t}\,\tilde\Pi_{\mathrm{id},+}+e^{+2\pi i\omega t}\,\tilde\Pi_{\mathrm{id},-},
$$

and the transform of an algebra-valued function is a pair of ordinary complex transforms on the two Peirce ideals. **The factorization is the abelian case of Peter–Weyl read in the coordinates the root supplies** — one character per one-dimensional summand, two summands, two scalars.

**What the transform does to the equation.** Differentiation becomes multiplication, and the multiplier is a biquaternion:

$$
\mathcal F\bigl[\partial_t F_{\mathrm{fn}}\bigr](\omega)=2\pi i\,\tilde{Z}\,\omega\,\mathcal F[F_{\mathrm{fn}}](\omega),
\qquad
\tilde\nabla_{\Phi}\longmapsto 2\pi i\,\tilde\Upsilon_{\Phi},
\qquad
\tilde\Upsilon_{\Phi}=i\,\nu_t^{\prime}e_t+\vec\nu_{\Phi} .
$$

The symbol of the d'Alembertian is a scalar and its zero set distinguishes the two operators: $-(2\pi)^2(\omega_0^2+\omega_1^2+\omega_2^2+\omega_3^2)$ vanishes only at the origin, so the elliptic operator has no propagating mode, while $-4\pi^2(\omega_0^2-\omega_1^2-\omega_2^2-\omega_3^2)$ vanishes on the null cone, and the transform of a solution is supported there. **A field equation becomes a polynomial equation on the dual, and its solution set on the dual is the mass shell.** For a carrier of mass wave number $\nu_m$ the polynomial is

$$
-\nu_t^{\prime\,2}+\nu_{\Phi}^{2}=-\nu_m^{2},
$$

which is the level set of the central quaternion norm $\tilde\Upsilon_{\Phi}\tilde\Upsilon_{\Phi}^{\natural}$.

**The algebra enters only in the multiplication.** The transform itself is the transform of the additive group, and the additive group of a number system is $\mathbb{R}^{n}$ for an $n$ fixed by the system — $\mathbb{R}^{4}$ for the quaternions, $\mathbb{R}^{8}$ for the biquaternions; what differs between the systems is the algebra in which convolution multiplies. This is why one transform serves the real, complex, split-complex, dual-number, quaternion and biquaternion rows alike, and why the series does not need a separate harmonic analysis per system.

## The Class-Function Degeneration: the Character Expansion

The general transform is operator-valued, so the statement that a mode has a scalar amplitude is false in general. It becomes true under one hypothesis on the function, and that hypothesis is what a gauge theory supplies.

**Proposition.** Let $f\in L^1(K)$ be a class function, $f(xkx^{-1})=f(k)$ for all $x,k\in K$. Then for every $\pi\in\operatorname{Irr}(K)$,

$$
(\mathcal F f)(\pi)=\lambda_\pi(f)\,I,\qquad \lambda_\pi(f)=\frac{1}{d_\pi}\int_K f(k)\,\overline{\chi_\pi(k)}\,dk .
$$

The proof is two lines: conjugating the integral by $\pi(x)$ leaves it unchanged because $f$ and $dk$ are both invariant, so the operator commutes with every $\pi(x)$, and Schur's lemma makes it a scalar; the trace then computes the scalar as the displayed integral.

**Read the two formulas side by side.** The class-function coefficient is the Fourier coefficient with $d_\pi$ left in. Set $d_\pi=1$ and it is $\int f\overline{\chi_\pi}\,dk$ exactly. Character expansion is therefore not a generalisation of Fourier and Fourier is not a special case of character expansion: they are the two ways the operator can collapse to a number, one because the representation is one-dimensional, the other because the function cannot see the non-commutativity.

**Where a class function comes from.** A gauge-invariant functional of a connection on a lattice depends on the link variable only through its conjugacy class, because the local transformation acts by conjugation at each end. The simplest such functional is the trace, which is the character. The Wilson action is built from it,

$$
S_W=\beta\sum\Bigl(1-\frac{2}{N}\operatorname{Re}\operatorname{Sc}\tilde U_{\imath\jmath}\Bigr),
$$

and $\mathrm{Sc}\,\tilde U$ is $d_\pi^{-1}$ times the character of the defining representation evaluated at the plaquette, since the corpus's trace is twice the real scalar part and the defining representation of the unit-quaternion group has dimension two. **The strong-coupling expansion of the lattice path integral is the character expansion**, and its coefficients are the $\lambda_\pi$ of the proposition, indexed by the highest weights.

**Multiplicities replace addition.** The single structural difference from the abelian case is that the product of two characters is not a character:

$$
\chi_\pi\chi_\sigma=\sum_{\tau\in\operatorname{Irr}(K)}m^{\tau}_{\pi\sigma}\,\chi_\tau,
\qquad
m^{\tau}_{\pi\sigma}=\int_K\chi_\pi\chi_\sigma\overline{\chi_\tau}\,dk ,
$$

with finitely many nonzero coefficients. In the abelian case $m^{\tau}_{\pi\sigma}=\delta_{\tau,\pi\sigma}$, the product is a single character, and the labels add — which is momentum conservation. In the non-abelian case they do not add; they fuse, and the coefficients are the structure constants of the representation ring. **This is why the strong-coupling expansion is a tiling expansion and not a term-by-term product**, and why the identity that separates the groups is an integral over two fundamentals: for $N\ge3$ the antisymmetric square of the fundamental contains no singlet and that integral vanishes, whereas for $N=2$ it does not.

## The Obstruction: No Scalar Transform of a Simple Group

A character into the circle is a homomorphism, so it is constant on the commutator subgroup. For a perfect group the commutator subgroup is the whole group and the only character is the trivial one. Every $\mathrm{SU}(N)$ with $N\ge2$ is simple and therefore perfect, so

$$
\operatorname{Hom}\bigl(\mathrm{SU}(N),S^{1}\bigr)=\{1\},
$$

the class-function part of the dual is a single point, and there is no family $\exp(ik\cdot g)$ to expand a function of $g$ in. The obstruction is not that the transform is hard; it is that the object the abelian transform is indexed by does not exist.

**The characters of the group are not the characters of its representations.** The statement above concerns the homomorphisms $G\to S^1$, of which there is one. The functions $\chi_\pi=\operatorname{Tr}\pi$ exist in abundance, one per irreducible representation, and they are what (d) of Peter–Weyl makes an orthonormal basis of the class functions. The two uses of the word differ, and the corpus's $\mathrm{SU}(N)$ bands use the second.

**What survives is the other factor.** The translations are abelian whatever the carrier's group is, so the momentum label is untouched by the obstruction. A mode of an $\mathrm{SU}(4)$ field still carries a wave number; what it does not carry is a group-valued plane wave. This is why the corpus has articles titled *in momentum space* for the carriers whose group is abelian or trivial and none for the Yang–Mills bands, and why that absence is a statement about one of the two labels and not about the transform as a whole.

## The Labels of a Mode

The two factors combine as follows. The column *expansion* names which of the two forms a band uses; the column *label* is what a mode is indexed by.

| carrier's group | dual | mode label | expansion |
|---|---|---|---|
| $\mathrm{SU}(1)=\{e\}$ | one point | none | translation only |
| $\mathrm{U}(1)$ | $\mathbb{Z}$ | $n$ | Fourier, labels add |
| $\mathrm{SU}(2)$ | $s\in\tfrac12\mathbb{Z}_{\ge0}$ | $2s+1$ weights, Wigner $D^{s}_{mn}$ | character, $d_s=2s+1$ |
| $\mathrm{SU}(2)\times\mathrm{U}(1)$ | $(s,n)$ | $(m_s,n)$ | product of the two |
| $\mathrm{SU}(3)$ | $(p,q)\in\mathbb{Z}_{\ge0}^{2}$ | weights of $(p,q)$ | character, $d=\tfrac{(p+1)(q+1)(p+q+2)}{2}$ |
| $\mathrm{SU}(4)$ | $(p,q,r)\in\mathbb{Z}_{\ge0}^{3}$ | weights of $(p,q,r)$ | character, $d=\tfrac{(p+1)(q+1)(r+1)(p+q+2)(q+r+2)(p+q+r+3)}{12}$ |
| $\mathbb{R}^{4}$ (translations) | $\mathbb{R}^{4}$ | $\nu_t^{\prime},\vec\nu_{\Phi}$ | biquaternion kernel |
| full Standard Model product | the product of the three | $(p,q;\,s;\,n)$ | product of the three |

The dimension formulas in the table are the Weyl dimension formula and are checkable on the smallest cases: $(1,0)$ of $\mathrm{SU}(3)$ is the fundamental of dimension $3$ and $(1,1)$ the adjoint of dimension $8$; $(1,0,0)$ of $\mathrm{SU}(4)$ is the fundamental of dimension $4$, $(0,1,0)$ the antisymmetric square of dimension $6$, and $(1,0,1)$ the adjoint of dimension $15$.

**Labels restrict, and that is the branching rule.** The series' groups are nested, $\mathrm{SU}(1)\subset\mathrm{SU}(2)\subset\mathrm{SU}(3)\subset\mathrm{SU}(4)$, with the strong rung the stabiliser of a line in the primordial rung, $\mathrm{SU}(3)=\mathrm{Stab}_{\mathrm{SU}(4)}(e_t)$. An irreducible of the larger group therefore restricts to a sum of irreducibles of the smaller, and a mode's label restricts with it: a $(p,q,r)$ becomes a set of $(p^{\prime},q^{\prime})$ each carrying the leftover abelian label. That label is not free. The corpus's breaking is $\mathrm{SU}(4)\to\mathrm{SU}(3)_c\times\mathrm{U}(1)_{B-L}$, the kernel of $\operatorname{ad}(iD)$ is $\mathfrak{u}(3)=\mathfrak{su}(3)_c\oplus\mathfrak{u}(1)_{B-L}$, and the rank moves $3\to2+1$; so the third integer of the $(p,q,r)$ becomes the $B-L$ charge. **A mode's labels are its weights, so the branching of the label set is the branching of the representation**, and the phrase *the mode expansion of the theory after breaking* means the expansion re-indexed along the restriction.

## What the Expansion Gives a Band, and What It Does Not

**It gives a diagonal symbol.** The equation in position space becomes a polynomial equation on the dual, and the polynomial is the algebra's quadratic form evaluated on the wave-number element. Where the corpus says the dispersion relation is the mass shell, this is the operation that produces the statement.

**It gives the zero set.** The solutions that propagate are the zeros of the symbol, the elliptic operators have none, and the hyperbolic ones have the null cone. A rank statement at a point of the dual is a count of the amplitude directions the symbol can reach, which the corpus reads as a polarisation count: three off the cone and two on it, the branch that crosses being one circular polarisation.

**It gives the basis the quantisation consumes.** The Fock space is built on the one-particle space, and the one-particle space is spanned by the modes. Nothing in the promotion to a commutator is meaningful without the basis, and the reason the quantisation articles can be written once per carrier and not once per group is that the basis exists in both expansions.

**It gives nothing dynamical.** No mass, no coupling, no representation assignment, no mechanism for a symmetry to break. The expansion is defined before any of those are chosen, and it is silent about which of its own labels the physical field occupies. The mass shell is read off the symbol, but the symbol contains the mass as a parameter; the expansion does not produce it.

**And it is classical.** The modes are a basis of solutions of a classical equation. That the coefficients are operators acting on a Fock space is a further postulate, imported in the section above and audited there. This article's slot in the ladder is before that section because the transform is taken of the equation and consumed by the apparatus; the reverse order has nothing to transform.

## Limits

**The biquaternion transform is not an isometry for every root.** Plancherel holds for the kernel exactly when the root is Hermitian, because the Peirce split is orthogonal for the Euclidean form exactly then. For a general root the transform is not unitary, functions of vanishing norm have transforms that fail to determine them, and the inversion formula has a degenerate set on which it does not apply — the light cone read as a set of frequencies. The abelian theorem quoted above is therefore the Hermitian case of a statement that does not hold in general, and the corpus's transform is a transform of an indefinite theory.

**The character expansion is a strong-coupling expansion and inherits its convergence.** The series in $\beta$ is asymptotic, and its truncation is a truncation in the number of plaquettes, not in the number of modes. Nothing here establishes convergence beyond the regime in which the expansion is used, and the corpus's lattice results are stated as strong-coupling results for that reason.

**The label set is not a group, so *momentum space* is a misnomer for the second factor.** There is no addition of labels, only fusion, and no conservation law of the kind the abelian case supplies. Reading a $(p,q)$ as a momentum would predict a conservation that does not hold.

**The expansion is defined for every representation.** Nothing in it selects one. A band that says *the field sits in the sixteen* has made a choice the expansion cannot check, and the choice is revisable without changing a single coefficient formula.

**The dual of a simple group is not classified here.** The article uses the labels $(p,q)$ and $(p,q,r)$ and the two dimension formulas, and stops. The Weyl character formula, the weight multiplicities, and the structure of the representation ring are mathematics the corpus cites and does not develop.

## Open Questions

**Is there a character theory of the algebra's own group?** The corpus has the kernel, the root, the idempotent split and the vanishing-norm issue, and it does not have the dual of $\mathbb{B}^{\times}$: the set of irreducible representations of the seven-dimensional group of unit-modulus biquaternions, with its characters and its Plancherel formula. Peter–Weyl applies to that group because it is compact, and the expansion has not been written.

**Does the indefinite case admit a Plancherel formula in a Krein space?** The non-Hermitian root gives a non-unitary transform; the Hermitian GNS construction gives a modular structure in place of positivity. The two are the same failure seen from two sides, and whether the transform has an isometry statement in the indefinite inner product is open in the corpus.

**Is the sixteen a single irreducible?** If the fermion multiplet is one irreducible of $\mathrm{SU}(4)$, its label is fixed and its restriction to the Standard Model is forced, and the branching statement above becomes a derivation rather than a bookkeeping. If it is a sum, the assignment is a choice. The corpus's counts bear on the answer, and the mode expansion is the language in which it would be stated.

**What is the convergence radius of the character expansion on the unit-quaternion lattice?** The lattice group is $\mathrm{SU}(2)$, whose characters are known in closed form, so the expansion is explicit; where it stops converging, and whether the deconfinement transition is visible as a singularity in $\beta$, are not addressed.

## Summary

A field on spacetime with values in a carrier is a function of two groups, the translations and the carrier's own, and a mode is a pair of characters, one from each. The general expansion is Peter–Weyl: the transform is operator-valued, indexed by the unitary dual, and it turns convolution into operator multiplication, with the matrix coefficients an orthonormal basis of $L^2(K)$ and the characters an orthonormal basis of the class functions. Two degenerations make the output scalar. If the group is abelian every irreducible is one-dimensional, the index set is a group, the labels add, and the expansion is the Fourier transform; for the biquaternion algebra the kernel is the character of the additive group with the direction supplied by a root of one, and under it the gradient becomes multiplication by $2\pi i\tilde\Upsilon_{\Phi}$, so the field equation becomes a polynomial whose zero set is the mass shell. If the function is a class function the operator collapses to $\lambda_\pi=d_\pi^{-1}\int f\overline{\chi_\pi}$ times the identity, and the expansion is in characters; a gauge-invariant functional of a link is such a function, its trace is the character, and the strong-coupling expansion of the lattice integral is this expansion, with multiplicities $m^{\tau}_{\pi\sigma}$ in place of the addition of labels. The obstruction is that a simple group has one character into the circle, so no scalar transform of the group variable exists for $\mathrm{SU}(3)$ or $\mathrm{SU}(4)$; the translation factor is unaffected, and a mode always keeps its momentum. The labels are $n$ for $\mathrm{U}(1)$, $s$ for $\mathrm{SU}(2)$, $(s,n)$ for the electroweak product, $(p,q)$ for $\mathrm{SU}(3)$, $(p,q,r)$ for $\mathrm{SU}(4)$, and they restrict along the nested ladder with the leftover abelian direction fixed by the breaking. The expansion supplies the diagonal symbol, its zero set, the polarisation count and the basis the quantisation consumes, and supplies no mass, no coupling and no choice of representation.

## Summary of Notation

| symbol | meaning |
|---|---|
| $K$, $G$ | a compact group, and the group of a carrier |
| $\operatorname{Irr}(K)$ | the unitary dual, a set and not a group for non-abelian $K$ |
| $K^{\vee}$ | the character group of an abelian $K$ |
| $d_\pi$ | the dimension of the irreducible $\pi$ |
| $\pi_{ij}(k)$ | a matrix coefficient, $\langle\pi(k)e_j,e_i\rangle$ |
| $\chi_\pi$ | the character $\operatorname{Tr}\pi$, an orthonormal basis of $L^2(K)^K$ |
| $(\mathcal F f)(\pi)$ | the transform, $\int_K f(k)\pi(k)\,dk\in\operatorname{End}(\mathcal H_\pi)$ |
| $\lambda_\pi(f)$ | the scalar $d_\pi^{-1}\int_K f\overline{\chi_\pi}$ for a class function |
| $m^{\tau}_{\pi\sigma}$ | the multiplicity of $\tau$ in $\pi\otimes\sigma$ |
| $W(t,\omega)$ | the biquaternion kernel $\exp(-2\pi i\tilde{Z}\omega t)$, $\tilde{Z}^{2}=e_t$ |
| $\tilde\Pi_{\mathrm{id},\pm}$ | the idempotent pair $\tfrac12(e_t\pm\tilde{Z})$ the kernel factors on |
| $\tilde\Upsilon_{\Phi}$ | the wave-number element $i\nu_t^{\prime}e_t+\vec\nu_{\Phi}$ |
| $\nu_t^{\prime}$, $\nu_{\Phi}$, $\nu_m$ | energy, momentum and mass wave numbers |
| $(p,q)$, $(p,q,r)$ | the highest weights of $\mathrm{SU}(3)$ and $\mathrm{SU}(4)$ |
| $\beta$ | the lattice coupling, $2N/\kappa^{2}$ |

## Further Reading

- *The Peter–Weyl Theorem*, for the statement, the analytic input, the proof and the consequences used throughout.
- [*Analysis on Compact Groups*](../articles_maths/analysis-on-compact-groups.html), for the operator-valued transform, the orthogonality relations, the inversion and Plancherel formulas, and the worked cases $\mathrm{SU}(2)$, $SO(3)$ and the finite groups.
- [*Harmonic Analysis on Groups*](../articles_maths/harmonic-analysis-on-groups.html), for the abelian theory, the obstruction for non-abelian groups, the matrix-valued transform, and the per-system transforms of the algebra layer.
- [*Character Theory*](../articles_maths/character-theory.html), for the finite-group case, the orthogonality of the character table and the ring of characters.
- [*Noncommutative Harmonic Analysis*](../articles_maths/noncommutative-harmonic-analysis.html), for the operator-algebraic completion of the transform.
- [*Biquaternion Continuous Harmonic Analysis*](../articles_maths/biquaternion-continuous-harmonic-analysis.html), for the kernel, the factorization into complex transforms, the convolution theorem and the vanishing-norm issue.
- [*Relations between the Biquaternion Exponential and the Fourier Kernel*](../articles_maths/relations-between-the-biquaternion-exponential-and-the-fourier-kernel.html), for the character the symbol multiplies.
- [*Inversion of the Biquaternion Fourier Transform: Poles, Tails and the Degenerate Set*](../articles_maths/inversion-of-the-biquaternion-fourier-transform-poles-tails-and-the-degenerate-set.html), for the degenerate set on which the inversion fails.
- *Derivatives, Fields and Transforms*, for the symbol, the wave-number element and the zero set of the operator.
- *Wave–Particle Duality and the Fourier Transform*, for the two quadratic forms and the transform as the switch between them.
- *Wave–Particle Duality and the Count of Degrees of Freedom: The Symbol's Rank On and Off the Cone*, for the rank of the symbol read as a polarisation count.
- *The Fourier Transform and the Klein–Gordon Equation in Biquaternionic Form*, for the transform of an equation and the obstruction read on the zero set, and its polar-variable companion for the seed gradient as the kernel's phase.
- *Lattice Connection Theory and the Biquaternion Path Integral*, for the Haar measure on the unit quaternions, the Wilson action, the character identities that separate $N=2$ from $N\ge3$, and the tiling expansion.
- *The Symmetry Group $\mathrm{SU}(1)$ of the Force-Free Case*, for the nested ladder $\mathrm{SU}(1)\subset\mathrm{SU}(2)\subset\mathrm{SU}(3)\subset\mathrm{SU}(4)$ and the strong rung as a stabiliser.
- *The Restructuring of the Primordial Force and the Mass of the Six Leptoquarks*, for the direction that survives a breaking as the abelian label.
- *The Hermitian GNS Construction in the Biquaternion Framework*, for the modular structure that replaces positivity, which is the state-side counterpart of the transform's non-unitarity.
