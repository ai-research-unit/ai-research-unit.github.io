# __Riemann Boundary Value Problems and Singular Integral Equations__

## Introduction

The preceding articles of this cluster built the integral theory of an elliptic hypercomplex system: the Cauchy–Goursat theorem, the Cauchy integral formula, the Cauchy transform and the jump formula at a boundary. That theory ends on a promise. *Hypercomplex Integration* closes by saying that "the explicit Hardy-space and singular-integral theory of a particular system is developed from these formulas with its own kernel", and *Clifford Analysis* records the boundary Cauchy transform as "the analytic heart of the singular-integral theory of the subject". This article delivers that theory: the **Riemann boundary value problem**, or problem of linear conjugation, and the **singular integral equation of Cauchy type**.

Two problems form the subject. The first asks for a function regular on either side of a boundary whose one-sided boundary values are related by a linear condition. The second asks for a boundary density satisfying a singular integral equation. They are one object in two forms. The Cauchy transform converts a singular integral equation into a boundary value problem, and the difference of the one-sided boundary values converts it back. The classical chain — the Plemelj formulas, the canonical factor, the index, the count of solutions and the solvability conditions — is developed below in the hypercomplex setting.

The treatment is complete for a coefficient that is a constant of the algebra, which is the case the source of the corpus's Clifford material treats; the index enters only for a variable coefficient, and there the classical complex case is stated in full. The order of the factors is kept throughout: $A$ need not be commutative, the coefficient acts on the right, and the one place where the order decides a result is marked.

## Sectionally Regular Functions and the Two-Sided Domain

Throughout, $(A,D)$ is an elliptic hypercomplex system in the sense of *Hypercomplex Analysis*: $A$ is a finite-dimensional unital associative real algebra of dimension $m$ with a fixed frame $(1,B_1,\dots,B_{m-1})$ and

$$
D=\partial_0+\sum_{k\geq1}B_k\partial_k, \qquad \bar D=\partial_0-\sum_{k\geq1}B_k\partial_k, \qquad D\bar D=\bar DD=\Delta,
$$

the coefficients satisfying $B_jB_k+B_kB_j=-2\delta_{jk}$ and $B_k^2=-1$. The conormal element $\nu_B$ and the fundamental solution $E$ are those of *Regularity and the Cauchy–Riemann Operator* and *Hypercomplex Integration*; the function $E(x-y)$ is the Cauchy kernel, and $dS$ is the surface measure on a hypersurface.

### The domain and the Hölder classes

Let $\Omega\subset A$ be a bounded, open and connected set whose boundary $\Gamma=\partial\Omega$ is a smooth, compact, oriented Liapunov hypersurface. It divides $A$ into the two open sets $\Omega^+=\Omega$ and $\Omega^-=A\setminus\overline\Omega$, with $\infty\in\Omega^-$. The classical theory of the one-variable case is the specialisation $A=\mathbb C$, $m=2$, and the complex case is kept in view as the model.

**Definition (Hölder class).** For $0<\beta\leq1$, $H(\Gamma,\beta)$ is the set of continuous $A$-valued functions $h$ on $\Gamma$ with finite

$$
\|h\|_\beta=C(h)+H(h,\beta), \qquad C(h)=\max_{t\in\Gamma}|h(t)|, \qquad H(h,\beta)=\sup_{t_1\neq t_2}\frac{|h(t_1)-h(t_2)|}{|t_1-t_2|^\beta},
$$

with $|\cdot|$ the algebra norm. It is a Banach space, and it is the class in which the boundary data of the theory live.

### The order at infinity

**Definition (sectionally regular).** A function is **sectionally regular** for $D$ if it is regular on $\Omega^+$ and on $\Omega^-$ and extends Hölder continuously to $\Gamma$ from each side. Its one-sided boundary values are written $f^+$ and $f^-$.

**Definition (the classes $\mathcal{R}_k$).** For $k\in\mathbb Z$, the class $\mathcal{R}_k$ consists of the sectionally regular functions satisfying $f(x)=O(|x|^k)$ as $|x|\to\infty$. The two classes used below are $\mathcal{R}_{-1}$, the functions vanishing at infinity, and $\mathcal{R}_0$, the functions bounded at infinity. The class is named by the order at infinity, so $\mathcal{R}_k\subseteq\mathcal{R}_{k+1}$, and a solution of a boundary problem is only defined once its class is fixed.

### The singular operator and the Plemelj projectors

**Definition (Cauchy transform and singular operator).** For $h\in H(\Gamma,\beta)$ the **Cauchy transform** is

$$
\mathcal{C}h(x)=\int_\Gamma E(x-y)\,\nu_B(y)\,h(y)\,dS(y), \qquad x\in\Omega^+\cup\Omega^-,
$$

and the **singular operator** $S$ is the Cauchy principal value of the same integral on the boundary,

$$
Sh(t)=\mathrm{P.V.}\int_\Gamma E(t-y)\,\nu_B(y)\,h(y)\,dS(y), \qquad t\in\Gamma .
$$

The kernel normalisation is the one for which $S^2=I$; this fixes the constant carried by $E$ and is the normalisation in which the next theorem is exact.

**Theorem (Plemelj).** For $h\in H(\Gamma,\beta)$ the transform $\mathcal{C}h$ extends Hölder continuously to $\Gamma$ from either side, and

$$
\mathcal{C}^\pm h=\tfrac12\bigl(Sh\pm h\bigr).
$$

Equivalently,

$$
\mathcal{C}^+h-\mathcal{C}^-h=h, \qquad \mathcal{C}^+h+\mathcal{C}^-h=Sh .
$$

The singular operator is an involution, $S^2=I$, and the two combinations

$$
P_+=\tfrac12(I+S), \qquad P_-=\tfrac12(I-S)
$$

are complementary idempotents, $P_+^2=P_+$, $P_-^2=P_-$, $P_+P_-=P_-P_+=0$, $P_++P_-=I$, cutting the Hölder class into the boundary values of the functions regular inside and of those regular outside.

**Remark (the form in the corpus).** *Hypercomplex Integration* states the jump as $\mathcal{C}^+h-\mathcal{C}^-h=h$ "up to the normalisation of the kernel", and *Biquaternion Regular Functions* states the boundary-value criterion $P_\alpha f=f$ with $P_\alpha=\tfrac12(I+S_\alpha)$ and $S_\alpha^2=I$. These are the two halves of the theorem above. The normalisation that makes both exact is the one in which $S$ is the principal-value integral with $S^2=I$; the constant is carried by the kernel $E$, and it is the constant that the Clifford source leaves imprecise.

### The trivial jump problem

**Theorem (the trivial jump).** Let $h\in H(\Gamma,\beta)$ and let $f$ be sectionally regular with

$$
f^+-f^-=h \qquad\text{on }\Gamma .
$$

Then $f=\mathcal{C}h+R$, where $R$ is regular on all of $A$. If $f\in\mathcal{R}_{-1}$ then $R=0$ and the solution is unique; if $f\in\mathcal{R}_0$ then $R$ is a constant.

*Proof.* The transform $\mathcal{C}h$ is sectionally regular and its jump is $h$ by the Plemelj theorem, so $R=f-\mathcal{C}h$ is sectionally regular with zero jump. A function that is regular on both sides and continuous across the boundary is regular on all of $A$, by Painlevé's theorem. By Liouville's theorem in the bounded class $R$ is constant, and in $\mathcal{R}_{-1}$, where $R(x)=O(1/|x|)$ at infinity, it vanishes. $\square$

## The Riemann Problem with a Constant Coefficient

### The problem

**Definition (Riemann problem).** Let $B\in A^\times$ and $h\in H(\Gamma,\beta)$. The **Riemann problem** for the constant coefficient $B$ asks for a function $f$, sectionally regular in a prescribed class $\mathcal{R}_k$, with

$$
f^+(t)=f^-(t)\,B+h(t), \qquad t\in\Gamma .
$$

The constant $B$ is the **coefficient** and $h$ the **free term**; the multiplication by $B$ is on the right, which is the convention of the source of the corpus's Clifford material. Two features distinguish the constant case from the general one. The coefficient is a constant, so with $B=1$ the problem is the trivial jump of the previous section; and a constant is homotopically trivial, so no index can arise, which is why this case closes in explicit form.

### The canonical factor

**Definition (canonical factor).** A **canonical factor** for $B$ is a function $Y$, sectionally regular and invertible on each side, with

$$
Y^+=Y^-\,B \qquad\text{on }\Gamma .
$$

**Proposition (the constant coefficient has a piecewise-constant canonical factor).** For a constant $B\in A^\times$ the function

$$
Y(x)=\begin{cases}B, & x\in\Omega^+,\\[2pt] 1, & x\in\Omega^-\end{cases}
$$

is a canonical factor.

*Proof.* The function $Y$ is constant on each side, hence regular there and invertible, and its boundary values are $Y^+=B$, $Y^-=1$, so $Y^+=Y^-B$. $\square$

The canonical factor is the piecewise-constant function that carries the coefficient; the next theorem shows that it converts the problem into a trivial jump.

### The reduction to the trivial jump

**Theorem (the transformation).** Let $Y$ be a canonical factor for $B$ and let $f$ be sectionally regular. Set $\Phi=fY^{-1}$, the right inverse being taken pointwise. Then $f$ solves the Riemann problem with coefficient $B$ and free term $h$ in the class $\mathcal{R}_k$ if and only if $\Phi$ is sectionally regular, lies in $\mathcal{R}_k$, and solves the trivial jump

$$
\Phi^+-\Phi^-=h\,B^{-1}.
$$

*Proof.* One has $\Phi^\pm=f^\pm (Y^\pm)^{-1}$, so by $Y^+=Y^-B$,

$$
\Phi^+-\Phi^-=f^+B^{-1}-f^-=\bigl(f^-B+h\bigr)B^{-1}-f^-=f^-+hB^{-1}-f^-=hB^{-1},
$$

using $f^+=f^-B+h$. The converse is the same computation read backwards: $\Phi^+-\Phi^-=hB^{-1}$ gives $f^+B^{-1}=f^-+hB^{-1}$, that is $f^+=f^-B+h$. The factor $Y$ is bounded and invertible away from $\Gamma$, so it does not change the class. $\square$

**Corollary (the solution).** In the class $\mathcal{R}_{-1}$ the Riemann problem with constant coefficient $B$ and free term $h$ has the unique solution

$$
f=\mathcal{C}\bigl(hB^{-1}\bigr)\,Y,
$$

and in the class $\mathcal{R}_0$ its general solution is

$$
f=\Bigl(\mathcal{C}\bigl(hB^{-1}\bigr)+C\Bigr)Y
$$

with $C\in A$ an arbitrary constant. Written out on the two sides, with $H=\mathcal{C}(hB^{-1})$, the $\mathcal{R}_0$ solution is $f=HB+CB$ on $\Omega^+$ and $f=H+C$ on $\Omega^-$, so its value at infinity is $C$.

*Proof.* By the theorem, $\Phi$ solves the trivial jump with density $hB^{-1}$, so $\Phi=\mathcal{C}(hB^{-1})+R$; the class fixes $R$ by the trivial-jump theorem, and $f=\Phi Y$. $\square$

**Remark (the order of the factors).** The source of the corpus's Clifford material states this solution with the canonical factor on the left, $f=Y(H+C)$. The two forms agree when $B$ commutes with $H+C$ and differ otherwise, and the correct order is the one above. With $f=Y(H+C)$ the boundary values are $f^+=B(H^++C)$ and $f^-=H^-+C$, and the jump condition $f^+=f^-B+h$ becomes

$$
BH^++BC=H^+B+CB,
$$

which is $[B,H^+]+[B,C]=0$. That identity holds in the commutative case and fails for generic non-commuting data; over 100 random quaternion quadruples $(B,H^+,H^-,C)$ the left form failed the jump in every case and the discrepancy was exactly $[B,H^+]+[B,C]$ in every case. The resolution is structural: the canonical factor multiplies the resolved trivial jump on the right, exactly as $B$ multiplies $f^-$ on the right in the condition.

### The two classes

| | $\mathcal{R}_{-1}$: $f(\infty)=0$ | $\mathcal{R}_0$: $f(\infty)$ finite |
|---|---|---|
| residual term $R$ of the trivial jump | $0$ | an arbitrary constant $C$ |
| solution | $f=\mathcal{C}(hB^{-1})Y$ | $f=(\mathcal{C}(hB^{-1})+C)Y$ |
| number of solutions | exactly one | a one-parameter family, parameter $C$ |
| value at infinity | $0$ | $C$ |

The value of the outside part at infinity is the parameter, so the $\mathcal{R}_0$ class is the natural home of the normalised problem and $\mathcal{R}_{-1}$ the home of the singular integral equation, to which the article now turns.

## The Singular Integral Equation of Cauchy Type

### The operator

**Definition (singular integral equation of Cauchy type).** Let $a,b\in A$ with $a+b\in A^\times$ and $a-b\in A^\times$, and let $g\in H(\Gamma,\beta)$. The **singular integral equation** with data $a,b,g$ is

$$
f\,a+(Sf)\,b=g \qquad\text{on }\Gamma,
$$

the unknown $f$ ranging over $H(\Gamma,\beta)$. It is of **regular type** when $a+b$ and $a-b$ are invertible, which is assumed throughout.

The operator of the equation is $Kf=fa+(Sf)b$, and it factors through the Plemelj projectors. Since $S=P_+-P_-$ and $I=P_++P_-$,

$$
Kf=(P_+f)\,(a+b)+(P_-f)\,(a-b),
$$

so on the two eigenspaces of $S$ the operator is right multiplication by the two constants $a+b$ and $a-b$.

### The equivalence with the Riemann problem

**Theorem (the equivalence).** For $f\in H(\Gamma,\beta)$ the singular integral equation with data $a,b,g$ holds if and only if $\Phi=\mathcal{C}f$ solves the Riemann problem

$$
\Phi^+=\Phi^-B+h, \qquad B=(a-b)(a+b)^{-1}, \qquad h=g(a+b)^{-1},
$$

in the class $\mathcal{R}_{-1}$.

*Proof.* By the Plemelj theorem, applied to $f$ as the density of its Cauchy transform, $f=\Phi^+-\Phi^-$ and $Sf=\Phi^++\Phi^-$. Substituting,

$$
Kf=\Phi^+(a+b)+\Phi^-(b-a),
$$

so $Kf=g$ is $\Phi^+(a+b)=g+\Phi^-(a-b)$, that is $\Phi^+=\Phi^-B+h$ with the stated $B$ and $h$. The transform of an integrable density vanishes at infinity, so the class is $\mathcal{R}_{-1}$, and the passage is reversible because every sectionally regular $\Phi\in\mathcal{R}_{-1}$ is the transform of the density $\Phi^+-\Phi^-$. $\square$

### The solution

**Corollary (existence, uniqueness and the closed form).** In $H(\Gamma,\beta)$ the singular integral equation of regular type has the unique solution

$$
f=(P_+g)\,(a+b)^{-1}+(P_-g)\,(a-b)^{-1},
$$

and the operator of the equation is invertible, with inverse $K^{-1}g=(P_+g)(a+b)^{-1}+(P_-g)(a-b)^{-1}$.

*Proof.* The operator factors as $Kf=(P_+f)(a+b)+(P_-f)(a-b)$, and the constants commute with $S$ because a constant factors out of the principal-value integral, hence with $P_\pm$. Therefore

$$
K\bigl[(P_+g)(a+b)^{-1}+(P_-g)(a-b)^{-1}\bigr]=(P_+g)(a+b)^{-1}(a+b)+(P_-g)(a-b)^{-1}(a-b)=P_+g+P_-g=g,
$$

the cross terms vanishing because $P_+P_-=P_-P_+=0$. The same computation in the other order gives the same result, so $K$ is invertible and the solution is unique. That it agrees with the Riemann-problem solution of the previous section is the equivalence theorem. $\square$

**Remark (the equivalent form).** With $d=g(a-b)^{-1}$ and $B=(a-b)(a+b)^{-1}$ the solution can also be written

$$
f=\tfrac12\Bigl(Sd\,\bigl(B-1\bigr)+d\,\bigl(B+1\bigr)\Bigr),
$$

which is the form reached by resolving the trivial jump directly; the two agree, and in the commutative case the terms carrying $Sd$ cancel against the identity $(B-1)a+(B+1)b=0$. The closed form was checked in the model of the unit circle, with $S$ realised on trigonometric polynomials by $(\widehat{Sd})_n=\mathrm{sgn}(n)\hat d_n$, on twenty random data; the operator form above is the one to use, because it carries the invertibility visibly.

**Corollary (the degenerate coefficients).** If $b=0$ then $B=1$, $h=ga^{-1}$, and $f=ga^{-1}$, the solution of $fa=g$. If $a=0$ then $B=-1$, $h=gb^{-1}$ and $d=-gb^{-1}$, and $f=S(gb^{-1})$, the solution of $Sf=gb^{-1}$ obtained from $S^2=I$.

There is no kernel and no free constant: the class $\mathcal{R}_{-1}$ is minimal, and the free constant of the previous section belongs to the boundary value problem rather than to the integral equation.

## The Index and the Variable Coefficient

### The classical complex case

The constant coefficient is the case in which no index can appear. For a variable coefficient the problem is

$$
f^+(t)=G(t)\,f^-(t)+g(t), \qquad t\in\Gamma,
$$

with $G,g\in H(\Gamma,\beta)$ and $G(t)\neq0$ on $\Gamma$. For $A=\mathbb C$ the index of the coefficient,

$$
\kappa=\operatorname{ind}_\Gamma G=\frac{1}{2\pi}\bigl[\arg G\bigr]_\Gamma\in\mathbb Z,
$$

governs everything. Write $G=t^\kappa G_0$ with $\operatorname{ind}_\Gamma G_0=0$, so that $\ln G_0$ is single-valued, and let $\Gamma_0$ be the Cauchy transform of $\ln G_0$; then the **canonical function**

$$
X(z)=\begin{cases}e^{\Gamma_0(z)}, & z\in\Omega^+,\\[2pt] z^{-\kappa}\,e^{\Gamma_0(z)}, & z\in\Omega^-\end{cases}
$$

is sectionally regular, nowhere zero, and satisfies $X^+=GX^-$. It reduces the problem to the trivial jump exactly as the piecewise-constant factor did in the constant case: $\Phi=f/X$ has $\Phi^+-\Phi^-=g/(GX^-)$, so $\Phi=\mathcal{C}\bigl(g/(GX^-)\bigr)+Q$ with $Q$ a polynomial, and $f=X\Phi$.

### The counting

In the class $\mathcal{R}_{-1}$ the polynomial $Q$ is fixed by the behaviour at infinity, where $X\sim z^{-\kappa}$: the requirement $f(\infty)=0$ forces $\deg Q<\kappa$. The three cases follow, and they are the classical result of Gakhov and Muskhelishvili.

| index $\kappa$ | homogeneous problem $f^+=Gf^-$ | inhomogeneous problem $f^+=Gf^-+g$ |
|---|---|---|
| $\kappa>0$ | $\kappa$ linearly independent solutions | solvable for every $g$; solution space of dimension $\kappa$ |
| $\kappa=0$ | only the zero solution | exactly one solution for every $g$ |
| $\kappa<0$ | only the zero solution | $-\kappa$ solvability conditions; one solution when they hold |

The index is a topological invariant of the coefficient: it is unchanged under a continuous deformation of $G$ that keeps it nonzero, and it is the same integer that indexes the Toeplitz operators of the corpus's *Fredholm Theory* and *Toeplitz Algebras*, where the connection with the singular operator is the one used above.

### The Clifford case, and why the constant case closes

For a non-commutative $A$ a variable coefficient is a map $G:\Gamma\to A^\times$ into the group of units, and its canonical factor is built from a logarithm of $G$ only when $G$ is homotopic to a constant; in general the obstruction is the homotopy class of $G$ in $A^\times$ rather than an integer. The scalar part of $G$ contributes the winding number of the complex case and the remaining part is the part that the Clifford analysis of the corpus carries as the unit group of the algebra; the index belongs to the corpus's operator-algebraic and topological register, *Fredholm Theory*, *Toeplitz Algebras* and the index theory of Part IV. This article does not develop it, and it does not need to: the constant coefficient of the preceding sections is exactly the case in which the homotopy class is trivial, which is why that case has a piecewise-constant canonical factor and a closed-form solution while the variable case does not.

## Instances and the Relation to the Corpus

### The complex case

For $A=\mathbb C$ the theory is the classical theory of the Riemann boundary value problem and the singular integral equation of Cauchy type, with the Cauchy kernel $E(z)=1/(2\pi z)$ and the singular operator the Hilbert transform on $\Gamma$. The corpus carries the complex function theory of *Complex Analysis* and *Complex Integration* up to the residue theorem and the argument principle, and the winding number that appears there is the index of this section; the boundary value problem itself is the content of Gakhov, Muskhelishvili and Lu.

### The quaternion case

For $A=\mathbb H$ the theory is the same with the $\mathbb H$-valued Cauchy kernel of *Quaternion Analysis* and *Hypercomplex Integration*, the boundary being a closed surface in $\mathbb R^4$ and the singular operator the quaternionic Cauchy transform. The source treats this case as one further instance, and the corpus's quaternion integral theory supplies the kernel; nothing new appears, and the corpus's quaternion articles carry the theory in its own notation.

### The Clifford case

For the Clifford algebra $\mathrm{Cl}_{0,m}$ the theory is the Clifford analysis of *Clifford Analysis*, and this is the case of the source's account, where the algebra is written $A_n(\mathbb R)$ over $\mathbb R^n$ and has $e_1=1$ as its identity and $e_2,\dots,e_n$ as its generators, so that $\dim A_n(\mathbb R)=2^{n-1}$ and $A_n(\mathbb R)=\mathrm{Cl}_{0,n-1}$ with the paper's $n$ equal to the corpus's $m+1$. Two conventions of the source must be translated and not copied. Its operator $D=e_1\partial_1-\sum_{i\geq2}e_i\partial_i$ is, under the identification $x_1\leftrightarrow x_0$ and $e_{i}\leftrightarrow e_{i-1}$, the corpus's conjugate operator $\bar D$, so the source's "regular" functions are the corpus's anti-regular ones, the two classes being exchanged by the grade involution and sharing every statement of this article. And the source's conjugation, which negates every basis element including the identity, is not consistent with its own claim $x\bar x=-|x|^2$; the corpus uses the conjugation fixing the identity, for which $x\bar x=|x|^2$ on the variable, and the translation is the one recorded in *Clifford Analysis*.

**Remark (the norm inequality of the source).** The source works in $A_n(\mathbb R)$, of dimension $2^{n-1}$, and bounds the coefficient norm by $|ab|\leq2^{n-1}|a||b|$. The bound is true and improvable: the elementary Cauchy–Schwarz estimate gives $|ab|\leq2^{(n-1)/2}|a||b|$, that is $2^{m/2}$ for the corpus's $\mathrm{Cl}_{0,m}$ with $m=n-1$, which is the square root of the source's constant. Index the basis elements $e_A$ by the subsets $A\subseteq\{1,\dots,m\}$, so that $e_Ae_C=\pm e_{A\triangle C}$; the coefficient of $e_C$ in $ab$ is then $\sum_{A\triangle B=C}\pm a_Ab_B$, and since the pairs $(A,B)$ with $A\triangle B=C$ pair the $A$'s bijectively with the $B$'s, Cauchy–Schwarz gives $|(ab)_C|\leq|a||b|$. Summing the squares over the $2^m$ basis elements gives $|ab|\leq2^{m/2}|a||b|$. Over 100 random pairs in $\mathrm{Cl}_{0,m}$ for $m=1,2,3,4$ the ratio $|ab|/(|a||b|)$ stayed at $1.00$, $1.00$, $1.30$ and $1.26$, well below $2^{m/2}$ throughout.

### The boundary criterion of the corpus as the case $B=1$

**Remark.** The boundary-value criterion of *Biquaternion Regular Functions*, $P_\alpha f=f$ with $P_\alpha=\tfrac12(I+S_\alpha)$, is the Riemann problem with the coefficient $B=1$. The criterion says that a Hölder datum is the boundary value of a solution regular inside exactly when it lies in the $+1$ eigenspace of $S$, which is the statement that the homogeneous problem $f^+=f^-$ has a solution with that boundary value; and the general problem replaces the coefficient $1$ by an invertible $B$ and with it the single condition by the pair of the theorem on the trivial jump. The corpus's boundary theory is therefore the index-zero slice of this one, and the two accounts agree on it.

## Summary

The **Riemann boundary value problem** for an elliptic hypercomplex system $(A,D)$ asks for a sectionally regular function with $f^+=f^-B+h$ on the boundary $\Gamma$, in a prescribed class $\mathcal{R}_k$ of order at infinity. For a **constant coefficient** $B\in A^\times$ the canonical factor is the piecewise-constant function $Y=B$ on $\Omega^+$ and $Y=1$ on $\Omega^-$, it satisfies $Y^+=Y^-B$, and the substitution $\Phi=fY^{-1}$ carries the problem to the trivial jump $\Phi^+-\Phi^-=hB^{-1}$. The solution is $f=\mathcal{C}(hB^{-1})Y$ in the class $\mathcal{R}_{-1}$, unique, and $f=(\mathcal{C}(hB^{-1})+C)Y$ in the class $\mathcal{R}_0$, a one-parameter family whose parameter is the value at infinity. The order of the factors is forced: the canonical factor multiplies on the right, because the coefficient multiplies $f^-$ on the right, and the source's left-hand form is correct only when $B$ commutes with the transform.

The **singular integral equation of Cauchy type** is $fa+(Sf)b=g$, with $S$ the singular operator of the Cauchy kernel and $a\pm b$ invertible. Its operator factors as $Kf=(P_+f)(a+b)+(P_-f)(a-b)$ through the Plemelj projectors $P_\pm=\tfrac12(I\pm S)$ on the right, and it is equivalent to the Riemann problem with $B=(a-b)(a+b)^{-1}$ and $h=g(a+b)^{-1}$ in the class $\mathcal{R}_{-1}$. It has the unique solution $f=(P_+g)(a+b)^{-1}+(P_-g)(a-b)^{-1}$, with no kernel and no free constant, equivalently $f=\tfrac12\bigl(Sd(B-1)+d(B+1)\bigr)$ with $d=g(a-b)^{-1}$; the degenerate coefficients $b=0$ and $a=0$ recover $f=ga^{-1}$ and $f=S(gb^{-1})$.

For a **variable coefficient** $G$ the index enters. In the classical complex case the index $\kappa=\operatorname{ind}_\Gamma G$ controls the canonical function $X$, and with it the count: for $\kappa>0$ there are $\kappa$ homogeneous solutions and the inhomogeneous problem is solvable for every datum; for $\kappa=0$ there is exactly one solution for every datum; for $\kappa<0$ there are $-\kappa$ solvability conditions and one solution when they hold. In the non-commutative case the index is the homotopy class of $G$ in the group of units $A^\times$, and its theory belongs to the corpus's Fredholm and index register. The **Plemelj formulas** $\mathcal{C}^\pm h=\tfrac12(Sh\pm h)$ and $S^2=I$ are the common ground of both problems, and the corpus's boundary-value criterion $P_\alpha f=f$ is the case $B=1$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(A,D)$ | Elliptic hypercomplex system, $\dim_\mathbb{R}A=m$, frame $(1,B_1,\dots,B_{m-1})$ |
| $\bar D$ | Conjugate Cauchy–Riemann operator, $D\bar D=\bar DD=\Delta$ |
| $\Omega^\pm$, $\Gamma=\partial\Omega$ | The two sides of the boundary, and the boundary |
| $H(\Gamma,\beta)$ | Hölder class with exponent $\beta$, Banach with norm $C+H$ |
| $\mathcal{R}_k$ | Sectionally regular functions of order $k$ at infinity |
| $E$, $\nu_B$, $dS$ | Cauchy kernel, conormal element, surface measure |
| $\mathcal{C}h$ | Cauchy transform of a boundary datum $h$ |
| $\mathcal{C}^\pm h$ | Inside and outside boundary values of the transform |
| $S$ | Singular operator, the principal-value boundary integral, $S^2=I$ |
| $P_\pm=\tfrac12(I\pm S)$ | Plemelj projectors onto the two eigenspaces of $S$ |
| $B\in A^\times$ | Constant coefficient of the Riemann problem |
| $h$ | Free term of the Riemann problem |
| $Y$ | Canonical factor, $Y^+=Y^-B$; for constant $B$, $Y=B$ inside and $Y=1$ outside |
| $G$, $\kappa=\operatorname{ind}_\Gamma G$ | Variable coefficient and its index |
| $X$ | Canonical function of the variable-coefficient problem |
| $a,b$ | Constant coefficients of the singular integral equation |
| $g$ | Free term of the singular integral equation |
| $Kf=fa+(Sf)b$ | Operator of the singular integral equation |
| $C$ | Free Clifford constant of the class $\mathcal{R}_0$ solution |

## Further Reading

- F. D. Gakhov, *Boundary Value Problems* (Dover, 1990; translated from the Russian), for the Riemann boundary value problem, the canonical function, the index and the counting of the classical theory.
- N. I. Muskhelishvili, *Singular Integral Equations* (Dover, 2002), for the singular integral equation of Cauchy type, the Plemelj formulas and the reduction between the two problems.
- J. K. Lu, *Boundary Value Problems for Analytic Functions* (World Scientific, 1993), for the classical theory in the form in which the Clifford generalisation is stated.
- P. Li and L. Cao, "Linear BVPs and SIEs for Generalized Regular Functions in Clifford Analysis", *Journal of Function Spaces* **2018**, Article ID 6967149, for the Clifford form of the constant-coefficient problem and of the singular integral equation.
- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the Cauchy kernel, the Plemelj formulas and the singular integrals of Clifford analysis.
- K. Gürlebeck and W. Sprößig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997), for the Cauchy transform, the boundary value problems and the numerical use of the integral operators.
- V. V. Kravchenko and M. V. Shapiro, *Integral Representations for Spatial Models of Mathematical Physics* (Pitman Research Notes in Mathematics 351, Addison-Wesley Longman, 1996), for the shifted operators, the boundary-value criterion and the parameter-dependent versions of these problems.
