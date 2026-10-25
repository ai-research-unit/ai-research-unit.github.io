# __Remarkable Subspaces and the Four General Products, Forms and Norms__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries four **general products**, and the four are read here on the six **remarkable subspaces**. Each product has a scalar-part **form**, a function of two arguments, and each form has an **algebraic norm**, its value at two equal arguments. The three objects form one chain,

$$
f\longmapsto \varphi=\mathrm{Sc}\circ f\longmapsto \langle\cdot\rangle=\varphi(\cdot,\cdot),
$$

and the chain is read here on the centre, the vector subspace, the quaternion subspace, the anti-quaternion subspace, the Hermitian subspace and the anti-Hermitian subspace, one subspace to a section. The three levels are collected in a single article so that each subspace is read once, at the three levels, rather than three times in three articles.

The chain decides what each level can see. The **product** is the finest object: it returns an element of the algebra, and a subspace can be closed under it, under its symmetrisation or under its bracket. The **form** keeps the scalar part of the product and loses the rest; it is still a function of two arguments, and on the two complex subspaces it carries an imaginary part that no single-argument function can carry. The **norm** keeps only the diagonal of the form, and on the four real-type subspaces that is enough, because there the form is real and is recovered from the norm by polarisation.

Two facts organise the article. First, the four products have the **same value set** on each subspace, because the two conjugations that distinguish them preserve every subspace of the list; the four differ in the structure they leave on the value, not in where they send a pair. Second, the symmetrisation and the bracket close on more subspaces than the product; the symmetrisation closes on the same subspaces for all four products, while the bracket closure depends on the product, and the Jordan and Jacobi identities decide which closures are algebras. The result is a small table of algebras, carried by six subspaces and four products, and it is stated in $\S$*The Four General Products* and justified subspace by subspace.

The article assumes the algebra and the conjugations of *The Biquaternion Algebra and Its Vector Spaces* and the subspaces, bases and dimensions of *Introduction to the Remarkable Subspaces*. The products, their relations and their comparison are *The Four General Products and Their Relations over the Biquaternion Algebra*; the forms and the algebraic norms are *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the two halves of a product are *Symmetric and Antisymmetric Decomposition of the Four General Products*; and the coordinate blocks are *Comparison of the Remarkable Subspaces*. None of that is restated. What the article adds is the reading of the chain on the six subspaces, the common value set, the collapse patterns, the real and imaginary parts of the restrictions, the signatures, and the separation the subspaces impose on the four norms. The physical interpretation of the two sectors is deferred to *The Informational Sector: States, Observables and Probability* and *The Material Sector: Four-Vectors, Interval and Lorentz Action*, and is recalled only in $\S$*The Material Interpretation*. The article replaces the three earlier articles that treated the four general products, the four forms and the four algebraic norms on the remarkable subspaces separately.

## Notational Conventions

$\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the biquaternion algebra, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, scalar unit $e_t=1$, vector units $\vec e_k^{2}=-e_t$, and central scalar imaginary $i$, $i^{2}=-1$. A general element is $\tilde Q=\sum_{\mu\in\{t,x,y,z\}}Q_\mu e_\mu$ with $Q_\mu\in\mathbb{C}$, written in the centre–vector split $\tilde Q=c+v$ with $c=Q_te_t\in\mathbb{C}_{\mathbb{B}}$ and $v=\sum_{k=1}^{3}Q_k\vec e_k\in\mathrm{Vect}(\mathbb{B})$. The scalar part is $\mathrm{Sc}$. The coefficientwise conjugation is $\bar{\cdot}$, the natural conjugation is ${}^{\natural}$, with $Q^{\natural}_\mu=\varepsilon_\mu Q_\mu$ and sign vector $\varepsilon=(1,-1,-1,-1)$, and the Hermitian conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$. The vector parts carry the complex bilinear dot product $(\vec P,\vec Q)=\sum_{k=1}^{3}P_kQ_k$ and the cross product $\vec P\times\vec Q$.

The six subspaces and their real bases are these.

| subspace | defining condition | real basis | $\dim_{\mathbb{R}}$ | blocks |
|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\vec Q=0$ | $e_t,\ ie_t$ | $2$ | $A_1\oplus A_2$ |
| $\mathrm{Vect}(\mathbb{B})$ | $Q_t=0$ | $\vec e_x,\ i\vec e_x,\ \vec e_y,\ i\vec e_y,\ \vec e_z,\ i\vec e_z$ | $6$ | $B_1\oplus B_2$ |
| $\mathbb{H}_{\mathbb{B}}$ | $Q_\mu\in\mathbb{R}$ | $e_t,\ \vec e_x,\ \vec e_y,\ \vec e_z$ | $4$ | $A_1\oplus B_1$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $Q_\mu\in i\mathbb{R}$ | $ie_t,\ i\vec e_x,\ i\vec e_y,\ i\vec e_z$ | $4$ | $A_2\oplus B_2$ |
| $\mathbb{M}_+$ | $Q_t\in\mathbb{R}$, $Q_k\in i\mathbb{R}$ | $e_t,\ i\vec e_x,\ i\vec e_y,\ i\vec e_z$ | $4$ | $A_1\oplus B_2$ |
| $\mathbb{M}_-$ | $Q_t\in i\mathbb{R}$, $Q_k\in\mathbb{R}$ | $ie_t,\ \vec e_x,\ \vec e_y,\ \vec e_z$ | $4$ | $A_2\oplus B_1$ |

The four **coordinate blocks** of *Comparison of the Remarkable Subspaces* are

$$
A_1=\mathbb{R}e_t,\qquad A_2=\mathbb{R}(ie_t),\qquad
B_1=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\},\qquad
B_2=\operatorname{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\},
$$

the two scalar blocks of dimension one and the two vector blocks of dimension three. The centre and the vector subspace are **complex subspaces**, with $iU=U$; the other four are **real-type subspaces**, with $iU\cap U=\{0\}$. The two sectors are $\mathbb{M}_+$, the informational sector, and $\mathbb{M}_-$, the material sector.

The four **general products** are the general plain bilinear, the general quaternionic bilinear, the general plain sesquilinear and the general quaternionic sesquilinear,

$$
f_{\mathrm{pl}}(\tilde Q_1,\tilde Q_2)=\tilde Q_1\tilde Q_2,\qquad
f_{\natural}(\tilde Q_1,\tilde Q_2)=\tilde Q_1^{\natural}\tilde Q_2,\qquad
f_{\mathrm{pl}*}(\tilde Q_1,\tilde Q_2)=\tilde Q_1\tilde Q_2^{*},\qquad
f_{\natural*}(\tilde Q_1,\tilde Q_2)=\tilde Q_1^{\natural}\tilde Q_2^{*},
$$

the subscript naming the first and the second slot in that order, $\mathrm{pl}$ for the plain slot and ${}^{*}$ for the starred one. The first and the third are $\mathbb{C}$-bilinear, the second and the fourth only over $\mathbb{R}$; the first is associative and the other three are not. Each product splits into a symmetric and an antisymmetric half, written $f^{+}$ and $f^{-}$, and the halves are $f_{\mathrm{pl}}^{+}=\bullet_{\mathrm{pl}}$ with $f_{\mathrm{pl}}^{-}=[\cdot,\cdot]$, $f_{\natural}^{+}=\bullet$ with $f_{\natural}^{-}=[\cdot,\cdot]_{\natural}$, and similarly for the two sesquilinear products.

The four **forms** are the scalar parts of the four products,

$$
\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Sc}(\tilde Q_1\tilde Q_2)=\sum_\mu\varepsilon_\mu Q_{1,\mu}Q_{2,\mu},
\qquad
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)=\sum_\mu Q_{1,\mu}Q_{2,\mu},
$$
$$
\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})=\sum_\mu Q_{1,\mu}\overline{Q_{2,\mu}},
\qquad
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2^{*})=\sum_\mu\varepsilon_\mu Q_{1,\mu}\overline{Q_{2,\mu}},
$$

the general plain bilinear, the general quaternionic bilinear, the general plain sesquilinear or **Hermitian**, and the general quaternionic sesquilinear or **Krein** form. The four **algebraic norms** are the same forms at two equal arguments, written with one argument,

$$
\langle\tilde Q\rangle=\sum_\mu\varepsilon_\mu Q_\mu^{2},\qquad
\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2},\qquad
\langle\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2},\qquad
\langle\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}.
$$

The one-argument bracket is the norm and the two-argument bracket is the form; the distinction is the one of *Conventions in the Biquaternion Universe*. On a real-type subspace the form is real and the norm is its diagonal; on a complex subspace the form is complex and the norm carries only part of it.

The four forms are collected in one table.

| pair of slots | product | form | name of the form | algebraic norm |
|---|---|---|---|---|
| $(\mathrm{id},\mathrm{id})$ | $f_{\mathrm{pl}}$ | $\langle\cdot,\cdot\rangle$ | general plain bilinear | $\langle\cdot\rangle$ |
| $({}^{\natural},\mathrm{id})$ | $f_{\natural}$ | $\langle\cdot,\cdot\rangle_{\natural}$ | general quaternionic bilinear | $\langle\cdot\rangle_{\natural}$ |
| $(\mathrm{id},{}^{*})$ | $f_{\mathrm{pl}*}$ | $\langle\cdot,\cdot\rangle_{*}$ | general plain sesquilinear, Hermitian | $\langle\cdot\rangle_{*}$ |
| $({}^{\natural},{}^{*})$ | $f_{\natural*}$ | $\langle\cdot,\cdot\rangle_{\natural*}$ | general quaternionic sesquilinear, Krein | $\langle\cdot\rangle_{\natural*}$ |

For a complex-valued form $\varphi$ on a real subspace $U$ the real and imaginary parts are $g=\operatorname{Re}\varphi$ and $\sigma=\operatorname{Im}\varphi$, so that $\varphi=g+i\sigma$; the letter $\omega$ is used for the imaginary part when it is alternating. The **signature** over $\mathbb{R}$ is written $(p,q)$, with $p$ positive and $q$ negative squares. The **Gram matrix** of a restriction is taken in the complex basis of the subspace, that is $(e_t)$ on the centre, $(\vec e_x,\vec e_y,\vec e_z)$ on the vector subspace and the real bases of the table on the four real-type subspaces. The **null set** of a form on $U$ is the set of $\tilde Q\in U$ with $\varphi(\tilde Q,\tilde Q)=0$. A form is **non-degenerate** on $U$ when $\varphi(\tilde Q_1,\tilde Q_2)=0$ for all $\tilde Q_2\in U$ forces $\tilde Q_1=0$.

## The Four General Products

Every subspace is a fixed or anti-fixed space of one of the four conjugations of *The Group of Involutions*, and the two conjugations ${}^{\natural}$ and ${}^{*}$ preserve every subspace of the list. This one observation settles the value set of the four products before any coordinate is written.

### The common value set

**Proposition.** For each remarkable subspace $U$ the real span of $f(\tilde Q_1,\tilde Q_2)$, as $\tilde Q_1$ and $\tilde Q_2$ run over $U$, is the same for the four general products $f$.

*Proof.* Since ${}^{\natural}U=U$ and ${}^{*}U=U$ for every subspace of the list,

$$
f_{\natural}(U,U)=U^{\natural}U=U\cdot U=f_{\mathrm{pl}}(U,U),\qquad
f_{\mathrm{pl}*}(U,U)=UU^{*}=U\cdot U,\qquad
f_{\natural*}(U,U)=U^{\natural}U^{*}=U\cdot U,
$$

so the four products take the same set of values on $U\times U$, and their common span is the span of the general plain bilinear product. The common spans are the subspace itself for the centre and for the quaternion subspace, the whole algebra for the vector subspace, the quaternion subspace for the anti-quaternion subspace, and $\mathbb{R}e_t\oplus\mathrm{Vect}(\mathbb{B})$ for the two Hermitian subspaces.

| subspace | common span of the four products | $\dim_{\mathbb{R}}$ |
|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\mathbb{C}_{\mathbb{B}}=A_1\oplus A_2$ | $2$ |
| $\mathrm{Vect}(\mathbb{B})$ | $\mathbb{B}$ | $8$ |
| $\mathbb{H}_{\mathbb{B}}$ | $\mathbb{H}_{\mathbb{B}}=A_1\oplus B_1$ | $4$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $\mathbb{H}_{\mathbb{B}}$ | $4$ |
| $\mathbb{M}_+$ | $A_1\oplus B_1\oplus B_2$ | $7$ |
| $\mathbb{M}_-$ | $A_1\oplus B_1\oplus B_2$ | $7$ |

The table is the first statement of the article: **the four products differ in the structure they leave on the value, not in the value set itself**. The product keeps a subspace inside itself for exactly two of the remarkable subspaces, the centre and the quaternion subspace, and for all four products at once. The vector, anti-quaternion, Hermitian and anti-Hermitian subspaces are closed under none of the four.

### The product, the symmetrisation and the bracket

For a product $f$ the two halves are

$$
\tilde Q_1\bullet_{f}\tilde Q_2=\tfrac12\bigl(f(\tilde Q_1,\tilde Q_2)+f(\tilde Q_2,\tilde Q_1)\bigr),\qquad
[\tilde Q_1,\tilde Q_2]_{f}=f(\tilde Q_1,\tilde Q_2)-f(\tilde Q_2,\tilde Q_1),
$$

so that $f=\bullet_{f}+\tfrac12[\cdot,\cdot]_{f}$. A subspace $U$ is a **Jordan algebra** for $f^{+}$ when the symmetrisation stays in $U$ and the Jordan identity holds there, and a **Lie algebra** for $f^{-}$ when the bracket stays in $U$ and the Jacobi identity holds there. The commutator of an associative product always satisfies Jacobi, so for the general plain bilinear product closure decides the Lie case; for the other three products Jacobi must be tested, and on the whole algebra it fails. The symmetrisation of the general plain bilinear product inherits the Jordan identity from the associative algebra, so closure decides the Jordan case for that product alone.

The result of the three tests, subspace by subspace, is this.

| subspace | closed under the product | Jordan algebra for | Lie algebra for |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | all four | general plain bilinear, general quaternionic bilinear | all four |
| $\mathrm{Vect}(\mathbb{B})$ | none | none | general plain bilinear, general quaternionic bilinear |
| $\mathbb{H}_{\mathbb{B}}$ | all four | general plain bilinear | general plain bilinear, general quaternionic sesquilinear |
| $i\mathbb{H}_{\mathbb{B}}$ | none | none | none |
| $\mathbb{M}_+$ | none | general plain bilinear, general plain sesquilinear | none |
| $\mathbb{M}_-$ | none | none | general plain bilinear, general plain sesquilinear |

The table is the answer; the six sections that follow carry the formulas and the witnesses. Three features of it are worth naming now. The **centre** is the only subspace that is a Lie algebra for all four products. The **quaternion subspace** is the only four-dimensional subspace that is at once closed under the product, a Jordan algebra and a Lie algebra. The **Hermitian and anti-Hermitian subspaces** divide the two halves of the product between them: the symmetrisation survives on $\mathbb{M}_+$ and the bracket on $\mathbb{M}_-$, and neither survives on the other.

## The Four Forms

### The restriction of a form

**Proposition (what the restriction inherits).** Let $U$ be one of the remarkable subspaces and $\varphi$ one of the four forms. The restriction $\varphi|_U$ is a form on the real vector space $U$ that inherits

- the **plain symmetry** $\varphi(\tilde Q_1,\tilde Q_2)=\varphi(\tilde Q_2,\tilde Q_1)$ for the two bilinear forms, and the **conjugate symmetry** $\varphi(\tilde Q_1,\tilde Q_2)=\overline{\varphi(\tilde Q_2,\tilde Q_1)}$ for the two sesquilinear forms;
- the **real scalar laws** $\varphi(\lambda\tilde Q_1,\tilde Q_2)=\varphi(\tilde Q_1,\lambda\tilde Q_2)=\lambda\varphi(\tilde Q_1,\tilde Q_2)$ for $\lambda\in\mathbb{R}$, the conjugate-linear second slot of the two sesquilinear forms being available for complex scalars only on the two complex subspaces;
- the **real–imaginary split** $\varphi=g+i\sigma$, with $g$ a real symmetric bilinear form and $\sigma$ a real bilinear form that is symmetric for the two bilinear forms and alternating for the two sesquilinear forms;
- the **non-degeneracy**: all twenty-four restrictions, four forms on six subspaces, are non-degenerate.

*Proof.* Symmetry and conjugate symmetry are inherited because the two arguments are confined to $U$ and the ambient identity involves nothing outside it. The scalar laws are the ambient ones read on real multiples. For the split, $g=\tfrac12(\varphi+\bar\varphi)$ and $\sigma=\tfrac{1}{2i}(\varphi-\bar\varphi)$ with $\bar\varphi(\tilde Q_1,\tilde Q_2)=\overline{\varphi(\tilde Q_1,\tilde Q_2)}$. For the two bilinear forms, whose $\varphi$ is symmetric, $\bar\varphi$ is symmetric and so is $\sigma$. For the two sesquilinear forms, whose $\varphi$ is conjugate-symmetric, $\bar\varphi(\tilde Q_1,\tilde Q_2)=\varphi(\tilde Q_2,\tilde Q_1)$, so $\sigma=\tfrac{1}{2i}\bigl(\varphi(\tilde Q_1,\tilde Q_2)-\varphi(\tilde Q_2,\tilde Q_1)\bigr)$ is alternating. Non-degeneracy is read on the Gram matrices: the test is that the $2d\times d$ real matrix $[\operatorname{Re}G;\operatorname{Im}G]$ of the Gram matrix $G$ has rank $d$, and on the twenty-four it does.

**Remark (what the algebraic norm does and does not give).** For the two bilinear forms the algebraic norm determines the form, by the polarisation identity

$$
\langle\tilde Q_1,\tilde Q_2\rangle=\tfrac12\bigl(\langle\tilde Q_1+\tilde Q_2\rangle-\langle\tilde Q_1\rangle-\langle\tilde Q_2\rangle\bigr),
$$

and with it the rank. For the two sesquilinear forms the algebraic norm is real and gives only the **real part** $g$; the imaginary part is separate data which the norm does not fix. On the four real-type subspaces the imaginary part happens to vanish, which is the fact the six sections verify; on the two complex subspaces it does not, and there the complex structure ties it to the real part. So the norm is enough for everything on this page, and it is enough for a reason worth keeping: on each remarkable subspace the imaginary part is either accessible through $i$ or zero.

### The two complex subspaces and the four real-type subspaces

The remarkable subspaces fall into two classes, and the class decides whether the four forms have an imaginary part. The test is multiplication by the central imaginary: the two complex subspaces satisfy $iU=U$, the four others satisfy $iU\cap U=\{0\}$.

| subspace | $iU=U$ | $\dim_{\mathbb{R}}$ | field of the values | imaginary part |
|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | yes | $2$ | $\mathbb{C}$ | non-zero, rank $2$ |
| $\mathrm{Vect}(\mathbb{B})$ | yes | $6$ | $\mathbb{C}$ | non-zero, rank $6$ |
| $\mathbb{H}_{\mathbb{B}}$ | no | $4$ | $\mathbb{R}$ | zero |
| $i\mathbb{H}_{\mathbb{B}}$ | no | $4$ | $\mathbb{R}$ | zero |
| $\mathbb{M}_+$ | no | $4$ | $\mathbb{R}$ | zero |
| $\mathbb{M}_-$ | no | $4$ | $\mathbb{R}$ | zero |

On the two **complex subspaces**, the centre and the vector subspace, all four forms are complex-valued, their imaginary parts are non-zero and non-degenerate, and the multiplication by $i$ is available inside the subspace, so the alternating companion is read off the real part by the Kähler identity below. On the four **real-type subspaces**, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$ and $\mathbb{M}_-$, all four forms are real-valued, their imaginary parts vanish, and each form is a real symmetric bilinear form recovered from its algebraic norm.

**The four forms carry a phase structure on the two complex subspaces and none on the four real-type subspaces.** The rest of the article verifies this subspace by subspace and draws its consequences.

### The real and imaginary parts

**Proposition (the split of a form on a subspace).** For each remarkable subspace and each of the four forms, $\varphi=g+i\sigma$ with $g$ real symmetric and $\sigma$ real, symmetric for the two bilinear forms and alternating for the two sesquilinear forms. The imaginary part vanishes identically on the four real-type subspaces, and on the two complex subspaces it is non-zero and non-degenerate, of rank $2$ on the centre and of rank $6$ on the vector subspace.

The proof is the proposition of $\S$*The restriction of a form* for the symmetry, the six sections for the vanishing, and the two Gram matrices of the centre and the vector subspace for the ranks.

**The Kähler identity.** On the two complex subspaces the alternating part of the two sesquilinear forms is the real part composed with the complex structure,

$$
\boxed{\;\omega(\tilde Q_1,\tilde Q_2)=g(\tilde Q_1,i\tilde Q_2)\;}
$$

for all $\tilde Q_1,\tilde Q_2$ in the subspace. *Proof.* $\langle\tilde Q_1,i\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1(i\tilde Q_2)^{*})$ and $(i\tilde Q_2)^{*}=-i\tilde Q_2^{*}$, since ${}^{*}$ is the coefficientwise conjugation composed with ${}^{\natural}$ and the two commute with $i$; so $\langle\tilde Q_1,i\tilde Q_2\rangle_{*}=-i\langle\tilde Q_1,\tilde Q_2\rangle_{*}$, whose real part is the imaginary part of the Hermitian form and whose imaginary part is minus its real part. The same computation holds for the Krein form.

**The companion identity for the bilinear pair.** The same computation with the second slot read without the star gives $\langle\tilde Q_1,i\tilde Q_2\rangle=i\langle\tilde Q_1,\tilde Q_2\rangle$, since a scalar pulls out of a bilinear slot without conjugation, and the real part of $i(g_{\mathrm{pl}}+i\sigma_{\mathrm{pl}})$ is $-\sigma_{\mathrm{pl}}$. Hence

$$
\boxed{\;\omega(\tilde Q_1,\tilde Q_2)=+g(\tilde Q_1,i\tilde Q_2)\ \text{for the two sesquilinear forms},\qquad
\sigma(\tilde Q_1,\tilde Q_2)=-g(\tilde Q_1,i\tilde Q_2)\ \text{for the two bilinear forms}\;}
$$

on the two complex subspaces, and the one sign is the whole difference between the two pairs. The identity says that the alternating part is not a second independent object on top of the real part: it is the real part read through the complex structure, and it is available only where the complex structure is. On the four real-type subspaces the complex structure leaves the subspace and the identity has no content.

**The two slotted conjugations and the two pairings.** The imaginary part of a form is symmetric when the form is bilinear and alternating when the form is sesquilinear, and the second slot is the slot that decides it: the star conjugates $i$ and flips the sign of the companion identity, and the conjugate symmetry of the two sesquilinear forms then forces their imaginary part to be alternating. The first slot, the natural conjugation, does not touch the value: it is applied before the two elements are multiplied, and no conjugation of $i$ reaches the product. The difference between the two families in the table of the imaginary part is the difference between the two second slots and nothing else.

### The Alternating Forms on the Whole Space

The imaginary parts of the two Hermitian forms are alternating forms on the whole algebra,
$$
\omega_{*}(\tilde Q_1,\tilde Q_2)=\operatorname{Im}\langle\tilde Q_1,\tilde Q_2\rangle_{*},\qquad
\omega_{\natural*}(\tilde Q_1,\tilde Q_2)=\operatorname{Im}\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*} .
$$
In the real coordinates $q_\mu,q'_\mu$ each is a direct sum over the four coefficients of the standard symplectic form on the pair $(q_\mu,q'_\mu)$, with the sign $\varepsilon_\mu$ for $\omega_{\natural*}$, so both are non-degenerate and of rank $8$. The real-linear isometry group of each is the real symplectic group $Sp(8,\mathbb{R})$, of real dimension $36$; the complex-linear isometries are $\mathrm{U}(4)$ for $\omega_{*}$ and $\mathrm{U}(1,3)$ for $\omega_{\natural*}$, the unitary groups of the two Hermitian forms; and the maximal isotropic subspaces are the Lagrangian planes, of real dimension $4$.

The two are **not** the scalar parts of the two antisymmetrised sesquilinear products. Those values are pure vector and their scalar part vanishes; the alternating forms are the scalar parts, divided by $2i$, of the two sesquilinear commutators,
$$
\omega_{*}=\tfrac{1}{2i}\operatorname{Sc}[\tilde Q_1,\tilde Q_2]_\varsigma ,
$$
and $\omega_{\natural*}$ is the corresponding object of the quaternionic family. The distinction is the one between a product and a form: the pure-vector value is the antisymmetrised product, whose Jacobi identity is a separate question, while the scalar part is a symplectic form, with isometry group $Sp(8,\mathbb{R})$ and Lagrangian planes.


## The Four Algebraic Norms

**The diagonal.** The restriction of an algebraic norm to a subspace $U$ is the ambient norm read on the elements of $U$, and it is the diagonal of the restricted form, $\langle\tilde Q\rangle=\varphi(\tilde Q,\tilde Q)$. On the four real-type subspaces the form is real and the norm recovers it by polarisation; on the two complex subspaces the norm is complex and the polarisation recovers the bilinear forms but gives only the real part of the sesquilinear ones. The signatures below are the signatures over $\mathbb{R}$ of the real quadratic form obtained by realifying $U$; on the two complex subspaces they are the signatures of the real parts of the complex norms.

The values are these, in the coordinates of each subspace.

| subspace | element | plain | Hermitian | quaternionic | Krein |
|---|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $Ae_t$ | $A^{2}$ | $\lvert A\rvert^{2}$ | $A^{2}$ | $\lvert A\rvert^{2}$ |
| $\mathrm{Vect}(\mathbb{B})$ | $\vec P$ | $-\sum_kP_k^{2}$ | $\sum_k\lvert P_k\rvert^{2}$ | $\sum_kP_k^{2}$ | $-\sum_k\lvert P_k\rvert^{2}$ |
| $\mathbb{H}_{\mathbb{B}}$ | $h$ | $h_t^{2}-\lvert\vec h\rvert^{2}$ | $\lvert h\rvert^{2}$ | $\lvert h\rvert^{2}$ | $h_t^{2}-\lvert\vec h\rvert^{2}$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $ih$ | $-h_t^{2}+\lvert\vec h\rvert^{2}$ | $\lvert h\rvert^{2}$ | $-\lvert h\rvert^{2}$ | $h_t^{2}-\lvert\vec h\rvert^{2}$ |
| $\mathbb{M}_+$ | $a_te_t+i\vec p$ | $a_t^{2}+\lvert\vec p\rvert^{2}$ | $a_t^{2}+\lvert\vec p\rvert^{2}$ | $a_t^{2}-\lvert\vec p\rvert^{2}$ | $a_t^{2}-\lvert\vec p\rvert^{2}$ |
| $\mathbb{M}_-$ | $ib_te_t+\vec q$ | $-b_t^{2}-\lvert\vec q\rvert^{2}$ | $b_t^{2}+\lvert\vec q\rvert^{2}$ | $-b_t^{2}+\lvert\vec q\rvert^{2}$ | $b_t^{2}-\lvert\vec q\rvert^{2}$ |

The signatures are these.

| subspace | plain | Hermitian | quaternionic | Krein |
|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $(1,1)$ | $(2,0)$ | $(1,1)$ | $(2,0)$ |
| $\mathrm{Vect}(\mathbb{B})$ | $(3,3)$ | $(6,0)$ | $(3,3)$ | $(0,6)$ |
| $\mathbb{H}_{\mathbb{B}}$ | $(1,3)$ | $(4,0)$ | $(4,0)$ | $(1,3)$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $(3,1)$ | $(4,0)$ | $(0,4)$ | $(1,3)$ |
| $\mathbb{M}_+$ | $(4,0)$ | $(4,0)$ | $(1,3)$ | $(1,3)$ |
| $\mathbb{M}_-$ | $(0,4)$ | $(4,0)$ | $(3,1)$ | $(1,3)$ |

**The collapses.** The four norms collapse on every subspace, to two functions or to two pairs of opposites, and the pattern of the collapse is the signature pattern. On the centre $\langle\cdot\rangle=\langle\cdot\rangle_{\natural}$ and $\langle\cdot\rangle_{*}=\langle\cdot\rangle_{\natural*}$; on the quaternion subspace $\langle\cdot\rangle=\langle\cdot\rangle_{\natural*}$ and $\langle\cdot\rangle_{*}=\langle\cdot\rangle_{\natural}$; on the anti-quaternion subspace $\langle\cdot\rangle=-\langle\cdot\rangle_{\natural*}$ and $\langle\cdot\rangle_{*}=-\langle\cdot\rangle_{\natural}$; on the vector subspace $\langle\cdot\rangle=-\langle\cdot\rangle_{\natural}$ and $\langle\cdot\rangle_{*}=-\langle\cdot\rangle_{\natural*}$; on $\mathbb{M}_+$ $\langle\cdot\rangle=\langle\cdot\rangle_{*}$ and $\langle\cdot\rangle_{\natural}=\langle\cdot\rangle_{\natural*}$; on $\mathbb{M}_-$ $\langle\cdot\rangle=-\langle\cdot\rangle_{*}$ and $\langle\cdot\rangle_{\natural}=-\langle\cdot\rangle_{\natural*}$. The collapses are not an accident of the coordinates: they are the fixed- and anti-fixed-space conditions of the four conjugations read on the norms. The signatures are the record of the signs, and the definiteness of each norm is the record of the signatures.

## The Centre Subspace

**The centre is both a Jordan algebra and a Lie algebra, and it is the only subspace that is a Lie algebra for all four products.** A central element is $Ae_t$ with $A\in\mathbb{C}$. The subspace is the fixed set of the natural conjugation ${}^{\natural}$, of real dimension two and complex dimension one, and it is the centre of the algebra. In the blocks of *Comparison of the Remarkable Subspaces* it is $A_1\oplus A_2$.

### The Four General Products

Because $Ae_t$ commutes with every element, the two products built on ${}^{\natural}$ are the plain product of the scalars, and the two built on ${}^{*}$ conjugate the second scalar:

$$
(Ae_t)(Ce_t)=(Ae_t)^{\natural}(Ce_t)=ACe_t,\qquad
(Ae_t)(Ce_t)^{*}=(Ae_t)^{\natural}(Ce_t)^{*}=A\overline{C}e_t.
$$

The two bilinear products therefore coincide on the centre, as do the two sesquilinear ones, and **all four keep the centre inside itself**; the first pair is the multiplication of $\mathbb{C}$ read inside the algebra. The centre is, with the quaternion subspace, one of the two subspaces closed under the product, and it is the only one of the six that is commutative for the two bilinear products, where it is the field $\mathbb{C}$ and is associative; the two sesquilinear products are neither commutative nor associative.

**The symmetrisation.** The symmetrised general plain bilinear product is again the multiplication of $\mathbb{C}$, and the symmetrised general quaternionic bilinear product is the same function:

$$
(Ae_t)\bullet_{\mathrm{pl}}(Be_t)=(Ae_t)\bullet(Be_t)=ABe_t.
$$

The centre is therefore a **Jordan algebra** for those two products, namely the field $\mathbb{C}$ itself. The two sesquilinear symmetrisations stay in the centre as well, but give **no Jordan algebra**: their common value,

$$
(Ae_t)\bullet_{*}(Be_t)=(Ae_t)\bullet_{\natural*}(Be_t)=\operatorname{Re}(A\overline{B})\,e_t,
$$

is commutative but only real-bilinear, and the Jordan identity fails. The failure is at $x=ie_t$, where $x\bullet_{*}x=e_t$, so that the two sides of $(x\bullet_{*}x)\bullet_{*}(x\bullet_{*}x)=x\bullet_{*}\bigl(x\bullet_{*}(x\bullet_{*}x)\bigr)$ are $e_t$ and $0$.

**The bracket.** The two bilinear brackets vanish on the centre, which is therefore an **abelian Lie algebra** for both. The two sesquilinear brackets do not vanish, and they agree:

$$
[Ae_t,Be_t]_{*}=[Ae_t,Be_t]_{\natural*}=2i\,\operatorname{Im}(A\overline{B})\,e_t.
$$

The bracket of two central elements is a real multiple of $ie_t$, so the derived subalgebra is the line $\mathbb{R}(ie_t)$, of dimension one and solvable. The algebra is not abelian, since $[e_t,ie_t]_{*}=[e_t,ie_t]_{\natural*}=-2ie_t$, and Jacobi holds. The real span of $e_t$ and $ie_t$ under that bracket is the **two-dimensional non-abelian Lie algebra**, the only one of dimension two up to isomorphism. The centre is thus a **Lie algebra for all four general products**: the one-dimensional abelian algebra for the two bilinear ones and the two-dimensional non-abelian algebra for the two sesquilinear ones.

### The Four Forms

On the centre the four forms collapse to two, the plain with the quaternionic and the Hermitian with the Krein:

$$
\langle\tilde Q_1,\tilde Q_2\rangle=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=AC,\qquad
\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=A\overline{C}.
$$

The first is the complex quadratic form $AC$ of the pair, the second the Hermitian form $A\overline{C}$. The collapse has one reason: the natural conjugation fixes the centre, so the first slot of the product is idle there and the difference between the plain and the quaternionic families disappears.

Writing $A=a+ib$ and $C=c+id$ with real coordinates,

$$
AC=(ac-bd)+i(ad+bc),\qquad
A\overline{C}=(ac+bd)+i(bc-ad).
$$

The first has a real part of signature $(1,1)$ and an imaginary part $\sigma_{\mathrm{pl}}=\sigma_{\natural}=ad+bc$, symmetric and of rank $2$; the second has a positive definite real part of signature $(2,0)$ and an imaginary part $\omega_{*}=\omega_{\natural*}=bc-ad$, alternating, of rank $2$. In the complex basis $(e_t)$ the Gram matrix of each of the four is the single entry

$$
\langle\cdot,\cdot\rangle=\langle\cdot,\cdot\rangle_{\natural}=\langle\cdot,\cdot\rangle_{*}=\langle\cdot,\cdot\rangle_{\natural*}=(1),
$$

non-singular, so all four restrictions are non-degenerate. In the real basis $(e_t,ie_t)$ the two parts are

$$
g_{\mathrm{pl}}=g_{\natural}=\begin{pmatrix}1&0\\ 0&-1\end{pmatrix},\qquad
\sigma_{\mathrm{pl}}=\sigma_{\natural}=\begin{pmatrix}0&1\\ 1&0\end{pmatrix},\qquad
g_{*}=g_{\natural*}=\mathrm I_2,\qquad
\omega_{*}=\omega_{\natural*}=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}.
$$

The single entry $(1)$ and the pair $(g,\sigma)$ carry the same information, the second being the first with its real and imaginary parts separated; the two real parts have signatures $(1,1)$ and $(2,0)$, which the complex matrix cannot show. The alternating form $\omega$ is non-degenerate, of rank $2$, and on the pair of real basis vectors it takes the value $\omega(e_t,ie_t)=-1$.

**The null set of each of the four on the centre is the origin alone.** The two bilinear forms vanish when $A^{2}=0$, and the centre has no zero divisors, so $A=0$; the two sesquilinear forms vanish when $\lvert A\rvert^{2}=0$, which is again $A=0$. The ambient null sets, the complex cone of the plain form and the zero-divisor cone of the quaternionic form, meet the centre in the origin alone.

### The Four Algebraic Norms

The four norms are the four forms at two equal arguments:

$$
\langle\tilde Q\rangle=\langle\tilde Q\rangle_{\natural}=A^{2},\qquad
\langle\tilde Q\rangle_{*}=\langle\tilde Q\rangle_{\natural*}=\lvert A\rvert^{2}.
$$

The two bilinear norms coincide and are the complex square; the two sesquilinear norms coincide and are the modulus square. Their signatures over $\mathbb{R}$ are $(1,1)$ and $(2,0)$ respectively, the same as the real parts of the forms. The norm $\langle\cdot\rangle_{*}$ is definite and $\langle\cdot\rangle$ is indefinite; the null set of the first is the origin, and the real null cone of the second is the pair of lines $\mathbb{R}(e_t\pm ie_t)$, which is not the complex null set, the origin.


## The Vector Subspace

**The vector subspace is a Lie algebra but not a Jordan algebra.** Under the two bilinear brackets it is $(\mathrm{Vect}(\mathbb{B}),[\cdot,\cdot])\cong\mathfrak{sl}(2,\mathbb{C})$, the general quaternionic bilinear bracket being the negative of the commutator, and it is **no Jordan algebra** for any of the four symmetrisations.

A pure vector is $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ with $Q_k\in\mathbb{C}$. Its scalar part vanishes and the natural conjugation reverses its sign, so the subspace, of real dimension six and complex dimension three, is the largest of the remarkable subspaces and the complex analogue of the imaginary quaternions. In the blocks it is $B_1\oplus B_2$. The three operations behave here as differently as anywhere: the product leaves the subspace at once, the symmetrisation collapses to the centre or to the Hermitian subspace, and only the bracket stays.

### The Four General Products

The square of a single basis vector already leaves the subspace, and is a nonzero central scalar for each of the four products:

$$
\vec e_x\vec e_x=-e_t,\qquad \vec e_x^{\natural}\vec e_x=e_t,\qquad \vec e_x\vec e_x^{*}=e_t,\qquad \vec e_x^{\natural}\vec e_x^{*}=-e_t.
$$

In general the product of two pure vectors is the sum of a scalar and a vector:

$$
\vec P\vec Q=-(\vec P,\vec Q)e_t+\vec P\times\vec Q,\qquad
\vec P^{\natural}\vec Q=(\vec P,\vec Q)e_t-\vec P\times\vec Q,
$$
$$
\vec P\vec Q^{*}=(\vec P,\overline{\vec Q})e_t-\vec P\times\overline{\vec Q},\qquad
\vec P^{\natural}\vec Q^{*}=-(\vec P,\overline{\vec Q})e_t+\vec P\times\overline{\vec Q}.
$$

The four products therefore have the same scalar–vector shape on the vector subspace, with the second factor conjugated where the star is present: $f_{\mathrm{pl}}$ and $f_{\natural*}$ with the sign of the plain product, and $f_{\natural}$ and $f_{\mathrm{pl}*}$ with the opposite signs. Since the scalar part is a general complex number and the vector part a general vector, each of the four products of a suitable pair **spans the whole algebra**, of real dimension eight. The vector subspace is therefore closed under **none of the four general products**.

**The symmetrisation.** No symmetrisation keeps the vector subspace inside itself either, and the bilinear and the sesquilinear products part company. The two bilinear symmetrisations collapse to the centre, the cross-product terms cancelling:

$$
\vec P\bullet_{\mathrm{pl}}\vec Q=-(\vec P,\vec Q)e_t,\qquad
\vec P\bullet\vec Q=(\vec P,\vec Q)e_t,
$$

so the pair $\vec P=\vec Q=\vec e_x$ has plain symmetrisation $-e_t$ and quaternionic symmetrisation $e_t$, a central element outside the subspace in either case. The contrast is sharp: the same two pure vectors whose plain product spans the whole algebra have their symmetrised product confined to the two-dimensional centre. The two sesquilinear symmetrisations land in the Hermitian subspace as well, and in fact in its central line,

$$
\vec P\bullet_{*}\vec Q=\tfrac12\bigl(\vec P\vec Q^{*}+\vec Q\vec P^{*}\bigr)=\operatorname{Re}(\vec P,\overline{\vec Q})\,e_t,\qquad
\vec P\bullet_{\natural*}\vec Q=-\operatorname{Re}(\vec P,\overline{\vec Q})\,e_t,
$$

again outside the vector subspace. The vector subspace is therefore a **Jordan algebra for none** of the four products. The collapse $\vec P\bullet_{\mathrm{pl}}\vec P=-(\vec P,\vec P)e_t$ explains the square-zero elements of the vector subspace, which are its zero divisors (*Introduction to the Remarkable Subspaces*).

**The bracket.** The commutator keeps the vector subspace inside itself, because the scalar part is symmetric and cancels:

$$
[\vec P,\vec Q]=2\,\vec P\times\vec Q\in\mathrm{Vect}(\mathbb{B}),\qquad
[\mathrm{Vect}(\mathbb{B}),\mathrm{Vect}(\mathbb{B})]=\mathrm{Vect}(\mathbb{B}).
$$

The bracket of two pure vectors is twice their complex cross product, and the cross products fill the whole subspace, so the algebra is perfect. It is the complex **Lie algebra $\mathfrak{sl}(2,\mathbb{C})$**, of complex dimension three, read in the coordinates $\vec e_x,\vec e_y,\vec e_z$ against the Pauli matrices. The general quaternionic bilinear bracket is the negative of the commutator,

$$
[\vec P,\vec Q]_{\natural}=(-\vec P)\vec Q-(-\vec Q)\vec P=-[\vec P,\vec Q],
$$

so it is a **Lie algebra** too, the same one with the opposite sign. The two sesquilinear brackets leave the subspace: their values are anti-Hermitian and fill $\mathbb{M}_-$,

$$
[\mathrm{Vect}(\mathbb{B}),\mathrm{Vect}(\mathbb{B})]_{*}=[\mathrm{Vect}(\mathbb{B}),\mathrm{Vect}(\mathbb{B})]_{\natural*}=\mathbb{M}_-,
$$

with the witness $[\vec e_x,i\vec e_x]_{*}=-2ie_t\notin\mathrm{Vect}(\mathbb{B})$. The vector subspace is therefore a **Lie algebra for exactly the two bilinear products** and a **Jordan algebra for none**; of the three operations only the antisymmetric half is carried by the subspace, and there it reproduces the classical Lie algebra of the whole algebra.

### The Four Forms

On the vector subspace the four forms are

$$
\langle\tilde Q_1,\tilde Q_2\rangle=-\sum_kP_{1,k}P_{2,k},\qquad
\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\sum_kP_{1,k}\overline{P_{2,k}},
$$
$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\sum_kP_{1,k}P_{2,k},\qquad
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=-\sum_kP_{1,k}\overline{P_{2,k}},
$$

so that $\langle\cdot,\cdot\rangle=-\langle\cdot,\cdot\rangle_{\natural}$ and $\langle\cdot,\cdot\rangle_{\natural*}=-\langle\cdot,\cdot\rangle_{*}$: the pair of bilinear forms is one complex symmetric form and its negative, and the pair of sesquilinear forms one Hermitian form and its negative.

Writing $P_{1,k}=p_k+iq_k$ and $P_{2,k}=r_k+is_k$ with real coordinates, the real part of the Hermitian form is the positive definite sum $g_{*}=\sum_k(p_kr_k+q_ks_k)$, of signature $(6,0)$, and its imaginary part is $\omega_{*}=\sum_k(q_kr_k-p_ks_k)$, alternating and of rank $6$. In the complex basis $(\vec e_x,\vec e_y,\vec e_z)$ the Gram matrices are

$$
\langle\cdot,\cdot\rangle=\langle\cdot,\cdot\rangle_{\natural*}=-\mathrm I_3,\qquad \langle\cdot,\cdot\rangle_{\natural}=\langle\cdot,\cdot\rangle_{*}=\mathrm I_3,
$$

each a multiple of the identity, hence non-singular of rank $3$: all four restrictions are non-degenerate, and the two families differ by one overall sign alone. In the real basis $(\vec e_x,i\vec e_x,\vec e_y,i\vec e_y,\vec e_z,i\vec e_z)$ the two parts are block sums of three copies of the elementary symplectic matrix, one in each coordinate plane $(\vec e_k,i\vec e_k)$:

$$
g_{*}=\mathrm I_6,\qquad
\omega_{*}=\begin{pmatrix}0&-1&0&0&0&0\\ 1&0&0&0&0&0\\ 0&0&0&-1&0&0\\ 0&0&1&0&0&0\\ 0&0&0&0&0&-1\\ 0&0&0&0&1&0\end{pmatrix},
$$

of ranks $6$ and $6$. The signatures of the real parts are $(3,3)$ for the two bilinear forms, $(6,0)$ for the Hermitian form and $(0,6)$ for the Krein form.

**The null sets on the vector subspace are two cones and two origins.** The two bilinear forms vanish on the complex cone $\sum_kP_k^{2}=0$, of real dimension four, the zero divisors of the vector subspace; the two sesquilinear forms vanish when $\sum_k\lvert P_k\rvert^{2}=0$, which is $P=0$. So the two bilinear forms have a genuine cone on the vector subspace while the two sesquilinear forms have none, exactly in reverse of the centre.

### The Four Algebraic Norms

The four norms are

$$
\langle\tilde Q\rangle=-\sum_kP_k^{2},\qquad
\langle\tilde Q\rangle_{*}=\sum_k\lvert P_k\rvert^{2},\qquad
\langle\tilde Q\rangle_{\natural}=\sum_kP_k^{2},\qquad
\langle\tilde Q\rangle_{\natural*}=-\sum_k\lvert P_k\rvert^{2},
$$

so that $\langle\cdot\rangle=-\langle\cdot\rangle_{\natural}$ and $\langle\cdot\rangle_{*}=-\langle\cdot\rangle_{\natural*}$. The signatures are $(3,3)$, $(6,0)$, $(3,3)$ and $(0,6)$ for $\langle\cdot\rangle$, $\langle\cdot\rangle_{*}$, $\langle\cdot\rangle_{\natural}$ and $\langle\cdot\rangle_{\natural*}$ in that order. The two bilinear norms are complex-valued and indefinite; the Hermitian norm is positive definite and the Krein norm negative definite. The vector subspace is thus the subspace on which the two sesquilinear norms are definite and the two bilinear ones are not, the exact reverse of the centre.


## The Quaternion Subspace

**The quaternion subspace is both a Jordan algebra and a Lie algebra.** Under $\bullet_{\mathrm{pl}}$ it is the symmetrised real quaternion algebra, and under $[\cdot,\cdot]$ and $[\cdot,\cdot]_{\natural*}$ it is $\mathbb{R}e_t\oplus\mathfrak{su}(2)$.

A quaternion element is $h=h_te_t+h_x\vec e_x+h_y\vec e_y+h_z\vec e_z$ with all four coefficients real. The subspace is the fixed set of the coefficientwise conjugation $\bar{\cdot}$, of real dimension four, and it is the real quaternion algebra $\mathbb{H}$. In the blocks it is $A_1\oplus B_1$. It is the larger of the two subspaces closed under the product, and, with the centre, one of the two that carry all three structures at once. Unlike the centre it is non-commutative, and the three structures are spread over the four products rather than shared between them.

### The Four General Products

**All four keep the quaternion subspace inside itself**; on the real quaternions they read $hg$, $\bar h g$, $h\bar g$ and $\bar h\bar g=\overline{gh}$:

$$
\boxed{\;\mathbb{H}_{\mathbb{B}}\mathbb{H}_{\mathbb{B}}=\mathbb{H}_{\mathbb{B}},\quad
\mathbb{H}_{\mathbb{B}}^{\natural}\mathbb{H}_{\mathbb{B}}=\mathbb{H}_{\mathbb{B}},\quad
\mathbb{H}_{\mathbb{B}}\mathbb{H}_{\mathbb{B}}^{*}=\mathbb{H}_{\mathbb{B}},\quad
\mathbb{H}_{\mathbb{B}}^{\natural}\mathbb{H}_{\mathbb{B}}^{*}=\mathbb{H}_{\mathbb{B}}\;}.
$$

It is therefore closed under all four products at once, and it is an associative subalgebra for exactly one of them, the general plain bilinear product; under that product it is the division algebra of the real quaternions, since the norm is a sum of four real squares and vanishes only at the origin. The other three products are not associative there: their counterexamples in *The Four General Products and Their Relations over the Biquaternion Algebra* §*The Failure of Associativity* are triples of the quaternion subspace, so each of them fails associativity inside the subspace already.

**The symmetrisation.** Only the general plain bilinear symmetrisation gives a **Jordan algebra**:

$$
\mathbb{H}_{\mathbb{B}}\bullet_{\mathrm{pl}}\mathbb{H}_{\mathbb{B}}=\mathbb{H}_{\mathbb{B}},
$$

the symmetrisation of the real quaternion algebra, a commutative Jordan algebra of real dimension four. The other three symmetrisations stay inside the subspace but **fail the Jordan identity**, so the quaternion subspace, closed under all four products, is a Jordan algebra for exactly one of them. The general plain sesquilinear and the general quaternionic bilinear symmetrisations coincide there and collapse to the centre:

$$
h\bullet k=h\bullet_{*}k=\bigl(h_tk_t+(\vec h,\vec k)\bigr)e_t,
$$

the trace form of the general quaternionic bilinear product; the general quaternionic sesquilinear one is the natural conjugate of the Jordan product, $h\bullet_{\natural*}k=(h\bullet_{\mathrm{pl}}k)^{\natural}$. Each of the three fails the identity at $x=\vec e_x$: for the general plain sesquilinear and the general quaternionic bilinear symmetrisations $x\bullet x=e_t$, so the two sides of $(x\bullet x)\bullet(x\bullet x)=x\bullet\bigl(x\bullet(x\bullet x)\bigr)$ are $e_t$ and $0$; for the general quaternionic sesquilinear one, where $x\bullet_{\natural*}x=-e_t$, they are $e_t$ and $-e_t$.

**The bracket.** The commutator stays inside the subspace and gives a **Lie algebra**:

$$
\boxed{\;[\mathbb{H}_{\mathbb{B}},\mathbb{H}_{\mathbb{B}}]=B_1,\qquad
(\mathbb{H}_{\mathbb{B}},[\cdot,\cdot])\cong\mathbb{R}e_t\oplus\mathfrak{su}(2)\;},
$$

the bracket of two real quaternions being twice the real cross product of their vector parts, a pure real quaternion, which is why the subspace closes. The derived subalgebra is $B_1$, the imaginary quaternions, which under the cross product is the Lie algebra $\mathfrak{su}(2)$ of $SU(2)$; the line $\mathbb{R}e_t$ is central, because $e_t$ is central in the algebra, so the Lie algebra of the subspace is $\mathbb{R}e_t\oplus\mathfrak{su}(2)$. The general quaternionic sesquilinear bracket is the commutator itself, the two conjugations cancelling on the subspace,

$$
[\mathbb{H}_{\mathbb{B}},\mathbb{H}_{\mathbb{B}}]_{\natural*}=[\mathbb{H}_{\mathbb{B}},\mathbb{H}_{\mathbb{B}}],
$$

so the quaternion subspace is a Lie algebra for the general plain bilinear product and for the general quaternionic sesquilinear product. The general plain sesquilinear and general quaternionic bilinear brackets stay inside — their values are pure vectors — but **fail the Jacobi identity**, at the triple $(e_t,\vec e_x,\vec e_y)$, where the cyclic sum is $+4\vec e_z$ for the general quaternionic bilinear bracket and $-4\vec e_z$ for the general plain sesquilinear one. The quaternion subspace is thus, with the centre, one of the two subspaces that are at once closed under the product, a Jordan algebra and a Lie algebra; of the four products the general plain bilinear one carries both structures, and the general quaternionic sesquilinear one the Lie structure alone.

### The Four Forms

On the quaternion subspace the four forms collapse to two, the plain with the Krein and the quaternionic with the Hermitian:

$$
\langle\tilde Q_1,\tilde Q_2\rangle=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=h_tk_t-\sum_{j=1}^{3}h_jk_j,\qquad
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\sum_{\mu\in\{t,x,y,z\}}h_\mu k_\mu.
$$

They are the two classical real forms of the quaternion algebra: the **Minkowski form** $h_tk_t-(\vec h,\vec k)$ of signature $(1,3)$ and the **Euclidean form** $(\vec h,\vec k)_{\mathbb{R}^4}$ of signature $(4,0)$. All four are real-valued, so the imaginary part vanishes identically and the splitting of each form into real and imaginary parts is the form itself. The Gram matrices are the diagonal matrices $\operatorname{diag}(1,-1,-1,-1)$ for the plain and the Krein forms and $\mathrm I_4$ for the Hermitian and the quaternionic forms, both of full rank, so all four restrictions are non-degenerate.

**The null sets are one null cone and two origins.** The plain and the Krein forms vanish on the real null cone $h_t^{2}=\lvert\vec h\rvert^{2}$, of real dimension three; the Hermitian and the quaternionic forms vanish at the origin alone. This is the subspace on which the Minkowski form is the algebraic norm of the plain and the Krein forms, and the Euclidean form that of the Hermitian and the quaternionic forms.

### The Four Algebraic Norms

The four norms are

$$
\langle\tilde Q\rangle=\langle\tilde Q\rangle_{\natural*}=h_t^{2}-\sum_{j=1}^{3}h_j^{2},\qquad
\langle\tilde Q\rangle_{*}=\langle\tilde Q\rangle_{\natural}=\sum_{\mu\in\{t,x,y,z\}}h_\mu^{2}.
$$

The bilinear plain norm and the quaternionic sesquilinear norm coincide and are the Minkowski norm, of signature $(1,3)$; the plain sesquilinear and quaternionic bilinear norms coincide and are the Euclidean norm, of signature $(4,0)$. The first is indefinite and the second is positive definite; this is the one subspace on which the Euclidean algebraic norm is also the norm of a bilinear form, and the reason the quaternion subspace is the real quaternion algebra inside the biquaternion algebra.

## The Anti-Quaternion Subspace

**The anti-quaternion subspace carries no algebra at all.** It is neither a Jordan nor a Lie algebra, for any product, any symmetrisation or any bracket; its only structure is that of a two-sided module over the quaternion subspace.

An anti-quaternion element is $ih$ with $h$ a real quaternion. The subspace equals $i\mathbb{H}_{\mathbb{B}}$, has real dimension four, and is the anti-fixed set of the coefficientwise conjugation, $\overline{ih}=-ih$. In the blocks it is $A_2\oplus B_2$, and it is the odd part of the $\mathbb{Z}/2$-grading whose even part is the quaternion subspace.

### The Four General Products

**None of the four keeps the anti-quaternion subspace inside itself.** The four products of a pair fall back into the quaternion subspace, the two factors being odd:

$$
(ih)(ik)=-hk,\qquad
(ih)^{\natural}(ik)=-\bar h k,\qquad
(ih)(ik)^{*}=h\bar k,\qquad
(ih)^{\natural}(ik)^{*}=\bar h\bar k=\overline{kh}.
$$

Each of the four **spans $\mathbb{H}_{\mathbb{B}}$**, so the anti-quaternion subspace is closed under none of the four products. The product of two odd elements is even, which is the statement that $\mathbb{B}=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$ is a grading, and the anti-quaternion subspace is a two-sided module over the quaternion subspace, the module structure being the only structure it carries.

**The symmetrisation.** **No symmetrisation keeps the anti-quaternion subspace inside itself** either; every value is even:

$$
(ih)\bullet_{\mathrm{pl}}(ik)=-h\bullet_{\mathrm{pl}}k,\qquad
(ih)\bullet(ik)=-\bigl(h\bullet k\bigr)\in\mathbb{R}e_t,\qquad
(ih)\bullet_{*}(ik)=h\bullet_{*}k\in\mathbb{R}e_t,\qquad
(ih)\bullet_{\natural*}(ik)=\bigl(h\bullet_{\mathrm{pl}}k\bigr)^{\natural}\in\mathbb{H}_{\mathbb{B}},
$$

the first and the fourth lying in the quaternion subspace, the second and the third in the centre. The anti-quaternion subspace is therefore a **Jordan algebra for none** of the four products.

**The bracket.** **No bracket keeps the anti-quaternion subspace inside itself** either; every value is again even:

$$
[ih,ik]=-[h,k],\qquad
[ih,ik]_{\natural}=-[h,k]_{\natural},\qquad
[ih,ik]_{*}=[h,k]_{*},\qquad
[ih,ik]_{\natural*}=[h,k],
$$

each lying in $B_1\subset\mathbb{H}_{\mathbb{B}}$. The subspace has an imaginary scalar part and an imaginary vector part, and every value above is real, so nothing returns. It is a **Lie algebra for none** of the four products and, with the symmetrisations, the subspace carries **no algebra at all**: not for the product and not for either of its two halves.

### The Four Forms

On the anti-quaternion subspace the four forms are

$$
P(\tilde Q_1,\tilde Q_2)=-h_tk_t+\sum_{j=1}^{3}h_jk_j,\qquad
H(\tilde Q_1,\tilde Q_2)=\sum_{\mu\in\{t,x,y,z\}}h_\mu k_\mu,
$$
$$
N(\tilde Q_1,\tilde Q_2)=-\sum_{\mu\in\{t,x,y,z\}}h_\mu k_\mu,\qquad
K(\tilde Q_1,\tilde Q_2)=h_tk_t-\sum_{j=1}^{3}h_jk_j,
$$

so that $\langle\cdot,\cdot\rangle=-\langle\cdot,\cdot\rangle_{\natural*}$ and $\langle\cdot,\cdot\rangle_{\natural}=-\langle\cdot,\cdot\rangle_{*}$: each is the negative of the corresponding form on the quaternion subspace, the plain of the Krein and the quaternionic of the Hermitian, and the two sign changes are those of the translation by $i$. The signatures are $(3,1)$ for the plain form, $(4,0)$ for the Hermitian, $(0,4)$ for the quaternionic and $(1,3)$ for the Krein, and the Gram matrices are $\operatorname{diag}(-1,1,1,1)$, $\mathrm I_4$, $-\mathrm I_4$ and $\operatorname{diag}(1,-1,-1,-1)$, all of full rank. All four are real-valued, so the imaginary part vanishes identically. The null sets are the real null cones of the plain and the Krein forms, of real dimension three, and the origins of the Hermitian and the quaternionic forms: the same pattern as the quaternion subspace, with the roles of the two signs exchanged.

### The Four Algebraic Norms

The four norms are

$$
\langle\tilde Q\rangle=-h_t^{2}+\sum_{j=1}^{3}h_j^{2},\qquad
\langle\tilde Q\rangle_{*}=\sum_{\mu\in\{t,x,y,z\}}h_\mu^{2},\qquad
\langle\tilde Q\rangle_{\natural}=-\sum_{\mu\in\{t,x,y,z\}}h_\mu^{2},\qquad
\langle\tilde Q\rangle_{\natural*}=h_t^{2}-\sum_{j=1}^{3}h_j^{2},
$$

with signatures $(3,1)$, $(4,0)$, $(0,4)$ and $(1,3)$ in that order. The bilinear norms are the negatives of those on the quaternion subspace, $\langle\cdot\rangle=-\langle\cdot\rangle_{\natural*}$ and $\langle\cdot\rangle_{\natural}=-\langle\cdot\rangle_{*}$, while the sesquilinear ones are unchanged; the translation by $i$ changes the sign of the two bilinear norms and leaves the two sesquilinear ones. The Hermitian norm is positive definite, the quaternionic norm negative definite, and the other two indefinite.


## The Hermitian Subspace

**The Hermitian subspace is a Jordan algebra but not a Lie algebra.** Under $\bullet_{\mathrm{pl}}$ and $\bullet_{*}$, which coincide there, it is $H_{2}(\mathbb{C})=J(\mathbb{B})$, and it is **no Lie algebra** for any of the four brackets.

A Hermitian element is $a_te_t+i\vec p$ with $a_t\in\mathbb{R}$ and $\vec p$ a real vector. The subspace is the fixed set of the Hermitian conjugation ${}^{*}$, has real dimension four, and in the blocks is $A_1\oplus B_2$. It is the mirror of the vector subspace — there the antisymmetric half is the richer, here the symmetric half — and it is the first subspace of the list that is a Jordan algebra but not a Lie algebra.

### The Four General Products

**None of the four keeps the Hermitian subspace inside itself.** The product of two Hermitian elements,

$$
(a_te_t+i\vec p)(c_te_t+i\vec q)=\bigl(a_tc_t+(\vec p,\vec q)\bigr)e_t-\vec p\times\vec q+i(a_t\vec q+c_t\vec p),
$$

has a real scalar part and a vector part that runs over the whole complex vector subspace, and the middle term $-\vec p\times\vec q$ is a real pure vector, which no Hermitian element has: the witness is $(i\vec e_x)(i\vec e_y)=-\vec e_z$. The four products come in two pairs on the subspace, $f_{\mathrm{pl}}=f_{\mathrm{pl}*}$ and $f_{\natural}=f_{\natural*}$, and each of the four **spans $\mathbb{R}e_t\oplus\mathrm{Vect}(\mathbb{B})$**, of real dimension seven. It is the failure of the interior term that does the work: the Hermitian subspace has no real vector part, and that is precisely what the product of two of its elements supplies.

**The symmetrisation.** This is the operation that stays. **All four symmetrisations keep the Hermitian subspace inside itself**, the special feature of this subspace: the cross-product term is antisymmetric and cancels, and the Hermitian conjugation fixes a Hermitian element, so the general plain bilinear and the general plain sesquilinear symmetrisations agree:

$$
(a_te_t+i\vec p)\bullet_{\mathrm{pl}}(c_te_t+i\vec q)=(a_te_t+i\vec p)\bullet_{*}(c_te_t+i\vec q)=\bigl(a_tc_t+(\vec p,\vec q)\bigr)e_t+i(a_t\vec q+c_t\vec p).
$$

This is the **Jordan product**, and

$$
\boxed{\;(\mathbb{M}_{+},\bullet_{\mathrm{pl}})\cong H_{2}(\mathbb{C})=J(\mathbb{B})\;}
$$

is the Hermitian Jordan algebra of degree two, with two orthogonal idempotents and Peirce dimensions $1+2+1$ (*Symmetric and Antisymmetric Decomposition of the Four General Products*). The two quaternionic symmetrisations also stay inside but are central,

$$
(a_te_t+i\vec p)\bullet(c_te_t+i\vec q)=(a_te_t+i\vec p)\bullet_{\natural*}(c_te_t+i\vec q)=\bigl(a_tc_t-(\vec p,\vec q)\bigr)e_t,
$$

and give **no Jordan algebra**, the identity failing at $x=i\vec e_x$, where $x\bullet x=e_t$ and the two sides of $(x\bullet x)\bullet(x\bullet x)=x\bullet\bigl(x\bullet(x\bullet x)\bigr)$ are $e_t$ and $0$. The Hermitian subspace is therefore a **Jordan algebra for the general plain bilinear product and for the general plain sesquilinear product**, which coincide there, and for neither of the two quaternionic products.

**The bracket.** **No bracket keeps the Hermitian subspace inside itself.** The bracket of two Hermitian elements has zero scalar part, because the scalar part of every product is symmetric and real on $\mathbb{M}_+$, so it is a pure vector; and the values are not all imaginary, so the subspace does not close. The commutator and the general plain sesquilinear bracket fill the real vector triple, and the two quaternionic brackets the whole complex vector subspace:

$$
[\mathbb{M}_+,\mathbb{M}_+]=B_1,\qquad
[\mathbb{M}_+,\mathbb{M}_+]_{\natural}=\mathrm{Vect}(\mathbb{B}),\qquad
[\mathbb{M}_+,\mathbb{M}_+]_*=B_1,\qquad
[\mathbb{M}_+,\mathbb{M}_+]_{\natural*}=\mathrm{Vect}(\mathbb{B}).
$$

The commutator of two Hermitian elements is twice the cross product of their two imaginary vector parts, a real pure vector outside the subspace, so the Hermitian subspace is a **Lie algebra for none** of the four products. It is the exact counterpart of the vector subspace: there the bracket is carried and the symmetrisation is not, here the symmetrisation is carried and the bracket is not, and the two are the subspaces on which the two halves of the product each find their richest expression.

### The Four Forms

On the Hermitian subspace the four forms collapse to two, the plain with the Hermitian and the quaternionic with the Krein:

$$
\langle\tilde Q_1,\tilde Q_2\rangle=\langle\tilde Q_1,\tilde Q_2\rangle_{*}=a_tc_t+(\vec p,\vec q),\qquad
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=a_tc_t-(\vec p,\vec q).
$$

They are the **Euclidean form** of signature $(4,0)$ and the **Minkowski form** of signature $(1,3)$. The collapse pairs each bilinear form with the sesquilinear form of the same family, the plain with the Hermitian and the quaternionic with the Krein; on the other subspaces the pairing is crossed or carries a sign. The reason is that on the Hermitian subspace the star of the second slot acts as the identity, since the coefficients are already real in the scalar slot and purely imaginary in the vector slots. All four are real-valued, so the imaginary part vanishes identically, and the Gram matrices are $\mathrm I_4$ for the plain and the Hermitian forms and $\operatorname{diag}(1,-1,-1,-1)$ for the quaternionic and the Krein forms, both of full rank. The null sets are the origin of the Euclidean pair, the plain and the Hermitian forms, and the null cone of the Minkowski pair, the quaternionic and the Krein forms, of real dimension three.

### The Four Algebraic Norms

The four norms are

$$
\langle\tilde Q\rangle=\langle\tilde Q\rangle_{*}=a_t^{2}+(\vec p,\vec p),\qquad
\langle\tilde Q\rangle_{\natural}=\langle\tilde Q\rangle_{\natural*}=a_t^{2}-(\vec p,\vec p),
$$

of signatures $(4,0)$ and $(1,3)$ respectively. The Euclidean pair is positive definite and the Minkowski pair indefinite. These are the two classical forms of the Jordan algebra $H_{2}(\mathbb{C})$: the Euclidean norm and the Minkowski norm, and the two coincide with the corresponding forms on the subspace.

## The Anti-Hermitian Subspace

**The anti-Hermitian subspace is a Lie algebra but not a Jordan algebra.** Under $[\cdot,\cdot]$ and $[\cdot,\cdot]_{*}$, the latter the negative of the former, it is $\mathfrak{u}(2)\cong\mathbb{R}(ie_t)\oplus B_1$, and it is **no Jordan algebra** for any of the four symmetrisations.

An anti-Hermitian element is $ib_te_t+\vec q$ with $b_t\in\mathbb{R}$ and $\vec q$ a real vector. It is the anti-fixed set of ${}^{*}$, has real dimension four, and in the blocks is $A_2\oplus B_1$. It is the image of the Hermitian subspace under multiplication by $ie_t$, and it is the **material sector** of the physical interpretation.

### The Four General Products

**None of the four keeps the anti-Hermitian subspace inside itself.** The product of two anti-Hermitian elements,

$$
(ib_te_t+\vec q)(id_te_t+\vec r)=\bigl(-b_td_t-(\vec q,\vec r)\bigr)e_t+\vec q\times\vec r+i(b_t\vec r+d_t\vec q),
$$

has a real scalar part and a vector part that runs over the whole complex vector subspace, and it is the real scalar part that leaves the subspace: the witness is $(ie_t)(ie_t)=-e_t$, whereas an anti-Hermitian element has a purely imaginary scalar part. Each of the four **spans $\mathbb{R}e_t\oplus\mathrm{Vect}(\mathbb{B})$**, of real dimension seven, and the subspace is closed under no product.

**The symmetrisation.** **No symmetrisation keeps the anti-Hermitian subspace inside itself.** The general plain bilinear symmetrisation is Hermitian-valued,

$$
(ib_te_t+\vec q)\bullet_{\mathrm{pl}}(id_te_t+\vec r)=\bigl(-b_td_t-(\vec q,\vec r)\bigr)e_t+i(b_t\vec r+d_t\vec q)\in\mathbb{M}_+,
$$

with a real scalar part and an imaginary vector part, and the general plain sesquilinear symmetrisation is its negative, since ${}^{*}$ negates an anti-Hermitian element. The two quaternionic symmetrisations are central, and are the negative of each other:

$$
(ib_te_t+\vec q)\bullet(id_te_t+\vec r)=\bigl(-b_td_t+(\vec q,\vec r)\bigr)e_t,\qquad
(ib_te_t+\vec q)\bullet_{\natural*}(id_te_t+\vec r)=\bigl(b_td_t-(\vec q,\vec r)\bigr)e_t.
$$

The anti-Hermitian subspace is therefore a **Jordan algebra for none** of the four products, and the symmetrised product of two anti-Hermitian elements is never anti-Hermitian. This is the sign reversal that separates the two sectors: multiplication by the central imaginary exchanges $\mathbb{M}_+$ and $\mathbb{M}_-$, but it does not carry the symmetrisation of one to the symmetrisation of the other, and only $\mathbb{M}_+$ is closed under it.

**The bracket.** This is the operation that stays. **The commutator keeps the anti-Hermitian subspace inside itself**, and gives a Lie algebra:

$$
\boxed{\;[\mathbb{M}_-,\mathbb{M}_-]=B_1,\qquad
(\mathbb{M}_-,[\cdot,\cdot])\cong\mathfrak{u}(2)\cong\mathbb{R}(ie_t)\oplus B_1\;},
$$

the bracket of two anti-Hermitian elements being twice the real cross product of their two real vector parts, a real pure vector. The derived subalgebra is $B_1$, which under the cross product is $\mathfrak{su}(2)$, and the line $\mathbb{R}(ie_t)$ is central; the algebra is therefore the direct sum of a central line and $\mathfrak{su}(2)$, which is the **Lie algebra $\mathfrak{u}(2)$** of $\mathrm{U}(2)$, the skew-Hermitian complex $2\times2$ matrices, with centre $\mathbb{R}(ie_t)$ and derived subalgebra $\mathfrak{su}(2)$. The general plain sesquilinear bracket is the negative of the commutator, since ${}^{*}$ negates an anti-Hermitian element:

$$
[\mathbb{M}_-,\mathbb{M}_-]_{*}=-[\mathbb{M}_-,\mathbb{M}_-],
$$

so the anti-Hermitian subspace is a **Lie algebra for the general plain bilinear product and for the general plain sesquilinear product**. The two quaternionic brackets leave the subspace: their values are complex pure vectors and fill the whole complex vector subspace,

$$
[\mathbb{M}_-,\mathbb{M}_-]_{\natural}=[\mathbb{M}_-,\mathbb{M}_-]_{\natural*}=\mathrm{Vect}(\mathbb{B}),
$$

with the witness $[ie_t,\vec e_x]_{\natural}=2i\vec e_x\notin\mathbb{M}_-$. The anti-Hermitian subspace is therefore a **Lie algebra for exactly the two products** whose brackets reproduce the commutator up to sign, and a **Jordan algebra for none**.

### The Four Forms

On the anti-Hermitian subspace the four forms are four distinct functions:

$$
\langle\tilde Q_1,\tilde Q_2\rangle=-b_td_t-(\vec q,\vec r),\qquad
\langle\tilde Q_1,\tilde Q_2\rangle_{*}=b_td_t+(\vec q,\vec r),
$$
$$
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=-b_td_t+(\vec q,\vec r),\qquad
\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=b_td_t-(\vec q,\vec r),
$$

with the two sign relations $\langle\cdot,\cdot\rangle=-\langle\cdot,\cdot\rangle_{\natural*}$ and $\langle\cdot,\cdot\rangle_{\natural}=-\langle\cdot,\cdot\rangle_{*}$. The signatures are $(0,4)$ for the plain form, $(4,0)$ for the Hermitian, $(3,1)$ for the quaternionic and $(1,3)$ for the Krein, and the Gram matrices are $-\mathrm I_4$, $\mathrm I_4$, $\operatorname{diag}(-1,1,1,1)$ and $\operatorname{diag}(1,-1,-1,-1)$, all of full rank. All four are real-valued, so the imaginary part vanishes identically. The null sets are the origins of the plain and the Hermitian forms and the null cones of the quaternionic and the Krein forms, of real dimension three.

**This is the material sector.** The four forms here are the two sesquilinear ones with their signs, $\langle\cdot,\cdot\rangle_{*}=b_t^{2}+(\vec q,\vec q)$ the **Euclidean square** of signature $(4,0)$ and $\langle\cdot,\cdot\rangle_{\natural*}=b_t^{2}-(\vec q,\vec q)$ of signature $(1,3)$, against the two bilinear ones $\langle\cdot,\cdot\rangle=-\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural}=-\langle\cdot,\cdot\rangle_{\natural*}$. The interval of the corpus is the general quaternionic bilinear norm $\langle\cdot\rangle_{\natural}=-b_t^{2}+(\vec q,\vec q)$, of signature $(3,1)$, and its negative is the Krein form; the pair of the material interpretation is the interval against the Euclidean square, and the null cone of the quaternionic norm against the definite Hermitian form. These are exactly the columns of the Hermitian and the quaternionic forms of the table above.

### The Four Algebraic Norms

The four norms are

$$
\langle\tilde Q\rangle=-b_t^{2}-(\vec q,\vec q),\qquad
\langle\tilde Q\rangle_{*}=b_t^{2}+(\vec q,\vec q),\qquad
\langle\tilde Q\rangle_{\natural}=-b_t^{2}+(\vec q,\vec q),\qquad
\langle\tilde Q\rangle_{\natural*}=b_t^{2}-(\vec q,\vec q),
$$

with signatures $(0,4)$, $(4,0)$, $(3,1)$ and $(1,3)$ in that order. The two bilinear norms are the negatives of those on the Hermitian subspace and the two sesquilinear ones agree with it: $\langle\cdot\rangle=-\langle\cdot\rangle_{*}$, $\langle\cdot\rangle_{\natural}=-\langle\cdot\rangle_{\natural*}$, while $\langle\cdot\rangle_{*}$ and $\langle\cdot\rangle_{\natural*}$ are unchanged. The Hermitian norm is positive definite, the plain norm negative definite, and the other two indefinite. The four values are the four norms of the material sector: the interval $\langle\cdot\rangle_{\natural}$, the Euclidean square $\langle\cdot\rangle_{*}$, and their negatives $\langle\cdot\rangle_{\natural*}$ and $\langle\cdot\rangle$.


## The Null Sets

The null set of each form on each subspace is this.

| subspace | plain | Hermitian | quaternionic | Krein |
|---|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ |
| $\mathrm{Vect}(\mathbb{B})$ | the complex cone, real dimension $4$ | $\{0\}$ | the complex cone, real dimension $4$ | $\{0\}$ |
| $\mathbb{H}_{\mathbb{B}}$ | the null cone, real dimension $3$ | $\{0\}$ | $\{0\}$ | the null cone, real dimension $3$ |
| $i\mathbb{H}_{\mathbb{B}}$ | the null cone, real dimension $3$ | $\{0\}$ | $\{0\}$ | the null cone, real dimension $3$ |
| $\mathbb{M}_+$ | $\{0\}$ | $\{0\}$ | the null cone, real dimension $3$ | the null cone, real dimension $3$ |
| $\mathbb{M}_-$ | $\{0\}$ | $\{0\}$ | the null cone, real dimension $3$ | the null cone, real dimension $3$ |

The rule behind the table is one line: **off the centre a form has a complex null cone on a subspace exactly when the real part of its restriction is indefinite there**, and the signature table of $\S$*The Four Algebraic Norms* says which are. On the centre the complex zeros are trivial for all four forms even though the real part of the two bilinear forms is indefinite, and it is the real zeros of the real part that form the cone there; the two kinds of zero are separated in $\S$*The Realified Form on the Subspaces*. The count of forms with a complex null cone is none on the centre, two on the vector subspace, the bilinear pair of signature $(3,3)$, and two on each of the four real-type subspaces: the plain and the Krein forms on the quaternion subspace and on its imaginary translate, the quaternionic and the Krein forms on the two sectors.

Two columns of the table are constant and are the two theorems of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra* read on the remarkable subspaces: **the Hermitian form is definite on all of them**, so its null set is the origin in each, and **it is the only form definite on all of them**, so each of the other three has a cone on some subspace. The collapses pair the columns, and the signatures in the table above are the record of which pairs are definite on which subspace.

**The ambient cones are cut by the subspaces.** The ambient null sets of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra* are the complex cone of the plain form, the zero-divisor cone of the quaternionic form and the real cone of the Krein form, of real dimensions six, six and seven. The table above is what those cones become on the remarkable subspaces, and the two are different pictures: the ambient cones have real dimension six or seven, and the cones of the table have real dimension four on the vector subspace and real dimension three on the four real-type subspaces, because the equations $\sum_kP_k^{2}=0$ in three complex unknowns and $h_t^{2}=\lvert\vec h\rvert^{2}$ in four real unknowns have those dimensions. A subspace is not a small copy of the ambient space for a cone.

## The Isometry Groups of the Restrictions

**Definition.** For a subspace $U$ of the remarkable subspaces the **isometry group of the restriction** is the group of real-linear maps of $U$ preserving the real part $g_{\mathrm{pl}}|_U$,

$$
\mathrm{Isom}(U,g_{\mathrm{pl}})=\{S\in GL_{\mathbb{R}}(U):g_{\mathrm{pl}}(Su,Sv)=g_{\mathrm{pl}}(u,v)\ \text{for all }u,v\in U\}.
$$

It is the real orthogonal group of the signature of $g_{\mathrm{pl}}$ on $U$, and its real dimension is $n(n-1)/2$ for $n=\dim_{\mathbb{R}}U$. The signatures of the previous sections give the table.

| subspace | signature of $g_{\mathrm{pl}}$ | isometry group | real dimension |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $(1,1)$ | $O(1,1)$ | $1$ |
| $\mathrm{Vect}(\mathbb{B})$ | $(3,3)$ | $O(3,3)$ | $15$ |
| $\mathbb{H}_{\mathbb{B}}$ | $(1,3)$ | $O(1,3)$ | $6$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $(3,1)$ | $O(3,1)\cong O(1,3)$ | $6$ |
| $\mathbb{M}_+$ | $(4,0)$ | $O(4)$ | $6$ |
| $\mathbb{M}_-$ | $(0,4)$ | $O(4)$ | $6$ |

The same rows with the signatures of the Hermitian, the quaternionic and the Krein forms give the isometry groups of their real parts, since each of the four forms is non-degenerate on $U$ and its group depends on the signature alone.

**Remark (the real part against the complex form).** On the two complex subspaces the group preserving the complex plain form itself is the smaller complex orthogonal group, $O_1(\mathbb{C})$ on the centre and $O_3(\mathbb{C})$ on the vector subspace, of real dimensions $0$ and $6$; the real groups $O(1,1)$ and $O(3,3)$ of the table preserve only the real part and are larger. On the four real-type subspaces the plain form is real and the two groups coincide, and the rows $O(4)$ and $O(1,3)$ are real forms of the complex orthogonal group $O_4(\mathbb{C})$ of *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*, §*The Isometry Groups of the Four Forms*.

## The Realified Form on the Subspaces

**The maximal definite subspaces.** The real part $g_{\mathrm{pl}}$ on the whole algebra has signature $(4,4)$, so its maximal positive definite and maximal negative definite dimensions are both $4$. The Hermitian subspace $\mathbb{M}_+$, of real dimension $4$ and positive definite, is a **maximal positive definite subspace**, and the anti-Hermitian subspace $\mathbb{M}_-$ a **maximal negative definite subspace**; neither can be enlarged while remaining definite, and the two are orthogonal complements. The centre is a hyperbolic plane, its signature $(1,1)$ being neither positive nor negative definite, and the quaternion and vector subspaces carry both signs.

**The three orthogonal splittings.** The form is diagonal in the natural bases, so three pairs of complementary subspaces split the algebra orthogonally, the signatures adding to $(4,4)$ in each:

$$
\boxed{\;\mathbb{B}=\mathbb{C}_{\mathbb{B}}\perp\mathrm{Vect}(\mathbb{B}),\qquad
\mathbb{B}=\mathbb{H}_{\mathbb{B}}\perp i\mathbb{H}_{\mathbb{B}},\qquad
\mathbb{B}=\mathbb{M}_+\perp\mathbb{M}_-\;}
$$

of signatures $(1,1)\perp(3,3)$, $(1,3)\perp(3,1)$ and $(4,0)\perp(0,4)$. Only the third splits the realified form into a positive definite and a negative definite piece; in the first two both sides carry isotropic vectors. The two restricted forms of the third split are exchanged by the central scalar, $\langle i\tilde Q_1,i\tilde Q_2\rangle=-\langle\tilde Q_1,\tilde Q_2\rangle$.

**The real null cones of $g_{\mathrm{pl}}=\operatorname{Re}\langle\cdot,\cdot\rangle$.** On each of the four indefinite rows the real zeros of $g_{\mathrm{pl}}$ form a cone through the origin of real codimension one, and one null element on each row exhibits it.

| subspace | signature | null element | real null cone, real dimension |
|---|---|---|---|
| $\mathbb{C}_{\mathbb{B}}$ | $(1,1)$ | $e_t+ie_t$ | $1$, the two lines $\mathbb{R}(e_t\pm ie_t)$ |
| $\mathrm{Vect}(\mathbb{B})$ | $(3,3)$ | $\vec e_x+i\vec e_x$ | $5$ |
| $\mathbb{H}_{\mathbb{B}}$ | $(1,3)$ | $e_t+\vec e_x$ | $3$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $(3,1)$ | $ie_t+i\vec e_x$ | $3$ |

Each element is null because the real part of its value vanishes, $1-1$ on the centre and on the vector and quaternion subspaces, $-1+1$ on the anti-quaternion subspace. On the centre, of real dimension two, the cone is the pair of lines $\mathbb{R}(e_t\pm ie_t)$. The two definite rows, $\mathbb{M}_+$ and $\mathbb{M}_-$, contribute no null element, so the isotropic rows are four and not six. These are the real zeros of $g_{\mathrm{pl}}$, and they are distinct from the complex null sets of the table above, which are the complex zeros of the plain form: on the four real-type subspaces the two agree, because there the plain form is real-valued, while on the centre and the vector subspace they do not — the complex null set of the plain form is the origin on the centre and the complex cone of real dimension $4$ on the vector subspace, against the two real lines and the cone of real dimension $5$ found here. On the vector subspace the cone $\sum_kp_k^2=\sum_kq_k^2$ contains the totally isotropic real plane $\mathrm{span}_{\mathbb{R}}\{\vec e_x+i\vec e_x,\vec e_y+i\vec e_y\}$, and the three elements $\vec e_k+i\vec e_k$ span a totally isotropic subspace of real dimension $3$, the maximum for signature $(3,3)$.

## The Two Splits and the Two Interpretations

The remarkable subspaces of this article are the homes of the parts of the four products under the **plain** exchange of the two arguments. The two parts of a bilinear product are read there directly, the antisymmetric parts of the two bilinear products spanning the vector subspace and the symmetric part of the quaternionic one collapsing to the centre; and the two parts of the plain sesquilinear product are the Hermitian subspace $\mathbb{M}_+$ and the anti-Hermitian subspace $\mathbb{M}_-$.

The **exchange by the coefficientwise conjugation**, $f^{c}(\tilde Q_1,\tilde Q_2)=\overline{f(\tilde Q_2,\tilde Q_1)}$, keeps the class of the two sesquilinear products, and its two parts sit in two other subspaces of the same list. This is the **adapted** reading, against the **plain** exchange of the first paragraph. For $f_{\mathrm{pl}*}$ they are the scalar part and the vector part of the value, so they lie in the **centre** $\mathbb{C}_{\mathbb{B}}$ and in the **vector subspace** $\mathrm{Vect}(\mathbb{B})$ — the two subspaces that carry the parts of the general quaternionic bilinear product under the plain exchange. For $f_{\natural*}$ the skew half is the cross product $\vec Q_1\times\overline{\vec Q_2}$ of the two vectors, so it lies in the **vector subspace**, while the conjugate-symmetric half carries the Krein form in its scalar part and is not central, so it lies in no subspace of the remarkable subspaces.

So three of the passages of the adapted reading land in the list — the centre and the vector subspace for $f_{\mathrm{pl}*}$, the vector subspace again for $f_{\natural*}$ — against the Hermitian and the anti-Hermitian subspace, where the plain reading of the same two products lands. The two readings are of one pair of products each and neither is the other; the twelve names of *Symmetric and Antisymmetric Decomposition of the Four General Products* belong to the **adapted** reading and not to the plain one tabulated here, and the plain reading's own four halves are the operations of *The Sesquilinear Symmetrised Product* and *The Sesquilinear Commutator*.

## What the Remarkable Subspaces Separate

The remarkable subspaces separate the four algebraic norms in a way that no single one of them does on the whole algebra. On $\mathbb{B}$ no algebraic norm is both definite and multiplicative, and the Hermitian and the quaternionic norms are two different functions; on the quaternion subspace the two functions become one, and on the anti-quaternion subspace they become opposite, the one subspace being the imaginary translate of the other. The coincidence of the quaternion subspace, and its failure on the other four subspaces, is the content of the real-form caution of *Symmetric and Antisymmetric Decomposition of the Four General Products* read at the two equal arguments and on the remarkable subspaces.

Three facts summarise the separation. **Only the Hermitian norm is definite on every one of the remarkable subspaces**; the plain norm is definite on exactly two, the two sectors, with exchanged signs; the quaternionic norm is definite on exactly two, positive on the quaternion subspace and negative on its imaginary translate; and the Krein norm is definite on exactly two, the centre and the vector subspace, where it is the positive definite form and its negative. The four algebraic norms are thus definite on the whole algebra only for the Hermitian; each of the other three is definite on a proper pair of subspaces, and the remarkable subspaces are the places where the pair is read.

## The Material Interpretation

The interpretation is an interpretation and not a theorem; it is the one the corpus gives to the four forms and it is sharpened here by the remarkable subspaces.

- On the **material sector** $\mathbb{M}_-$ the four forms are real and the article adds nothing to the four algebraic norms: the interval $\langle\cdot\rangle_{\natural}$, the Euclidean square $\langle\cdot\rangle_{*}$ and their negatives $\langle\cdot\rangle_{\natural*}$ and $\langle\cdot\rangle$. The material sector carries no imaginary part, so it carries no phase pairing, and the null cone there is the interval's.
- On the **two complex subspaces** the four forms carry, besides the intervals and the squares of their algebraic norms, a second real form: symmetric for the two bilinear forms and alternating for the two sesquilinear ones. The alternating companion is non-degenerate, so the centre carries one canonical pair and the vector subspace three, one to a spatial direction.
- The alternating companion is the **phase**, or area, pairing: the object a canonical pair needs, and the one the corpus has so far read only through the imaginary part of the Hermitian form. On the centre it is the pairing of the complex line with itself, of rank $2$; on the vector subspace it is the pairing of the three complex directions, of rank $6$; on the four real-type subspaces, and in particular on the material sector, it is absent.

So the corpus's four forms are, on the two complex subspaces, **four intervals and two symplectic forms**, and on the four real-type subspaces four intervals alone. The second half of that sentence is what the diagonal, the algebraic norm, records; the first half is what the two-argument form adds.


## Summary

**One chain.** The four general products, their scalar-part forms and their algebraic norms are read on the six remarkable subspaces. The four products have the same value set on each subspace, because ${}^{\natural}$ and ${}^{*}$ preserve every subspace of the list; they differ in the structure they leave on the value. The product keeps a subspace inside itself for exactly the centre and the quaternion subspace, for all four products. The symmetrisation keeps it for exactly the centre, the quaternion subspace and the Hermitian subspace; the bracket for exactly the centre (all four products), the quaternion subspace (the general plain bilinear and general quaternionic sesquilinear products), the vector subspace (the two bilinear products) and the anti-Hermitian subspace (the general plain bilinear and general plain sesquilinear products). The resulting algebras are: the centre, the field $\mathbb{C}$ for the two bilinear products and a Lie algebra for all four; the vector subspace, $\mathfrak{sl}(2,\mathbb{C})$ for the two bilinear products and no Jordan algebra; the quaternion subspace, a Jordan algebra for the general plain bilinear product and the Lie algebra $\mathbb{R}e_t\oplus\mathfrak{su}(2)$ for the general plain bilinear and general quaternionic sesquilinear products; the anti-quaternion subspace, no algebra at all; $\mathbb{M}_+$, the Jordan algebra $H_2(\mathbb{C})$ for the two plain products and no Lie algebra; and $\mathbb{M}_-$, the Lie algebra $\mathfrak{u}(2)$ for the two plain products and no Jordan algebra.

**The forms.** All twenty-four restrictions are non-degenerate. Each form splits as $\varphi=g+i\sigma$, with $g$ real symmetric and $\sigma$ symmetric for the two bilinear forms, alternating for the two sesquilinear forms. The imaginary part vanishes on the four real-type subspaces and is non-degenerate on the two complex subspaces, of rank $2$ on the centre and rank $6$ on the vector subspace. The Kähler identity $\omega(\tilde Q_1,\tilde Q_2)=g(\tilde Q_1,i\tilde Q_2)$ holds for the two sesquilinear forms on the complex subspaces, and the companion identity $\sigma=-g(\cdot,i\cdot)$ for the two bilinear forms.

**The norms.** The signatures over $\mathbb{R}$ are tabulated in $\S$*The Four Algebraic Norms*; the pattern is the one that separates the subspaces. Only the Hermitian norm is definite on every subspace; the plain norm is definite on the two sectors, the quaternionic on the quaternion subspace and its imaginary translate, and the Krein on the centre and the vector subspace. The four norms collapse to two on the centre, the quaternion subspace and the Hermitian subspace, and to two pairs of opposites on the vector subspace, the anti-quaternion subspace and the anti-Hermitian subspace; the collapse is the fixed- or anti-fixed-space condition of a conjugation read on the norm.

**The separation.** The subspaces do not filter the four products into one scale. They expose, on six different subspaces, the four faces of one algebra: the field on the centre, the complex Lie algebra on the vector subspace, the real division algebra with both structures on the quaternion subspace, the module with no algebra on its imaginary translate, and the two sectors on which the symmetric and antisymmetric halves of the product find their richest expression.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$, $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ | the centre, the vector, quaternion, anti-quaternion, Hermitian and anti-Hermitian subspaces |
| $A_1=\mathbb{R}e_t$, $A_2=\mathbb{R}(ie_t)$, $B_1$, $B_2$ | the two scalar and the two vector coordinate blocks |
| $f_{\mathrm{pl}}$, $f_{\natural}$, $f_{\mathrm{pl}*}$, $f_{\natural*}$ | the four general products: plain bilinear, quaternionic bilinear, plain sesquilinear, quaternionic sesquilinear |
| $\bullet_{\mathrm{pl}}$, $\bullet$, $\bullet_{*}$, $\bullet_{\natural*}$ | their symmetrisations |
| $[\cdot,\cdot]$, $[\cdot,\cdot]_{\natural}$, $[\cdot,\cdot]_{*}$, $[\cdot,\cdot]_{\natural*}$ | their brackets |
| $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural*}$ | the four forms: plain bilinear, quaternionic bilinear, plain sesquilinear or Hermitian, quaternionic sesquilinear or Krein |
| $\langle\cdot\rangle$, $\langle\cdot\rangle_{\natural}$, $\langle\cdot\rangle_{*}$, $\langle\cdot\rangle_{\natural*}$ | the four algebraic norms, the four forms at two equal arguments |
| $g$, $\sigma$, $\omega$ | the real part, the imaginary part, and the imaginary part when alternating |
| $(p,q)$ | the signature over $\mathbb{R}$ of a real quadratic form |

## Further Reading

- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the four products, their coordinate rules, their relations and their comparison.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the forms and the algebraic norms themselves, their Gram matrices, their isometry groups and their separation.
- [Symmetric and Antisymmetric Decomposition of the Four General Products](symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html), for the twelve operations, the two exchanges and the Jordan and Jacobi failures used here.
- [Introduction to the Remarkable Subspaces](introduction-to-the-remarkable-subspaces.html), for the six subspaces, their defining conditions, their bases, their dimensions and their role.
- [Comparison of the Remarkable Subspaces](comparison-of-the-remarkable-subspaces.html), for the coordinate blocks, the pairwise intersections, the sums and the three decompositions.
- [The Sesquilinear Symmetrised Product](the-sesquilinear-symmetrised-product.html) and [The Sesquilinear Commutator](the-sesquilinear-commutator.html), for the plain reading's own halves.
- [Conventions in the Biquaternion Universe](../articles_physics/conventions-in-the-biquaternion-universe.html), for the convention of the four pairings, the four names and the pairs, and for the interpretations of the four on the algebra and on the material sector.
- [The Four General Products: Composition, Probability, Causality, Gauge](../articles_physics/the-four-general-products-composition-probability-causality-gauge.html), for the physical interpretations of the four forms and their signature table on the remarkable subspaces.
- [The Norm Defined by a Form](the-norm-defined-by-a-form.html) and [Hermitian Forms over Algebras and Norms](hermitian-forms-over-algebras-and-norms.html), for the passage from a form to its algebraic norm, and for the real part, the imaginary part and the alternating companion of a Hermitian form.

