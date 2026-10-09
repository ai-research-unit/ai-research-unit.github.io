
# __The Graded Adjoint Action on a Module over a Clifford Algebra__

## Introduction

The Clifford algebra is a $\mathbb{Z}/2$-graded algebra, $A=A^0\oplus A^1$ with the even part and the odd part, and its modules are graded: a **graded Clifford module** is a module $M=M^0\oplus M^1$ with $A^iM^j\subseteq M^{i+j}$, the spinor module being graded by the chirality. The **adjoint action** is the action carried by the **graded dual** $M^\vee$: for a homogeneous element $x$ of degree $\lvert x\rvert$ and a homogeneous functional $f$ of degree $\lvert f\rvert$ it is

$$
(\rho^{\vee}(x)f)(m)=-(-1)^{\lvert x\rvert\lvert f\rvert}\,f\bigl(\rho(x)m\bigr) ,
$$

the Koszul sign $(-1)^{\lvert x\rvert\lvert f\rvert}$ being forced by the module axiom. This article defines the graded dual, constructs the adjoint action, proves that the sign rule is exactly what makes it a graded action, and treats the **coadjoint action** — the adjoint action on the dual of the algebra itself — as the worked case, where the invariant standard form identifies the coadjoint module with the algebra and reduces the coadjoint action to the adjoint action of the conjugated parameter. The article completes the group: it is the module-level form of the adjoints of the one-sided and two-sided operators treated in the preceding entries.

**The boundaries.** The graded action, the sign rule and the graded bracket are *The Graded Action on a Module over a Graded Algebra*; the modules over the Clifford algebra and the chirality grading are *Modules over a Clifford Algebra* and *Clifford Modules*; the algebra and its grading are *Clifford Algebras*; the invariant standard form and the adjoint $L_a^*=L_{\hat a}$ are *The Adjoint of the Left Multiplication on a Clifford Algebra*; the sandwich adjoint is *The Signed Adjoint Sandwich on a Clifford Algebra*. The analytic adjoint of an operator on a Hilbert space belongs to a later Part and is named only. The base is a field $F$ of characteristic not $2$, $A=\mathrm{Cl}(V,q)$ with the parity grading, and modules are finite-dimensional.

## Graded Clifford Modules and the Graded Dual

**Definition.** A **graded Clifford module** is a module $M$ over $A=\mathrm{Cl}(V,q)$ with a decomposition $M=M^0\oplus M^1$ such that $A^iM^j\subseteq M^{i+j}$; an element of $M^i$ is homogeneous of degree $i$, written $\lvert m\rvert=i$. The **chirality grading** of the spinor module in even dimension, $S=S^+\oplus S^-$, is the fundamental example.

**Definition.** The **graded dual** $M^{\vee}$ is the graded vector space with $(M^{\vee})^i=(M^i)^{*}$ for each $i$; a functional in $(M^i)^{*}$ has degree $i$.

**Proposition.** The **evaluation pairing** $\langle f,m\rangle=f(m)$ vanishes unless $\lvert f\rvert=\lvert m\rvert$ and is a map of degree zero; it is non-degenerate on each side for a finite-dimensional module; the parity shift $M[1]$ with $(M[1])^i=M^{i+1}$ satisfies $(M[1])^{\vee}=M^{\vee}[1]$.

**Proof.** A functional in $(M^i)^*$ vanishes on $M^j$ for $j\neq i$ and eats only $M^i$; the equality $i=j$ in $\mathbb{Z}/2$ means $i+j=0$, so the pairing has degree zero; non-degeneracy is the finite-dimensional duality; the shift statement is the reindexing of the dual.

**Remark (the chirality example).** For the spinor module $S=S^+\oplus S^-$ the graded dual is $(S^\vee)^\pm=(S^\pm)^*$, and the Clifford multiplication by a vector interchanges the two summands; the dual action therefore interchanges the dual summands as well, with the sign computed below.

## The Adjoint Action

**Definition.** Let $\rho$ be a graded action of $A$ on $M$. The **adjoint action** on $M^{\vee}$ is

$$
\bigl(\rho^{\vee}(x)f\bigr)(m) = -(-1)^{\lvert x\rvert\lvert f\rvert}\,f\bigl(\rho(x)m\bigr)
$$

for homogeneous $x,f$ and every $m$, extended bilinearly.

**Theorem.** The adjoint action is a graded action: $\rho^{\vee}$ is linear, homogeneous of degree zero, and satisfies the graded bracket identity

$$
\rho^{\vee}([x,y])=\rho^{\vee}(x)\rho^{\vee}(y)-(-1)^{\lvert x\rvert\lvert y\rvert}\rho^{\vee}(y)\rho^{\vee}(x)
$$

for homogeneous $x,y$; equivalently, the sign $(-1)^{\lvert x\rvert\lvert f\rvert}$ is exactly the sign that makes the transpose respect the graded bracket.

**Proof.** For homogeneous $x,y,f,m$ the module axiom of a graded action reads $x\cdot(y\cdot m)-(-1)^{\lvert x\rvert\lvert y\rvert}y\cdot(x\cdot m)=[x,y]\cdot m$, and unwinding the definition gives

$$
\bigl(\rho^{\vee}(x)\rho^{\vee}(y)f\bigr)(m)=(-1)^{\lvert x\rvert\lvert f\rvert+\lvert y\rvert\lvert f\rvert}\,f(y\cdot x\cdot m) , \qquad
\bigl(\rho^{\vee}([x,y])f\bigr)(m)=-(-1)^{(\lvert x\rvert+\lvert y\rvert)\lvert f\rvert}f([x,y]\cdot m) ,
$$

and the two agree after inserting $(-1)^{\lvert x\rvert\lvert y\rvert}$ in front of the second term and using $(-1)^{(\lvert x\rvert+\lvert y\rvert)\lvert f\rvert}=(-1)^{\lvert x\rvert\lvert f\rvert+\lvert y\rvert\lvert f\rvert}$; the linearity and degree are immediate.

**Remark (the Clifford generators).** For the Clifford algebra the generators are odd and satisfy the graded anticommutation $uv+vu=2B(u,v)$; the adjoint action of a vector $u$ on the graded dual is

$$
\rho^{\vee}(u)f = (-1)^{\lvert f\rvert}\,\bigl(f\circ\rho(u)\bigr) ,
$$

the sign being $+$ on functionals of even degree and $-$ on functionals of odd degree; the graded dual therefore carries the same Clifford relations with the signs distributed by the parity of the functional, which is the module-level form of the relation $c(v)^*=-c(v)$ for the odd functionals.

**Remark (the associative case and the star).** The dual of a graded left module over a graded associative algebra is naturally a graded **right** module, $f\cdot a=\rho(a)^{t}f$; when the algebra carries an element star $x\mapsto x^{\dagger}$, $({}^{\dagger})^2=\mathrm{id}$, $(xy)^{\dagger}=y^{\dagger}x^{\dagger}$ — for the Clifford algebra the Clifford conjugation $\hat{}$ or the Hermitian conjugation of *Hermitian Clifford Structures* — the same computation with $x^{\dagger}$ in place of $[x,\cdot]$ makes the adjoint action a graded **left** action on $M^\vee$, the star supplying the reversal of the order, and the Koszul sign is unchanged.

**Corollary (the sign rule).** The adjoint action satisfies the sign rule: for homogeneous $x,y$,

$$
\rho^{\vee}(x)\rho^{\vee}(y)=(-1)^{\lvert x\rvert\lvert y\rvert}\rho^{\vee}(y)\rho^{\vee}(x)+\rho^{\vee}([x,y]) ;
$$

in particular the odd generators of the Clifford algebra graded-anticommute on the dual, as they do on the module.

## The Coadjoint Action

**Definition.** The **adjoint action of the algebra on itself** is $\mathrm{ad}_x(y)=xy-yx$ on the odd part and $xy-(-1)^{\lvert x\rvert\lvert y\rvert}yx$ in general; the **coadjoint action** is the adjoint action on the graded dual $A^{\vee}$ of the algebra.

**Proposition.** The standard form $\langle x,y\rangle=\operatorname{Sc}(\hat xy)$ is invariant under the left and right multiplications of *The Adjoint of the Left Multiplication on a Clifford Algebra* in the sense that it identifies the coadjoint module with the algebra, and under that identification the coadjoint action is the adjoint action of the **conjugated parameter**,

$$
\rho^{\vee}(a)\ \longleftrightarrow\ \mathrm{ad}_{\alpha(\hat a)} ,
$$

the module-level form of the adjoint formula $L_a^*=L_{\hat a}$ of the operator theory.

**Proof.** The standard form is non-degenerate and satisfies $\langle ax,y\rangle=\langle x,\hat ay\rangle$; it therefore gives an isomorphism $A\to A^\vee$, $y\mapsto\langle y,\cdot\rangle$, and transports the coadjoint action to the action on $A$ computed by duality: $(\rho^\vee(a)f)(y)=-(-1)^{\lvert a\rvert\lvert f\rvert}f(ay)$. Reading $f=\langle z,\cdot\rangle$ and using the invariance gives the transported action $z\mapsto$ the element paired with $\hat a z$, which is the adjoint action of $\alpha(\hat a)$ on the opposite algebra; the explicit case is the display.

**Corollary.** The coadjoint action is an involution-free statement: its parameter involution is the same twisted conjugation $\alpha(\hat{})$ as for the signed left multiplication, and for a self-adjoint operator $L_a=L_{\hat a}$ the coadjoint action is the ordinary adjoint action. The invariant form is the reason the two stories agree, and it is the form of the category.

**Proof.** The parameter involution is read from the proof; the self-adjoint case is the identification of the conjugation, and the last statement is the definition of the invariant form.

## Worked Cases

### The Algebra as a Module over Itself

For $M=A$ with the left regular action, the graded dual is $A^\vee$ and the adjoint action is the coadjoint action; with the standard form the module is identified with the algebra and the action is $\mathrm{ad}_{\alpha(\hat a)}$, as displayed. The action of a vector $u$ is the adjoint action $\mathrm{ad}_u$ up to the sign of the parity, since $\alpha(\hat u)=u$.

### The Spinor Module

For the graded spinor module $S=S^+\oplus S^-$ of an even-dimensional Clifford algebra, the graded dual is $S^\vee=(S^+)^*\oplus(S^-)^*$ and the adjoint action interchanges the two summands; with the spinor inner product of *Hermitian Clifford Structures* the dual is identified with the conjugate module, and the adjoint action is the ordinary Clifford multiplication there, the Koszul sign reproducing the skew-adjointness $c(v)^*=-c(v)$ on the odd functionals.

### The Exterior Algebra

For the exterior algebra $\Lambda W$ with the Clifford structure of the neutral form, the module is graded by the degree modulo two, the graded dual is the exterior algebra of the dual space, and the adjoint action is the contraction; the coadjoint identification by the standard form is the Poincaré duality pairing, and the adjoint action of a vector is the sum of the exterior and interior multiplications.

## Summary

For a graded Clifford module $M=M^0\oplus M^1$ the **graded dual** $M^{\vee}$ has $(M^{\vee})^i=(M^i)^*$ and the evaluation pairing of degree zero, and the **adjoint action** is

$$
(\rho^{\vee}(x)f)(m)=-(-1)^{\lvert x\rvert\lvert f\rvert}f(\rho(x)m) ,
$$

which is a graded action precisely because of the Koszul sign $(-1)^{\lvert x\rvert\lvert f\rvert}$: the graded bracket identity holds with that sign and fails without it. For the Clifford generators, which are odd, the sign depends only on the parity of the functional, reproducing $c(v)^*=-c(v)$ at the module level; with an element star the adjoint action becomes a graded **left** action on the dual. The **coadjoint action** — the adjoint action on the dual of the algebra — is identified by the invariant standard form of the category with the adjoint action of the **conjugated parameter**, the module-level form of $L_a^*=L_{\hat a}$. The article is the last of the category: the graded action is *The Graded Action on a Module over a Graded Algebra*, the modules are *Modules over a Clifford Algebra* and *Clifford Modules*, the invariant form is *The Adjoint of the Left Multiplication on a Clifford Algebra*, and the analytic adjoint on a Hilbert space belongs to a later Part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A=A^0\oplus A^1$ | Clifford algebra with the parity grading |
| $M=M^0\oplus M^1$, $A^iM^j\subseteq M^{i+j}$ | Graded Clifford module |
| $M^{\vee}$, $(M^{\vee})^i=(M^i)^*$ | Graded dual |
| $\langle f,m\rangle=f(m)$ | Evaluation pairing, of degree zero |
| $(\rho^{\vee}(x)f)(m)=-(-1)^{\lvert x\rvert\lvert f\rvert}f(\rho(x)m)$ | Adjoint action; Koszul sign |
| $\rho^{\vee}([x,y])=\rho^{\vee}(x)\rho^{\vee}(y)-(-1)^{\lvert x\rvert\lvert y\rvert}\rho^{\vee}(y)\rho^{\vee}(x)$ | Graded bracket identity |
| $\mathrm{ad}_x$, $\rho^{\vee}$ on $A^{\vee}$ | Adjoint and coadjoint actions |
| $\langle x,y\rangle=\operatorname{Sc}(\hat xy)$ | Invariant standard form; identifies the coadjoint module |

## Further Reading

- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2 (Springer, 1997), for the graded structure of the Clifford algebra and the contragredient modules.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1989), for the sign rule of the graded transpose and the graded modules.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the chirality grading of the spinor module and the dual spinor module.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the invariant forms and the identification of a module with its dual.
